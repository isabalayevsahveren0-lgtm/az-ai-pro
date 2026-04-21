
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sənin API açarın
genai.configure(api_key="AIzaSyBWw9U7yHt2Nk2KBOkwhqATI7hoYfi8cp0")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")

st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

# Yan menyu
st.sidebar.title("Seçimlər")
secim = st.sidebar.radio("Nə etmək istəyirsən?", ["💬 Söhbət", "📸 Şəkil Analizi"])

if secim == "💬 Söhbət":
    st.subheader("Ağıllı Söhbət")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sualınızı yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                full_prompt = f"Sən Az AI Pro köməkçisisən. Azərbaycan dilində cavab ver. Sual: {prompt}"
                response = model.generate_content(full_prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Xəta: {e}")

elif secim == "📸 Şəkil Analizi":
    st.subheader("Şəkli Analiz Et")
    uploaded_file = st.file_uploader("Şəkil yüklə...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Yüklənən şəkil', use_column_width=True)
        
        if st.button("Analiz Et"):
            with st.spinner('Analiz edilir...'):
                try:
                    response = model.generate_content(["Bu şəkli Azərbaycan dilində ətraflı təsvir et.", image])
                    st.success("Nəticə:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Xəta: {e}")
    