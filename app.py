import streamlit as st
import pandas as pd
from models.cliente import Cliente
from services.cliente_service import crear_cliente


st.title("Demo POO - Ciencia de Datos")
st.write("Ingrese los datos del cliente:")

# Inputs
nombre = st.text_input("Nombre")
edad = st.number_input("Edad", min_value = 0)
saldo = st.number_input("Saldo", min_value = 0.0)

# Botón
if st.button("Crear Cliente"):

    try:
        # Crea Cliente + Mensaje
        cliente, mensaje = crear_cliente(nombre, edad, saldo)

        st.success("Cliente creado correctamente")
        st.info(mensaje)

        #Guardar en Memoria
        st.session_state.clientes.append({
            "Nombre": cliente.get_nombre(),
            "Edad": cliente.get_edad(),
            "Saldo": cliente.get_saldo()
        })
    
    except Exception as e:
        st.error(str(e))

#Mostrar tabla acomulada
if len(st.session_state.clientes) > 0:

    st.write("### Tabla de Clientes")
    df = pd.DataFrame(st.session_state.clientes)
    st.dataframe(df)

    # FOR -> recorrer clientes
    st.write("### Lista de clientes (for)")
    for c in st.session_state.clientes:
        st.write(f"{c['Nombre']} - S/ {c['Saldo']}")


    # WHILE -> recorrido alternativo
    st.write("### Recorrido con While")
    i = 0
    while i < len(st.session_state.clientes):
        c = st.session_state.clientes[i]
        st.write(f"{c['Nombre'] - Edad: {c['Edad']}}")
        i += 1
    
    # Análisis: Total de clientes
    contador = 0
    for c in st.session_state.clientes:
        contador += 1
    
    st.write(f"Total de Clientes: {contador}")

    # Promedio de saldo
    suma = 0
    for c in st.session_state.clientes:
        suma += C["Saldo"]
    
    promedio = suma / contador
    st.write(f"Promedio de saldo: S/ {round(promedio, 2)}")

else:
    st.warning("Aún no hay clientes registrados")