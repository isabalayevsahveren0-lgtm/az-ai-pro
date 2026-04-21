import streamlit as st
import google.generativeai as genai

# Sənin yeni və təzə API açarın
api_key_yeni = "AIzaSyD3JCEUzQUOfVutCP1dWF90rjhrntwesco"

genai.configure(api_key=api_key_yeni)

# Ən stabil model 'gemini-pro' istifadə edirik
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")

st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

st.subheader("Ağıllı Söhbət")
user_input = st.text_input("Sualını bura yaz və Enter düyməsini sıx...")

if user_input:
    with st.spinner('Düşünürəm...'):
        try:
            response = model.generate_content(user_input)
            st.info(response.text)
        except Exception as e:
            st.error("Xəta baş verdi. Zəhmət olmasa bir az sonra yenidən yoxlayın.")
            st.write(f"Texniki xəta: {e}")

st.sidebar.markdown("### Haqqında")
st.sidebar.info("Bu Süni İntellekt tətbiqi Sahvərən tərəfindən yaradılmışdır.")
