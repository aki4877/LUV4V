import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Dear Vinny 💗", layout="wide")

# Function to convert image to base64
def get_image_base64(file_path):
    try:
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except Exception as e:
        print(f"Error loading image {file_path}: {e}")
        return ""

# List of image paths and captions (assuming images are in root directory)
slides = [
    {"caption": "core memory of uss", "filename": "1.jpg"},
    {"caption": "aki and vinny on the terrace", "filename": "2.jpg"},
    {"caption": "the eyes I fell in love with", "filename": "3.jpg"},
    {"caption": "our first cheers!", "filename": "4.jpg"},
    {"caption": "how my gf looks like", "filename": "5.jpg"},
    {"caption": "life feels so good when she is beside", "filename": "6.jpg"},
    {"caption": "cute shoes hehe", "filename": "7.jpg"},
    {"caption": "one of the first pic of us together as a couple!", "filename": "8.jpg"},
    {"caption": "i love her eyes so much ahhh", "filename": "9.jpg"},
    {"caption": "our first cab ride togetherr", "filename": "10.jpg"},
    {"caption": "confused couple lol", "filename": "11.jpg"},
    {"caption": "peak bower mun fits", "filename": "12.jpg"},
    {"caption": "and just like that", "filename": "13.jpg"},
    {"caption": "an entire month has passed...", "filename": "14.jpg"},
    {"caption": "I love you bangaram!!!", "filename": "15.jpg"},
]

# Convert images to base64
for slide in slides:
    file_path = slide["filename"]  # Use filename directly from root
    if os.path.exists(file_path):
        slide["src"] = f"data:image/jpeg;base64,{get_image_base64(file_path)}"
    else:
        slide["src"] = "https://via.placeholder.com/300"  # Fallback image
        print(f"Image not found: {file_path}")

# Read and modify HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Inject slides data into HTML
slides_js = f"const slides = {str(slides).replace('src', 'src')};"
html_content = html_content.replace("const slides = [", f"{slides_js}\n// Original slides array replaced")

components.html(html_content, height=900)
