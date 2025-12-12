import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import io
import os
from pathlib import Path
import tempfile

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

st.markdown('<div class="main-header">☁️ iSeeU Cloud</div>', unsafe_allow_html=True)

# Initialize session state
if 'wordcloud' not in st.session_state:
    st.session_state.wordcloud = None

# Function to transform mask image (from original)
def transform_format(val):
    """Transform mask values to proper format for wordcloud"""
    if val != 0:
        return 255
    else:
        return 0

# Sidebar for configuration
st.sidebar.title("⚙️ Configuration")

# Font upload section (NEW FEATURE #1)
st.sidebar.markdown("### 📝 Font Files")
uploaded_fonts = st.sidebar.file_uploader(
    "Upload Font Files (.ttf, .otf)",
    type=["ttf", "otf"],
    accept_multiple_files=True,
    help="Upload one or more font files to use in the word cloud"
)

# Check for default font from original
default_font_path = './Montserrat-Bold.otf'
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
elif os.path.exists(default_font_path):
    font_paths = [default_font_path]
    st.sidebar.info("Using default Montserrat-Bold font")
else:
    st.sidebar.info("Using system default font")

# Font size configuration (NEW FEATURE #2)
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

# Keep original black-on-white option or allow color
use_original_style = st.sidebar.checkbox(
    "Use Original Black-on-White Style",
    value=True,
    help="Mimics the original iSeeU style with black text on white background"
)

if not use_original_style:
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
else:
    background_color = "white"
    colormap = None

max_words = st.sidebar.number_input(
    "Max Words",
    min_value=10,
    max_value=1000,
    value=200,
    step=10,
    help="Maximum number of words to display"
)

repeat_words = st.sidebar.checkbox(
    "Repeat Words",
    value=True,
    help="Allow words to appear multiple times (original behavior)"
)

# Main content area
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown('<div class="section-header">📤 Upload Mask Image</div>', unsafe_allow_html=True)
    mask_image = st.file_uploader(
        "Upload a black and white silhouette image",
        type=["png", "jpg", "jpeg"],
        help="Upload a silhouette image where white areas will be filled with words"
    )
    
    if mask_image:
        mask_img_display = Image.open(mask_image)
        st.image(mask_img_display, caption="Uploaded Silhouette", use_container_width=True)

with col_right:
    st.markdown('<div class="section-header">💬 Word Input</div>', unsafe_allow_html=True)
    
    # Tab for different word categories (NEW FEATURE #3)
    tab1, tab2, tab3 = st.tabs(["🔥 Priority Words", "📝 Regular Words", "📄 Text Input"])
    
    with tab1:
        st.markdown("**High Priority Words** (will appear larger)")
        priority_words = st.text_area(
            "Enter priority words (one per line or comma-separated)",
            height=120,
            placeholder="Important\nKeyword\nHighlight",
            help="These words will appear larger in the word cloud",
            key="priority"
        )
        
        priority_weight = st.slider(
            "Priority Multiplier",
            1.0,
            10.0,
            5.0,
            0.5,
            help="How much larger should priority words be?"
        )
    
    with tab2:
        st.markdown("**Regular Words**")
        regular_words = st.text_area(
            "Enter regular words (one per line or comma-separated)",
            height=120,
            placeholder="word1\nword2\nword3",
            help="These words will appear at normal sizes",
            key="regular"
        )
    
    with tab3:
        st.markdown("**Full Text Input** (original method)")
        full_text = st.text_area(
            "Enter full text (like original app)",
            height=120,
            placeholder="Enter your text here...",
            help="Original iSeeU method - enter full text and stopwords will be filtered",
            key="fulltext"
        )

# Function to generate word cloud (enhanced from original)
def generate_word_cloud(text, priority_text, regular_text, mask_image, font_path, 
                       min_size, max_size, bg_color, colormap, max_words, repeat,
                       priority_mult, use_black_style):
    """
    Generate word cloud combining original functionality with new features
    """
    # Setup stopwords (from original)
    stopwords = set(STOPWORDS)
    stopwords.update(["drink", "now", "wine", "flavor", "flavors"])
    
    # Process mask if provided (original method)
    if mask_image is not None:
        mask = np.array(Image.open(mask_image).convert('L'))
        transformed_mask = np.ndarray((mask.shape[0], mask.shape[1]), np.int32)
        for i in range(len(mask)):
            transformed_mask[i] = list(map(transform_format, mask[i]))
    else:
        st.warning("Please upload a mask image.")
        return None
    
    # Black color function from original
    def black_color_func(word=None, font_size=None, position=None, 
                        orientation=None, font_path=None, random_state=None):
        return "rgb(0, 0, 0)"
    
    # Determine if using word frequency method or text method
    use_frequency = bool(priority_text or regular_text)
    
    if use_frequency:
        # NEW: Priority word method
        def parse_words(text):
            if not text:
                return []
            words = text.replace(',', '\n').split('\n')
            return [w.strip() for w in words if w.strip()]
        
        priority_list = parse_words(priority_text)
        regular_list = parse_words(regular_text)
        
        # Create word frequency dictionary
        word_freq = {}
        
        # Add priority words with higher frequency
        for word in priority_list:
            word_freq[word.upper()] = int(100 * priority_mult)
        
        # Add regular words
        for word in regular_list:
            if word.upper() not in word_freq:
                word_freq[word.upper()] = 10
        
        if not word_freq:
            st.warning("Please enter at least some words.")
            return None
        
        # Create WordCloud with frequency
        wc = WordCloud(
            background_color=bg_color,
            mask=transformed_mask,
            font_path=font_path if font_path else None,
            stopwords=stopwords,
            max_words=max_words,
            repeat=repeat,
            min_font_size=min_size,
            max_font_size=max_size,
            colormap=colormap if not use_black_style else None,
            color_func=black_color_func if use_black_style else None
        )
        wc.generate_from_frequencies(word_freq)
    else:
        # ORIGINAL: Text method
        if not text:
            st.warning("Please enter some text.")
            return None
        
        wc = WordCloud(
            background_color=bg_color,
            mask=transformed_mask,
            font_path=font_path if font_path else None,
            stopwords=stopwords,
            max_words=max_words,
            repeat=repeat,
            min_font_size=min_size,
            max_font_size=max_size,
            colormap=colormap if not use_black_style else None,
            color_func=black_color_func if use_black_style else None
        )
        wc.generate(text.upper())
    
    return wc

# Generate button
if st.button("🎨 Generate Word Cloud", type="primary", use_container_width=True):
    with st.spinner("Generating word cloud..."):
        try:
            # Select font path
            selected_font = font_paths[0] if font_paths else None
            
            wc = generate_word_cloud(
                text=full_text,
                priority_text=priority_words,
                regular_text=regular_words,
                mask_image=mask_image,
                font_path=selected_font,
                min_size=min_font_size,
                max_size=max_font_size,
                bg_color=background_color,
                colormap=colormap if not use_original_style else None,
                max_words=max_words,
                repeat=repeat_words,
                priority_mult=priority_weight,
                use_black_style=use_original_style
            )
            
            if wc is not None:
                st.session_state.wordcloud = wc
                st.success("✅ Word cloud generated successfully!")
        except Exception as e:
            st.error(f"❌ Error generating word cloud: {str(e)}")
            st.exception(e)

# Display word cloud if it exists (from original with enhancements)
if st.session_state.wordcloud is not None:
    st.markdown('<div class="section-header">✨ Generated Word Cloud</div>', unsafe_allow_html=True)
    
    # Display image
    st.image(st.session_state.wordcloud.to_image(), caption='Word Cloud', use_container_width=True)
    
    # Download button (improved from original)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmpfile:
        st.session_state.wordcloud.to_image().save(tmpfile.name)
        with open(tmpfile.name, "rb") as image_file:
            st.download_button(
                label="⬇️ Download Word Cloud Image",
                data=image_file,
                file_name="wordcloud.png",
                mime="image/png",
                use_container_width=True
            )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>iSeeU Cloud - Enhanced Word Cloud Generator</p>
        <p>Upload a silhouette, customize your settings, and create beautiful word clouds!</p>
    </div>
""", unsafe_allow_html=True)
