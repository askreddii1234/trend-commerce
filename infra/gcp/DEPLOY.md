# GCP deployment target

Project: `gcpnetwork-508018`
Region: `asia-south1`

The repository contains a manual GitHub Actions workflow at `.github/workflows/deploy-gcp.yml`.

Before running it, provision these resources once in GCP:

- Artifact Registry Docker repository: `trend-commerce`
- Cloud Storage bucket: `gcpnetwork-508018-trend-media`
- Cloud SQL PostgreSQL instance: `trend-db`
- Database: `trendcommerce`
- Database user: `trendapp`
- Runtime service account: `trend-runtime@gcpnetwork-508018.iam.gserviceaccount.com`
- Deployment service account: `trend-deployer@gcpnetwork-508018.iam.gserviceaccount.com`
- Secret Manager secrets: `django-secret`, `openai-api-key`, `db-password`
- GitHub Workload Identity Provider restricted to `askreddii1234/trend-commerce`

Add the provider resource name as the GitHub Actions repository variable `GCP_WIF_PROVIDER`.

The runtime service account requires access to Cloud SQL, the private media bucket, and the three runtime secrets. The deployment service account requires enough permissions to push images to Artifact Registry, deploy Cloud Run services/jobs, inspect Cloud SQL, and act as the runtime service account.

## Deployment

After the one-time GCP bootstrap and GitHub variable are complete:

1. Merge the GCP deployment PR.
2. Open GitHub Actions.
3. Select **Deploy GCP**.
4. Run the workflow from `main`.
5. The workflow builds and pushes API/web images, deploys the API, runs migrations and trend seeding, deploys the web app, then restricts API CORS to the deployed web URL.

Initial guardrails are intentionally conservative: Cloud Run min instances `0`, max instances `3`, free generation cap `100/day`, and application AI budget cap `$1/day`.
