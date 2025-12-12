# ☁️ iSeeU - WordCloud Generator

An advanced word cloud generator that creates beautiful word clouds fitted to silhouette images with customizable fonts, sizes, and word priorities.

## ✨ Features

### New Features Added

1. **Multiple Font Support** 🎨
   - Upload multiple font files (.ttf, .otf)
   - Mix different fonts in the same word cloud
   - Fallback to system fonts if no custom fonts provided

2. **Font Size Control** 📏
   - Adjustable minimum and maximum font sizes
   - Full control over size range (4px to 500px)
   - Fine-tune text size variability

3. **Priority Word Categories** 🔥
   - Separate input for high-priority words
   - Adjustable priority multiplier (1x to 10x)
   - Regular words with standard sizing
   - Priority words automatically appear larger

4. **Advanced Customization** ⚙️
   - Background color picker
   - 10+ color schemes
   - Adjustable word density (max words)
   - Relative scaling control
   - Horizontal/vertical text preference
   - Custom canvas dimensions

## 🚀 Deployment on Dokploy

### Prerequisites

- Dokploy instance running
- Git repository with this code
- Docker support enabled

### Step-by-Step Deployment

1. **Push Code to Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Dokploy**
   
   a. Log in to your Dokploy dashboard
   
   b. Click "Create Application"
   
   c. Select "Docker Compose" or "Dockerfile" deployment
   
   d. Configure:
      - **Name**: wordcloud-app
      - **Repository**: Your Git repository URL
      - **Branch**: main
      - **Port**: 8501
      - **Dockerfile Path**: ./Dockerfile (if using Dockerfile deployment)
   
   e. Set Environment Variables (optional):
      ```
      STREAMLIT_SERVER_PORT=8501
      STREAMLIT_SERVER_ADDRESS=0.0.0.0
      STREAMLIT_SERVER_HEADLESS=true
      ```
   
   f. Click "Deploy"

3. **Access Your Application**
   - Once deployed, Dokploy will provide a URL
   - Access your word cloud generator at: `https://your-dokploy-domain.com`

### Alternative: Docker Compose Deployment

If your Dokploy supports Docker Compose:

```bash
# Clone your repository on the server
git clone YOUR_REPO_URL
cd wordcloud-app

# Deploy using Docker Compose
docker-compose up -d
```

## 💻 Local Development

### Installation

1. Clone the repository:
   ```bash
   git clone YOUR_REPO_URL
   cd wordcloud-app
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open browser to `http://localhost:8501`

### Docker Development

```bash
# Build image
docker build -t wordcloud-app .

# Run container
docker run -p 8501:8501 wordcloud-app
```

## 📖 Usage Guide

### Basic Workflow

1. **Upload Silhouette** (optional)
   - Use a black and white image
   - White areas will be filled with words
   - Black areas remain empty

2. **Upload Fonts** (optional)
   - Upload one or more .ttf or .otf font files
   - Multiple fonts will be randomly mixed
   - Leave empty to use default font

3. **Configure Font Sizes**
   - Set minimum size (4-100px)
   - Set maximum size (10-500px)
   - Larger range = more size variability

4. **Enter Words**
   - **Priority Words Tab**: Words you want larger/prominent
   - **Regular Words Tab**: Standard words
   - Separate words by newlines or commas
   - Adjust priority multiplier (how much bigger priority words should be)

5. **Customize Appearance**
   - Choose background color
   - Select color scheme
   - Adjust canvas size
   - Fine-tune advanced settings

6. **Generate**
   - Click "Generate Word Cloud"
   - Download the result as PNG

### Tips for Best Results

- **For Silhouettes**: Use high-contrast black and white images
- **Font Selection**: Mix serif and sans-serif fonts for visual interest
- **Priority Words**: Use 3-10 priority words for best effect
- **Size Range**: Wider range (10-200) gives more dramatic effect
- **Color Schemes**: 
  - `viridis`, `plasma`: Professional, scientific
  - `rainbow`, `turbo`: Colorful, playful
  - `twilight`: Elegant, subtle

## 🔧 Configuration Options

### Font Size Range
- **Min Font Size**: 4-100px (default: 10px)
- **Max Font Size**: 10-500px (default: 100px)

### Priority Multiplier
- Range: 1.0x - 10.0x (default: 3.0x)
- Higher values = more size difference

### Advanced Options
- **Relative Scaling**: Controls size variation (0.0-1.0)
- **Horizontal Preference**: Word orientation (0.0-1.0)
- **Max Words**: Maximum words displayed (10-1000)

## 📦 Project Structure

```
wordcloud-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker build exclusions
├── .gitignore           # Git exclusions
└── README.md            # This file
```

## 🔄 Updating the Deployed App

### Method 1: Git Push (Recommended)

If you have auto-deploy enabled on Dokploy:

```bash
# Make your changes
git add .
git commit -m "Your update message"
git push origin main
```

Dokploy will automatically detect the changes and redeploy.

### Method 2: Manual Redeploy

1. Push changes to Git
2. Go to Dokploy dashboard
3. Find your application
4. Click "Redeploy" or "Rebuild"

### Method 3: Direct Update

For quick updates on the server:

```bash
# SSH into your server
cd /path/to/wordcloud-app
git pull
docker-compose down
docker-compose up -d --build
```

## 🛠️ Troubleshooting

### Common Issues

1. **Font Upload Not Working**
   - Ensure fonts are .ttf or .otf format
   - Check file size (keep under 10MB per font)

2. **Word Cloud Not Generating**
   - Verify words are entered (at least in one category)
   - Check if mask image is valid (should be black and white)

3. **Container Won't Start**
   - Check logs: `docker logs wordcloud-app`
   - Verify port 8501 is available
   - Ensure all dependencies are installed

4. **Memory Issues**
   - Reduce canvas size (width/height)
   - Decrease max words count
   - Use smaller images for masks

## 📝 Dependencies

- **streamlit**: Web framework
- **wordcloud**: Word cloud generation
- **matplotlib**: Visualization
- **numpy**: Array operations
- **Pillow**: Image processing

## 🤝 Contributing

To add new features or fix bugs:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the Apache License 2.0.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Word cloud generation by [wordcloud library](https://github.com/amueller/word_cloud)
- Deployed on [Dokploy](https://dokploy.com/)

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review Dokploy documentation

---

Made with ❤️ for creating beautiful word clouds
