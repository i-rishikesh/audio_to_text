import streamlit as st
import pyaudio as pa
import speech_recognition as sr
import os
from pydub import AudioSegment,silence
recog=sr.Recognizer()
final_result=""

st.markdown("<h1 style='text-align:center; color:blue'> Audio to Text Convertor</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
audio=st.file_uploader("Upload your  Audio", type=['mp3', 'wav'])
if audio:
    st.audio(audio)
    audio_segment=AudioSegment.from_file(audio)
    chunks=silence.split_on_silence(audio_segment, min_silence_len=1000, silence_thresh=audio_segment.dBFS-20,keep_silence=100)
    for index,chunk in enumerate(chunks):
        chunk.export(str(index)+".wav", format="wav")
        with sr.AudioFile(str(index)+".wav") as source:
           recorded=recog.record(source)
           try:
               text=recog.recognize_google(recorded)
               final_result=final_result+" "+text
               print(text)
           except:
               print("None")
               final_result=final_result+"unaudible"
    with st.form("result"):
        result=st.text_area("Text", final_result, height=200, max_chars=None, key=None)
        d_btn=st.form_submit_button("Download")
        if d_btn:
            user_loc=os.environ.get("USERPROFILE")
            loc=user_loc+"\\Downloads\\transcrip.txt"
            with open(loc,"w") as file:
                file.write(result)



        
                

