import streamlit as st
import google.generativeai as genai

# Səhifə nizamlamaları
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API açarını Streamlit Secrets-dən oxuyuruq
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("API açarı tapılmadı. Zəhmət olmasa Secrets hissəsini yoxlayın.")

# Model nizamlaması - Ən stabil model budur
model = genai.GenerativeModel('gemini-1.5-flash')

# Mesaj yaddaşı (Söhbət tarixçəsi)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Köhnə mesajları göstər
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# İstifadəçi sualı
if prompt := st.chat_input("Mənə bir sual ver..."):
    # İstifadəçi mesajını yadda saxla və göstər
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI-dan cavab al
    with st.chat_message("assistant"):
        try:
            # Ən sadə müraciət forması
            response = model.generate_content(prompt)
            
            if response.text:
                full_response = response.text
                st.markdown(full_response)
                # AI mesajını yadda saxla
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                st.warning("AI cavab qaytara bilmədi, lütfən yenidən yoxlayın.")
                
        except Exception as e:
            # Əgər model adı tapılmasa, bir də yoxla (Alternativ model adı ilə)
            st.error(f"Xəta baş verdi. Sistem modeli yenidən yükləyir... (Xəta: {e})")
