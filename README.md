# Trend Commerce

A GCP-first AI trend-commerce engine: detect a fast-moving social trend, publish it as a configurable digital product, let users upload an image, generate a personalized result, and share it.

## MVP

- Next.js storefront
- Django REST API
- Config-driven trend products
- Free generation limits and daily budget guardrails
- OpenAI image edit provider abstraction
- GCS-ready media storage
- Cloud Run deployment files
- First product: `retro-80s-india`

## Local quick start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_trends
python manage.py runserver 0.0.0.0:8000
```

### Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

Open http://localhost:3000.

## GCP target

- Cloud Run: frontend + API
- Cloud SQL for PostgreSQL: production database
- Cloud Storage: source/result images
- Secret Manager: Django/OpenAI/database secrets
- Artifact Registry + Cloud Build/GitHub Actions: container delivery

See `infra/gcp/README.md`.
