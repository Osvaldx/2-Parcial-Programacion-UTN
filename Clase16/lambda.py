# FUNCIONES LAMBDA
# Objetos de primera clase:
# 1) devolver
# 2) recibir como parametros
# 3) asignar a variables

def sumar(a, b):
    return a + b
def resta(a, b):
    return a - b
def multi(a, b):
    return a * b
def division(a, b):
    return a / b

def calcular(a, b, operacion):
    return operacion(a, b)

resultado = calcular(5, 6, multi)
print(resultado)

#######################################################

suma = lambda x, y : x + y

resultado = suma(5,7)
print(resultado)

print(calcular(5,7, lambda x, y : x + y))
######################################################

lista_numeros = [1,6,1,3,6,7,2,3,8,4]

lista = list(map(lambda numero : numero * 2, lista_numeros))

print(lista)