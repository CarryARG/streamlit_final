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

if page == "Home":
    import home
elif page == "Dashboard":
    import dashboard
elif page == "Modelos":
    import modelos
