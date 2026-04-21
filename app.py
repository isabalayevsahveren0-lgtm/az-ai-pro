import streamlit as st
import google.generativeai as genai

# Sənin ən son aldığın API açarını bura dırnaq içində yapışdır
API_KEY = "AIzaSyB04qO-lslUj7JJfBDu3sypTza-9z5A6QmQ"

# Konfiqurasiya - Versiya problemini həll etmək üçün
genai.configure(api_key=API_KEY)

# Modeli çağırmaq üçün ən stabil üsul
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

user_input = st.text_input("Sualınızı bura yazın:")

if user_input:
    with st.spinner('Süni intellekt cavab verir...'):
        try:
            # generate_content funksiyasını ən sadə formada çağırırıq
            response = model.generate_content(user_input)
            st.success("Cavab:")
            st.write(response.text)
        except Exception as e:
            st.error("Bağlantı xətası! API açarı hələ tam aktiv olmaya bilər.")
            # Xətanın tam detallarını burada görəcəksən:
            with st.expander("Xətanın detalları"):
                st.write(str(e))

st.sidebar.info("Az AI Pro v1.1 | Google Gemini Pro tərəfindən dəstəklənir")
