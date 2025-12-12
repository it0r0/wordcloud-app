# 🖥️ Dokploy UI Navigation Guide
## Visual Step-by-Step for Raw Compose Deployment

---

## 🎯 Overview

This guide shows you exactly what to click and where in the Dokploy interface.

---

## Step 1: Access Dokploy Dashboard

```
┌─────────────────────────────────────────────────────────┐
│  🏠 Dokploy                                    👤 Admin  │
├─────────────────────────────────────────────────────────┤
│  📊 Dashboard                                            │
│  🚀 Applications      ← Click here                      │
│  🗄️  Databases                                           │
│  ⚙️  Settings                                            │
└─────────────────────────────────────────────────────────┘
```

**Action:** Click **"Applications"** in the left sidebar

---

## Step 2: Create New Application

```
┌─────────────────────────────────────────────────────────┐
│  Applications                                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [+ Create Application]  ← Click here                   │
│                                                          │
│  (Your existing applications will appear here)          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Click **"+ Create Application"** button

---

## Step 3: Choose Deployment Type

```
┌─────────────────────────────────────────────────────────┐
│  Select Deployment Type                                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │
│  │  🐳 Docker  │  │  📦 Docker  │  │  📝 Git     │    │
│  │             │  │  Compose    │  │  Repository │    │
│  └─────────────┘  └─────────────┘  └─────────────┘    │
│                         ↑                               │
│                    Click here                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Click **"Docker Compose"** option

---

## Step 4: Application Basic Info

```
┌─────────────────────────────────────────────────────────┐
│  Create Application                                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Application Name: *                                     │
│  ┌────────────────────────────────────────────────┐    │
│  │ wordcloud-app                                  │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  Description: (optional)                                 │
│  ┌────────────────────────────────────────────────┐    │
│  │ Enhanced WordCloud Generator                   │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** 
- Type `wordcloud-app` in **Application Name**
- Add description (optional)

---

## Step 5: Select Raw Compose Input

```
┌─────────────────────────────────────────────────────────┐
│  Deployment Configuration                                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ⚪ Use Compose File from Repository                    │
│  ⚫ Raw Compose Input              ← Select this        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Select **"Raw Compose Input"** radio button

---

## Step 6: Enter Raw Compose Configuration

```
┌─────────────────────────────────────────────────────────┐
│  Docker Compose Configuration                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │ version: '3.8'                                 │    │
│  │                                                 │    │
│  │ services:                                       │    │
│  │   wordcloud:                                    │    │
│  │     image: wordcloud-app:latest                 │    │
│  │     build:                                      │    │
│  │       context: .                                │    │
│  │       dockerfile: Dockerfile                    │    │
│  │     ports:                                      │    │
│  │       - "8501:8501"                             │    │
│  │     environment:                                │    │
│  │       - STREAMLIT_SERVER_PORT=8501             │    │
│  │       - STREAMLIT_SERVER_ADDRESS=0.0.0.0       │    │
│  │     restart: unless-stopped                     │    │
│  │     healthcheck:                                │    │
│  │       test: ["CMD", "curl", "-f",              │    │
│  │         "http://localhost:8501/_stcore/health"]│    │
│  │       interval: 30s                             │    │
│  │       timeout: 10s                              │    │
│  │       retries: 3                                │    │
│  │                                                 │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Copy and paste the complete Docker Compose configuration

---

## Step 7: Configure Git Repository

```
┌─────────────────────────────────────────────────────────┐
│  Source Code Repository                                  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Repository URL: *                                       │
│  ┌────────────────────────────────────────────────┐    │
│  │ https://github.com/YOUR_USER/wordcloud-app.git │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  Branch: *                                               │
│  ┌────────────────────────────────────────────────┐    │
│  │ main                                           │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  Authentication: (if private repo)                       │
│  ⚪ None    ⚪ SSH Key    ⚪ Personal Token             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:**
- Paste your **Repository URL** (replace YOUR_USER with your username)
- Type `main` in **Branch** field
- Select authentication method if private repository

---

## Step 8: Port Configuration (Auto-detected)

```
┌─────────────────────────────────────────────────────────┐
│  Port Mapping                                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Container Port: *                                       │
│  ┌────────────────────────────────────────────────┐    │
│  │ 8501                    (auto-detected)        │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  Host Port:                                              │
│  ┌────────────────────────────────────────────────┐    │
│  │ 8501          (or leave blank to auto-assign)  │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:**
- Verify **Container Port** shows `8501`
- Set **Host Port** to `8501` or leave blank for auto-assignment

---

## Step 9: Environment Variables (Optional)

```
┌─────────────────────────────────────────────────────────┐
│  Environment Variables                    [+ Add]        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────────────┬───────────────────────────┐  │
│  │ Key                  │ Value                     │  │
│  ├──────────────────────┼───────────────────────────┤  │
│  │ STREAMLIT_...PORT    │ 8501                      │  │
│  │ STREAMLIT_...ADDRESS │ 0.0.0.0                   │  │
│  │ STREAMLIT_...HEADLESS│ true                      │  │
│  └──────────────────────┴───────────────────────────┘  │
│                                                          │
│  (Optional - already in compose file)                    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** 
- **Skip this section** (environment variables already in compose file)
- OR add them here if you prefer

---

## Step 10: Domain Configuration (Optional)

```
┌─────────────────────────────────────────────────────────┐
│  Domains                                  [+ Add Domain] │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Domain Name:                                            │
│  ┌────────────────────────────────────────────────┐    │
│  │ wordcloud.yourdomain.com                       │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  ☑️ Enable SSL/HTTPS                                    │
│  ☑️ Auto-renew certificate                              │
│                                                          │
│  Or use Dokploy subdomain:                               │
│  wordcloud-app.your-dokploy-domain.com                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:**
- **Skip for now** (you can add later)
- OR add your custom domain
- OR use Dokploy-provided subdomain

---

## Step 11: Advanced Settings (Optional)

```
┌─────────────────────────────────────────────────────────┐
│  Advanced Settings                           [Expand ▼] │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ☑️ Enable Auto Deploy                                  │
│  ☑️ Enable Health Checks                                │
│  ☐ Restart on Failure                                   │
│                                                          │
│  Resource Limits:                                        │
│  Memory Limit: ┌─────┐ MB                              │
│  CPU Limit:    ┌─────┐ cores                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:**
- Check **"Enable Auto Deploy"** (recommended)
- Check **"Enable Health Checks"** (recommended)
- Set resource limits if needed (optional)

---

## Step 12: Review and Deploy

```
┌─────────────────────────────────────────────────────────┐
│  Review Configuration                                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ✅ Application Name: wordcloud-app                     │
│  ✅ Deployment Type: Docker Compose                     │
│  ✅ Repository: github.com/YOUR_USER/wordcloud-app.git  │
│  ✅ Branch: main                                         │
│  ✅ Container Port: 8501                                 │
│  ✅ Configuration: Valid                                 │
│                                                          │
│                                                          │
│  [Cancel]                    [Create & Deploy] ← Click  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Click **"Create & Deploy"** button

---

## Step 13: Monitor Deployment

```
┌─────────────────────────────────────────────────────────┐
│  wordcloud-app                            🟡 Building   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  📋 Logs    📊 Metrics    ⚙️ Settings    🌐 Domains     │
│  ────────                                                │
│                                                          │
│  [Deployment Logs]                                       │
│  ┌────────────────────────────────────────────────┐    │
│  │ Cloning repository...                          │    │
│  │ Building image...                               │    │
│  │ Step 1/8 : FROM python:3.11-slim               │    │
│  │ Step 2/8 : WORKDIR /app                        │    │
│  │ Step 3/8 : RUN apt-get update...               │    │
│  │ ...                                             │    │
│  │ Successfully built image                        │    │
│  │ Starting container...                           │    │
│  │ Container started successfully                  │    │
│  │ Running health checks...                        │    │
│  │ ✅ Health check passed                          │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** 
- Watch the logs
- Wait for status to change from 🟡 Building → 🟢 Running

---

## Step 14: Access Your Application

```
┌─────────────────────────────────────────────────────────┐
│  wordcloud-app                            🟢 Running    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Application URL:                                        │
│  🔗 http://your-dokploy-ip:8501                         │
│  [Copy URL]  [Open in Browser] ← Click                  │
│                                                          │
│  Status: ✅ Healthy                                      │
│  Uptime: 2 minutes                                       │
│  Requests: 0                                             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Action:** Click **"Open in Browser"** to access your app

---

## 🎉 Success Screen

```
┌─────────────────────────────────────────────────────────┐
│                                                          │
│                  ☁️ iSeeU Cloud                          │
│                                                          │
│  ─────────────────────────────────────────────────      │
│                                                          │
│  [Sidebar]                    [Main Content]            │
│  ⚙️ Configuration              📤 Upload Mask Image     │
│  📝 Font Files                 💬 Word Input            │
│  📏 Font Size Range                                     │
│  🎨 Word Cloud Settings        🔥 Priority Words        │
│                                📝 Regular Words         │
│                                                          │
│                  [🎨 Generate Word Cloud]               │
│                                                          │
└─────────────────────────────────────────────────────────┘

✅ Deployment Successful!
```

---

## 🔄 Making Updates Later

### In Dokploy Dashboard:

```
┌─────────────────────────────────────────────────────────┐
│  wordcloud-app                            🟢 Running    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  [🔄 Redeploy]  [⚙️ Settings]  [🗑️ Delete]             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**After pushing changes to Git:**
- If auto-deploy is ON: Automatic redeployment ✨
- If auto-deploy is OFF: Click **"🔄 Redeploy"** button

---

## 📊 Status Indicators

| Icon | Status | Meaning |
|------|--------|---------|
| 🟡 | Building | Deployment in progress |
| 🟡 | Starting | Container starting up |
| 🟢 | Running | Application is live |
| 🔴 | Failed | Deployment error |
| 🟠 | Stopped | Application stopped |

---

## ⚠️ Troubleshooting in UI

### View Logs:
```
Application → Logs Tab → View real-time logs
```

### Restart Application:
```
Application → Settings → Restart Container
```

### Check Health:
```
Application → Metrics Tab → Health Status
```

### Redeploy:
```
Application → Redeploy Button
```

---

## 💡 UI Tips

1. **Use Search**: Find your app quickly in the applications list
2. **Bookmark URL**: Save the application URL for quick access
3. **Monitor Logs**: Keep logs tab open during first deployment
4. **Set Alerts**: Configure notifications for deployment failures
5. **Test Locally First**: Always test changes locally before deploying

---

## 🎯 Common UI Locations

| What | Where |
|------|-------|
| Logs | Application → Logs tab |
| Settings | Application → Settings tab |
| Metrics | Application → Metrics tab |
| Domains | Application → Domains tab |
| Rebuild | Application → Redeploy button |
| Delete | Application → Settings → Delete |

---

For detailed written instructions, see **MANUAL_DEPLOYMENT_GUIDE.md**
For quick reference, see **DEPLOYMENT_CHEAT_SHEET.md**
