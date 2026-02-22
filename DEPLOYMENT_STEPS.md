# Deploy to Render.com - Step by Step

## ✅ Pre-Deployment Checklist
- [x] Code pushed to GitHub: https://github.com/839083/backend
- [x] `render.yaml` configured ✓
- [x] `requirements.txt` updated ✓
- [x] `Dockerfile` ready ✓
- [x] `.streamlit/config.toml` added ✓
- [x] `final_advanced_multi_domain_model.keras` included ✓

## 📋 Deployment Steps (Manual - Copy & Follow)

### Step 1: Access Render Dashboard
1. Go to https://dashboard.render.com
2. Sign in with your GitHub account (or create account)
3. Click "New +" button in top right

### Step 2: Create New Web Service
1. Select **"Web Service"** from dropdown
2. Click **"Connect Repository"**
3. Search for and select: `839083/backend`
4. Click "Connect"

### Step 3: Configure Service
| Field | Value |
|-------|-------|
| **Name** | `preventive-health-ai` |
| **Environment** | `Python 3` |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run main.py --server.port 10000 --server.address 0.0.0.0` |

### Step 4: Resource Configuration
1. Choose **"Free"** plan (for testing) or **"Starter"** ($7/month)
2. Click **"Advanced"** to expand options

### Step 5: Environment Variables (Optional)
Leave empty for now - not needed for this app

### Step 6: Deploy
1. Review all settings
2. Click **"Create Web Service"**
3. Wait for build to complete (3-5 minutes)

## ✨ After Deployment

When deployment succeeds, you'll get a URL like:
```
https://preventive-health-ai-xxxxx.onrender.com
```

### Access Your App
- Visit the URL in your browser
- First load may take 30-60 seconds (TensorFlow startup)
- You'll see: "🩺 Preventive Health AI"

### Monitoring
- Logs available in Render dashboard
- Auto-restart on crashes
- Manual redeploy from dashboard anytime

## 🔄 Auto-Deployment
From now on, any push to `main` branch auto-deploys!

## ⚠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Build fails | Check `requirements.txt` for correct versions |
| App crashes on startup | Check model file path in code |
| Slow first request | Normal - TensorFlow takes time to load |
| 403 Permission error | Make sure GitHub account is authenticated |

## 💡 Alternative: Deploy via Render CLI

```powershell
# Install Render CLI
npm install -g render-cli

# Authenticate
render login

# Deploy
render deploy --repo https://github.com/839083/backend
```

---
**Questions?** Check the main README.md for more details.
