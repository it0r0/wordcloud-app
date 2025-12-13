import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import tempfile
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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">☁️ iSeeU Cloud</div>', unsafe_allow_html=True)

# Initialize session state
if 'wordcloud' not in st.session_state:
    st.session_state.wordcloud = None
if 'wordcloud_image' not in st.session_state:
    st.session_state.wordcloud_image = None

# Function to transform mask image (from original)
def transform_format(val):
    """Transform mask values to proper format for wordcloud"""
    return 255 if val != 0 else 0

# MAIN MODE TOGGLE - Single Switch
st.sidebar.title("⚙️ Mode Selection")
enhanced_mode = st.sidebar.toggle(
    "🚀 Enhanced Mode", 
    value=False,
    help="Toggle ON for new features (multiple fonts, priority words). Toggle OFF for original simple mode."
)

if enhanced_mode:
    st.sidebar.info("🚀 Enhanced Mode: Multiple fonts, priority words, and advanced settings enabled")
else:
    st.sidebar.info("📝 Simple Mode: Classic iSeeU experience")

st.sidebar.markdown("---")

# Configuration based on mode
if enhanced_mode:
    # ENHANCED MODE - All new features
    st.sidebar.markdown("### 📝 Font Files")
    uploaded_fonts = st.sidebar.file_uploader(
        "Upload Font Files (.ttf, .otf)",
        type=["ttf", "otf"],
        accept_multiple_files=True,
        help="Upload one or more font files"
    )
    
    # Check for default font
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
        st.sidebar.info("Using Montserrat-Bold font")
    
    # Font size configuration
    st.sidebar.markdown("### 📏 Font Size Range")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        min_font_size = st.number_input("Min", 4, 100, 10, 1)
    with col2:
        max_font_size = st.number_input("Max", 10, 500, 100, 10)
    
    st.sidebar.markdown("### 🎨 Settings")
    max_words = st.sidebar.number_input("Max Words", 10, 500, 100, 10, help="Lower = faster generation")
else:
    # SIMPLE MODE - Original settings
    default_font_path = './Montserrat-Bold.otf'
    font_paths = [default_font_path] if os.path.exists(default_font_path) else []
    min_font_size = 10
    max_font_size = 100
    max_words = 200

# Main content area
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### 📤 Upload Mask Image")
    mask_image = st.file_uploader(
        "Upload silhouette image",
        type=["png", "jpg", "jpeg"],
        help="Black and white silhouette"
    )
    
    if mask_image:
        st.image(Image.open(mask_image), caption="Silhouette", use_container_width=True)

with col_right:
    st.markdown("### 💬 Word Input")
    
    if enhanced_mode:
        # ENHANCED MODE - Three tabs
        tab1, tab2, tab3 = st.tabs(["🔥 Priority", "📝 Regular", "📄 Full Text"])
        
        with tab1:
            priority_words = st.text_area(
                "Priority words (one per line or comma-separated)",
                height=100,
                placeholder="Important\nKeyword",
                key="priority"
            )
            priority_weight = st.slider("Priority Multiplier", 1.0, 10.0, 5.0, 0.5)
        
        with tab2:
            regular_words = st.text_area(
                "Regular words (one per line or comma-separated)",
                height=100,
                placeholder="word1\nword2",
                key="regular"
            )
        
        with tab3:
            full_text = st.text_area(
                "Full text (original method)",
                height=100,
                placeholder="Enter text here...",
                key="fulltext"
            )
    else:
        # SIMPLE MODE - Single text input
        full_text = st.text_area(
            "Enter your text",
            height=200,
            placeholder="Type your text here...",
            key="simple_text"
        )
        priority_words = ""
        regular_words = ""
        priority_weight = 1.0

# Generate word cloud function
def generate_word_cloud(text, priority_text, regular_text, mask_image, font_path, 
                       min_size, max_size, max_words, priority_mult):
    """Generate word cloud - optimized for speed"""
    
    # Setup stopwords
    stopwords = set(STOPWORDS)
    stopwords.update(["drink", "now", "wine", "flavor", "flavors"])
    
    # Process mask
    if mask_image is not None:
        mask = np.array(Image.open(mask_image).convert('L'))
        # Optimized transformation using vectorization
        transformed_mask = np.where(mask != 0, 255, 0).astype(np.int32)
    else:
        st.warning("Please upload a mask image.")
        return None
    
    # Black color function
    def black_color_func(word=None, font_size=None, position=None, 
                        orientation=None, font_path=None, random_state=None):
        return "rgb(0, 0, 0)"
    
    # Determine generation method
    use_frequency = bool(priority_text or regular_text)
    
    if use_frequency:
        # Priority word method
        def parse_words(text):
            if not text:
                return []
            words = text.replace(',', '\n').split('\n')
            return [w.strip() for w in words if w.strip()]
        
        priority_list = parse_words(priority_text)
        regular_list = parse_words(regular_text)
        
        word_freq = {}
        for word in priority_list:
            word_freq[word.upper()] = int(100 * priority_mult)
        for word in regular_list:
            if word.upper() not in word_freq:
                word_freq[word.upper()] = 10
        
        if not word_freq:
            st.warning("Please enter at least some words.")
            return None
        
        wc = WordCloud(
            background_color="white",
            mask=transformed_mask,
            font_path=font_path if font_path else None,
            stopwords=stopwords,
            max_words=max_words,
            repeat=True,
            min_font_size=min_size,
            max_font_size=max_size,
            color_func=black_color_func,
            relative_scaling=0.5,
            prefer_horizontal=0.9
        )
        wc.generate_from_frequencies(word_freq)
    else:
        # Text method
        if not text:
            st.warning("Please enter some text.")
            return None
        
        wc = WordCloud(
            background_color="white",
            mask=transformed_mask,
            font_path=font_path if font_path else None,
            stopwords=stopwords,
            max_words=max_words,
            repeat=True,
            min_font_size=min_size,
            max_font_size=max_size,
            color_func=black_color_func,
            relative_scaling=0.5,
            prefer_horizontal=0.9
        )
        wc.generate(text.upper())
    
    return wc

# Generate button
if st.button("🎨 Generate Word Cloud", type="primary", use_container_width=True):
    with st.spinner("Generating word cloud..."):
        try:
            selected_font = font_paths[0] if font_paths else None
            
            wc = generate_word_cloud(
                text=full_text if not enhanced_mode else full_text,
                priority_text=priority_words if enhanced_mode else "",
                regular_text=regular_words if enhanced_mode else "",
                mask_image=mask_image,
                font_path=selected_font,
                min_size=min_font_size,
                max_size=max_font_size,
                max_words=max_words,
                priority_mult=priority_weight if enhanced_mode else 1.0
            )
            
            if wc is not None:
                # Store both the wordcloud object and the image
                st.session_state.wordcloud = wc
                st.session_state.wordcloud_image = wc.to_image()
                st.success("✅ Word cloud generated!")
                st.rerun()
                
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.exception(e)

# Display section - ALWAYS visible if wordcloud exists
if st.session_state.wordcloud_image is not None:
    st.markdown("---")
    st.markdown("### ✨ Generated Word Cloud")
    
    # Display the cached image for instant preview
    st.image(
        st.session_state.wordcloud_image, 
        caption='Your Word Cloud',
        use_container_width=True
    )
    
    # Download button with cached image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Convert image to bytes for download
        import io
        buf = io.BytesIO()
        st.session_state.wordcloud_image.save(buf, format='PNG')
        buf.seek(0)
        
        st.download_button(
            label="⬇️ Download Word Cloud",
            data=buf,
            file_name="wordcloud.png",
            mime="image/png",
            use_container_width=True
        )
    
    # Clear button
    if st.button("🗑️ Clear and Start New", use_container_width=True):
        st.session_state.wordcloud = None
        st.session_state.wordcloud_image = None
        st.rerun()

# Footer
st.markdown("---")
mode_text = "Enhanced Mode" if enhanced_mode else "Simple Mode"
st.markdown(f"""
    <div style='text-align: center; color: #7f8c8d;'>
        <p>iSeeU Cloud - {mode_text}</p>
        <p>Toggle the mode switch in the sidebar to change between simple and enhanced features</p>
    </div>
""", unsafe_allow_html=True)
