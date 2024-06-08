
####################################
# EJERCICIO A
print("_"*30)
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

cuadrados = list(map(lambda x : x ** 2, lista_numeros))

print(cuadrados)
####################################
####################################
# EJERCICIO B
print("_"*30)
pares = list(filter(lambda x: x % 2 == 0, lista_numeros))

print(pares)
####################################
####################################
# EJERCICIO C
print("_"*30)
palabras = ['hola', 'mundo', 'python', 'lambda']

lista_palabras = list(map(lambda palabra: palabra.upper(), palabras))

print(lista_palabras)
####################################
####################################
# EJERCICIO D
print("_"*30)
palabras2 = ['¡hola!', 'mundo?', 'python', 'lambda', 'pedro73']

lista_palabras2 = list(filter(lambda palabra : palabra.isalpha(), palabras2))

print(lista_palabras2)
####################################
# Profe esto es algo EXTRA porque dijo q no le gustaba el formato del print de los dict
def print_lindo(lista: list[dict])->None:
    print("_"*30)
    print("- LISTA MAYORES -")
    for persona in lista:
        print(f"Nombre: {persona['nombre']} | Edad: {persona['edad']}")
def print_lindo_nombre(lista: list)->None:
    print("- LISTA NOMBRES -")
    for nombre in lista:
        print(f"Nombre: {nombre}")
    print("_"*30)
####################################
# EJERCICIO E
personas = [
    {'nombre': 'Juan', 'edad': 15},
    {'nombre': 'Ana', 'edad': 22},
    {'nombre': 'Pedro', 'edad': 19},
    {'nombre': 'María', 'edad': 17},
    {'nombre': 'Laura', 'edad': 20}
]

lista_mayores = list(filter(lambda personas : personas["edad"] >= 18, personas))
print_lindo(lista_mayores)

print("_"*30)
lista_nombres = list(map(lambda personas : personas["nombre"].upper(), personas))
print_lindo_nombre(lista_nombres)

####################################