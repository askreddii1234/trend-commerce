import uuid
import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [("trends", "0001_initial")]
    operations = [
        migrations.CreateModel(
            name="Generation",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("source_image", models.ImageField(upload_to="source/%Y/%m/%d/")),
                ("result_image", models.ImageField(blank=True, upload_to="results/%Y/%m/%d/")),
                ("variant", models.CharField(blank=True, max_length=80)),
                ("status", models.CharField(choices=[("queued", "Queued"), ("processing", "Processing"), ("completed", "Completed"), ("failed", "Failed")], default="queued", max_length=20)),
                ("prompt_snapshot", models.TextField(blank=True)),
                ("provider", models.CharField(default="openai", max_length=40)),
                ("model", models.CharField(blank=True, max_length=80)),
                ("estimated_cost_usd", models.DecimalField(decimal_places=4, default=0, max_digits=9)),
                ("error", models.TextField(blank=True)),
                ("source", models.CharField(blank=True, max_length=80)),
                ("referral_code", models.CharField(blank=True, max_length=40)),
                ("ip_hash", models.CharField(blank=True, db_index=True, max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("completed_at", models.DateTimeField(blank=True, null=True)),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="generations", to="trends.trendproduct")),
            ],
            options={"ordering": ["-created_at"]},
        )
    ]
