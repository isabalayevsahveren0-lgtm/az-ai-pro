import streamlit as st
import google.generativeai as genai

# Sənin aktiv API açarın (Secrets-dən oxuyur)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("API açarı tapılmadı! Lütfən Secrets hissəsinə əlavə edin.")
    st.stop()

# Ən stabil modeli çağırmağın ən qısa yolu
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤖 Az AI Pro")
user_input = st.text_input("Sualınızı yazın:")

if user_input:
    try:
        # Heç bir əlavə parametr olmadan sadə müraciət
        response = model.generate_content(user_input)
        st.write(response.text)
    except Exception as e:
        st.error(f"Xəta: {e}")
