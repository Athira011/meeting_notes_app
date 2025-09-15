import streamlit as st
from app import transcribe_audio, extract_notes_and_actions

st.title("📝 Meeting Notes & Action Item Extractor")

uploaded_file = st.file_uploader("Upload meeting audio", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.read())

    st.info("Transcribing...")
    transcript = transcribe_audio("temp_audio.mp3")
    st.subheader("Transcript")
    st.write(transcript)

    st.info("Extracting notes and action items...")
    result = extract_notes_and_actions(transcript)
    st.subheader("Output")
    st.write(result)
