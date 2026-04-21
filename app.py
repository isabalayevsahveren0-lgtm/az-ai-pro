import streamlit as st
import google.generativeai as genai

# Diqqət: Burada API açarı yazılmır!
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("API açarı Seyfdə (Secrets) tapılmadı!")
    st.stop()

st.title("🤖 Az AI Pro")

user_input = st.text_input("Sualınızı yazın:")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Xəta: {e}")
