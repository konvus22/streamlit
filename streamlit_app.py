import streamlit as st
import openai

st.title('🦜🔗 Aplicación de inicio rápido')
openai_api_key = st.sidebar.text_input('Clave API OpenAI')
def generate_response(text_input):
  llm = openai(temperatura=0.7,  openai_api_key=openai_api_key)
  st.info(llm(text_input))
with st.form('my_form'):
    text = st.text_area('Introduzca texto:', '¿Cuáles son los tres consejos clave para aprender a programar?')
    submitted = st.form_submit_button('Enviar')
    if not openai_api_key.startswith('sk-'):
        st.warning('Introduzca su clave API OpenAI', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
