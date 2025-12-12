# 🎯 Quick Reference Guide

## Essential Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 8502
```

### Docker Commands
```bash
# Build image
docker build -t wordcloud-app .

# Run container
docker run -p 8501:8501 wordcloud-app

# View logs
docker logs -f wordcloud-app

# Stop container
docker stop wordcloud-app

# Remove container
docker rm wordcloud-app
```

### Docker Compose Commands
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart
docker-compose up -d --build

# View running services
docker-compose ps
```

### Git Workflow
```bash
# Initial setup
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main

# Regular updates
git add .
git commit -m "Description of changes"
git push origin main
```

## Feature Settings Quick Reference

### Font Sizes
| Use Case | Min Size | Max Size | Multiplier |
|----------|----------|----------|------------|
| Subtle | 15 | 60 | 2.0x |
| Normal | 10 | 100 | 3.0x |
| Dramatic | 10 | 200 | 5.0x |
| Extreme | 5 | 300 | 8.0x |

### Canvas Sizes
| Purpose | Width | Height |
|---------|-------|--------|
| Preview | 600 | 400 |
| Standard | 800 | 600 |
| High Quality | 1600 | 1200 |
| Large Display | 2000 | 2000 |
| Instagram | 1080 | 1080 |
| Facebook | 1200 | 630 |
| Twitter | 1200 | 675 |

### Color Schemes by Mood
| Mood | Recommended Schemes |
|------|---------------------|
| Professional | viridis, cividis, twilight |
| Energetic | plasma, inferno, turbo |
| Fun | rainbow, jet, hsv |
| Elegant | twilight, magma |
| Technical | viridis, cividis |

### Word Count Guidelines
| Canvas Size | Max Words |
|-------------|-----------|
| Small (600x400) | 50-100 |
| Medium (800x600) | 100-150 |
| Large (1600x1200) | 150-250 |
| Extra Large (2000x2000) | 200-400 |

## Keyboard Shortcuts in Streamlit

| Action | Shortcut |
|--------|----------|
| Rerun app | `Ctrl/Cmd + R` |
| Clear cache | `C` |
| Settings | `S` |
| View source | `?` |

## Troubleshooting Checklist

### App Won't Start
- [ ] Check port 8501 is available
- [ ] Verify all dependencies installed
- [ ] Check Python version (3.8+)
- [ ] Review error logs

### Font Upload Issues
- [ ] File is .ttf or .otf format
- [ ] File size under 10MB
- [ ] Font file not corrupted
- [ ] Check browser console for errors

### Generation Fails
- [ ] At least one word entered
- [ ] Silhouette image is valid (if uploaded)
- [ ] Image not too large (under 10MB)
- [ ] Valid font size range (min < max)

### Slow Performance
- [ ] Reduce canvas size
- [ ] Decrease max words
- [ ] Use smaller silhouette images
- [ ] Close other heavy applications

## File Size Limits

| Item | Recommended | Maximum |
|------|-------------|---------|
| Font file | < 2MB | 10MB |
| Silhouette | < 1MB | 5MB |
| Total upload | < 5MB | 50MB |

## Environment Variables

```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Optional
STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
STREAMLIT_SERVER_ENABLE_CORS=false
```

## Dokploy Deployment Checklist

- [ ] Code pushed to Git repository
- [ ] Dockerfile present and tested
- [ ] Requirements.txt up to date
- [ ] Port 8501 configured
- [ ] Environment variables set
- [ ] Health check configured
- [ ] Domain/subdomain configured
- [ ] HTTPS enabled
- [ ] Resource limits set
- [ ] Auto-deploy enabled (optional)

## Update Procedure

1. Make changes to code
2. Test locally: `streamlit run app.py`
3. Commit: `git commit -am "Description"`
4. Push: `git push origin main`
5. Verify deployment in Dokploy
6. Test production URL
7. Monitor logs for errors

## Performance Optimization

### For Speed
- Reduce canvas size
- Limit max words (50-100)
- Use simpler silhouettes
- Smaller font size range

### For Quality
- Increase canvas size (1600x1200+)
- More words (200-300)
- Wider font size range
- High-resolution silhouettes

## Common Error Messages

| Error | Solution |
|-------|----------|
| "Port already in use" | Stop other app on port 8501 or use different port |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Permission denied" | Check file permissions: `chmod +x file.sh` |
| "Out of memory" | Reduce image sizes or increase container memory |
| "Invalid font" | Ensure font file is not corrupted |

## Best Practices

### ✅ Do
- Test locally before deploying
- Use version control (Git)
- Set resource limits in production
- Regular backups
- Monitor logs
- Document custom changes
- Use meaningful commit messages

### ❌ Don't
- Commit sensitive data (API keys, passwords)
- Upload corrupted fonts
- Use extremely large images
- Ignore error logs
- Deploy without testing
- Skip documentation

## Support Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **WordCloud Docs**: https://amueller.github.io/word_cloud/
- **Dokploy Docs**: https://docs.dokploy.com
- **Docker Docs**: https://docs.docker.com

## Quick Links

- Local App: http://localhost:8501
- Health Check: http://localhost:8501/_stcore/health
- Container Stats: `docker stats wordcloud-app`
- Logs: `docker logs -f wordcloud-app`

---

💡 **Pro Tip**: Bookmark this page for quick reference!
