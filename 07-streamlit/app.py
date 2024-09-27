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
if st.session_state.page == "Home":
    st.title("Bienvenido a la página principal")
    st.write("Aquí puedes agregar contenido sobre la página principal.")
elif st.session_state.page == "Dashboard":
    st.title("Dashboard")
    st.write("Aquí puedes mostrar tus gráficos de Plotly.")
elif st.session_state.page == "Modelos":
    st.title("Modelos")
    st.write("Aquí puedes describir los modelos disponibles.")
