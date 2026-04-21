import streamlit as st
import google.generativeai as genai

# Səhifə başlığı
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API Key yoxlanışı
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Lütfən Streamlit Settings > Secrets hissəsinə GOOGLE_API_KEY əlavə edin!")
else:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        
        # Zəmanətli model adı (0.4.1 versiyası üçün ən stabil budur)
        model = genai.GenerativeModel('gemini-pro')

        # Mesaj yaddaşı
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Tarixçəni göstər
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # İstifadəçi girişi
        if prompt := st.chat_input("Sualınızı yazın..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                try:
                    # Cavabın alınması
                    response = model.generate_content(prompt)
                    if response.text:
                        st.markdown(response.text)
                        st.session_state.messages.append({"role": "assistant", "content": response.text})
                    else:
                        st.warning("Model cavab qaytarmadı. API limitini yoxlayın.")
                except Exception as e:
                    st.error(f"AI Cavab Xətası: {e}")
                    
    except Exception as e:
        st.error(f"Sistem Xətası: {e}")
