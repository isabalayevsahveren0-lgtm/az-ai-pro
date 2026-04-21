import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")

# API nizamlaması
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key Secrets-də tapılmadı!")

# Ehtiyat variantlı model yükləməsi
try:
    # Birinci cəhd: Ən yeni model
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Yoxlamaq üçün kiçik bir test (xətanı dərhal tutmaq üçün)
    test_res = model.generate_content("test") 
except:
    try:
        # İkinci cəhd: Əgər flash tapılmasa, bunu yoxla
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        st.error(f"Heç bir model işləmədi. Xəta: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Mənə bir sual ver..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Sistem cavab verə bilmir: {e}")
