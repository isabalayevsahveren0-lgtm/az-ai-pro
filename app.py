import streamlit as st
import google.generativeai as genai

# API konfiqurasiyası
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API açarı Secrets-də tapılmadı!")
    st.stop()

st.title("🤖 Az AI Pro")

# Modeli birbaşa təyin edirik
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Sualınızı yazın:")

if user_input:
    try:
        # Köhnə versiya xətalarını keçmək üçün ən sadə çağırış
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Xəta detalları: {str(e)}")
