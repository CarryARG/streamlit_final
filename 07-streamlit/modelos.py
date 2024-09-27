import streamlit as st
import home  # Asegúrate de que home.py esté correctamente definido
import dashboard  # Importa el archivo dashboard.py
import modelos  # Importa el archivo modelos_ml.py
import base64
from PIL import Image

def modelos_page():
    st.title("Modelos de Machine Learning")
    st.write("Aquí se mostrarán los modelos de Machine Learning.")
