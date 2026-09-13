from django.core.management.base import BaseCommand
from apps.trends.models import TrendProduct

PROMPT = """Transform the supplied portrait into a believable Indian studio/cinema portrait from the mid-1980s. Preserve the person's identity, facial structure, skin tone, approximate age and recognizability. Use period-appropriate Indian fashion, hairstyle, warm analogue film color, gentle grain, soft studio lighting, natural skin texture and an authentic printed-photo feeling. Keep the result elegant and realistic rather than cartoonish. Do not imitate a specific actor, celebrity, film poster or copyrighted character. Do not add logos, watermarks or text."""

class Command(BaseCommand):
    help = "Seed launch trend products"

    def handle(self, *args, **kwargs):
        product, created = TrendProduct.objects.update_or_create(
            slug="retro-80s-india",
            defaults={
                "title": "80s India Portrait",
                "eyebrow": "Trending in India",
                "description": "Upload one portrait and see yourself reimagined as a warm, authentic Indian 1980s studio photograph.",
                "status": "active",
                "is_free": True,
                "price_inr": 0,
                "badge": "Free launch",
                "base_prompt": PROMPT,
                "daily_generation_cap": 250,
                "variants": [
                    {"id": "classic", "label": "Classic Studio", "prompt_suffix": "Classic Indian portrait studio, warm neutral backdrop."},
                    {"id": "bollywood", "label": "Cinema Glam", "prompt_suffix": "Generic glamorous 1980s Indian cinema styling, without resembling any specific actor or film."},
                    {"id": "kerala", "label": "Kerala Retro", "prompt_suffix": "Understated 1980s Kerala styling, natural fabrics and a vintage South Indian family-photo atmosphere."},
                    {"id": "saree", "label": "Retro Saree", "prompt_suffix": "Elegant period-appropriate saree styling with authentic 1980s studio portrait aesthetics."},
                ],
                "input_schema": {"image": {"type": "file", "required": True}, "variant": {"type": "string", "required": True}},
            },
        )
        self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} {product.slug}"))
