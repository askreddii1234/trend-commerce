from django.db import transaction
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.trends.models import TrendProduct
from .models import Generation
from .serializers import GenerationSerializer
from .services import build_prompt, enforce_free_limits, generate_image, hash_ip

class GenerationCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        slug = request.data.get("product_slug")
        variant = request.data.get("variant", "classic")
        image = request.FILES.get("image")
        if not slug or not image:
            return Response({"detail": "product_slug and image are required"}, status=status.HTTP_400_BAD_REQUEST)
        if image.size > 10 * 1024 * 1024:
            return Response({"detail": "Image must be 10MB or smaller"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = TrendProduct.objects.get(slug=slug, status="active")
        except TrendProduct.DoesNotExist:
            return Response({"detail": "Trend product not found"}, status=status.HTTP_404_NOT_FOUND)

        forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
        raw_ip = forwarded.split(",")[0].strip() if forwarded else request.META.get("REMOTE_ADDR", "")
        ip_hash = hash_ip(raw_ip)

        try:
            with transaction.atomic():
                if product.is_free:
                    enforce_free_limits(product, ip_hash)
                generation = Generation.objects.create(
                    product=product,
                    source_image=image,
                    variant=variant,
                    prompt_snapshot=build_prompt(product, variant),
                    ip_hash=ip_hash,
                    source=request.data.get("source", "web"),
                )
            generation = generate_image(generation)
            return Response(GenerationSerializer(generation, context={"request": request}).data, status=status.HTTP_201_CREATED)
        except ValueError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_429_TOO_MANY_REQUESTS)
        except Exception as exc:
            if "generation" in locals():
                generation.status = "failed"
                generation.error = str(exc)[:1000]
                generation.save(update_fields=["status", "error"])
            return Response({"detail": "Generation failed. Please try again."}, status=status.HTTP_502_BAD_GATEWAY)

class GenerationDetailView(APIView):
    def get(self, request, generation_id):
        try:
            generation = Generation.objects.select_related("product").get(id=generation_id)
        except Generation.DoesNotExist:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(GenerationSerializer(generation, context={"request": request}).data)
