from Package_Input.input import get_init

######################################################################################################

def sumar_naturales(numero:int) -> int:

    if numero == 1:
        return 1
    elif numero == None:
        print("Error, numero no valido")
        return None
    
    return numero + sumar_naturales(numero - 1)

numero = get_init("Ingrese un numero: ", "ERROR, el numero no esta en el rango", 0, 10, 2)
resultado = sumar_naturales(numero)
print(resultado)

######################################################################################################

def calcular_potencia(base:int, exponente:int) -> int:

    if exponente == 0:
        return 1
    
    return base * calcular_potencia(base, exponente - 1)

numero = get_init("Ingrese la base de un numero: ", "ERROR, el numero no esta en el rango", 0, 10, 2)
exponente = get_init("Ingrese el exponente del numero: ", "ERROR, el numero no esta en el rango", 0, 10, 2)
resultado = calcular_potencia(numero, exponente)
print(resultado)

#####################################################################################################

def sumar_digitos(numero:int) -> int:

    if numero == 0:
        return 0
    else:
        suma = numero % 10 + sumar_digitos(numero // 10)
        return suma

numero = get_init("Ingrese un numero: ", "ERROR", 0, 200, 2)
sumas = sumar_digitos(numero)
print(f"La suma de los digitos da: {sumas}")