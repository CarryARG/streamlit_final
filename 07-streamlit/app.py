import streamlit as st
import base64
import nltk
from PIL import Image

# Configurar la página
st.set_page_config(
    layout="wide",
    page_title="Análisis de Sentimientos de Reviews de Walgreens",
    page_icon="star"
)

# Descargar paquetes NLTK si no están presentes
nltk_packages = ['punkt', 'wordnet']
for package in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{package}')
    except LookupError:
        nltk.download(package)

# Función para convertir imágenes a base64
def get_image_b64(path):
    try:
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    except FileNotFoundError:
        return None

# Definir las páginas
def home_page():
    st.header("Bienvenidos ⭐", divider='rainbow')
    
    intro = """
    Hola, en esta plataforma podrás gestionar y administrar de manera útil y práctica las opiniones de los clientes. Esta herramienta servirá como punto central para detectar oportunidades de negocio y mejorar procesos en todos los niveles, desde las tiendas locales hasta los directivos a nivel global."""           
                
    a ="➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
    b = "➡️ Ver estadísticas sobre las reseñas, como la distribución de los sentimientos y las palabras más comunes."
    c = "➡️ Explorar las reseñas en detalle, con la capacidad de filtrar por sentimiento y buscar palabras clave."
    d = "➡️ Dashboard de control que permite una visualización que facilita el monitoreo del negocio basados en las plataformas Google y Yelp."
                
    st.markdown(f'<h3 style="text-align: left;">{intro}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{a}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{b}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{c}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{d}</h3>', unsafe_allow_html=True)
    st.divider()

def dashboard_page():
    st.title("Dashboard")
    st.write("Aquí puedes agregar el contenido de tu dashboard.")
    # Agrega gráficos, estadísticas y otros elementos necesarios

def modelos_page():
    st.title("Modelos")
    st.write("Aquí puedes agregar el contenido relacionado con los modelos de machine learning.")
    # Agrega los elementos y modelos necesarios

# Definir la navegación con botones en la parte superior
st.markdown("""
    <style>
    .top-nav {
        display: flex;
        justify-content: center;
        background-color: #2e2e2e;
        padding: 10px;
    }
    .top-nav button {
        margin: 0 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
    }
    .top-nav button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Botones de navegación
st.markdown("""
    <div class="top-nav">
        <button onclick="window.location.href = '?page=Home';">Home</button>
        <button onclick="window.location.href = '?page=Dashboard';">Dashboard</button>
        <button onclick="window.location.href = '?page=Modelos';">Modelos</button>
    </div>
""", unsafe_allow_html=True)

# Cambiar la página según el parámetro de URL
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["Home"])[0]

if page == "Home":
    home_page()
elif page == "Dashboard":
    dashboard_page()
elif page == "Modelos":
    modelos_page()

