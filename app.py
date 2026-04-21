import streamlit as st
import google.generativeai as genai

# Sənin yeni API açarın artıq buradadır
genai.configure(api_key="AIzaSyBww9U7yHt2NkZ8OkwmQATI7hoYfI8cp0")

# Model adını ən yeni və stabil versiyaya dəyişdik
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Az AI Pro", page_icon="🤖")
st.title("🤖 Az AI Pro - Sənin Köməkçin")
st.markdown("---")

user_input = st.text_input("Sualını bura yaz və Enter düyməsini sıx...")

if user_input:
    with st.spinner('Düşünürəm...'):
        try:
            # Süni intellektə sualı göndəririk
            response = model.generate_content(user_input)
            st.success("Cavab:")
            st.write(response.text)
        except Exception as e:
            st.error("Xəta baş verdi. Zəhmət olmasa bir az sonra yenidən yoxlayın.")
            # Texniki xətanı anlamaq üçün bura gizli qeyd (yalnız sən görəcəksən):
            st.write(f"Səbəb: {str(e)}")
