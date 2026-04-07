import streamlit as st
from services.cliente_service import crear_cliente


def procesar_cliente(nombre, edad, saldo):

    try:
        if nombre == "":
            st.warning("Ingrese un nombre válido")
        elif saldo < 0:
            st.warning("El saldo no puede ser negativo")
        else:
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
        
    except ValueError as e:
        st.warning(str(e))

    except Exception:
        st.error(str(e))