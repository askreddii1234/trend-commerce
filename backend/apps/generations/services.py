import base64
import hashlib
from django.conf import settings
from django.core.files.base import ContentFile
from django.db.models import Sum
from django.utils import timezone
from openai import OpenAI
from .models import Generation


def hash_ip(ip: str) -> str:
    return hashlib.sha256((ip or "unknown").encode()).hexdigest()


def enforce_free_limits(product, ip_hash: str):
    today = timezone.localdate()
    qs = Generation.objects.filter(created_at__date=today)
    if qs.count() >= settings.FREE_DAILY_GENERATION_LIMIT:
        raise ValueError("Today's free generation capacity has been reached.")
    if qs.filter(product=product).count() >= product.daily_generation_cap:
        raise ValueError("This trend has reached today's free generation limit.")
    if qs.filter(ip_hash=ip_hash, product=product).exists():
        raise ValueError("One free generation per person per day for this trend.")
    spend = qs.aggregate(total=Sum("estimated_cost_usd"))["total"] or 0
    if float(spend) >= settings.FREE_DAILY_BUDGET_USD:
        raise ValueError("Today's free AI budget has been reached.")


def build_prompt(product, variant_id: str) -> str:
    suffix = ""
    for variant in product.variants:
        if variant.get("id") == variant_id:
            suffix = variant.get("prompt_suffix", "")
            break
    return f"{product.base_prompt}\n\nSelected variation: {suffix}".strip()


def generate_image(generation: Generation) -> Generation:
    if not settings.OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not configured")

    generation.status = "processing"
    generation.model = settings.OPENAI_IMAGE_MODEL
    generation.save(update_fields=["status", "model"])

    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    generation.source_image.open("rb")
    try:
        result = client.images.edit(
            model=settings.OPENAI_IMAGE_MODEL,
            image=generation.source_image.file,
            prompt=generation.prompt_snapshot,
            size="1024x1024",
            quality=settings.OPENAI_IMAGE_QUALITY,
        )
    finally:
        generation.source_image.close()

    image_b64 = result.data[0].b64_json
    if not image_b64:
        raise RuntimeError("Image provider returned no image")
    image_bytes = base64.b64decode(image_b64)
    generation.result_image.save(f"{generation.id}.png", ContentFile(image_bytes), save=False)
    generation.status = "completed"
    generation.completed_at = timezone.now()
    generation.save(update_fields=["result_image", "status", "completed_at"])
    return generation
