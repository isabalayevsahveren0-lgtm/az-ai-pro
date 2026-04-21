import streamlit as st
import google.generativeai as genai

# Səhifə nizamlamaları
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API açarını Streamlit Secrets-dən oxuyuruq
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Model nizamlaması
model = genai.GenerativeModel('gemini-pro')

# Mesaj yaddaşı (Söhbət tarixçəsi)
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
        message_placeholder = st.empty()
        full_response = ""
        try:
            response = model.generate_content(prompt)
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Xəta baş verdi: {e}")
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
