import streamlit as st
import google.generativeai as genai

# Sənin tam yeni və aktiv API açarın
API_KEY = "AIzaSyB04qO-lslUj7JJfBDu3sypTza-9z5A6QmQ"

genai.configure(api_key=API_KEY)

# Ən stabil işləyən model versiyası
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

user_input = st.text_input("Sualını bura yaz və Enter sıx...")

if user_input:
    with st.spinner('Süni intellekt cavab hazırlayır...'):
        try:
            response = model.generate_content(user_input)
            st.success("Süni İntellektin Cavabı:")
            st.write(response.text)
        except Exception as e:
            st.error("Bir xəta baş verdi. Zəhmət olmasa API açarının tam aktivləşməsi üçün 1-2 dəqiqə gözləyin.")
            st.info("Texniki detallar üçün aşağıya baxın:")
            st.code(str(e))
