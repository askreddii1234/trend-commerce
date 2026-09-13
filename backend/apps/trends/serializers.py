from rest_framework import serializers
from .models import TrendProduct

class TrendProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendProduct
        fields = ["slug", "title", "eyebrow", "description", "is_free", "price_inr", "category", "badge", "input_schema", "variants", "output_count", "daily_generation_cap"]
