import streamlit as st
import google.generativeai as genai

# Səhifə nizamlamaları
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API açarını Secrets-dən oxuyuruq
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key tapılmadı! Lütfən Secrets hissəsini yoxlayın.")

# Model nizamlaması - Ən zəmanətli ad budur
# Əgər gemini-1.5-flash işləməsə, avtomatik olaraq digərini yoxlayacaq
try:
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except:
    model = genai.GenerativeModel('models/gemini-pro')

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
        try:
            # Modelə müraciət
            response = model.generate_content(prompt)
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.warning("Model cavab qaytarmadı, API limitini və ya açarınızı yoxlayın.")
        except Exception as e:
            # Əgər hələ də 404 xətası verirsə, ekranda daha aydın mesaj göstərsin
            st.error(f"Bağlantı xətası: {e}")
