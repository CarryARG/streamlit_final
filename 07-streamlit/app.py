import streamlit as st
import base64

# Función para cargar imágenes en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

# Establecer la aplicación en modo wide
st.set_page_config(layout="wide")

# Incluir Bootstrap CSS y JavaScript
st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" 
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" 
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9P/ScQsAP7hUibX39j13EVY4pQ11VVn1+kpZ60" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" 
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

# Ocultar los elementos no deseados del menú superior y el espaciado adicional
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;} /* Ocultar el menú de arriba a la derecha */
        footer {visibility: hidden;} /* Ocultar el pie de página */
        header {visibility: hidden;} /* Ocultar el header */
        .css-18e3th9 {padding: 0;} /* Eliminar padding sobrante */
    </style>
""", unsafe_allow_html=True)

# Inicializar la variable de sesión para la navegación entre páginas
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Funciones para cambiar de página
def go_home():
    st.session_state.page = "Home"

def go_dashboard():
    st.session_state.page = "Dashboard"

def go_modelos():
    st.session_state.page = "Modelos"

# Navegación entre páginas
page = st.sidebar.radio("Navegación", ["Home", "Modelos"])


# Crear el navbar con Bootstrap
st.markdown("""
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Mi Aplicación</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#" onclick="window.location.href='/?page=home';">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" onclick="window.location.href='/?page=dashboard';">Dashboard</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" onclick="window.location.href='/?page=modelos';">Modelos</a>
          </li>
        </ul>
      </div>
    </nav>
""", unsafe_allow_html=True)

# Dependiendo de la página seleccionada, mostrar contenido distinto
if page == "Home":
    import streamlit as st
    from PIL import Image
    import base64
    
    def get_image_b64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    
    # Logo de la empresa
    img1 = Image.open('./07-streamlit/images/arcope-logo.jpeg')
    st.markdown(f"<div style='text-align: center;'><img src='data:image/jpeg;base64,{get_image_b64('./07-streamlit/images/arcope-logo.jpeg')}' width='300'/></div>", unsafe_allow_html=True)
    
    # Título del proyecto
    st.header("ARCOPE Proyecto Final - Henry", divider='rainbow')
    
    # Descripción del proyecto
    st.markdown("""
    ## Proyecto: Data Product orientado a la sostenibilidad y rentabilidad para Uber en la ciudad de New York.
    
    ### Objetivo Principal:
    Transformar el negocio de Uber en un referente de sostenibilidad y rentabilidad a largo plazo...
    
    ### Cliente Objetivo:
    Empresa de Ride-Hailing, 'Uber'...
    
    ### Estrategia de Negocio:
    Uber busca herramientas para mejorar su imagen corporativa, incrementar la rentabilidad...
    
    ### Alcance:
    Proponemos un MVP centrado en analizar y procesar datos proporcionados por Uber...
    
    ### Justificación:
    El mercado está en plena transición hacia modelos sostenibles. Las empresas que adoptan prácticas sostenibles...
    
    ## Objetivos Particulares:
    
    ### 1. Mejorar la Imagen Corporativa a través de la Sostenibilidad
    **KPI**: Reducción de CO2 y mejora de la calidad del aire...
    
    ### 2. Incrementar la Rentabilidad a Largo Plazo
    **KPI**: Costos y beneficios por vehículo eléctrico...
    
    ### 3. Maximizar la Eficiencia Operativa
    **KPI**: Ingresos por milla recorrida...
    
    """)
    
    # Divider
    st.divider()
    
    # Información del equipo
    st.header("Desarrollado por ⚙️", divider='rainbow')
    
    personas = [
        {"nombre": "Cristian Moreira", "profesion": "Project Manager", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/cristian.jpeg"},
        {"nombre": "Andres Aguirre", "profesion": "Technical Project Manager & Data Analytics", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/andres.jpeg"},
        {"nombre": "Jeison Zapata", "profesion": "Data Scientist & Data Analyst", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/jeison.jpeg"},
        {"nombre": "Libardo Alarcon", "profesion": "Data Scientist", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/libardo.jpeg"},
        {"nombre": "Manuel Carruitero", "profesion": "Data Engineer", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/manuel.jpeg"},
        {"nombre": "Lucas Carranza", "profesion": "Data Engineer", "github": "https://github.com/", "linkedin": "https://www.linkedin.com/", "imagen_link": "./07-streamlit/images/lucas.jpeg"}
    ]
    
    columns = st.columns(len(personas))
    for idx, persona in enumerate(personas):
        with columns[idx]:
            st.markdown(f'<h2 style="text-align: center; margin-bottom: 0px;">{persona["nombre"]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<h4 style="text-align: center; color: gray;">{persona["profesion"]}</h4>', unsafe_allow_html=True)
            
            persona_image = get_image_b64(persona["imagen_link"])
            if persona_image:
                st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{persona_image}" style="border-radius: 50%;" width="150"/></div>', unsafe_allow_html=True)
            
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

elif page == "Dashboard":
    # Muestra la página de modelos
    dashboard_page()
elif page == "Modelos":
    # Muestra la página de modelos
    modelos_page()
