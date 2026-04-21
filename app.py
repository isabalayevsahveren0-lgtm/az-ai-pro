import streamlit as st
import google.generativeai as genai

# Sənin yeni göndərdiyin API açarı
genai.configure(api_key="AIzaSyB04q0JslUj7JJfBDu3sypTza-9z5A6QmQ")

# Ən sürətli və stabil model
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")

st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

# İstifadəçi girişi
user_input = st.text_input("Sualınızı bura yazın və Enter sıxın...")

if user_input:
    with st.spinner('Süni intellekt cavab verir...'):
        try:
            # Süni intellektdən cavabın alınması
            response = model.generate_content(user_input)
            st.success("Cavab:")
            st.write(response.text)
        except Exception as e:
            st.error("Bağlantı xətası! API açarı hələ aktiv olmaya bilər.")
            # Xətanı dəqiq görmək üçün (lazım olsa):
            # st.write(str(e))

st.sidebar.info("Bu tətbiq Gemini AI tərəfindən idarə olunur.")
