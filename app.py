import streamlit as st


# ----------------------------------------
# CLASE (POO)
# ----------------------------------------

class Cliente:
    def __init__(self, nombre, edad, saldo):
        self.__nombre = nombre
        self.__edad = edad
        self.__saldo = saldo

    #GETTERS (encapsulamiento)
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad

    def get_saldo(self):
        return self.__saldo
  

    # Método
    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Saldo: S/ {self-__saldo}"

# ----------------------------------------
# STREAMLIT
# ----------------------------------------

st.title("Demo POO - Ciencia de Datos")

st.write("Ingrese los datos del cliente:")