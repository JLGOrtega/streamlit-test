import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(
    page_title="Tu Prima",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",

)

option = st.sidebar.selectbox(label="Selecciona Pagina: ", options=["Home", "Charts", "Cousin"], index=0)
st.write(f"Has elegido {option}")

df = pd.read_csv("streamlit/data/red_recarga_acceso_publico_2021.csv", sep=";")
uploaded_files = st.sidebar.file_uploader("Choose a CSV file", 
                                accept_multiple_files=False,
                                type=["csv"])
if uploaded_files:
    df = pd.read_csv(uploaded_files, sep=";")
    st.balloons()


if option == "Home":

    image = Image.open('streamlit/baby-7463137_1280.jpg')


    st.title("My First Streamlit APP")
    st.image(image, caption='Sunrise by the mountains', width=200)




    with st.expander("Click for details:"):
        st.write("Esto es una aplicacion web construida en Streamlit que muestra puntos de carga en Madrid")

    

elif option=="Charts":

    filtro_operador = st.sidebar.selectbox(label="Selecciona Operador: ", options=df.OPERADOR.unique(), index=0)
    df_to_show = df[df.OPERADOR == filtro_operador].copy()

    with st.echo():
        # Que guapa es tu primaOPERADOR
        st.dataframe(df_to_show)

elif option=="Cousin":
    st.write("Tu prima is in proces...")

