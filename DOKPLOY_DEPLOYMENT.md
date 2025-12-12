# 🚀 Dokploy Deployment Guide

This guide walks you through deploying the WordCloud app on Dokploy.

## Prerequisites

- A Dokploy instance (self-hosted or cloud)
- Git repository containing this code
- Basic familiarity with Dokploy interface

## Deployment Methods

### Method 1: Using Dokploy UI (Recommended)

#### Step 1: Prepare Your Repository

1. Create a new repository on GitHub/GitLab/Gitea
2. Push this code to your repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: WordCloud app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/wordcloud-app.git
   git push -u origin main
   ```

#### Step 2: Create Application in Dokploy

1. Log into your Dokploy dashboard
2. Click on "Applications" in the sidebar
3. Click "Create Application" button
4. Fill in the details:
   - **Application Name**: `wordcloud-app`
   - **Application Type**: Select "Docker"
   - **Repository URL**: Your Git repository URL
   - **Branch**: `main`
   - **Build Type**: Choose "Dockerfile"

#### Step 3: Configure Build Settings

1. **Dockerfile Path**: `./Dockerfile`
2. **Docker Context**: `./`
3. **Build Arguments**: (leave empty unless needed)

#### Step 4: Configure Runtime Settings

1. **Port Mapping**:
   - Container Port: `8501`
   - Host Port: `8501` (or auto-assign)

2. **Environment Variables** (optional but recommended):
   ```
   STREAMLIT_SERVER_PORT=8501
   STREAMLIT_SERVER_ADDRESS=0.0.0.0
   STREAMLIT_SERVER_HEADLESS=true
   STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
   ```

3. **Health Check**:
   - Enable health check
   - Path: `/_stcore/health`
   - Interval: 30s
   - Timeout: 10s

#### Step 5: Configure Domain (Optional)

1. In the "Domains" section, add your custom domain
2. Or use the Dokploy-provided subdomain
3. Enable HTTPS if desired

#### Step 6: Deploy

1. Click "Create and Deploy"
2. Monitor the build logs in real-time
3. Wait for deployment to complete (usually 2-5 minutes)

#### Step 7: Verify Deployment

1. Once deployed, click on the application URL
2. You should see the WordCloud app interface
3. Test by uploading a font and generating a word cloud

### Method 2: Using Docker Compose in Dokploy

If your Dokploy instance supports Docker Compose deployments:

1. In Dokploy, create a new application
2. Select "Docker Compose" as the deployment type
3. Point to your repository
4. Dokploy will automatically detect the `docker-compose.yml` file
5. Deploy

### Method 3: Manual Docker Deployment on Dokploy Server

If you have SSH access to your Dokploy server:

```bash
# SSH into your Dokploy server
ssh user@your-dokploy-server.com

# Clone the repository
git clone https://github.com/YOUR_USERNAME/wordcloud-app.git
cd wordcloud-app

# Build and run
docker build -t wordcloud-app .
docker run -d \
  --name wordcloud-app \
  -p 8501:8501 \
  --restart unless-stopped \
  wordcloud-app
```

## Post-Deployment Configuration

### Setting Up Automatic Updates

Enable auto-deployment in Dokploy:

1. Go to your application settings
2. Enable "Auto Deploy" option
3. Configure webhook (if using GitHub/GitLab)
4. Now, every push to `main` branch will trigger redeployment

### Configuring Resource Limits

To prevent the app from consuming too many resources:

1. In Dokploy, go to application settings
2. Set resource limits:
   - **Memory Limit**: 512MB - 1GB (recommended)
   - **CPU Limit**: 0.5 - 1.0 CPU core
   - **Memory Reservation**: 256MB

### Setting Up Persistent Storage (Optional)

If you want to persist uploaded fonts:

1. Create a volume in Dokploy
2. Mount it to `/app/fonts` in the container
3. Update docker-compose.yml if needed

## Monitoring and Maintenance

### Viewing Logs

In Dokploy:
1. Navigate to your application
2. Click on "Logs" tab
3. View real-time logs

Or via command line:
```bash
docker logs -f wordcloud-app
```

### Updating the Application

When you make changes to the code:

1. Commit and push to your repository:
   ```bash
   git add .
   git commit -m "Update: description of changes"
   git push origin main
   ```

2. If auto-deploy is enabled, Dokploy will automatically rebuild and redeploy

3. If not, manually trigger redeploy in Dokploy UI

### Rollback

If something goes wrong:

1. In Dokploy, go to your application
2. Click on "Deployments" tab
3. Find the previous working deployment
4. Click "Rollback to this version"

## Troubleshooting

### Issue: Application Won't Start

**Check:**
- Logs in Dokploy dashboard
- Port 8501 is not already in use
- Dockerfile builds successfully locally

**Solution:**
```bash
# Test build locally
docker build -t wordcloud-test .
docker run -p 8501:8501 wordcloud-test

# Check logs
docker logs wordcloud-test
```

### Issue: Font Upload Not Working

**Check:**
- File size limits in Dokploy/reverse proxy
- Streamlit max upload size

**Solution:**
- Increase upload size limit in `.streamlit/config.toml`:
  ```toml
  [server]
  maxUploadSize = 200
  ```

### Issue: High Memory Usage

**Solution:**
- Reduce image size limits
- Add memory limits in Dokploy:
  ```
  Memory Limit: 1GB
  Memory Reservation: 512MB
  ```

### Issue: Slow Generation

**Check:**
- Server resources
- Image sizes being processed

**Solution:**
- Limit max words in the UI
- Reduce canvas size defaults
- Optimize images before upload

## Security Best Practices

1. **Environment Variables**: Store sensitive data in Dokploy's environment variables, not in code

2. **HTTPS**: Always enable HTTPS for production deployments

3. **Access Control**: Use Dokploy's authentication features if needed

4. **Updates**: Regularly update dependencies:
   ```bash
   pip list --outdated
   # Update requirements.txt accordingly
   ```

## Scaling Considerations

For high-traffic scenarios:

1. **Horizontal Scaling**: 
   - Deploy multiple instances behind Dokploy's load balancer
   
2. **Resource Optimization**:
   - Cache generated word clouds (add Redis)
   - Use background job queue for heavy processing

3. **CDN**: 
   - Serve static assets through CDN
   - Cache frequently generated word clouds

## Backup Strategy

Regular backups:

1. **Code**: Already in Git repository ✅
2. **User-uploaded fonts**: Configure volume backup in Dokploy
3. **Configuration**: Export Dokploy application settings

## Advanced Configuration

### Custom Nginx Configuration

If you need custom reverse proxy settings:

1. In Dokploy, add custom Nginx config
2. Example for handling large uploads:
   ```nginx
   client_max_body_size 50M;
   proxy_read_timeout 300;
   proxy_connect_timeout 300;
   proxy_send_timeout 300;
   ```

### Environment-Specific Settings

For staging vs production:

```bash
# Staging
STREAMLIT_SERVER_PORT=8501
ENVIRONMENT=staging

# Production  
STREAMLIT_SERVER_PORT=8501
ENVIRONMENT=production
```

## Cost Optimization

1. **Right-size resources**: Don't over-provision
2. **Use auto-scaling**: Scale down during low traffic
3. **Optimize images**: Compress Docker images
4. **Cache aggressively**: Reduce compute time

## Getting Help

- **Dokploy Documentation**: https://docs.dokploy.com
- **Streamlit Forums**: https://discuss.streamlit.io
- **GitHub Issues**: Open issue in your repository

## Next Steps

After successful deployment:

1. ✅ Test all features thoroughly
2. ✅ Set up monitoring/alerts
3. ✅ Configure custom domain
4. ✅ Enable HTTPS
5. ✅ Set up automated backups
6. ✅ Document any custom configurations
7. ✅ Share with users!

---

**Congratulations!** 🎉 Your WordCloud app is now deployed on Dokploy!
