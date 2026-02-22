# Preventive Health AI - Deployment Guide

## Project Overview
This is a Streamlit-based multi-domain health risk detection system powered by a pre-trained TensorFlow model.

## Deployment on Render.com

### Quick Start

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the branch to deploy
   - Render will auto-detect `render.yaml` configuration
   - Click "Create Web Service"

### Alternative: Docker Deployment

If deploying to other platforms (Heroku, AWS, etc.):

```bash
# Build Docker image
docker build -t preventive-health-ai .

# Run locally
docker run -p 8501:8501 preventive-health-ai

# For production: Push to Docker Hub or your registry
docker tag preventive-health-ai:latest your-docker-user/preventive-health-ai:latest
docker push your-docker-user/preventive-health-ai:latest
```

## File Structure
```
backend/
├── main.py                          # Main Streamlit app entry point
├── pages/
│   ├── 1_User_Input.py             # User data collection
│   ├── 2_Lifestyle_Symptoms.py     # Lifestyle assessment
│   └── 3_Prediction.py             # Model predictions
├── final_advanced_multi_domain_model.keras  # Trained model
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── render.yaml                      # Render.com configuration
├── .streamlit/config.toml           # Streamlit settings
└── README.md                        # This file
```

## Key Configuration
- **Python Version**: 3.10
- **Framework**: Streamlit
- **Model**: TensorFlow/Keras
- **Port**: 8501 (Streamlit default)

## Environment Variables
If you need to set environment variables on Render:
1. Go to your service settings
2. Click "Environment"
3. Add your variables (e.g., API keys, secrets)

## Testing Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run main.py
```

## Troubleshooting

**Model Not Found**: Ensure `final_advanced_multi_domain_model.keras` is in the root directory.

**Slow Startup**: The initial TensorFlow import can take 30-60 seconds. This is normal.

**Memory Issues**: If deployment fails with memory errors, the model might be too large. Consider using cloud storage or quantization.

## Next Steps
- Add logging for monitoring
- Implement user analytics
- Add error handling and user feedback
- Consider CI/CD pipeline for automated deployments
