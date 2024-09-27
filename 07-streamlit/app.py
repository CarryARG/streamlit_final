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

# Inyectar el CSS personalizado
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        section[data-testid='stSidebar'] {
            background-color: #2E3159 !important;
            flex-shrink: unset !important;
        }
        .custom-button {
            background-color: #4CAF50; 
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;  
        }    
        .card {
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: 0.3s;
            border-radius: 5px;
        }
        .card:hover {
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);  
        }
    </style>
""", unsafe_allow_html=True)

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

# Sidebar
with st.sidebar:
    st.title("Mi Aplicación")

# Crear pestañas
tab1, tab2, tab3 = st.tabs(["Home", "Dashboard", "Modelos"])

# Contenido de la pestaña Home
if tab1:
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
            "nombre": "Florencia Lascurain",
            "profesion": "Project Manager & Data Scientist",
            "github": "https://github.com/FlorLascu",
            "linkedin": "https://www.linkedin.com/in/florencia-lascurain-1a890938/",
            "imagen_link": "./07-streamlit/images/Flor.png"
        },
        {
            "nombre": "Facundo Denis",
            "profesion": "Machine Learning Engineer",
            "github": "https://github.com/Facundo022",
            "linkedin": "https://www.linkedin.com/in/facundo-nicolas-denis-60933b199/",
            "imagen_link": "./07-streamlit/images/Facu.png"
        },
        {
            "nombre": "Cristhian Huanqui",
            "profesion": "Machine Learning Engineer",
            "github": "https://github.com/Kipros21",
            "linkedin": "https://www.linkedin.com/in/cristhian-huanqui-tapia-35a653185/",
            "imagen_link": "./07-streamlit/images/Cris.png"
        },
        {
            "nombre": "Gabriel Rojas",
            "profesion": "Data Analyst",
            "github": "https://github.com/ga-romu",
            "linkedin": "https://www.linkedin.com/in/g-a-ro-mu/",
            "imagen_link": "./07-streamlit/images/Gabi.png"
        },
        {
            "nombre": "Iván Parra",
            "profesion": "Data Engineer",
            "github": "https://github.com/Ivan2125",
            "linkedin": "https://www.linkedin.com/in/ivan-parra-2501/",
            "imagen_link": "./07-streamlit/images/Ivan.png"
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

elif tab2 == "Dashboard":
    st.header("Dashboard 📊", divider='rainbow', anchor=False)
    
    intro = "Hola,"
    a = "➡️ Analizar las reseñas de Walgreens en Google y Yelp, y obtener una visión general de los sentimientos expresados en ellas."
    
    st.markdown(f'<h3 style="text-align: left;">{intro}</h3>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: left; font-size: 23px;">{a}</h3>', unsafe_allow_html=True)
    
    # Función para cargar y mostrar el gráfico de Tableau
    def mostrar_tableau():
        embed_code = """
        <div style='display: flex; justify-content: center; width: 100%; margin: auto'>
            <div class='tableauPlaceholder' id='viz1713209577914' style='position: relative; margin: auto'>
                <noscript>
                    <a href='#'><img alt='Principales competidores ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1&#47;1_rss.png' style='border: none' /></a>
                </noscript>
                <object class='tableauViz' style='display:none;'>
                    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
                    <param name='embed_code_version' value='3' /> 
                    <param name='name' value='Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1' />
                    <param name='tabs' value='no' />
                    <param name='toolbar' value='yes' />
                    <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Wa&#47;Walgreens-reviewsanalysisonGoogleYelp&#47;Tablero1&#47;1.png' /> 
                    <param name='animate_transition' value='yes' />
                    <param name='display_static_image' value='yes' />
                    <param name='display_spinner' value='yes' />
                    <param name='display_overlay' value='yes' />
                    <param name='display_count' value='yes' />
                    <param name='language' value='es-ES' />
                </object>
            </div>
        </div>
        <script type='text/javascript'>
            var divElement = document.getElementById('viz1713209577914');
            var vizElement = divElement.getElementsByTagName('object')[0];
            if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
            else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';}
            else { vizElement.style.width='100%';vizElement.style.height='977px';}                     
            var scriptElement = document.createElement('script');
            scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
            vizElement.parentNode.insertBefore(scriptElement, vizElement);
        </script>
        """
        components.html(embed_code, height=2000, width=1709)

    mostrar_tableau()
