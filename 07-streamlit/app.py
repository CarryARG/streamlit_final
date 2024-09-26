import streamlit as st
from PIL import Image
import base64

# Función para cargar imágenes en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

# Imagen de la empresa
img1 = Image.open('./07-streamlit/images/arcope-logo.jpeg')  # Cambié la ruta a la que subiste
st.image(img1, use_column_width=True)

# Bienvenida
st.header("Bienvenidos ⭐", divider='rainbow')

intro = """
Hola, en esta plataforma podrás gestionar y administrar de manera útil y práctica las opiniones de los clientes. 
Esta herramienta servirá como punto central para detectar oportunidades de negocio y mejorar procesos en todos los niveles, 
desde las tiendas locales hasta los directivos a nivel global.
""" 

a ="➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
b = "➡️ Ver estadísticas sobre las reseñas, como la distribución de los sentimientos y las palabras más comunes."
c = "➡️ Explorar las reseñas en detalle, con la capacidad de filtrar por sentimiento y buscar palabras clave."
d = "➡️ Dashboard de control que permite una visualización que facilita el monitoreo del negocio basado en Google y Yelp."

st.markdown(f"<p style='text-align: center; font-size: 20px;'>{intro}</p>", unsafe_allow_html=True)

# Lista de puntos clave
for punto in [a, b, c, d]:
    st.markdown(f"<p style='text-align: left; font-size: 18px;'>{punto}</p>", unsafe_allow_html=True)

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

# Mejora en la disposición del equipo
columns = st.columns(len(personas))
for idx, persona in enumerate(personas):
    with columns[idx]:
        # Nombre y profesión centrados
        st.markdown(f'<h2 style="text-align: center; margin-bottom: 0px;">{persona["nombre"]}</h2>', unsafe_allow_html=True)
        st.markdown(f'<h3 style="text-align: center; color: gray;">{persona["profesion"]}</h3>', unsafe_allow_html=True)
        
        # Imagen del equipo
        persona_image = get_image_b64(persona["imagen_link"])
        if persona_image:
            st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{persona_image}" style="border-radius: 50%;" width="150"/></div>', unsafe_allow_html=True)

        # Logos de redes sociales
        linkedin_logo = get_image_b64("./07-streamlit/images/LI-In-Bug.png")
        github_logo = get_image_b64("./07-streamlit/images/github-mark-white.png")
        st.markdown(
            f'''
            <div style="display: flex; justify-content: center; margin-top: 10px;">
                <a href="{persona["linkedin"]}"><img src="data:image/png;base64,{linkedin_logo}" alt="LinkedIn" width="30" style="margin-right: 10px;"/></a>
                <a href="{persona["github"]}"><img src="data:image/png;base64,{github_logo}" alt="GitHub" width="30"/></a>
            </div>
            ''', 
            unsafe_allow_html=True
        )
