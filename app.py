import streamlit as st
from models.cliente import Cliente
from services.cliente_service import crear_cliente


st.title("Demo POO - Ciencia de Datos")
st.write("Ingrese los datos del cliente:")

nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value = 0)
saldo = st.number_input("Saldo", min_value = 0.0)

if st.button("Crear Cliente"):

    try:
        #Secuencia
        cliente = crear_cliente(nombre, edad, saldo)

        st.success("Cliente creado correctamente")

        st.write("### Información del cliente: ")
        st.write(cliente.mostrar_info())
    
    except Exception as e:
        st.error(str(e))