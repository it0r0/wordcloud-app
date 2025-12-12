# 📝 Quick Deployment Cheat Sheet
## For Dokploy with Raw Compose Input

---

## 🎯 5-Minute Quick Start

### Step 1: Create Git Repo (2 minutes)
```bash
# On GitHub/GitLab: Create new repository named "wordcloud-app"
# Copy the repository URL

# In terminal:
cd wordcloud-app
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### Step 2: Deploy in Dokploy (3 minutes)
```
1. Dokploy → Applications → Create Application
2. Choose "Docker Compose"
3. Select "Raw Compose Input"
4. Paste the compose config below
5. Add repository URL
6. Set branch: main
7. Click Deploy
```

---

## 📋 Raw Compose Configuration (Copy & Paste)

```yaml
version: '3.8'

services:
  wordcloud:
    image: wordcloud-app:latest
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8501:8501"
    environment:
      - STREAMLIT_SERVER_PORT=8501
      - STREAMLIT_SERVER_ADDRESS=0.0.0.0
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

---

## ⚙️ Configuration Values

| Field | Value |
|-------|-------|
| **Application Name** | `wordcloud-app` |
| **Repository URL** | `https://github.com/YOUR_USERNAME/wordcloud-app.git` |
| **Branch** | `main` |
| **Container Port** | `8501` |
| **Host Port** | `8501` |
| **Dockerfile Path** | `./Dockerfile` |

---

## 🔧 Environment Variables (Optional)

```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

## ✅ Verification Steps

After deployment:
1. ✅ Check Dokploy status → Should show "Running" (green)
2. ✅ Open the provided URL
3. ✅ See "☁️ iSeeU Cloud" header
4. ✅ Upload test_wc.png image
5. ✅ Enter some text
6. ✅ Click "Generate Word Cloud"
7. ✅ Download works

---

## 🚨 Common Issues & Quick Fixes

### Build Failed
```bash
# Check repository URL is correct
# Verify all files are in Git repo
# Check Dockerfile exists in root
```

### Port Conflict
```yaml
# Change to different port
ports:
  - "8502:8501"  # Use 8502 instead
```

### App Not Loading
```bash
# Wait 2-3 minutes for health check
# Check logs in Dokploy
# Verify port 8501 is open
```

---

## 🔄 Making Updates

```bash
# 1. Edit files locally
nano app.py

# 2. Commit and push
git add .
git commit -m "Update: description"
git push origin main

# 3. In Dokploy: Click "Redeploy"
```

---

## 📦 Required Files Checklist

Before pushing to Git, ensure you have:
- [ ] app.py
- [ ] Dockerfile
- [ ] docker-compose.yml
- [ ] requirements.txt
- [ ] .dockerignore
- [ ] .gitignore
- [ ] .streamlit/config.toml
- [ ] Montserrat-Bold.otf
- [ ] README.md

---

## 🌐 Access URLs

After deployment, your app will be available at:
- `http://YOUR_DOKPLOY_IP:8501`
- OR `https://wordcloud-app.YOUR_DOMAIN.com` (if domain configured)

---

## 🎉 Success!

If you can:
1. Access the URL
2. See the app interface
3. Generate word clouds
4. Download images

**You're done!** 🚀

---

## 📞 Quick Help

**Issue:** Build fails
**Solution:** Check repository URL and verify all files are pushed

**Issue:** Can't access app
**Solution:** Wait 2 minutes, check port 8501, review logs

**Issue:** Fonts not uploading
**Solution:** Check file size < 10MB, use .ttf or .otf format

---

## 💡 Pro Tips

- Enable auto-deploy in Dokploy for automatic updates on Git push
- Add custom domain for professional URL
- Enable HTTPS/SSL for security
- Monitor logs regularly for issues
- Keep Git repository clean and organized

---

For detailed instructions, see **MANUAL_DEPLOYMENT_GUIDE.md**
