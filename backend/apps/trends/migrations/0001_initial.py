from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="TrendProduct",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(unique=True)),
                ("title", models.CharField(max_length=160)),
                ("eyebrow", models.CharField(blank=True, max_length=120)),
                ("description", models.TextField()),
                ("status", models.CharField(choices=[("draft", "Draft"), ("active", "Active"), ("archived", "Archived")], default="active", max_length=20)),
                ("is_free", models.BooleanField(default=True)),
                ("price_inr", models.PositiveIntegerField(default=0)),
                ("category", models.CharField(default="image", max_length=80)),
                ("badge", models.CharField(blank=True, max_length=80)),
                ("base_prompt", models.TextField()),
                ("input_schema", models.JSONField(blank=True, default=dict)),
                ("variants", models.JSONField(blank=True, default=list)),
                ("output_count", models.PositiveSmallIntegerField(default=1)),
                ("daily_generation_cap", models.PositiveIntegerField(default=250)),
                ("active_from", models.DateTimeField(blank=True, null=True)),
                ("active_until", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_at"]},
        )
    ]
