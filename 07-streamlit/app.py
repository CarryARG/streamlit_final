import streamlit as st
from PIL import Image
import base64

# Función para obtener la imagen en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        return None

# Definir el logo de Arcope
img1 = Image.open('./07-streamlit/images/arcope-logo.jpeg')

# Convertir la imagen a base64
with open("./07-streamlit/images/arcope-logo.jpeg", "rb") as img_file:
    b64_1 = base64.b64encode(img_file.read()).decode()

# CSS para personalizar los botones y el diseño general
st.markdown("""
    <style>
        /* Estilos de los botones */
        .custom-btn {
            display: inline-block;
            padding: 10px 25px;
            margin: 0 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            background-color: #FFB74D;  /* Ajusta según los colores que prefieras */
            color: #FFF;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        /* Efecto hover */
        .custom-btn:hover {
            background-color: #FFA726;  /* Cambiar al color que prefieras */
        }

        /* Centrar los botones */
        .centered-btns {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        /* Centrar la imagen */
        .centered-img {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Barra de navegación con los botones personalizados
st.markdown(f"""
    <div class="centered-btns">
        <button onclick="window.location.href='/?page=home'" class="custom-btn">Home</button>
        <button onclick="window.location.href='/?page=dashboard'" class="custom-btn">Dashboard</button>
        <button onclick="window.location.href='/?page=modelos'" class="custom-btn">Modelos</button>
    </div>
""", unsafe_allow_html=True)

# Obtener los parámetros de la URL para cambiar de página sin abrir una nueva pestaña
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]

# Lógica para mostrar el contenido según la página seleccionada
if page == "home":
    # Mostrar el logo de Arcope en el centro
    st.markdown(f'''
        <div class="centered-img">
            <img src="data:image/jpeg;base64,{b64_1}" style="width: 300px; height: 300px;" />
        </div>
    ''', unsafe_allow_html=True)

    st.header("Bienvenidos ⭐")

    intro = """
    Hola, en esta plataforma podrás gestionar y administrar de manera útil y práctica las opiniones de los clientes. Esta herramienta servirá como punto central para detectar oportunidades de negocio y mejorar procesos en todos los niveles, desde las tiendas locales hasta los directivos a nivel global.
    """

    a = "➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
    b = "➡️ Ver estadísticas sobre las reseñas, como la distribución de los sentimientos y las palabras más comunes."
    c = "➡️ Explorar las reseñas en detalle, con la capacidad de filtrar por sentimiento y buscar palabras clave."
    d = "➡️ Dashboard de control que permite una visualización que facilita el monitoreo del negocio basados en las plataformas Google y Yelp."

    st.markdown(f'<h3>{intro}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3>{a}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3>{b}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3>{c}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3>{d}</h3>', unsafe_allow_html=True)

elif page == "dashboard":
    st.title("Dashboard 📊")
    st.write("Aquí irá el contenido del dashboard.")

elif page == "modelos":
    st.title("Modelos 🧠")
    st.write("Aquí irá el contenido relacionado con los modelos.")

# Información del equipo
st.header("Desarrollado por ⚙️")

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

        linkedin_logo = get_image_b64("./07-streamlit/images/LI-In-Bug.png")
        github_logo = get_image_b64("./07-streamlit/images/github-mark-white.png")
        st.markdown(f'''
            <div style="display: flex; justify-content: center;">
                <a href="{persona["linkedin"]}"><img src="data:image/png;base64,{linkedin_logo}" alt="LinkedIn" width="50"/></a>
                <a href="{persona["github"]}"><img src="data:image/png;base64,{github_logo}" alt="GitHub" width="40"/></a>
            </div>
        ''', unsafe_allow_html=True)
