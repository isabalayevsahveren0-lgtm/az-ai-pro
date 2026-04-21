import streamlit as st
import google.generativeai as genai

# Sənin tam yeni API açarın bura yerləşdirildi
API_KEY = "AIzaSyAbVjGQvztSI9MvogqdTkrXd3ju71xBcoI"

try:
    genai.configure(api_key=API_KEY)
    # Ən yeni və sürətli model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    st.set_page_config(page_title="Az AI Pro", page_icon="🤖", layout="centered")
    
    st.title("🤖 Az AI Pro - Sənin Köməkçin")
    st.markdown("---")

    # Giriş hissəsi
    user_input = st.text_input("Sualını bura yaz və Enter sıx...", placeholder="Məsələn: Salam, necəsən?")

    if user_input:
        with st.spinner('Süni intellekt cavab hazırlayır...'):
            try:
                response = model.generate_content(user_input)
                st.success("Süni İntellektin Cavabı:")
                st.write(response.text)
            except Exception as e:
                # Xətanın nə olduğunu anlamaq üçün ətraflı mesaj
                st.error("Bağlantı xətası! API açarı hələ aktiv olmaya bilər.")
                st.info("Texniki detal:")
                st.code(str(e))
                
    # Səhifənin aşağısına imza
    st.markdown("---")
    st.caption("Developed by Sahveren | Az AI Pro v1.0")

except Exception as main_e:
    st.error(f"Sistem xətası: {main_e}")
