
# Botón para histograma

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Exploración de Datos de Vehículos Usados")

# 1. Histograma del odómetro
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma del kilometraje (odómetro)')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# 2. Gráfico de dispersión odómetro vs precio
if st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)'):
    st.write('Gráfico de dispersión: Precio vs Odómetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

# 3. Boxplot por tipo de vehículo
if st.checkbox('Mostrar boxplot por tipo de vehículo'):
    st.write('Distribución de precios por tipo de vehículo')
    fig = px.box(car_data, x='type', y='price', title='Distribución de precios por tipo de vehículo')
    st.plotly_chart(fig, use_container_width=True)

# 4. Gráfico de violín por condición del vehículo
if st.checkbox('Mostrar gráfico de violín por condición del vehículo'):
    st.write('Precio por estado del vehículo')
    fig = px.violin(car_data, x='condition', y='price', box=True, points='all',
                    title='Precio por estado del vehículo (con puntos individuales)')
    st.plotly_chart(fig, use_container_width=True)

# 5. Dispersión precio vs año modelo, coloreado por tipo
if st.checkbox('Mostrar dispersión precio vs año del modelo y tipo'):
    st.write('Precio por año del modelo y tipo de vehículo')
    fig = px.scatter(car_data, x="model_year", y="price", color="type",
                     title="Precio de vehículos por año y tipo")
    st.plotly_chart(fig, use_container_width=True)

# 6. Mapa de calor de correlaciones
if st.checkbox('Mostrar mapa de calor de correlaciones'):
    st.write('Matriz de correlación entre variables numéricas')
    
    numeric_df = car_data.select_dtypes(include='number')
    corr_matrix = numeric_df.corr()

    fig = ff.create_annotated_heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns.tolist(),
        y=corr_matrix.index.tolist(),
        annotation_text=corr_matrix.round(2).values,
        colorscale='Viridis',
        showscale=True
    )

    fig.update_layout(
        title='Matriz de correlación entre variables numéricas',
        xaxis_title='Variables',
        yaxis_title='Variables',
        autosize=True
    )

    st.plotly_chart(fig, use_container_width=True)
