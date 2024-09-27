import streamlit as st
import home  # Asegúrate de que home.py esté correctamente definido
import dashboard  # Importa el archivo dashboard.py
import modelos_ml  # Importa el archivo modelos_ml.py
import base64
from PIL import Image

def dashboard_page():
    st.title("Dashboard")
    st.write("Aquí se mostrará el dashboard con gráficas y KPIs.")
