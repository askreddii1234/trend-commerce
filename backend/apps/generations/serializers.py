from rest_framework import serializers
from .models import Generation

class GenerationSerializer(serializers.ModelSerializer):
    product_slug = serializers.CharField(source="product.slug", read_only=True)
    result_url = serializers.SerializerMethodField()

    class Meta:
        model = Generation
        fields = ["id", "product_slug", "variant", "status", "result_url", "error", "created_at", "completed_at"]

    def get_result_url(self, obj):
        request = self.context.get("request")
        if not obj.result_image:
            return None
        url = obj.result_image.url
        return request.build_absolute_uri(url) if request else url
