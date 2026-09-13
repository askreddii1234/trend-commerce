from django.contrib import admin
from .models import TrendProduct

@admin.register(TrendProduct)
class TrendProductAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "is_free", "price_inr", "daily_generation_cap", "updated_at")
    list_filter = ("status", "is_free", "category")
    search_fields = ("title", "slug", "description")
