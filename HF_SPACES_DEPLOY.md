# Hugging Face Spaces Deployment Guide

## Quick Deploy Instructions

### Option 1: Deploy via Hugging Face Web Interface (Easiest)

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name**: `preventive-health-ai`
   - **License**: Choose any
   - **Private/Public**: Public
   - **Space SDK**: `Docker`
4. Click **"Create space"**
5. On the next page, click **"Clone your Space"** and copy the git URL
6. Run in terminal:
   ```bash
   git clone <the-space-url>
   cd preventive-health-ai
   rm -rf * .git* # Clear defaults
   git clone https://github.com/839083/backend .
   git push
   ```

### Option 2: Link Your GitHub Repo Directly (Simplest Alternative)

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Name: `preventive-health-ai`
4. SDK: **`Streamlit`** (not Docker)
5. Click **"Create space"**
6. Go to **Settings** tab
7. Under "Repository" → Link your GitHub repo: `https://github.com/839083/backend`
8. Auto-deploy happens!

**Your live URL will be:**
```
https://huggingface.co/spaces/YOUR-USERNAME/preventive-health-ai
```

---

**Result**: A shareable public URL you can use anywhere!
