from models.cliente import Cliente

def crear_cliente(nombre, edad, saldo):
    if edad < 18:
        raise ValueError ("El cliente debe ser mayor de edad")
    
    return CLiente(nombre, edad, saldo)
