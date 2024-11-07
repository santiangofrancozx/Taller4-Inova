import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar y depurar los datos
@st.cache_data
def load_data():
    data = pd.read_excel("datos2023.xlsx")
    data = data[data['AÑO'].isin([2020, 2021, 2022])]
    data['ADMITIDOS'] = pd.to_numeric(data['ADMITIDOS'], errors='coerce')
    data = data.dropna(subset=['ADMITIDOS'])
    data['SEXO'] = data['SEXO'].str.strip()
    data['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'] = data['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'].str.strip()
    return data

# Cargar los datos completos
data = load_data()

# Sidebar para filtros
st.sidebar.title("Filtros y Opciones")
year_filter = st.sidebar.multiselect("Selecciona los años", options=[2020, 2021, 2022], default=[2020, 2021, 2022])
institution_filter = st.sidebar.selectbox("Selecciona la Institución", options=data['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'].unique())

# Filtrar datos
data_filtrada = data[(data['AÑO'].isin(year_filter)) & (data['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'] == institution_filter)]

# Título y descripción
st.title("Dashboard de Educación en Colombia")
st.write("Este dashboard muestra datos educativos de los años 2020 a 2022.")

# Sección para Datos Filtrados
st.markdown("## Datos Filtrados (Por Filtros Seleccionados)")

# Mostrar tabla de datos filtrados
st.write(data_filtrada)

# Gráficos y métricas - Datos filtrados
st.markdown("### Total de Admitidos por Año (Filtrados)")
admitidos_por_ano = data_filtrada.groupby("AÑO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_ano)

st.markdown("### Total de Admitidos por Sexo (Filtrados)")
admitidos_por_sexo = data_filtrada.groupby("SEXO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_sexo)

st.markdown("### Total de Admitidos por Programa Académico (Filtrados)")
admitidos_por_programa = data_filtrada.groupby("PROGRAMA ACADÉMICO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_programa)

campo1_default = data_filtrada.columns[0]  # Primer campo por defecto
campo2_default = data_filtrada.columns[1]  # Segundo campo por defecto
campo3_default = data_filtrada.columns[2]  # Tercer campo por defecto

campo1 = st.selectbox("Selecciona el primer campo (Filtrado)", data_filtrada.columns, index=data_filtrada.columns.get_loc(campo1_default))
campo2 = st.selectbox("Selecciona el segundo campo (Filtrado)", data_filtrada.columns, index=data_filtrada.columns.get_loc(campo2_default))
campo3 = st.selectbox("Selecciona el tercer campo (Filtrado)", data_filtrada.columns, index=data_filtrada.columns.get_loc(campo3_default))

# Agrupar los datos por los tres campos seleccionados
consulta_filtrada = data_filtrada.groupby([campo1, campo2, campo3]).size().reset_index(name="Total")
st.markdown(f"### Consulta Filtrada: {campo1} - {campo2} - {campo3}")
st.write(consulta_filtrada)

# Gráfico de barras apiladas (filtrado)
st.markdown(f"### Distribución de {campo1}, {campo2} y {campo3} (Filtrado)")
pivot_data = consulta_filtrada.pivot_table(index=campo1, columns=campo2, values="Total", aggfunc="sum")
st.bar_chart(pivot_data)

# Separador para los datos generales
st.markdown("---")  # Línea divisoria

# Sección para Datos Generales
st.markdown("## Datos Generales (Sin Filtros)")

# Gráficos y métricas basados en los datos completos (sin filtros)
st.markdown("### Total de Admitidos por Año (Datos Generales)")
admitidos_por_ano_general = data.groupby("AÑO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_ano_general)

st.markdown("### Total de Admitidos por Sexo (Datos Generales)")
admitidos_por_sexo_general = data.groupby("SEXO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_sexo_general)

st.markdown("### Total de Admitidos por Programa Académico (Datos Generales)")
admitidos_por_programa_general = data.groupby("PROGRAMA ACADÉMICO")["ADMITIDOS"].sum()
st.bar_chart(admitidos_por_programa_general)

# Gráfico de barras apiladas (datos generales)
campo1_general_default = data.columns[0]  # Primer campo por defecto
campo2_general_default = data.columns[1]  # Segundo campo por defecto
campo3_general_default = data.columns[2]  # Tercer campo por defecto

campo1_general = st.selectbox("Selecciona el primer campo (General)", data.columns, index=data.columns.get_loc(campo1_general_default))
campo2_general = st.selectbox("Selecciona el segundo campo (General)", data.columns, index=data.columns.get_loc(campo2_general_default))
campo3_general = st.selectbox("Selecciona el tercer campo (General)", data.columns, index=data.columns.get_loc(campo3_general_default))

# Agrupar los datos por los tres campos seleccionados (sin filtro)
consulta_filtrada_general = data.groupby([campo1_general, campo2_general, campo3_general]).size().reset_index(name="Total")
st.markdown(f"### Consulta General: {campo1_general} - {campo2_general} - {campo3_general}")
st.write(consulta_filtrada_general)

# Gráfico de barras apiladas (con datos generales)
st.markdown(f"### Distribución de {campo1_general}, {campo2_general} y {campo3_general} (General)")
pivot_data_general = consulta_filtrada_general.pivot_table(index=campo1_general, columns=campo2_general, values="Total", aggfunc="sum")
st.bar_chart(pivot_data_general)

# Agregar más métricas clave utilizando los datos completos (sin filtros)
año_max_admitidos_general = admitidos_por_ano_general.idxmax()  # Año con más admitidos
max_admitidos_año_general = admitidos_por_ano_general.max()  # Total de admitidos en el año con más admitidos
programa_max_admitidos_general = admitidos_por_programa_general.idxmax()  # Programa con más admitidos
max_admitidos_programa_general = admitidos_por_programa_general.max()  # Total de admitidos en el programa con más admitidos
sexo_max_admitidos_general = admitidos_por_sexo_general.idxmax()  # Sexo con más admitidos
max_admitidos_sexo_general = admitidos_por_sexo_general.max()  # Total de admitidos en el sexo con más admitidos

# Usar los datos generales para calcular el total de instituciones y promedio de admitidos por institución
total_instituciones_general = data['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'].nunique()  # Total de instituciones en todos los datos
promedio_admitidos_institucion_general = data.groupby('INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)')['ADMITIDOS'].mean().mean()  # Promedio de admitidos por institución, en todos los datos

# Mostrar las métricas clave (con datos generales)
st.metric("Año con más Admitidos (General)", año_max_admitidos_general)
st.metric("Máximo de Admitidos en un Año (General)", max_admitidos_año_general)
st.metric("Programa con más Admitidos (General)", programa_max_admitidos_general)
st.metric("Máximo de Admitidos en un Programa (General)", max_admitidos_programa_general)
st.metric("Sexo con más Admitidos (General)", sexo_max_admitidos_general)
st.metric("Máximo de Admitidos en un Sexo (General)", max_admitidos_sexo_general)
st.metric("Total de Instituciones (General)", total_instituciones_general)
st.metric("Promedio de Admitidos por Institución (General)", promedio_admitidos_institucion_general)
