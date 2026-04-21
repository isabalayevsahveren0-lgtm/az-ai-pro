import streamlit as st
import google.generativeai as genai

st.title("🤖 Az AI Pro")

# API açarını yoxla
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Secrets hissəsinə API açarını qoymağı unutmusunuz!")
else:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

    # Model siyahısını yoxlayan və ən uyğununu seçən sistem
    try:
        # Ən çox işləyən model adı budur
        model = genai.GenerativeModel('gemini-1.5-flash')
        # İşləyib-işləmədiyini yoxlamaq üçün boş test
        model.generate_content("hi") 
    except:
        # Əgər yuxarıdakı tapılmasa, bunu yoxla
        model = genai.GenerativeModel('gemini-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Sualınızı bura yazın..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Xəta: {e}")
