# Alumno: Nahuel Osvaldo Romano
# 
# 1) Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números

####################################################################

lista = [5, 12, 42, -9, 23, 42, -21]


def promedio_numeros(lista: list)-> int | float:
    """Esta funcion recibe como parametros una lista de numeros enteros para despues calcular el promedio de los numeros

    Argumentos:
        lista (list): una lista ya predefinida

    Retorno:
        int | float: el retorno puede ser un numero entero como flotante
    """
    acumulador = 0

    for i in range(len(lista)):
        acumulador += lista[i]
    promedio = acumulador / len(lista)

    return promedio

resultado_promedio = promedio_numeros(lista)
mensaje = f"El promedio de la lista es: {resultado_promedio}"
print(mensaje)

# ####################################################################

# # 2) Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

# ####################################################################

def promedio_numero_positivos(lista: list)-> int | float:
    """Esta funcion recibe como parametros una lista de numeros y calcula el promedio de solo los numeros positivos

    Argumentos:
        lista (list): una lista ya predefinida

    Retorno:
        int | float: el retorno puede ser un numero entero como flotante
    """
    acumulador = 0
    cantidad_positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            acumulador += lista[i]
            cantidad_positivos += 1
    promedio = acumulador / cantidad_positivos

    return promedio

resultado_promedio = promedio_numero_positivos(lista)
mensaje = f"El promedio de los numeros positivos es: {resultado_promedio}"
print(mensaje)

####################################################################

# 3) Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

####################################################################

def producto_elementos(lista: list)-> int:
    """Esta funcion recibe como parametro una lista de numeros y calcula el producto de estos

    Argumentos:
        lista (list): una lista ya predefinida

    Returns:
        int : retorna un numero entero
    """
    producto = 1

    for i in range(len(lista)):
        producto = producto * lista[i]
        
    return producto

producto = producto_elementos(lista)
print(producto)

####################################################################

# 4) Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

####################################################################

def valor_maximo(lista: list)->int:
    """Esta funcion recibe como parametros una lista de numeros y se encarga de encontrar la posicion del valor maximo encontrado

    Argumentos:
        lista (list): una lista ya predefinida

    Retorno:
        int : se retorna un numero entero
    """
    for i in range(len(lista)):
        if i == 0 or lista[i] > numero_maximo:
            numero_maximo = lista[i]
            posicion_maxima = i + 1

    return posicion_maxima

posicion_max = valor_maximo(lista)
mensaje = f"La posicion del numero maximo es: {posicion_max}"
print(mensaje)

####################################################################

# 5) Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

###################################################################

def numeros_maximos_posiciones(lista: list)->None:
    """Esta funcion recibe como parametros una lista de numeros y muesta las posiciones de los numeros maximos encontrados

    Argumentos:
        lista (list): una lista ya predefinida.

    Retorno:
        None: No hay retorno porque ya se encarga de mostrarlo en consola.
    """
    numero_maximo = 0

    for i in range(len(lista)):
        if i == 0 or lista[i] > numero_maximo:
            numero_maximo = lista[i]
        
    for i in range(len(lista)):
        if numero_maximo == lista[i]:
            posicion_maxima = i
            print(f"El numero maximo es {numero_maximo} y esta en la posicion: {posicion_maxima}")

numeros_maximos_posiciones(lista)

####################################################################

# 6) Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y 
# su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente 
# reemplazo y luego retornar la cantidad total de reemplazos realizados.

####################################################################

lista_nombres = ["Ferman", "Bauti", "Fede", "Lucas", "Nahuel","Fede","Fede"]

def reemplazar_nombres(lista_nombres: list, nombre_buscar: str, nombre_reemplazar: str)->int:
    """Esta funcion recibe como parametros una lista de nombres, el nombre a buscar y el nombre por el que se va a reemplazar en la lista 
    para despues retornar la cantidad de reemplazos que se hizo

    Argumentos:
        lista_nombres (list): una lista de nombre predefinida
        nombre_buscar (str): el nombre que se buscara en la lista
        nombre_reemplazar (str): el nombre que va a reemplazar al buscado

    Retorno:
        int: se retorna un numero entero
    """
    cantidad_reemplazos = 0

    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_buscar:
            lista_nombres[i] = nombre_reemplazar
            cantidad_reemplazos += 1

    return cantidad_reemplazos

cantidad_reemplazos = reemplazar_nombres(lista_nombres, "Fede", "Epifania")
mensaje = f"El nombre fue reemplazado con exito unas {cantidad_reemplazos}"
print(mensaje)

####################################################################