import streamlit as st
import moviepy.editor as mp
import tempfile
import os

st.set_page_config(page_title="JUVASON Online Converter", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    .stButton>button { background-color: #FF4500; color: white; font-weight: bold; width: 100%; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

st.title("JUVASON Online 🚀")
st.write("Convertissez vos fichiers audio et vidéo en un clic.")

uploaded_file = st.file_uploader("Choisissez un fichier", type=['mp4', 'mov', 'wav', 'mp3'])

if uploaded_file is not None:
    target_format = st.selectbox("Format de sortie :", ["MP3", "WAV", "MP4", "GIF"])
    
    if st.button("Lancer la Conversion"):
        with st.spinner('Conversion en cours...'):
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
                tmp.write(uploaded_file.read())
                input_path = tmp.name
            
            output_ext = f".{target_format.lower()}"
            output_path = input_path.replace(os.path.splitext(input_path)[1], output_ext)
            
            clip = mp.VideoFileClip(input_path)
            if target_format in ["MP3", "WAV"]:
                clip.audio.write_audiofile(output_path, logger=None)
            else:
                clip.write_videofile(output_path, logger=None)
            clip.close()

            with open(output_path, "rb") as f:
                st.download_button("⬇️ Télécharger le fichier", f, file_name=f"juvason_converted{output_ext}")
            
            os.remove(input_path)
            os.remove(output_path)
