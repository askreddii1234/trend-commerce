import uuid
from django.db import models
from apps.trends.models import TrendProduct

class Generation(models.Model):
    STATUS_CHOICES = [("queued", "Queued"), ("processing", "Processing"), ("completed", "Completed"), ("failed", "Failed")]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(TrendProduct, on_delete=models.PROTECT, related_name="generations")
    source_image = models.ImageField(upload_to="source/%Y/%m/%d/")
    result_image = models.ImageField(upload_to="results/%Y/%m/%d/", blank=True)
    variant = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="queued")
    prompt_snapshot = models.TextField(blank=True)
    provider = models.CharField(max_length=40, default="openai")
    model = models.CharField(max_length=80, blank=True)
    estimated_cost_usd = models.DecimalField(max_digits=9, decimal_places=4, default=0)
    error = models.TextField(blank=True)
    source = models.CharField(max_length=80, blank=True)
    referral_code = models.CharField(max_length=40, blank=True)
    ip_hash = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
