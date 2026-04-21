import streamlit as st
import google.generativeai as genai
import os

# Sənin ən son aldığın və aktiv olan API açarın
API_KEY = "AIzaSyB04qO-lslUj7JJfBDu3sypTza-9z5A6QmQ"

# Google-un ən yeni modelini çağırmaq üçün konfiqurasiya
genai.configure(api_key=API_KEY)

# Səhifə dizaynı
st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro")
st.caption("Sənin şəxsi süni intellekt köməkçin")

# Modeli ən stabil formatda başladırıq
model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Sualınızı bura yazın:", placeholder="Salam, necəsən?")

if user_input:
    with st.spinner('Cavab hazırlanır...'):
        try:
            # Ən sadə və birbaşa metodla mətni alırıq
            response = model.generate_content(user_input)
            
            if response.text:
                st.subheader("Cavab:")
                st.markdown(response.text)
            else:
                st.warning("Süni intellekt boş cavab qaytardı. Yenidən yoxlayın.")
                
        except Exception as e:
            st.error("Bağlantıda kiçik bir problem oldu.")
            # Xətanın tam kodunu burada göstəririk ki, həll edə bilək
            with st.expander("Xəta detalları (Texniki)"):
                st.code(str(e))

st.divider()
st.info("Az AI Pro v1.2 | Google AI tərəfindən gücləndirilib")
