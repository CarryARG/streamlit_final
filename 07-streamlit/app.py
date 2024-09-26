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

# Título de la aplicación
st.title("Análisis de Sentimientos de Reviews de Walgreens")

# Menú de navegación
page = st.sidebar.selectbox("Selecciona una página:", ["Home", "Dashboard", "Modelos"])

# Almacenamos el estado de la página seleccionada
if 'page' not in st.session_state or st.session_state.page != page:
    st.session_state.page = page
    st.experimental_rerun()  # Reinicia la aplicación al cambiar de página

# Cargamos la página correspondiente
if st.session_state.page == "Home":
    import home  # Importar la página de presentación
elif st.session_state.page == "Dashboard":
    import dashboard  # Importar la página de dashboard
elif st.session_state.page == "Modelos":
    import modelos  # Importar la página de modelos
