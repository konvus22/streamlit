import streamlit as st
import openai
from PIL import Image

# Función para generar respuestas con el modelo de OpenAI
def generate_response(text_input, openai_api_key):
    llm = openai(temperatura=0.7, openai_api_key=openai_api_key)
    st.info(llm(text_input))

# Definir la configuración de la página
st.set_page_config(
    page_title="Aplicación OpenAI",
    page_icon="🦜🔗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Crear una barra lateral para la entrada de la clave API
st.sidebar.title("Configuración de la Aplicación")
st.sidebar.markdown("### Clave API OpenAI")
openai_api_key = st.sidebar.text_input('Introduce tu clave', type='password')

# Comprobar si la clave API es válida
if not openai_api_key.startswith('sk-'):
    st.sidebar.warning('Por favor, introduce una clave API válida de OpenAI.', icon='⚠')

# Crear una columna para el título y el subtítulo
col1, col2 = st.beta_columns(2)

with col1:
    st.title('🦜🔗 Aplicación de inicio rápido')

with col2:
    st.image(Image.open('openai_logo.png'), use_column_width=True)  # Asegúrate de tener la imagen 'openai_logo.png' en tu directorio

# Crear una entrada para el texto
st.markdown("### Por favor, introduce el texto a continuación")
with st.form('my_form'):
    text = st.text_area('Texto:', '¿Cuáles son los tres consejos clave para aprender a programar?')
    submitted = st.form_submit_button('Generar Respuesta')

# Generar una respuesta si se ha enviado el formulario y la clave API es válida
if submitted and openai_api_key.startswith('sk-'):
    generate_response(text, openai_api_key)
