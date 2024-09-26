import streamlit as st
import base64
import nltk
from PIL import Image

st.header("Bienvenido a la Página Principal")
st.write("Este es el contenido de la pestaña Home.")

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

# Crear un encabezado para la navegación
st.title("Análisis de Sentimientos de Reviews de Walgreens")

# Crear botones para la navegación
nav_options = st.radio("Selecciona una sección:", ("Home", "Dashboard", "Modelos"))

# Contenido de la sección Home
if nav_options == "Home":
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

    # Contenido adicional
    st.markdown("""
    ![Logo del Proyecto](./imagenes/logo/Logo_ARCOPE_fondo_transparente.png)

    # ARCOPE Proyecto Final - Henry

    ## Proyecto: Data Product orientado a la sostenibilidad y rentabilidad para Uber en la ciudad de New York.

    ### Objetivo Principal:
    Transformar el negocio de Uber en un referente de sostenibilidad y rentabilidad a largo plazo mediante la optimización operativa, la inversión en tecnología sustentable y la mejora de la imagen corporativa, para atraer tanto a clientes conscientes del medio ambiente como a inversores interesados en sostenibilidad.

    ### Cliente Objetivo:
    Empresa de Ride-Hailing, 'Uber', que conecta pasajeros con conductores de vehículos de alquiler a través de aplicaciones móviles y sitios web.

    ### Estrategia de Negocio:
    Uber busca herramientas para mejorar su imagen corporativa, incrementar la rentabilidad y maximizar la eficiencia operativa, con el objetivo de alinear su negocio hacia un enfoque más sustentable y atractivo para los inversores.

    ### Alcance:
    Proponemos un MVP centrado en analizar y procesar datos proporcionados por Uber y organismos gubernamentales, ofreciendo soluciones que permitan la toma de decisiones estratégicas basadas en sostenibilidad y rentabilidad.

    ### Contexto:
    Ciudad de Nueva York, EEUU.

    ### Justificación:
    El mercado está en plena transición hacia modelos sostenibles. Las empresas que adoptan prácticas sostenibles no solo mejoran su imagen pública, sino que también aseguran su rentabilidad a largo plazo al alinearse con normativas futuras. Este proyecto posicionará a Uber como líder en sostenibilidad en el sector Ride-Hailing, atrayendo a clientes conscientes del medio ambiente y ofreciendo nuevas oportunidades de negocio e incentivos fiscales.

    ## Objetivos Particulares:

    ### 1. Mejorar la Imagen Corporativa a través de la Sostenibilidad
    - **KPI**: Reducción de CO2 y mejora de la calidad del aire.
    - **Medir**: Comparar las emisiones de CO2 de la flota actual con una nueva flota de vehículos híbridos y eléctricos. También se medirá la calidad del aire en áreas con alta concentración de operaciones.
    - **Impacto**: Posicionamiento como líder en sostenibilidad, atracción de un segmento de mercado más consciente del medio ambiente, y mejora de la percepción pública.

    ### 2. Incrementar la Rentabilidad a Largo Plazo mediante Inversión en Vehículos Eléctricos/Híbridos
    - **KPI**: Costos y beneficios por vehículo eléctrico en relación a la distancia recorrida.
    - **Medir**: Comparar los costos operativos y beneficios de los vehículos eléctricos frente a los de combustión interna.
    - **Impacto**: Reducción de costos operativos, acceso a incentivos fiscales, y mejora en la rentabilidad a largo plazo.

    ### 3. Maximizar la Eficiencia Operativa y la Rentabilidad del Servicio
    - **KPI 3a**: Ingresos por milla recorrida. 
      - **Medir**: (Total_amount - Tolls_amount - Congestion_Surcharge - Airport_fee) / Trip_distance.
      - **Impacto**: Optimización de rutas, asignación de vehículos y tarifas para maximizar ingresos.
      
    - **KPI 3b**: Tasa de utilización de vehículos.
      - **Medir**: Total de viajes / Número total de horas disponibles.
      - **Impacto**: Incremento de la rentabilidad al mejorar la utilización de la flota.

    - **KPI 3c**: Promedio de pasajeros por viaje.
      - **Medir**: Promedio(Passenger_count) por zona, tipo de servicio y hora del día.
      - **Impacto**: Fomento del uso compartido de vehículos para incrementar la rentabilidad y reducir la cantidad de vehículos necesarios.

    ## Análisis de Impacto:
    Implementar estos KPIs proporcionará una visión clara del desempeño de Uber en términos de sostenibilidad y rentabilidad. Basándose en estos análisis, se podrán tomar decisiones estratégicas como expandir la flota de vehículos eléctricos, optimizar rutas para reducir emisiones y costos, y rediseñar campañas de marketing centradas en el compromiso ambiental.

    Este proyecto ayudará a Uber no solo a cumplir con sus objetivos de sostenibilidad, sino también a mejorar su imagen pública y garantizar su rentabilidad a largo plazo, consolidándose como un líder en innovación dentro del sector de Ride-Hailing.
    """)

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
                <div style="display: flex; justify-content: center; gap: 10px;">
                    <a href="{persona["linkedin"]}" target="_blank">
                        <img src="data:image/png;base64,{linkedin_logo}" width="40"/>
                    </a>
                    <a href="{persona["github"]}" target="_blank">
                        <img src="data:image/png;base64,{github_logo}" width="40"/>
                    </a>
                </div>
                ''', unsafe_allow_html=True
            )
