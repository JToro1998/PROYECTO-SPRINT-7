import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

car_data = load_data()

# ENCABEZADO PRINCIPAL
st.title('🚗 Análisis de Datos de Vehículos')
st.header('Exploración interactiva del mercado de automóviles usados')

# Mostrar información básica de los datos
st.subheader('📊 Información del Dataset')
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de vehículos", len(car_data))
with col2:
    st.metric("Precio promedio", f"${car_data['price'].mean():,.0f}")
with col3:
    st.metric("Año promedio", f"{car_data['model_year'].mean():.0f}")

# SECCIÓN DE HISTOGRAMAS
st.header('📈 Distribución de Precios')

# Casilla de verificación para filtrar datos
show_expensive = st.checkbox('Mostrar solo vehículos caros (>$50,000)')

# Filtrar datos según la casilla
if show_expensive:
    filtered_data = car_data[car_data['price'] > 50000]
    st.write(f"Mostrando {len(filtered_data)} vehículos caros")
else:
    filtered_data = car_data
    st.write(f"Mostrando todos los {len(filtered_data)} vehículos")

# Histograma de precios
fig_hist = px.histogram(
    filtered_data, 
    x='price', 
    nbins=50,
    title='Distribución de Precios de Vehículos',
    labels={'price': 'Precio ($)', 'count': 'Cantidad de vehículos'},
    color_discrete_sequence=['#1f77b4']
)
fig_hist.update_layout(
    xaxis_title="Precio ($)",
    yaxis_title="Cantidad de vehículos",
    showlegend=False
)
st.plotly_chart(fig_hist, use_container_width=True)

# SECCIÓN DE GRÁFICO DE DISPERSIÓN
st.header('🔍 Relación entre Odómetro y Precio')

# Botón para mostrar/ocultar gráfico de dispersión
if st.button('Crear gráfico de dispersión'):
    # Gráfico de dispersión
    fig_scatter = px.scatter(
        car_data, 
        x='odometer', 
        y='price',
        color='condition',
        title='Relación entre Kilometraje y Precio',
        labels={
            'odometer': 'Kilometraje (millas)', 
            'price': 'Precio ($)',
            'condition': 'Condición'
        },
        hover_data=['model_year', 'fuel']
    )
    fig_scatter.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Precio ($",
    )
    st.plotly_chart(fig_scatter, use_container_width=True)