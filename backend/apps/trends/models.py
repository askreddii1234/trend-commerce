from django.db import models

class TrendProduct(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=160)
    eyebrow = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, default="active", choices=[("draft", "Draft"), ("active", "Active"), ("archived", "Archived")])
    is_free = models.BooleanField(default=True)
    price_inr = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=80, default="image")
    badge = models.CharField(max_length=80, blank=True)
    base_prompt = models.TextField()
    input_schema = models.JSONField(default=dict, blank=True)
    variants = models.JSONField(default=list, blank=True)
    output_count = models.PositiveSmallIntegerField(default=1)
    daily_generation_cap = models.PositiveIntegerField(default=250)
    active_from = models.DateTimeField(null=True, blank=True)
    active_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
