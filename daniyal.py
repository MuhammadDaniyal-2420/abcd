import streamlit as st
import requests

url = "https://text-translator2.p.rapidapi.com/translate"

st.title("Text Translator")

source_language = st.selectbox("Source Language", ["en", "id"])
target_language = st.selectbox("Target Language", ["eu", "id"])
text = st.text_input("Enter Text")

payload = {
    "source_language": source_language,
    "target_language": target_language,
    "text": text
}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "aa699afe73msh0b5ec5a9501d381p19948ejsn0881e0164e4c",
    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

if st.button("Translate"):
    response = requests.post(url, data=payload, headers=headers)
    translation = response.json().get("translated_text")
    st.success(f"Translation: {translation}")
