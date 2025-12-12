# 🚀 Manual Dokploy Deployment Guide
## Using Raw Docker Compose Input

This guide walks you through deploying your WordCloud app to Dokploy when you need to:
1. Manually create the Git repository
2. Use the "Raw Compose" input method in Dokploy

---

## 📋 Prerequisites Checklist

Before starting, ensure you have:
- [ ] Dokploy instance running and accessible
- [ ] GitHub/GitLab/Gitea account for repository
- [ ] All app files from the wordcloud-app folder
- [ ] Basic familiarity with Git commands
- [ ] Text editor (VS Code, Sublime, etc.)

---

## Part 1: Create Git Repository (Manual)

### Step 1: Create Repository on Git Platform

#### Option A: GitHub
1. Go to https://github.com
2. Click the **"+"** button (top right) → **"New repository"**
3. Fill in details:
   - **Repository name**: `wordcloud-app` (or your preferred name)
   - **Description**: "Enhanced WordCloud Generator for Dokploy"
   - **Visibility**: Public or Private (your choice)
   - **Initialize**: ❌ DO NOT check "Add README" (we have our own files)
4. Click **"Create repository"**
5. **Copy the repository URL** (you'll need this)
   - Example: `https://github.com/YOUR_USERNAME/wordcloud-app.git`

#### Option B: GitLab
1. Go to https://gitlab.com
2. Click **"New project"** → **"Create blank project"**
3. Fill in:
   - **Project name**: `wordcloud-app`
   - **Visibility**: Public or Private
   - **Initialize**: ❌ Uncheck "Initialize repository with a README"
4. Click **"Create project"**
5. **Copy the repository URL**

#### Option C: Gitea (Self-hosted)
1. Go to your Gitea instance
2. Click **"+"** → **"New Repository"**
3. Fill in project details
4. Click **"Create Repository"**
5. **Copy the repository URL**

### Step 2: Prepare Your Local Files

Open terminal/command prompt and navigate to where you want to work:

```bash
# Create a working directory
mkdir ~/wordcloud-project
cd ~/wordcloud-project
```

### Step 3: Copy All App Files

Copy all files from the `wordcloud-app` folder you downloaded to this directory.

**Required files:**
```
wordcloud-app/
├── app.py                      # Main application
├── Montserrat-Bold.otf         # Font file
├── test_wc.png                 # Test image
├── requirements.txt            # Dependencies
├── Dockerfile                  # Docker config
├── docker-compose.yml          # Compose config
├── .dockerignore               # Docker exclusions
├── .gitignore                  # Git exclusions
├── .streamlit/
│   └── config.toml             # Streamlit config
└── README.md                   # Documentation
```

### Step 4: Initialize Git and Push to Repository

```bash
# Navigate to your project directory
cd ~/wordcloud-project/wordcloud-app

# Initialize Git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: WordCloud app for Dokploy"

# Rename branch to main (if needed)
git branch -M main

# Add your remote repository (use YOUR repository URL)
git remote add origin https://github.com/YOUR_USERNAME/wordcloud-app.git

# Push to repository
git push -u origin main
```

**Note:** You may need to authenticate with GitHub/GitLab:
- GitHub: Use Personal Access Token (not password)
- GitLab: Use Personal Access Token or password
- Gitea: Use your credentials

### Step 5: Verify Repository

1. Go to your repository URL in a browser
2. Verify all files are uploaded
3. Check that you can see:
   - app.py
   - Dockerfile
   - docker-compose.yml
   - requirements.txt
   - All other files

✅ **Git repository setup complete!**

---

## Part 2: Deploy to Dokploy Using Raw Compose

### Step 1: Access Dokploy Dashboard

1. Open your browser
2. Navigate to your Dokploy instance URL
3. Log in with your credentials

### Step 2: Create New Application

1. In Dokploy dashboard, click **"Applications"** (left sidebar)
2. Click **"Create Application"** or **"+ New Application"**
3. You'll see deployment options

### Step 3: Select "Docker Compose" Deployment

1. Choose **"Docker Compose"** as the deployment type
2. Look for **"Raw Compose"** or **"Compose Configuration"** option
3. Select **"Raw Compose Input"** method

### Step 4: Configure Application Details

Fill in the basic information:

**Application Name:**
```
wordcloud-app
```

**Description (optional):**
```
Enhanced WordCloud Generator with priority words and multi-font support
```

### Step 5: Enter Raw Docker Compose Configuration

In the "Docker Compose" or "Raw Compose" text area, paste this configuration:

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

### Step 6: Configure Git Repository Connection

In the repository section:

**Repository URL:**
```
https://github.com/YOUR_USERNAME/wordcloud-app.git
```
(Replace with YOUR actual repository URL)

**Branch:**
```
main
```

**Dockerfile Path (if asked):**
```
./Dockerfile
```

**Build Context (if asked):**
```
./
```

### Step 7: Configure Port Mapping

Dokploy should auto-detect from the compose file, but verify:

**Container Port:** `8501`
**Host Port:** `8501` (or let Dokploy auto-assign)

### Step 8: Set Environment Variables (Optional)

If Dokploy has a separate environment variables section, add these:

```
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

**Note:** These are already in the compose file, so this is optional.

### Step 9: Configure Domain (Optional)

If you want a custom domain:

1. Find the **"Domains"** section
2. Add your custom domain (e.g., `wordcloud.yourdomain.com`)
3. Or use the Dokploy-provided subdomain

### Step 10: Review Configuration

Before deploying, verify:
- ✅ Application name is correct
- ✅ Repository URL is correct
- ✅ Branch is "main"
- ✅ Docker Compose configuration is pasted correctly
- ✅ Port 8501 is configured
- ✅ Environment variables are set (if applicable)

### Step 11: Deploy!

1. Click **"Create"** or **"Deploy"** button
2. Dokploy will start the deployment process

---

## Part 3: Monitor Deployment

### Step 1: Watch Build Logs

1. In Dokploy, navigate to your application
2. Click on **"Logs"** or **"Build Logs"** tab
3. Watch the build progress

You should see:
```
Step 1/8 : FROM python:3.11-slim
Step 2/8 : WORKDIR /app
Step 3/8 : RUN apt-get update...
...
Successfully built [image-id]
Successfully tagged wordcloud-app:latest
```

### Step 2: Wait for Deployment

The process typically takes 2-5 minutes:
1. **Cloning** repository (10-30 seconds)
2. **Building** Docker image (1-3 minutes)
3. **Starting** container (10-30 seconds)
4. **Health check** verification (30-60 seconds)

### Step 3: Check Deployment Status

Look for status indicators:
- 🟡 **Building** - In progress
- 🟡 **Starting** - Container starting
- 🟢 **Running** - Successfully deployed
- 🔴 **Failed** - Check logs for errors

---

## Part 4: Access Your Application

### Step 1: Get Application URL

Once deployed, Dokploy will provide a URL. It could be:
- `http://your-dokploy-ip:8501`
- `https://wordcloud-app.your-dokploy-domain.com`
- `https://your-assigned-subdomain.dokploy.com`

### Step 2: Test the Application

1. Open the URL in your browser
2. You should see: **"☁️ iSeeU Cloud"** header
3. Verify the interface loads correctly

### Step 3: Quick Functionality Test

Test basic features:

1. **Upload a mask image:**
   - Use the test_wc.png file
   - Or any black and white silhouette

2. **Enter text in "Text Input" tab:**
   ```
   HELLO WORLD CLOUD TEST WORD GENERATION
   ```

3. **Click "Generate Word Cloud"**

4. **Verify:**
   - Word cloud generates successfully
   - Black text on white background (default style)
   - Download button works

✅ **If all tests pass, deployment is successful!**

---

## Part 5: Troubleshooting Common Issues

### Issue 1: Build Fails

**Symptoms:**
- Red/failed status
- Build logs show errors

**Solutions:**

1. **Check Dockerfile path:**
   - Ensure it's `./Dockerfile` or just `Dockerfile`
   - Verify file exists in repository

2. **Check repository URL:**
   - Test the URL in a browser
   - Ensure it's accessible
   - Verify branch name is correct

3. **Check dependencies:**
   - Review build logs for specific errors
   - Verify requirements.txt is correct

**Fix and redeploy:**
```bash
# If you need to fix files
cd ~/wordcloud-project/wordcloud-app
# Make your changes
git add .
git commit -m "Fix: [describe the fix]"
git push origin main

# Then in Dokploy, click "Redeploy" or "Rebuild"
```

### Issue 2: Container Starts but App Not Accessible

**Symptoms:**
- Status shows "Running"
- But URL doesn't load

**Solutions:**

1. **Check port mapping:**
   - Verify port 8501 is mapped correctly
   - Check firewall settings

2. **Check logs:**
   ```bash
   # In Dokploy logs tab, look for:
   You can now view your Streamlit app in your browser.
   ```

3. **Verify health check:**
   - Wait 1-2 minutes for health check to pass
   - Check health check logs

### Issue 3: "Port Already in Use"

**Solutions:**

1. **Change port in compose file:**
   ```yaml
   ports:
     - "8502:8501"  # Use different host port
   ```

2. **Or let Dokploy auto-assign port**

### Issue 4: Font Upload Not Working

**Symptoms:**
- Error when uploading fonts
- Fonts don't apply

**Solutions:**

1. **Check file size limits:**
   - Fonts should be under 10MB
   - Check Dokploy upload limits

2. **Verify font format:**
   - Only .ttf or .otf files
   - Ensure files aren't corrupted

3. **Check container permissions:**
   - May need to adjust Dockerfile

---

## Part 6: Post-Deployment Configuration

### Enable HTTPS (Recommended)

1. In Dokploy, go to your application settings
2. Find SSL/HTTPS section
3. Enable SSL certificate (Let's Encrypt)
4. Dokploy will handle certificate generation

### Set Up Custom Domain

1. Point your domain DNS to Dokploy server
2. In Dokploy, add domain in "Domains" section
3. Enable SSL for the domain

### Configure Auto-Deploy (Optional)

To automatically redeploy on Git push:

1. In Dokploy, find "Webhooks" or "Auto Deploy"
2. Enable auto-deployment
3. Copy the webhook URL
4. Add webhook to your Git repository:

**For GitHub:**
- Repository → Settings → Webhooks
- Add webhook URL from Dokploy
- Content type: application/json
- Events: "Just the push event"

**For GitLab:**
- Project → Settings → Webhooks
- Add webhook URL
- Trigger: Push events

Now, every `git push` will trigger automatic redeployment!

---

## Part 7: Making Updates

### Method 1: Update Code and Redeploy

```bash
# Make your changes locally
cd ~/wordcloud-project/wordcloud-app
nano app.py  # or use your preferred editor

# Test locally (optional)
streamlit run app.py

# Commit changes
git add .
git commit -m "Update: added new color scheme"
git push origin main

# In Dokploy:
# If auto-deploy is enabled: Automatic ✨
# If not: Click "Redeploy" button
```

### Method 2: Update Docker Compose Config

1. In Dokploy, go to your application
2. Edit the Raw Compose configuration
3. Make changes (e.g., add environment variables)
4. Click "Save" or "Update"
5. Click "Redeploy"

---

## Part 8: Monitoring & Maintenance

### View Logs

**Real-time logs:**
1. Dokploy Dashboard → Your App → Logs
2. Watch in real-time for errors or issues

**Container logs:**
```bash
# If you have SSH access to Dokploy server
docker logs -f wordcloud-app
```

### Check Resource Usage

In Dokploy dashboard:
- CPU usage
- Memory usage
- Network traffic

### Set Resource Limits (Optional)

Update compose file to add limits:

```yaml
services:
  wordcloud:
    # ... existing config ...
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

### Backup Strategy

**Regular backups:**
1. **Code**: Already in Git ✅
2. **Configuration**: Export from Dokploy
3. **User uploads** (if any): Configure volume backups

---

## Quick Reference: Complete Raw Compose Configuration

Here's the complete Docker Compose configuration you need:

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
    # Optional: Add resource limits
    # deploy:
    #   resources:
    #     limits:
    #       cpus: '1.0'
    #       memory: 1G
    #     reservations:
    #       cpus: '0.5'
    #       memory: 512M
```

---

## Deployment Checklist

Use this checklist to ensure smooth deployment:

### Pre-Deployment
- [ ] All files copied to local directory
- [ ] Git repository created (GitHub/GitLab/Gitea)
- [ ] Files committed and pushed to repository
- [ ] Repository URL copied and ready
- [ ] Dokploy instance accessible

### Dokploy Configuration
- [ ] New application created in Dokploy
- [ ] "Docker Compose" deployment type selected
- [ ] Raw Compose configuration pasted
- [ ] Repository URL configured
- [ ] Branch set to "main"
- [ ] Port 8501 configured
- [ ] Environment variables set (optional)

### Post-Deployment
- [ ] Build logs checked for errors
- [ ] Deployment status shows "Running"
- [ ] Application URL accessible
- [ ] Basic functionality tested
- [ ] Domain configured (optional)
- [ ] HTTPS enabled (recommended)
- [ ] Auto-deploy configured (optional)

---

## Getting Help

If you encounter issues:

1. **Check the logs first** - Most issues show up in logs
2. **Review this guide** - Ensure all steps followed correctly
3. **Test locally** - Rule out code issues: `streamlit run app.py`
4. **Check Dokploy documentation** - Your Dokploy version may have specifics
5. **Verify repository** - Ensure all files are present and accessible

---

## Success Criteria

Your deployment is successful when:
- ✅ Application loads at the provided URL
- ✅ You can see "☁️ iSeeU Cloud" header
- ✅ Sidebar shows configuration options
- ✅ You can upload mask images
- ✅ You can generate word clouds
- ✅ Download button works
- ✅ Status in Dokploy shows "Running" (green)
- ✅ Health checks pass

---

## Next Steps After Successful Deployment

1. **Share the URL** with your users
2. **Configure custom domain** for professional URL
3. **Enable HTTPS** for security
4. **Set up monitoring** to track usage
5. **Create backups** of your configuration
6. **Document any customizations** you make

---

**Congratulations! Your WordCloud app is now live on Dokploy!** 🎉

For detailed usage instructions, refer to:
- `EXAMPLES.md` - Usage examples
- `QUICK_REFERENCE.md` - Quick commands
- `README.md` - Full documentation
