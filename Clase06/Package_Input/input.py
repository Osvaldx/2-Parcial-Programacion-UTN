from .validate import *

######################################################################################################

def get_init(mensaje:str,mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    """esta funcion se encarga de permitir el ingreso de un numero entero al usuario para despues con otra funcion validarlo

    Args:
        mensaje (str): el mensaje que se usara para indicarle al usuario que dato ingresar
        mensaje_error (str): el mensaje de error que saldra
        minimo (int): el numero minimo del rango permitido
        maximo (int): el numero maximo del rango permitido
        reintentos (int): la cantidad de reintentos que tiene el usuario

    Returns:
        int | None: se espera una respuesta de un numero entero o none
    """
    contador = 0

    numero = input(mensaje)
    numero = int(numero)
    
    if validate_number(numero, minimo, maximo):
        return numero
    
    while numero < minimo or numero > maximo:
        print(mensaje_error)
        if contador == reintentos:
            print("Alcanzo el maximo de intentos..")
            return None
        
        numero = input("Ingrese nuevamente el numero: ")
        numero = int(numero)

        contador += 1

    return numero

######################################################################################################

def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int) -> float | None:
    """esta funcion se encarga de permitir el ingreso de un numero flotante al usuario para despues con otra funcion validarlo

    Args:
        mensaje (str): el mensaje que se usara para indicarle al usuario que dato ingresar
        mensaje_error (str): el mensaje de error que saldra
        minimo (int): el numero minimo del rango permitido
        maximo (int): el numero maximo del rango permitido
        reintentos (int): la cantidad de reintentos que tiene el usuario

    Returns:
        float | None: se espera una respuesta de un numero flotante o none
    """
    altura = input(mensaje)
    altura = float(altura)

    for i in range(reintentos):
        if altura < minimo or altura > maximo:
            print(mensaje_error)
            altura = input("Ingrese nuevamente su altura: ")
            altura = float(altura)
    
    if validate_number(altura, minimo, maximo):
        return altura
    
    print("Alcanzaste el limite de intentos...")

######################################################################################################

def get_string(mensaje:str, mensaje_error:str, longitud:int, reintentos:int) -> str | None:
    """esta funcion permite al usuario poder ingresar una string o mejor dicho una palabra

    Args:
        mensaje (str): el mensaje con el que se le indicara al usuario que ingresar
        mensaje_error (str): el mensaje de error que saldra
        longitud (int): la longitud permitida que se establecio para la palabra
        reintentos (int): la cantidad de reintentos para el usuario

    Returns:
        str | None: se espera un respuesta en formato string o none
    """

    palabra = input(mensaje)

    for i in range(reintentos):
        if validate_length(palabra, longitud):
            print(mensaje_error)
            palabra = input("Ingrese nuevamente la palabra: ")
    
    print("Esta palabra no supera las 7 letras :)")

######################################################################################################