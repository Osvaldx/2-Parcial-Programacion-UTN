# Alumno: Nahuel Osvaldo Romano

# 1) Crear una función que reciba por parámetro una cadena y un caracter.
# La función deberá contar cuántas veces aparece dicho caracter en la cadena y retornar ese valor.

cadena = "Hola como estan"

def contador_caracter(cadena: str, caracter: str)-> int:
    """Esta funcion recibe como parametros un cadena y un caracter para contar cuantas veces aparece dicho caracter en la cadena

    Argumentos:
        cadena (str): Una cadena ya predefinida
        caracter (str): Un caracter que se le pide al usuario

    Retorna:
        int: Retorna un numero entero
    """
    contador = 0
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            contador += 1
    
    return contador

print(contador_caracter(cadena, "o"))

# 2) Crear una función que reciba una cadena y un caracter. 
# La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, 
# o -1 en caso de que no esté.

def indice_caracter(cadena: str, caracter: str)->int:
    """Esta funcion recibe como parametros una cadena y un caracter, la funcion busca el índice en el que se encuentre la primera incidencia de dicho caracter

    Argumentos:
        cadena (str): Una cadena ya predefinida
        caracter (str): Un caracter que se le pide al usuario

    Retorna:
        int: Retorna un numero entero
    """

    indice = -1
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i
            break
    
    return indice

print(indice_caracter(cadena, "o"))

# 3) Crear una función que reciba una cadena y retorne la misma pero al reverso.
# Ej: Si recibe la cadena “hola”, deberá retornar “aloh”.

def cadena_reverso(cadena: str)->str:
    """Esta funcion recibe como parametros una cadena y retorne la misma pero al reverso

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        str: Retorna una string de la cadena
    """

    cadena_reverso = ""
    for i in range(len(cadena) -1, -1, -1):
        cadena_reverso += cadena[i]

    return cadena_reverso

print(cadena_reverso(cadena))

# 4) Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
#	Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

cadena_dos = "Hooola"

def caracter_repetidos(cadena: str)->str:
    """Esta funcion recibe como parámetro una cadena y suprima los caracteres repetidos

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        str: Retorna una string de la cadena
    """
    sin_repeticiones = ""

    for i in range(len(cadena) - 1):
        if cadena[i] != cadena[i + 1]:
            sin_repeticiones += cadena[i]

    sin_repeticiones += cadena[i+1]
    
    return sin_repeticiones

print(caracter_repetidos(cadena_dos))

# 5) Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def suprimir_vocales(cadena: str)->str:
    """Esta funcion recibe como parametros una cadena y suprima las vocales de la misma.

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        str: Retorna una string de la cadena
    """
    vocales = ["a", "e", "i", "o", "u"]
    cadena_sin_vocales = ""

    for i in range(len(cadena)):
        es_vocal = False
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                es_vocal = True
        
        if es_vocal == False:
            cadena_sin_vocales += cadena[i]
    
    return cadena_sin_vocales

print(suprimir_vocales(cadena))

# 6) Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

def subcadena_encontrar(cadena: str, subcadena: str)->int:
    """Esta funcion recibe como parametros una cadena y una subcadena y cuenta cuantas veces aparece la subcadena en la cadena

    Retorna:
        cadena (str): Una cadena ya predefinida
        subcadena (str): Una subcadena ya predefinida

    Returns:
        int: Retorna un numero entero
    """
    contador = 0

    for i in range(len(cadena)):
        if cadena[i:i + len(subcadena)] == subcadena:
            contador += 1

    return contador

cadena = "El pan del panadero"
subcadena = "pan"
print(subcadena_encontrar(cadena, subcadena))