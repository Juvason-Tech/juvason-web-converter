import streamlit as st
from PIL import Image
from moviepy.editor import VideoFileClip
import os
import io
import tempfile

# --- CONFIGURATION & DESIGN JUVASON PRO ---
st.set_page_config(page_title="JUVASON PRO CONVERTER - Professional Edition", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    /* 1. Fond noir profond */
    .stApp { background-color: #000000; }
    
    /* 2. Titre Orange Juvason */
    h1 {
        color: #FF4500;
        font-family: 'Impact', sans-serif;
        font-size: 55px !important;
        text-align: center;
        text-shadow: 2px 2px #8B2500;
        margin-top: -30px;
    }
    
    /* 3. Cadre central avec bordure orange lumineuse */
    div[data-testid="stFrame"] {
        background-color: #121212;
        border: 3px solid #FF4500;
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0px 0px 15px #FF4500;
        margin-top: 20px;
    }
    
    /* 4. Bouton de téléchargement (Look différent pour la sélection) */
    .stFileUploader>button {
        background-color: #1A1A1A;
        color: white;
        border: 3px solid #FF4500;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
    }
    .stFileUploader label { color: white !important; font-weight: bold; }
    
    /* 5. Menu déroulant orange */
    .stSelectbox>div>div {
        background-color: #FF4500;
        color: black;
        border-radius: 10px;
        font-weight: bold;
    }
    .stSelectbox label { color: white !important; font-weight: bold; }
    
    /* 6. BOUTON VERT "LANCER LA CONVERSION" (L'effet WAHOU !) */
    .stButton>button {
        background-color: #28a745;
        color: white;
        border-radius: 15px;
        font-weight: bold;
        height: 60px;
        width: 100%;
        font-size: 20px !important;
        text-shadow: 1px 1px black;
        box-shadow: 2px 4px 6px rgba(0,0,0,0.5);
    }
    .stButton>button:hover {
        background-color: #218838;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFACE JUVASON PRO ---
st.markdown("<h1>JUVASON CONVERTER</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: white;'>Multi-Formats • Haute Fidélité • 2026</p>", unsafe_allow_html=True)

with st.container():
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
                
                # Logic de conversion (identique au précédent)
                if out_ext in ["mp4", "avi", "mov", "mkv", "mp3", "wav", "aac"]:
                    clip = VideoFileClip(tmp_path)
                    if out_ext in ["mp3", "wav", "aac"]:
                        clip.audio.write_audiofile(output_filename)
                    else:
                        clip.write_videofile(output_filename, codec="libx264")
                else:
                    img = Image.open(tmp_path).convert("RGB")
                    img.save(output_filename, target_format)

                with open(output_filename, "rb") as f:
                    st.download_button("⬇️ TÉLÉCHARGER LE FICHIER CONVERTI", f, file_name=output_filename)
                    st.success("Conversion JUVASON réussie !")

            except Exception as e: st.error(f"Erreur : {e}")
            finally: 
                if os.path.exists(tmp_path): os.remove(tmp_path)
