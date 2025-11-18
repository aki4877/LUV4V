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
    {"caption": "one of our first gmeets", "filename": "1.jpg"},
    {"caption": "akis first tatto for jani", "filename": "2.jpg"},
    {"caption": "the eyes I fell in love with", "filename": "3.jpg"},
    {"caption": "the first pic I saw of u", "filename": "4.jpg"},
    {"caption": "how my gf looks like", "filename": "5.jpg"},
    {"caption": "but how it feels like talking to her", "filename": "6.jpg"},
    {"caption": "one of akis key memory of gmeets", "filename": "7.jpg"},
    {"caption": "aki and jani meet for the first timeeeee", "filename": "8.jpg"},
    {"caption": "aki and jani hold hands for the first timee", "filename": "9.jpg"},
    {"caption": "our first kisss!", "filename": "10.jpg"},
    {"caption": "together, foreverr!", "filename": "11.jpg"},
    {"caption": "jani being jani", "filename": "12.jpg"},
    {"caption": "our first mirror pic", "filename": "13.jpg"},
    {"caption": "janis first painting ab aki and jani and family", "filename": "14.jpg"},
    {"caption": "janis iconic heart XD", "filename": "15.jpg"},
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
