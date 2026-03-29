import streamlit as st
from PIL import Image
from moviepy.editor import VideoFileClip
import os
import io
import tempfile

# --- DESIGN JUVASON PRO ---
st.set_page_config(page_title="JUVASON PRO CONVERTER", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #FF4500; font-family: 'Impact', sans-serif; font-size: 50px !important; text-align: center; }
    .stButton>button { background-color: #28a745; color: white; font-weight: bold; border-radius: 10px; height: 3em; }
    .stSelectbox label, .stFileUploader label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>JUVASON CONVERTER</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: white;'>Multi-Formats • Haute Fidélité • 2026</p>", unsafe_allow_html=True)

# --- LOGIQUE DE CONVERSION ---
uploaded_file = st.file_uploader("Sélectionnez un fichier (Image, Doc, Vidéo, Audio)", type=None)

if uploaded_file:
    # Liste complète de tes extensions
    formats = ["PDF", "WEBP", "PNG", "JPG", "GIF", "BMP", "TIFF", "MP3", "WAV", "AAC", "MP4", "AVI", "MOV", "MKV"]
    target_format = st.selectbox("CHOISIR LE FORMAT :", formats)

    if st.button("LANCER LA CONVERSION"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        try:
            out_ext = target_format.lower()
            output_filename = f"Juvason_Converted.{out_ext}"
            
            # 1. VIDÉO & AUDIO (MoviePy)
            if out_ext in ["mp4", "avi", "mov", "mkv", "mp3", "wav", "aac"]:
                clip = VideoFileClip(tmp_path)
                if out_ext in ["mp3", "wav", "aac"]:
                    clip.audio.write_audiofile(output_filename)
                else:
                    clip.write_videofile(output_filename, codec="libx264")
                
            # 2. IMAGES (Pillow)
            else:
                img = Image.open(tmp_path).convert("RGB")
                img.save(output_filename, target_format)

            with open(output_filename, "rb") as f:
                st.download_button("⬇️ TÉLÉCHARGER LE FICHIER CONVERTI", f, file_name=output_filename)
                st.success("Conversion JUVASON réussie !")

        except Exception as e:
            st.error(f"Erreur : {e}")
