from django.contrib import admin
from .models import Generation

@admin.register(Generation)
class GenerationAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "variant", "status", "provider", "model", "estimated_cost_usd", "created_at")
    list_filter = ("status", "provider", "product")
    readonly_fields = ("id", "created_at", "completed_at")
