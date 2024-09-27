import streamlit as st
import home  # Importar la página 'home.py'
import base64

# Configuración general de la página (debe ir antes de cualquier otro comando de Streamlit)
st.set_page_config(page_title="ARCOPE App", layout="wide")

# Función para cargar imágenes en base64
def get_image_b64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        return None

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

# Función para la navegación mediante URL de consulta (query parameter)
def navigate_to(page):
    st.experimental_set_query_params(page=page)

# Obtener la página actual de los parámetros de consulta (URL)
query_params = st.query_params
page = query_params.get("page", ["home"])[0]

# Asignar clases CSS condicionales
home_active = "active" if page == "home" else ""
other_active = "active" if page == "otra_pagina" else ""

# Menú de navegación con Bootstrap
st.markdown("""
    <style>
    .navbar {
        overflow: hidden;
        background-color: #333;
        position: fixed;
        top: 0;
        width: 100%;
    }
    
    .navbar a {
        float: left;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
        font-size: 17px;
    }
    
    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }
    
    .navbar a.active {
        background-color: #04AA6D;
        color: white;
    }
    
    .content {
        padding: 16px;
        margin-top: 50px;
    }
    </style>

    <div class="navbar">
        <a href="#" class="{}" onclick="window.location.href='/?page=home'">Home</a>
        <a href="#" class="{}" onclick="window.location.href='/?page=otra_pagina'">Otra Página</a>
    </div>
    """, unsafe_allow_html=True)

# Contenido basado en la página seleccionada
if page == "home":
    home.home_page()  # Llama a la función home_page del archivo home.py
elif page == "otra_pagina":
    st.write("Aquí puedes cargar otra página o funcionalidad")
