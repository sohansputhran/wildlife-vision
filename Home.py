import streamlit as st
import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent / "src"))

# Page configuration
st.set_page_config(
    page_title="Wildlife Vision",
    page_icon="🦁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        color: #2E7D32;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #555;
        margin-bottom: 2rem;
    }
    .feature-box {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f8f0;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🦁 Wildlife Vision</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">AI-Powered Wildlife Analysis & Conservation Platform</p>',
    unsafe_allow_html=True
)

# Introduction
st.markdown("""
Welcome to **Wildlife Vision**, a comprehensive platform that combines computer vision, 
data analytics, and AI to help you explore wildlife data, identify species, and gain 
conservation insights.
""")

st.divider()

# Features Overview
st.header("🌟 Platform Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🔍 Species Identification
    Upload wildlife images and get instant species identification powered by 
    state-of-the-art deep learning models.
    
    ### 📊 Data Explorer
    Explore comprehensive wildlife datasets with interactive filters, visualizations, 
    and analytics tools.
    
    ### 🎮 Fun Zone
    Test your wildlife knowledge with quizzes, games, and daily wildlife facts!
    """)

with col2:
    st.markdown("""
    ### 🌍 Conservation Insights
    Discover biodiversity metrics, endangered species data, and conservation 
    hotspots with interactive dashboards.
    
    ### 🖼️ Image Gallery
    Browse high-quality wildlife images with advanced filtering and quality 
    assessment tools.
    
    ### 💬 Ask Wildlife Expert
    Chat with an AI-powered wildlife expert that can answer questions about 
    species, behavior, and conservation.
    """)

st.divider()

# Getting Started
st.header("🚀 Getting Started")

st.markdown("""
1. **Navigate** using the sidebar to explore different features
2. **Upload** your wildlife images for species identification
3. **Explore** the dataset using our interactive tools
4. **Learn** about conservation through our insights dashboard
5. **Have fun** with wildlife quizzes and games!
""")

# Project Status
st.divider()
st.header("📈 Project Status")

progress_col1, progress_col2, progress_col3 = st.columns(3)

with progress_col1:
    st.metric("Sprint", "0", "Foundation")
    
with progress_col2:
    st.metric("Features", "1/6", "In Development")
    
with progress_col3:
    st.metric("Completion", "5%", "Getting Started")

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #777; padding: 2rem 0;'>
        <p>Built with ❤️ using Streamlit, PyTorch, and wildlife_datasets</p>
        <p>🌱 Committed to Wildlife Conservation 🌱</p>
    </div>
""", unsafe_allow_html=True)