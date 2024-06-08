cadena = "Hola como estan" 

def reemplazar_caracteres(cadena: str, caracter: str, reemplazo: str)->str:

    cadena_modificada = ""
    for i in range(len(cadena)):
        if cadena[i] != caracter:
            cadena_modificada += cadena[i]
        else:
            cadena_modificada += reemplazo
    
    return cadena_modificada

print(reemplazar_caracteres(cadena, "o", "*"))


# Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el 
# que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.


def retornar_indice(cadena: str, caracter: str)->int:

    indice = -1
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            indice = i
            break
        
    return indice


print(retornar_indice(cadena, "o"))


# Crear una función que reciba una cadena y retorne la misma pero al reverso.
# Ej: Si recibe la cadena “hola”, deberá retornar “aloh”.


def cadena_reverso(cadena: str)->str:

    cadena_reverso = ""
    for i in range(len(cadena) -1, -1, -1):
        cadena_reverso += cadena[i]
    
    return cadena_reverso

print(cadena_reverso(cadena))