import streamlit as st
from streamlit.components.v1 import html

from config import Config

from helpers.image_helper import create_temp_file

from helpers.llm_helper import analyze_image_file, stream_parser


page_title = Config.PAGE_TITLE

# Configures page settings
st.set_page_config(page_title=page_title, initial_sidebar_state="expanded", layout="wide")

# Define CSS styles
css_styles = """
<style>
.stApp {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.stTitle {
    font-size: 24px;
    font-weight: bold;
    color: #333;
}

.stText {
    font-size: 16px;
    color: #555;
}

.stImage {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
}
</style>
"""

# Add CSS styles to the app
html(css_styles)

# Page title
st.title(page_title)

st.markdown("Select an image file to analyze.")

# Displays file upload widget
uploaded_file = st.file_uploader("Choose image file", type=['png', 'jpg', 'jpeg'])

# Sets up sidebar nav widgets (if needed)
# with st.sidebar:  # Uncomment if you need sidebar elements

image_model = 'llava:7b'  # Example model selection (uncomment if using a model choice)

if chat_input := st.chat_input("What would you like to ask?"):

    if uploaded_file is None:
        st.error('You must select an image file to analyze!')
        st.stop()

    with st.spinner("Processing image..."):
        # Create temporary file and display image preview
        temp_image = create_temp_file(uploaded_file)
        if temp_image:
            col1, col2 = st.columns([2, 8])
            with col1:
                st.image(temp_image, width=300)  # Increased image width
            with col2:
                # Rest of the content goes here

                # Analyze the image
                stream = analyze_image_file(uploaded_file, model=image_model, user_prompt=chat_input)
                stream_output = st.write_stream(stream_parser(stream))

    st.success("Image analysis complete!")