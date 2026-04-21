import streamlit as st
import google.generativeai as genai

# Streamlit Secrets-dən açarı oxuyuruq
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("API açarı tapılmadı! Zəhmət olmasa Streamlit panelində Secrets hissəsinə əlavə edin.")
        st.stop()
except Exception as e:
    st.error(f"Xəta: {e}")
    st.stop()

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

user_input = st.text_input("Sualınızı yazın:")

if user_input:
    with st.spinner('Cavab hazırlanır...'):
        try:
            response = model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"Süni intellekt cavab verə bilmədi: {e}")
