import streamlit as st
from audio_recorder_streamlit import audio_recorder
import time
import tempfile
import whisper
import speech_recognition as sr
# import ffmpeg
import os


st.title("Speech-to-text ")

def save_file(file):
    folder_path = "Data"
    if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    file_path = os.path.join(folder_path, file.name)
    with open(file_path, 'wb') as f:
        f.write(file.getbuffer())
    
    return file_path



model = whisper.load_model("base")


file = st.file_uploader("Choose the audio file", type=["wav","mp3","m4a"])

if file is not None :
    st.audio(file, format="audio/wav")
    file_path = save_file(file)
    with st.spinner("Reading the File ..."):
        time.sleep(5)
    st.success("Generating Transcribe ....")
    # st.write(transcribe_wav(file))
    result = model.transcribe(file_path)
    print(result["text"])
    st.write(result["text"])




st.divider()
st.write("Made w")

