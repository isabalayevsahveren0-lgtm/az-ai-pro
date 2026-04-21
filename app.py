import streamlit as st
import google.generativeai as genai

# API açarını sistemin gizli yaddaşından (Secrets) götürürük
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API açarı tapılmadı! Zəhmət olmasa Secrets hissəsinə əlavə edin.")

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Az AI Pro")

user_input = st.text_input("Sualınızı yazın:")

if user_input:
    try:
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Xəta: {e}")
