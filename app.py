import streamlit as st 
import pandas as pd 
import lasio 
st.title('Aplicacion para Registros')
st.sidebar.title('Menu')
archivo_las= lasio.read('LGAE-040.las')
df= archivo_las.df()
opciones_inicio= st.sidebar.radio('Seleccione una Opcion',['Inicio', 'Datos', 'Calculos'])
if opciones_inicio == 'Inicio':
	st.write('Ingreso al inicio')
	st.write(df)
	st.write('Esto es un DataFrame')
if opciones_inicio == 'Datos':
	st.write('Ingreso a datos')
	barra_deslizadora= st.slider('Seleccione un valor',1,100,30)
	st.write('Ud selecciono:',barra_deslizadora)
if opciones_inicio == 'Calculos':
	st.write('Ingreso al calculos')
	seleccion= st.selectbox('Seleccione un valor',[2, 4, 6, 'Opcion A'])
	ingreso_numero= st.number_input('Ingrese un valor',min_value=0.00, max_value=1000.00, value=100.00)
archivo_subido=st.sidebar.file_uploader('Cargue archivo .las',type=['.las','.LAS'])
check1= st.checkbox('Activar')
if check1 == True:
	st.write('Check activado')
