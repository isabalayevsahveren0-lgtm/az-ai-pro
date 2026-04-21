import streamlit as st
import google.generativeai as genai

# API açarını Secrets-dən götürürük
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API açarı tapılmadı!")
    st.stop()

st.title("🤖 Az AI Pro")

# Xətanın qarşısını almaq üçün modeli birbaşa stabil yolla çağırırıq
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

user_input = st.text_input("Sualınızı yazın:", key="user_sual")

if user_input:
    try:
        # v1beta xətasını keçmək üçün ən təmiz metod
        response = model.generate_content(user_input)
        st.success("Süni İntellekt:")
        st.write(response.text)
    except Exception as e:
        # Əgər hələ də xəta olsa, burada nə olduğunu tam görəcəyik
        st.error(f"Sistem xətası: {str(e)}")
