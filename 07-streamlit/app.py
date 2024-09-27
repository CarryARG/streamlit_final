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

# CSS para personalizar el navbar y eliminar los espacios sobrantes
st.markdown("""
    <style>
        /* Ocultar el menú de hamburguesa, el botón de compartir y el botón de editar */
        #MainMenu, header, footer {
            visibility: hidden;
        }

        /* Estilos de los botones en el navbar */
        .nav-item {
            background-color: #F2A649;
            color: #FFF;
            padding: 10px 20px;
            border-radius: 5px;
          }

        /* Efecto hover en los botones del navbar */
        .nav-item:hover {
            background-color: #F25E3D; /* Color más oscuro para el hover */
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2); /* Sombra suave */
        }

        /* Estilos para centrar y justificar los elementos del navbar */
        .navbar-custom {
            background-color: #000000;
            padding: 20px;
            display: flex;
            justify-content: space-around;
            width: 100%; /* Ocupa todo el ancho de la pantalla */
            margin: 0; /* Eliminar margen superior */
            position: fixed; /* Fijar el navbar en la parte superior */
            top: 0;
            left: 0;
            z-index: 1000; /* Asegurar que quede encima de otros elementos */
        }

        /* Eliminar el padding alrededor de la aplicación */
        .css-18e3th9 {
            padding: 0;
        }

        /* Ajustar margen superior del contenido para que no quede detrás del navbar */
        .main-content {
            margin-top: 80px;  /* Ajusta según la altura del navbar */
        }

    </style>
""", unsafe_allow_html=True)

# HTML para el Navbar utilizando Bootstrap con los botones personalizados
st.markdown(f"""
    <nav class="navbar-custom">
        <a href="#" class="nav-item" onclick="window.location.href='/?page=home'">Home</a>
        <a href="#" class="nav-item" onclick="window.location.href='/?page=dashboard'">Dashboard</a>
        <a href="#" class="nav-item" onclick="window.location.href='/?page=modelos'">Modelos</a>
    </nav>
""", unsafe_allow_html=True)

# Contenido basado en la página seleccionada
if page == "home":
    home.home_page()  # Llama a la función home_page del archivo home.py
elif page == "dashboard":
    dashboard.dashboard_page()  # Llama a la función dashboard_page del archivo dashboard.py
elif page == "modelos":
    modelos_ml.modelos_page()  # Llama a la función modelos_ml_page del archivo modelos_ml.py
