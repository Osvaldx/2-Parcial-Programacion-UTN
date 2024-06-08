# Funciones Parte I

# Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# Crear una función que le solicite al usuario el ingreso de una cadena y la retorna. 
# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables (que reciban el mensaje de pedido de datos por parámetro). Agregar validaciones.
# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# Recordar realizar la documentación necesaria para cada una de ellas.

# Alumno: Nahuel Osvaldo Romano

# PUNTO 1
def numero_entero()->int:
    """Le solicita al usuario ingresar un numero entero y lo devuelve"""
    numero_base = input("Ingrese un número entero: ")
    numero_base = int(numero_base)

    return numero_base

numero_solicitado_uno = numero_entero()
print(numero_solicitado_uno)

# PUNTO 2
def numero_flotante()->float:
    """Le solicta al usuario ingresar un número flotante y lo devuelve"""
    numero_base = input("Ingrese un número flotante: ")
    numero_base = float(numero_base)

    return numero_base

numero_solicitado_dos = numero_flotante()
print(numero_solicitado_dos)

# PUNTO 3
def cadena()->str:
    """Le solicta al usuario ingresar una cadena de caracteres o numeros"""
    cadena_ingresada = input("Ingrese una palabra o número: ")
    cadena_ingresada = str(cadena_ingresada)

    return cadena_ingresada

numero_solicitado_tres = cadena()
print(numero_solicitado_tres)

# PUNTO 4
def numero_entero_dos(mensaje:str,rango_uno:int,rango_dos:int)->int:
    """Le solicta al usuario ingresar su edad y verifica que este en el rango permitido"""
    numero_base = input(mensaje)
    numero_base = int(numero_base)

    while numero_base <= rango_uno or numero_base > rango_dos:
        numero_base = input(mensaje)
        numero_base = int(numero_base)

    return numero_base

mensaje = "Ingrese su edad: "
edad = numero_entero_dos(mensaje, 1, 100)

print(edad)

def numero_flotante_dos(mensaje:str,rango_uno:float,rango_dos:float):
    """Le solicta al usuario ingresar su altura y verifca que este en el rango permitido"""
    numero_base = input(mensaje)
    numero_base = float(numero_base)

    while numero_base < rango_uno or numero_base > rango_dos:
        numero_base = input(mensaje)
        numero_base = float(numero_base)

    return numero_base

mensaje = "Ingrese su altura: "
altura = numero_flotante_dos(mensaje, 0.70, 2.50)

print(altura)

def cadena_dos(mensaje:str):
    """Le solicita al usuario ingresar su nombre y verifica que este este compuesto unicamente de caracteres alfabeticos"""
    nombre_ingresado = input(mensaje)

    while not nombre_ingresado.isalpha():
        nombre_ingresado = input(mensaje)

    return nombre_ingresado

mensaje = "Ingrese su nombre: "
nombre = cadena_dos(mensaje)

print(nombre)

# PUNTO 5

def calculo_area_circulo(radio:float) -> float:
    pi = 3.14
    area_circulo = pi * (radio ** 2)

    return area_circulo

area_circulo = calculo_area_circulo(3)
print(area_circulo)


# PUNTO 6

def numero_par_impar(numero_ingresado:int) -> None:
    calculo = numero_ingresado % 2

    if calculo == 1:
        mensaje = "El numero es impar"
    else:
        mensaje = "El numero es par"

    print(mensaje)

# PUNTO 7

def maximo_numeros(mensaje:str):
    """Le solicta al usuario ingresar 3 numeros y le devuelve el numero mayor"""
    numero_mayor = None
    primer_numero_ingresado = input(mensaje)
    primer_numero_ingresado = int(primer_numero_ingresado)

    segundo_numero_ingresado = input(mensaje)
    segundo_numero_ingresado = int(segundo_numero_ingresado)

    tercer_numero_ingresado = input(mensaje)
    tercer_numero_ingresado = int(tercer_numero_ingresado)

    if primer_numero_ingresado > segundo_numero_ingresado and primer_numero_ingresado > tercer_numero_ingresado:
        numero_mayor = primer_numero_ingresado
        resultado = f"El número mayor es: {numero_mayor}"
    elif segundo_numero_ingresado > tercer_numero_ingresado:
        numero_mayor = segundo_numero_ingresado
        resultado = f"El número mayor es: {numero_mayor}"
    else:
        numero_mayor = tercer_numero_ingresado
        resultado = f"El número mayor es: {numero_mayor}"

    return resultado

mensaje = "Ingrese un numero: "
numero_maximo = maximo_numeros(mensaje)

print(numero_maximo)

# PUNTO 8

def calcular_potencia(mensaje:str,mensaje_dos:str):
    """Le solicta al usuario un numero base y un numero potenciado, este le devuelve el resultado"""
    numero_base = input(mensaje)
    numero_base = int(numero_base)

    numero_exponente = input(mensaje_dos)
    numero_exponente = int(numero_exponente)

    calculo = numero_base ** numero_exponente
    mensaje_final = f"{numero_base} elevado a {numero_exponente} es: {calculo}"

    return mensaje_final

mensaje = "Ingrese el número base: "
mensaje_dos = "Ingrese el número exponente: "
numero_potenciado_resultado = calcular_potencia(mensaje,mensaje_dos)

print(numero_potenciado_resultado)
    

