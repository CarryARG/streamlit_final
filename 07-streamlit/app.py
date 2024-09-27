import streamlit as st
from PIL import Image
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

# Incluir Bootstrap desde CDN
st.markdown("""
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
""", unsafe_allow_html=True)

# Inicializar la variable de sesión para controlar la página actual
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Funciones para cambiar de página
def go_home():
    st.session_state.page = "Home"

def go_dashboard():
    st.session_state.page = "Dashboard"

def go_modelos():
    st.session_state.page = "Modelos"

# CSS para personalizar el navbar y eliminar los espacios sobrantes
st.markdown("""
    <style>
        /* Ocultar el menú de hamburguesa, el botón de compartir y el botón de editar */
        #MainMenu, header, footer {
            visibility: hidden;
        }

        /* Estilos de los botones en el navbar */
        .nav-item {
            font-weight: bold;
            text-align: center;
            text-decoration: none;
            background-color: #FFB74D;
            color: #FFF !important;
            border-radius: 8px;
            padding: 10px 20px;
            margin: 0 15px;
            border: 2px solid #E65100;
            transition: background-color 0.3s ease, border-color 0.3s ease;
        }

        /* Efecto hover en los botones del navbar */
        .nav-item:hover {
            background-color: #FFA726;
            border-color: #FB8C00;
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
            z-index: 1; /* Asegurar que quede encima de otros elementos */
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

# Agregar JavaScript para ocultar el navbar cuando se haga scroll hacia abajo y mostrarlo cuando se haga scroll hacia arriba
st.markdown("""
    <script>
        var prevScrollpos = window.pageYOffset;
        window.onscroll = function() {
            var currentScrollPos = window.pageYOffset;
            if (prevScrollpos > currentScrollPos) {
                document.querySelector('.navbar-custom').style.top = "0";
            } else {
                document.querySelector('.navbar-custom').style.top = "-100px";
            }
            prevScrollpos = currentScrollPos;
        }
    </script>
""", unsafe_allow_html=True)

# HTML para el Navbar utilizando Bootstrap con los botones personalizados
st.markdown(f"""
    <nav class="navbar-custom">
        <a href="/?page=home" class="nav-item">Home</a>
        <a href="/?page=dashboard" class="nav-item">Dashboard</a>
        <a href="/?page=modelos" class="nav-item">Modelos</a>
    </nav>
""", unsafe_allow_html=True)

# Espacio para evitar que el contenido quede detrás del navbar
st.markdown('<div class="main-content"></div>', unsafe_allow_html=True)

# Lógica de navegación entre páginas basada en el estado
if st.session_state.page == "Home":
    # Imagen de la empresa con tamaño ajustado
    img1 = Image.open('./07-streamlit/images/arcope-logo.jpeg')  # Cambié la ruta a la que subiste
    # Usa un contenedor HTML para centrar la imagen
    st.markdown(
        f"<div style='text-align: center;'><img src='data:image/jpeg;base64,{get_image_b64('./07-streamlit/images/arcope-logo.jpeg')}' width='300'/></div>",
        unsafe_allow_html=True
    )
    
    # Título del proyecto
    st.header("ARCOPE Proyecto Final - Henry", divider='rainbow')
    
    # Descripción del proyecto
    st.markdown("""
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
    
    ---
    ## **Propuesta y Stack Tecnológico**
    
    ---
    
    ### **1. Ingesta de Datos y ETL (Extract, Transform, Load)**
    
    **Herramientas y Tecnologías:**
    
    - **Lenguaje de Programación: Python**
      - **Descripción:** Lenguaje versátil y ampliamente utilizado en ciencia de datos y machine learning.
      
    - **Bibliotecas de Python:**
      - **Pandas:** Para la manipulación y limpieza de datos provenientes de archivos CSV o Parquet.
      - **PyArrow:** Para leer y escribir archivos Parquet de manera eficiente.
      
    - **Data Lake: MinIO**
      - **Descripción:** MinIO es un sistema de almacenamiento de objetos. Se utiliza para almacenar datos en bruto y transformados, facilitando su acceso durante las etapas de ETL.
      
    - **Gestión de Entornos:**
      - **Visual Studio Code:** Facilita la gestión de paquetes y entornos virtuales, asegurando que todas las dependencias estén correctamente instaladas.
    
    **Justificación:**
    - **Python**, junto con **Pandas** y **PyArrow**, proporciona una solución robusta y flexible para la ingesta y transformación de datos, permitiendo manejar diferentes formatos de archivo de manera eficiente.
    - **MinIO** actúa como un Data Lake, proporcionando almacenamiento centralizado y escalable para grandes volúmenes de datos en diferentes formatos, facilitando el acceso rápido y eficiente para las siguientes fases del pipeline.
    
    ---
    ## **2. Ingreso en la Base de Datos (Data Warehouse)**
    
    ### **Herramientas y Tecnologías:**
    
    - **Sistema de Gestión de Bases de Datos: MySQL**
      - **Descripción**: Base de datos relacional ampliamente utilizada, adecuada para almacenar datos transformados y modelos entrenados.
    
    - **Interfaz de Administración: phpMyAdmin**
      - **Descripción**: Herramienta web para gestionar MySQL de manera visual y sencilla, facilitando la administración y consulta de la base de datos.
    
    - **Conexión y ORM: SQLAlchemy**
      - **Descripción**: Biblioteca de Python para interactuar con bases de datos SQL de manera eficiente y segura.
    
    ### **Justificación:**
    MySQL es una opción sólida para almacenar datos estructurados, y phpMyAdmin ofrece una interfaz amigable para la administración. SQLAlchemy simplifica las interacciones entre Python y la base de datos, permitiendo una integración fluida en el pipeline.
    
    ---
    ## **3. Entrenamiento del Modelo de Machine Learning**
    
    ### **Herramientas y Tecnologías:**
    
    - **Bibliotecas de Machine Learning:**
      - **Scikit-learn**: Ideal para modelos de machine learning básicos y medianamente complejos, como regresión y clasificación.
    
    - **Serialización de Modelos:**
      - **Pickle**: Para guardar y cargar modelos entrenados de manera sencilla.
    
    - **Entorno de Desarrollo:**
      - **Jupyter Notebook**: Para desarrollar, entrenar y documentar modelos de manera interactiva.
    
    ### **Justificación:**
    Scikit-learn es perfecto para comenzar con machine learning gracias a su simplicidad y eficacia. Jupyter Notebook facilita la experimentación y documentación del proceso de entrenamiento.
    
    ---
    ## **4. Creación de Dashboards e Informes**
    
    ### **Herramientas y Tecnologías:**
    
    - **Visualización de Datos:**
      - **Matplotlib y Seaborn**: Para crear gráficos estáticos y visualizaciones detalladas.
      - **Plotly** (opcional): Para visualizaciones interactivas si se requiere mayor dinamismo en los dashboards.
    
    - **Generación de Informes:**
      - **Jupyter Notebook**: Para crear informes interactivos que combinan código, visualizaciones y texto descriptivo.
      - **ReportLab** (opcional): Para generar informes en formato PDF si se necesita distribuir documentos estáticos.
    
    - **Desarrollo de Dashboards Interactivos:**
      - **Streamlit** o **Dash**: Frameworks de Python para crear aplicaciones web interactivas y dashboards de manera rápida y sencilla.
    
    ### **Justificación:**
    Matplotlib y Seaborn ofrecen una base sólida para la visualización de datos, mientras que herramientas como Streamlit permiten transformar estos gráficos en dashboards interactivos. Jupyter Notebook combina análisis y visualización en un solo entorno, facilitando la creación de informes comprensibles y detallados.
    
    ---
    ## **Infraestructura y Seguridad**
    
    ### **Herramientas y Tecnologías:**
    
    - **Servidor Local:**
      - **Descripción**: Un servidor donde se alojarán MySQL y phpMyAdmin, accesible desde internet para permitir conexiones remotas.
    
    - **Seguridad de la Base de Datos:**
      - **Configuración de MySQL para Acceso Remoto**: Asegurar que MySQL esté configurado para aceptar conexiones remotas de manera segura.
      - **Autenticación y Autorización**: Gestionar permisos de usuarios para controlar el acceso a diferentes partes de la base de datos.
      - **Uso de SSH o VPN**: Para cifrar las conexiones y proteger los datos en tránsito.
    
    - **Orquestador:**
      - **Apache Airflow**: Para gestionar y orquestar los flujos de trabajo de ETL y entrenamiento de modelos.
    
    ### **Justificación:**
    Garantizar la seguridad es crucial cuando se permite el acceso remoto a la base de datos. Configurar MySQL correctamente y utilizar métodos de cifrado como SSH o VPN protege los datos y asegura que solo usuarios autorizados puedan acceder al sistema. Apache Airflow facilita la automatización y programación de tareas complejas en el flujo de trabajo.
    
    ---
    ## **Resumen del Stack Tecnológico**
    
    | **Fase**                                  | **Herramientas y Tecnologías**                                                                                           |
    |-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
    | **1. Ingesta de Datos y ETL**             | Python, Pandas, PyArrow, MinIO                                                                                           |
    | **2. Ingreso en la Base de Datos**        | MySQL, phpMyAdmin, SQLAlchemy                                                                                              |
    | **3. Entrenamiento de Machine Learning**  | Scikit-learn, Pickle, Jupyter Notebook                                                   |
    | **4. Creación de Dashboards e Informes**  | Matplotlib, Seaborn, Plotly, Jupyter Notebook, Streamlit/Dash                            |
    | **5. Orquestador**                       | Apache Airflow                                                                                                            |
    | **Infraestructura y Seguridad**           | Servidor Local, Configuración de MySQL para Acceso Remoto, SSH/VPN                                                        |
    
    ---
    ### **Ejemplo de Diagrama:**
    
    1. **Ingesta de Datos y ETL**
       - MinIO → Python → Pandas/PyArrow → Transformaciones → Python
    
    2. **Ingreso en la Base de Datos**
       - Python/SQLAlchemy → MySQL → phpMyAdmin
    
    3. **Entrenamiento de ML**
       - MySQL → Python/Scikit-learn → Modelo Entrenado → MySQL
    
    4. **Creación de Dashboards e Informes**
       - MySQL → Python/Matplotlib/Seaborn → Jupyter Notebook/Streamlit → Dashboards/Informes
    
    5. **Orquestación**
       - Apache Airflow → Ingesta de Datos y ETL → Entrenamiento de ML → Creación de Dashboards e Informes
    """)
    
    st.divider()
    
    # Información del equipo
    st.header("Desarrollado por ⚙️", divider='rainbow')
    
    personas = [
        {
            "nombre": "Cristian Moreira",
            "profesion": "Project Manager",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/cristian.jpeg"
        },
        {
            "nombre": "Andres Aguirre",
            "profesion": "Technical Project Manager & Data Analytics",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/andres.jpeg"
        },
        {
            "nombre": "Jeison Zapata",
            "profesion": "Data Scientist & Data Analyst",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/jeison.jpeg"
        },
        {
            "nombre": "Libardo Alarcon",
            "profesion": "Data Scientist",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/libardo.jpeg"
        },
        {
            "nombre": "Manuel Carruitero",
            "profesion": "Data Engineer",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/manuel.jpeg"
        },
        {
            "nombre": "Lucas Carranza",
            "profesion": "Data Engineer",
            "github": "https://github.com/",
            "linkedin": "https://www.linkedin.com/",
            "imagen_link": "./07-streamlit/images/lucas.jpeg"
        }
    ]
    
    # Mejora en la disposición del equipo
    columns = st.columns(len(personas))
    for idx, persona in enumerate(personas):
        with columns[idx]:
            # Nombre y profesión centrados
            st.markdown(f'<h2 style="text-align: center; margin-bottom: 0px;">{persona["nombre"]}</h2>', unsafe_allow_html=True)
            st.markdown(f'<h4 style="text-align: center; color: gray;">{persona["profesion"]}</h4>', unsafe_allow_html=True)
            
            # Imagen del equipo
            persona_image = get_image_b64(persona["imagen_link"])
            if persona_image:
                st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{persona_image}" style="border-radius: 50%;" width="150"/></div>', unsafe_allow_html=True)
    
            # Logos de redes sociales
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

elif st.session_state.page == "Dashboard":
    st.title("Página Dashboard")
    st.write("Contenido del Dashboard.")
elif st.session_state.page == "Modelos":
    st.title("Página Modelos")
    st.write("Contenido de los Modelos.")
