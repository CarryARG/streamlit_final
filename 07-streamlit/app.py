import streamlit as st
import home  # Importar la página 'home.py'
import dashboard  # Importar la página 'dashboard.py'
import modelos  # Importar la página 'modelos_ml.py'
import base64

# Configuración general de la página
st.set_page_config(page_title="ARCOPE App", layout="wide")
st.cache_data.clear()  # Limpiar la caché al cargar la página

# Incluir Bootstrap CSS y JavaScript
st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

# Ocultar elementos no deseados
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .css-18e3th9 {padding: 0;}
    </style>
""", unsafe_allow_html=True)

# Obtener la página actual desde los parámetros de consulta
query_params = st.query_params  # Usamos st.query_params
page = query_params.get("page", ["home"])[0]  # Recupera el valor de 'page'

# CSS para personalizar el navbar
st.markdown("""
    <style>
        .navbar-custom {
            background-color: #000000;
            padding: 20px;
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 1000;
        }
        .nav-item {
            background-color: #F2A649;
            color: #FFF;
            padding: 10px 20px;
            border-radius: 5px;
            margin-right: 10px; /* Espaciado entre botones */
        }
        .nav-item:hover {
            background-color: #F25E3D; /* Color para hover */
        }
    </style>
""", unsafe_allow_html=True)

# HTML para el Navbar utilizando Bootstrap
st.markdown(f"""
    <nav class="navbar-custom">
        <a class="nav-item" href="/?page=home">Home</a>
        <a class="nav-item" href="/?page=dashboard">Dashboard</a>
        <a class="nav-item" href="/?page=modelos">Modelos</a>
    </nav>
""", unsafe_allow_html=True)

# Contenido basado en la página seleccionada
if page == "home":
    home.home_page()  # Asegúrate de que esta función esté correctamente definida
elif page == "dashboard":
    dashboard.dashboard_page()  # Asegúrate de que esta función esté correctamente definida
elif page == "modelos":
    modelos.modelos_page()  # Asegúrate de que esta función esté correctamente definida
