import streamlit as st
import google.generativeai as genai

# Secrets-dən açarı götürürük
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API açarı tapılmadı! Lütfən Secrets-ə əlavə edin.")
    st.stop()

st.title("🤖 Az AI Pro")

# Modeli birbaşa təyin edirik
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Sualınızı yazın:")

if user_input:
    try:
        # Ən sadə müraciət metodu
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Sistem xətası: {str(e)}")
