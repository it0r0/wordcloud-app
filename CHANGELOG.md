# Changelog

All notable changes to the WordCloud App will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-12-13

### Added
- **Multiple Font Support**: Upload and use multiple font files (.ttf, .otf) simultaneously
- **Font Size Range Control**: Adjustable minimum (4-100px) and maximum (10-500px) font sizes
- **Priority Word Categories**: Separate input for high-priority vs regular words
- **Priority Multiplier**: Adjust how much larger priority words appear (1x-10x)
- **Enhanced UI**: Modern, organized interface with tabs and sections
- **Color Picker**: Custom background color selection
- **10+ Color Schemes**: Multiple colormap options for word styling
- **Canvas Size Control**: Adjustable width and height (400-2000px)
- **Advanced Settings**: 
  - Relative scaling control
  - Horizontal/vertical text preference
  - Maximum word count adjustment
- **Download Feature**: Direct PNG download of generated word clouds
- **Docker Support**: Full containerization with Dockerfile and docker-compose
- **Dokploy Ready**: Complete deployment configuration for Dokploy platform
- **Comprehensive Documentation**:
  - README.md with full feature documentation
  - DOKPLOY_DEPLOYMENT.md for deployment guide
  - EXAMPLES.md with usage examples
  - QUICK_REFERENCE.md for quick access
  - CHANGELOG.md for version tracking

### Changed
- Improved word input interface with tabs
- Better error handling and user feedback
- Enhanced visual feedback during generation
- Optimized silhouette mask processing
- Updated UI with custom CSS styling
- Reorganized settings in logical sections

### Technical Updates
- Streamlit 1.31.0
- WordCloud 1.9.3
- Matplotlib 3.8.2
- NumPy 1.26.3
- Pillow 10.2.0
- Added .streamlit/config.toml for better configuration
- Added health checks for Docker deployments
- Implemented proper file handling for uploads

### Fixed
- Font loading and rendering issues
- Silhouette mask conversion edge cases
- Memory optimization for large images
- Better handling of invalid inputs

## [1.0.0] - Initial Release

### Added
- Basic word cloud generation
- Silhouette image upload
- Single font support (Montserrat-Bold.otf)
- Basic word input
- Simple Streamlit interface
- Requirements.txt for dependencies
- Basic README

---

## Upcoming Features (Roadmap)

### [2.1.0] - Planned
- [ ] Word frequency analysis from text files
- [ ] Preset templates (heart, star, circle, etc.)
- [ ] Color customization per word
- [ ] Export to multiple formats (SVG, PDF)
- [ ] Batch generation from CSV
- [ ] Interactive word cloud editor
- [ ] Save/load configurations
- [ ] User profiles and history

### [2.2.0] - Planned
- [ ] API endpoint for programmatic access
- [ ] Webhook integration
- [ ] Cloud storage integration
- [ ] Collaboration features
- [ ] Gallery of generated word clouds
- [ ] A/B testing for different designs
- [ ] Analytics dashboard

### [3.0.0] - Future
- [ ] AI-powered word suggestions
- [ ] Animated word clouds
- [ ] 3D word cloud generation
- [ ] Video word cloud generator
- [ ] Mobile app version
- [ ] Plugin system for extensions

---

## Version History Summary

| Version | Date | Key Features |
|---------|------|--------------|
| 2.0.0 | 2024-12-13 | Multi-font, priority words, Dokploy deployment |
| 1.0.0 | Earlier | Initial release with basic features |

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## Migration Guide

### From 1.x to 2.x

**Breaking Changes:**
- None - fully backward compatible

**New Features Available:**
1. Upload multiple fonts instead of relying on single default font
2. Use priority word categories for better control
3. Adjust font size ranges for more dramatic effects

**Recommended Updates:**
```python
# Old way (still works):
words = ["word1", "word2", "word3"]

# New way (recommended):
priority_words = ["important", "keyword"]
regular_words = ["word1", "word2", "word3"]
```

---

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Check documentation in `/docs`
- Review troubleshooting guide

## License

This project is licensed under the Apache License 2.0.

---

**Note**: This is an active project. Features and improvements are continuously being added.
Check back regularly for updates!
