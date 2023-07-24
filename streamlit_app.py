
import streamlit as st
import openai

# Configuración de la página
st.set_page_config(
    page_title="Aplicación OpenAI",
    page_icon="🦜🔗",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Estilos CSS para personalizar el aspecto de la aplicación
st.markdown("""
    <style>
        .reportview-container {
            background: #F5F5F5;
        }
        .main .block-container {
            background: white;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1), 0 1px 2px rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            padding: 2em;
        }
        .sidebar .sidebar-content {
            background: #F5F5F5;
        }
        h1 {
            color: #5e9cd3;
        }
    </style>
    """, unsafe_allow_html=True)

# Función para generar respuestas con el modelo de OpenAI
def generate_response(text_input, openai_api_key):
    llm = openai(temperatura=0.7, openai_api_key=openai_api_key)
    st.info(llm(text_input))

# Sidebar para la configuración de la aplicación
st.sidebar.title("Configuración de la Aplicación")
st.sidebar.markdown("### Clave API OpenAI")
openai_api_key = st.sidebar.text_input('Introduce tu clave', type='password')

# Comprobar si la clave API es válida
if not openai_api_key.startswith('sk-'):
    st.sidebar.warning('Por favor, introduce una clave API válida de OpenAI.')

# Título y descripción de la aplicación
st.title('🦜🔗 Aplicación de inicio rápido')
st.markdown("""
Esta aplicación genera respuestas a las preguntas introducidas utilizando la API de OpenAI. 
Por favor, introduce tu clave API y la pregunta en los campos correspondientes y pulsa el botón 'Generar Respuesta'.
""")

# Entrada de texto y botón de envío
with st.form('my_form'):
    text = st.text_area('Introduce la pregunta:', '¿Cuáles son los tres consejos clave para aprender a programar?')
    submitted = st.form_submit_button('Generar Respuesta', on_click=generate_response)

# Generar una respuesta si se ha enviado el formulario y la clave API es válida
if submitted and openai_api_key.startswith('sk-'):
    generate_response(text, openai_api_key)
