#!/bin/bash
echo "🚀 Building Docker image..."
docker build -t ai-drift-threat .

echo "🌍 Deploying to Google Cloud Run..."
gcloud builds submit --tag gcr.io/$(gcloud config get-value project)/ai-drift-threat
gcloud run deploy ai-drift-threat \
  --image gcr.io/$(gcloud config get-value project)/ai-drift-threat \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501

echo "✅ Deployed! Your app is live at:"
gcloud run services describe ai-drift-threat --platform managed --region us-central1 --format 'value(status.url)'