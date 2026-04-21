import streamlit as st
import google.generativeai as genai

# Sənin göndərdiyin tam yeni API açarı
API_KEY = "AIzaSyBC515_iJJ__xYk-TPesZJgD2im725H6Ao"

# Google AI Konfiqurasiyası
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Saytın interfeys ayarları
st.set_page_config(page_title="Az AI Pro", page_icon="🤖", layout="centered")

st.title("🤖 Az AI Pro")
st.subheader("Sənin şəxsi süni intellekt köməkçin")
st.markdown("---")

# İstifadəçi sualı üçün sahə
user_query = st.text_input("Sualınızı bura yazın:", placeholder="Məsələn: Süni intellekt gələcəkdə nələri dəyişəcək?")

if user_query:
    with st.spinner('Cavab hazırlanır, zəhmət olmasa gözləyin...'):
        try:
            # Süni intellektdən cavabın alınması
            response = model.generate_content(user_query)
            st.success("🤖 Cavab:")
            st.write(response.text)
        except Exception as e:
            st.error("Bir xəta baş verdi. API açarı hələ tam aktiv olmaya bilər.")
            with st.expander("Xətanın detalları"):
                st.code(str(e))

# Alt hissə
st.markdown("---")
st.caption("Az AI Pro v1.0 | Google Gemini Pro tərəfindən dəstəklənir")
