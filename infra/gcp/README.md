# GCP deployment

Recommended MVP topology:

- `trend-web`: Cloud Run (public)
- `trend-api`: Cloud Run (public API, restrict admin separately)
- Cloud SQL PostgreSQL
- Cloud Storage bucket for uploads/results
- Secret Manager for `DJANGO_SECRET_KEY`, `OPENAI_API_KEY`, and database URL
- Artifact Registry for containers

## Bootstrap

```bash
export PROJECT_ID=your-project
export REGION=asia-south1
export REPO=trend-commerce

gcloud config set project $PROJECT_ID
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com sqladmin.googleapis.com secretmanager.googleapis.com storage.googleapis.com

gcloud artifacts repositories create $REPO --repository-format=docker --location=$REGION
```

For the fastest first deploy, use `gcloud run deploy --source` from `backend/` and `frontend/`. For repeatable production delivery, switch to Cloud Build or GitHub Actions building into Artifact Registry.

## Cost guardrails

Start Cloud Run with min instances `0`. Set API max instances to a small number during the free launch. Add application-level daily generation/budget limits before sharing publicly.
