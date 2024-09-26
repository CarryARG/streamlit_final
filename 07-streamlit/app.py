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

# Menú de navegación
page = st.sidebar.selectbox("Selecciona una página:", ["Home", "Dashboard", "Modelos"])

# Contenido de la pestaña Home
if page == "Home":
    st.header("Bienvenido a la Página Principal")
    st.write("Este es el contenido de la pestaña Home.")
    
    # Mostrar imágenes
    img1_b64 = get_image_b64('./07-streamlit/images/g1-logo.png')
    img2_b64 = get_image_b64('./07-streamlit/images/walg-logo.png')
    
    if img1_b64 and img2_b64:
        st.markdown(f'''
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{img1_b64}" style="margin-right: 10px; width: 300px; height: 300px;" />
                <img src="data:image/png;base64,{img2_b64}" style="margin-left: 100px; width: 600px; height: 200px;" />
            </div>
        ''', unsafe_allow_html=True)

    intro = """
    Hola, en esta plataforma podrás gestionar y administrar de manera útil y práctica las opiniones de los clientes. Esta herramienta servirá como punto central para detectar oportunidades de negocio y mejorar procesos en todos los niveles, desde las tiendas locales hasta los directivos a nivel global.
    """
    st.markdown(intro, unsafe_allow_html=True)

    # Lista de funciones
    funciones = [
        "➡️ Analizar las reseñas de Walgreens en Google y Yelp.",
        "➡️ Ver estadísticas sobre las reseñas.",
        "➡️ Explorar las reseñas en detalle.",
        "➡️ Dashboard de control para el monitoreo del negocio."
    ]
    
    for funcion in funciones:
        st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{funcion}</h3>', unsafe_allow_html=True)

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
        }
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

# Contenido de la pestaña Dashboard
elif page == "Dashboard":
    st.header("Dashboard")
    st.write("Aquí puedes agregar el contenido de tu dashboard.")
    # Agrega gráficos, estadísticas y otros elementos necesarios

# Contenido de la pestaña Modelos
elif page == "Modelos":
    st.header("Modelos de Machine Learning")
    st.write("Aquí puedes agregar el contenido relacionado con los modelos de machine learning.")
    # Agrega los elementos y modelos necesarios

