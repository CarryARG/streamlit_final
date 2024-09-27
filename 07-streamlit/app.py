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
