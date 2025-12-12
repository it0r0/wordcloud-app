import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="iSeeU - WordCloud Generator",
    page_icon="☁️",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">☁️ iSeeU - WordCloud Generator</div>', unsafe_allow_html=True)

# Sidebar for configuration
st.sidebar.title("⚙️ Configuration")

# Font upload section
st.sidebar.markdown("### 📝 Font Files")
uploaded_fonts = st.sidebar.file_uploader(
    "Upload Font Files (.ttf, .otf)",
    type=["ttf", "otf"],
    accept_multiple_files=True,
    help="Upload one or more font files to use in the word cloud"
)

# Save uploaded fonts temporarily
font_paths = []
if uploaded_fonts:
    fonts_dir = Path("/tmp/fonts")
    fonts_dir.mkdir(exist_ok=True)
    
    for font_file in uploaded_fonts:
        font_path = fonts_dir / font_file.name
        with open(font_path, "wb") as f:
            f.write(font_file.getbuffer())
        font_paths.append(str(font_path))
    
    st.sidebar.success(f"✅ {len(font_paths)} font(s) loaded")
else:
    st.sidebar.info("Using default font")

# Font size configuration
st.sidebar.markdown("### 📏 Font Size Range")
col1, col2 = st.sidebar.columns(2)
with col1:
    min_font_size = st.number_input(
        "Min Size",
        min_value=4,
        max_value=100,
        value=10,
        step=1,
        help="Minimum font size for words"
    )
with col2:
    max_font_size = st.number_input(
        "Max Size",
        min_value=10,
        max_value=500,
        value=100,
        step=10,
        help="Maximum font size for words"
    )

# Word cloud configuration
st.sidebar.markdown("### 🎨 Word Cloud Settings")
background_color = st.sidebar.color_picker(
    "Background Color",
    "#FFFFFF",
    help="Background color of the word cloud"
)

colormap = st.sidebar.selectbox(
    "Color Scheme",
    ["viridis", "plasma", "inferno", "magma", "cividis", "twilight", "turbo", "rainbow", "jet", "hsv"],
    help="Color map for the words"
)

width = st.sidebar.slider("Width (pixels)", 400, 2000, 800, step=100)
height = st.sidebar.slider("Height (pixels)", 400, 2000, 600, step=100)

# Main content area
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown('<div class="section-header">📤 Upload Silhouette</div>', unsafe_allow_html=True)
    uploaded_mask = st.file_uploader(
        "Upload a black and white silhouette image",
        type=["png", "jpg", "jpeg"],
        help="Upload a silhouette image where white areas will be filled with words"
    )
    
    if uploaded_mask:
        mask_image = Image.open(uploaded_mask)
        st.image(mask_image, caption="Uploaded Silhouette", use_container_width=True)

with col_right:
    st.markdown('<div class="section-header">💬 Word Input</div>', unsafe_allow_html=True)
    
    # Tab for different word categories
    tab1, tab2 = st.tabs(["🔥 Priority Words", "📝 Regular Words"])
    
    with tab1:
        st.markdown("**High Priority Words** (will appear larger)")
        priority_words = st.text_area(
            "Enter priority words (one per line or comma-separated)",
            height=150,
            placeholder="Important\nKeyword\nHighlight",
            help="These words will appear larger in the word cloud",
            key="priority"
        )
        
        priority_weight = st.slider(
            "Priority Multiplier",
            1.0,
            10.0,
            3.0,
            0.5,
            help="How much larger should priority words be?"
        )
    
    with tab2:
        st.markdown("**Regular Words**")
        regular_words = st.text_area(
            "Enter regular words (one per line or comma-separated)",
            height=150,
            placeholder="word1\nword2\nword3",
            help="These words will appear at normal sizes",
            key="regular"
        )

# Additional options
st.markdown('<div class="section-header">🔧 Advanced Options</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    relative_scaling = st.slider(
        "Relative Scaling",
        0.0,
        1.0,
        0.5,
        0.1,
        help="0 = font sizes are determined by frequency only, 1 = font sizes vary greatly"
    )

with col2:
    prefer_horizontal = st.slider(
        "Horizontal Preference",
        0.0,
        1.0,
        0.9,
        0.1,
        help="Probability of words being horizontal (0=all vertical, 1=all horizontal)"
    )

with col3:
    max_words = st.number_input(
        "Max Words",
        min_value=10,
        max_value=1000,
        value=200,
        step=10,
        help="Maximum number of words to display"
    )

# Generate button
if st.button("🎨 Generate Word Cloud", type="primary", use_container_width=True):
    # Validate inputs
    if not priority_words and not regular_words:
        st.error("⚠️ Please enter at least some words!")
    else:
        with st.spinner("Generating word cloud..."):
            try:
                # Parse words
                def parse_words(text):
                    if not text:
                        return []
                    # Handle both newline and comma separated
                    words = text.replace(',', '\n').split('\n')
                    return [w.strip() for w in words if w.strip()]
                
                priority_list = parse_words(priority_words)
                regular_list = parse_words(regular_words)
                
                # Create word frequency dictionary
                word_freq = {}
                
                # Add priority words with higher frequency
                for word in priority_list:
                    word_freq[word] = int(100 * priority_weight)
                
                # Add regular words with normal frequency
                for word in regular_list:
                    if word not in word_freq:  # Don't override priority words
                        word_freq[word] = 10
                
                # Prepare mask if provided
                mask = None
                if uploaded_mask:
                    mask_image_array = np.array(Image.open(uploaded_mask))
                    # Convert to grayscale if needed
                    if len(mask_image_array.shape) == 3:
                        mask = mask_image_array[:, :, 0]
                    else:
                        mask = mask_image_array
                
                # Function to randomly select font (if multiple are provided)
                def font_function(font_size, font_path=None, orientation=None, **kwargs):
                    if font_paths:
                        return np.random.choice(font_paths)
                    return None
                
                # Generate word cloud
                wordcloud = WordCloud(
                    width=width,
                    height=height,
                    background_color=background_color,
                    mask=mask,
                    colormap=colormap,
                    font_path=font_paths[0] if font_paths else None,
                    min_font_size=min_font_size,
                    max_font_size=max_font_size,
                    relative_scaling=relative_scaling,
                    prefer_horizontal=prefer_horizontal,
                    max_words=max_words,
                    random_state=42
                ).generate_from_frequencies(word_freq)
                
                # If multiple fonts, regenerate with random font selection
                if len(font_paths) > 1:
                    wordcloud = WordCloud(
                        width=width,
                        height=height,
                        background_color=background_color,
                        mask=mask,
                        colormap=colormap,
                        font_path=font_function,
                        min_font_size=min_font_size,
                        max_font_size=max_font_size,
                        relative_scaling=relative_scaling,
                        prefer_horizontal=prefer_horizontal,
                        max_words=max_words,
                        random_state=42
                    ).generate_from_frequencies(word_freq)
                
                # Display the word cloud
                st.markdown('<div class="section-header">✨ Generated Word Cloud</div>', unsafe_allow_html=True)
                
                fig, ax = plt.subplots(figsize=(15, 10))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                plt.tight_layout(pad=0)
                
                st.pyplot(fig)
                
                # Download button
                buf = io.BytesIO()
                wordcloud.to_image().save(buf, format='PNG')
                buf.seek(0)
                
                st.download_button(
                    label="⬇️ Download Word Cloud",
                    data=buf,
                    file_name="wordcloud.png",
                    mime="image/png",
                    use_container_width=True
                )
                
                st.success("✅ Word cloud generated successfully!")
                
            except Exception as e:
                st.error(f"❌ Error generating word cloud: {str(e)}")
                st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>Made with ❤️ using Streamlit and WordCloud</p>
        <p>Upload a silhouette, customize your settings, and create beautiful word clouds!</p>
    </div>
""", unsafe_allow_html=True)
