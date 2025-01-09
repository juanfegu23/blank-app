import streamlit as st
import pandas as pd
import plotly.express as px

# Subir el archivo CSV
st.title("Dashboard Interactivo con IA")
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    # Leer los datos
    data = pd.read_csv(uploaded_file)
    st.write("Vista previa de los datos:", data.head())
    
    # Mostrar métricas clave
    st.subheader("Métricas clave")
    st.write(f"Total de filas: {len(data)}")
    st.write(f"Columnas: {', '.join(data.columns)}")
    
    # Visualización interactiva
    st.subheader("Gráfico interactivo")
    column_to_plot = st.selectbox("Selecciona una columna para graficar", data.columns)
    fig = px.histogram(data, x=column_to_plot)
    st.plotly_chart(fig)
