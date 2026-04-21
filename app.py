import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sənin yeni və təzə API açarın
genai.configure(api_key="AIzaSyCSnXK8sJiYB7fJNyvUn8snnBDMk2grfEg")

# Modeli 'gemini-pro' olaraq təyin etdik (Söhbət üçün ən stabil versiya)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")

st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

# Yan menyu
st.sidebar.title("Seçimlər")
secim = st.sidebar.radio("Nə etmək istəyirsən?", ["💬 Söhbət", "🖼️ Şəkil Analizi"])

if secim == "💬 Söhbət":
    st.subheader("Ağıllı Söhbət")
    user_input = st.text_input("Sualını bura yaz...", placeholder="Məsələn: Süni intellekt nədir?")
    
    if user_input:
        with st.spinner('Düşünürəm...'):
            try:
                response = model.generate_content(user_input)
                st.info(response.text)
            except Exception as e:
                st.error("API açarı ilə bağlı problem var və ya limit dolub. Zəhmət olmasa bir az sonra yoxlayın.")

elif secim == "🖼️ Şəkil Analizi":
    st.subheader("Şəkil Analizi")
    uploaded_file = st.file_uploader("Şəkil yüklə...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption='Yüklənmiş şəkil', use_column_width=True)
        
        if st.button("Şəkli analiz et"):
            # Şəkil üçün flash modelini istifadə edirik
            vision_model = genai.GenerativeModel('gemini-1.5-flash')
            with st.spinner('Şəklə baxıram...'):
                try:
                    response = vision_model.generate_content(["Bu şəkildə nə var? Azərbaycan dilində izah et.", image])
                    st.success(response.text)
                except Exception as e:
                    st.error("Bu funksiya üçün hələlik icazə yoxdur.")
