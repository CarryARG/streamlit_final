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
    # Abrir la imagen del logo
    img1 = Image.open('./07-streamlit/images/arcope-logo.jpeg')        

    # Convertir la imagen a base64
    with open("./07-streamlit/images/arcope-logo.jpeg", "rb") as img_file:
        b64_1 = base64.b64encode(img_file.read()).decode()
    
    # Mostrar la imagen del logo centrada
    st.markdown(f'''
        <div class="centered-img" style="display: flex; justify-content: center; margin-top: 20px;">
            <img src="data:image/jpeg;base64,{b64_1}" style="width: 300px; height: 300px;" />
        </div>
    ''', unsafe_allow_html=True)
    
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

    # Información del equipo
    st.header("Desarrollado por ⚙️", divider='rainbow')

    personas = [
        {
            "nombre": "Cristian Moreira",
            "profesion": "Project Manager",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/cristian.jpeg"
        },
        {
            "nombre": "Andres Aguirre",
            "profesion": "Technical Project Manager - Data Analytics",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/andres.jpeg"
        },
        {
            "nombre": "Jeison Zapata",
            "profesion": "Data Scientist - Data Analyst",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/jeison.jpeg"
        },
        {
            "nombre": "Libardo Alarcon",
            "profesion": "Data Scientist",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/libardo.jpeg"
        },
        {
            "nombre": "Manuel Carruitero",
            "profesion": "Data Engineer",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/manuel.jpeg"
        },
        {
            "nombre": "Lucas Carranza",
            "profesion": "Data Engineer",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/lucas.jpeg"
        }
    ]

    columns = st.columns(len(personas))
    for idx, persona in enumerate(personas):
        with columns[idx]:
            st.markdown(f'<h2 style="text-align: center;">{persona["nombre"]}</h2>', unsafe_allow_html=True)
            persona_image = get_image_b64(persona["imagen_link"])
            if persona_image:
                st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{persona_image}" width="200"/></div>', unsafe_allow_html=True)
            st.markdown(f'<h3 style="text-align: center;">{persona["profesion"]}</h3>', unsafe_allow_html=True)

            # Logos de redes sociales
            linkedin_logo = get_image_b64("./07-streamlit/images/LI-In-Bug.png")
            github_logo = get_image_b64("./07-streamlit/images/github-mark-white.png")
            st.markdown(
                f'''
                <div style="display: flex; justify-content: center;">
                    <a href="{persona["linkedin"]}"><img src="data:image/png;base64,{linkedin_logo}" alt="LinkedIn" width="50"/></a>
                    <a href="{persona["github"]}"><img src="data:image/png;base64,{github_logo}" alt="GitHub" width="40"/></a>
                </div>
                ''', 
                unsafe_allow_html=True
            )

# Definir otras páginas
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
    body {
        background-color: #2e2e2e;
        color: white;
    }
    .centered-img {
        display: flex;
        justify-content: center;
        align-items: center;
    }
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

# HTML para los botones
st.markdown(f"""
    <div class="centered-btns">
        <a href="/?page=home" class="custom-btn">Home</a>
        <a href="/?page=dashboard" class="custom-btn">Dashboard</a>
        <a href="/?page=modelos" class="custom-btn">Modelos</a>
    </div>
""", unsafe_allow_html=True)

# Lógica de navegación
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# Muestra la página correspondiente
if page == "home":
    st.write("Estás en Home")
elif page == "dashboard":
    st.write("Estás en el Dashboard")
elif page == "modelos":
    st.write("Estás en Modelos")
