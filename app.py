import streamlit as st
import google.generativeai as genai

# Səhifə nizamlamaları
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API açarını Secrets-dən oxuyuruq
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API açarı tapılmadı! Lütfən Settings > Secrets hissəsini yoxlayın.")

# Model nizamlaması - Ən son stabil versiya
model = genai.GenerativeModel('gemini-1.5-flash')

# Mesaj yaddaşı
if "messages" not in st.session_state:
    st.session_state.messages = []

# Köhnə mesajları göstər
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# İstifadəçi sualı
if prompt := st.chat_input("Mənə bir sual ver..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI-dan cavab al
    with st.chat_message("assistant"):
        try:
            # Düzgün generasiya metodu
            response = model.generate_content(prompt)
            if response and response.text:
                full_response = response.text
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                st.error("AI cavab verə bilmədi. API açarınızı və ya model adını yoxlayın.")
        except Exception as e:
            st.error(f"Xəta: {e}")
