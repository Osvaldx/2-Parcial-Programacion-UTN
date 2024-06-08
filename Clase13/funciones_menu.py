from funciones import *

###################################################################################################
# FUNCIONES DEL MENU STARK!
# B
def nombre_superheroes_nb(lista: list, valor: str, clave: str)->None:
    """esta función recibe como parámetros una lista y se encarga de sacar el nombre de todos los superhéroes no binarios

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    heroes = obtener_dato_cantidad(lista, valor, clave)
    print("--------------------\n ---- HEROES NB ----")
    stark_imprimir_nombre_heroes(heroes)
# C Y D
def superheroe_alto(lista: list, valor :str, clave: str)->None:
    """esta función recibe como parámetros una lista y utiliza otras funciones para poder sacar El Héroe más alto de los femeninos

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    heroes = obtener_dato_cantidad(lista, valor, clave)
    numero_heroe_alto = obtener_maximo(heroes, "altura")
    print(f"--------------------\n ---- HEROE {valor} MAS ALTO ----")
    stark_imprimir_heroes(obtener_dato_cantidad(heroes, numero_heroe_alto, "altura"))
# E Y F
def superheroe_mas_debil(lista: list, valor: str, clave: str)->None:
    """esta función recibe como parámetros una lista y utiliza otras funciones para sacar El Héroe más débil de los masculinos

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    heroes = obtener_dato_cantidad(lista, valor, clave)
    numero_heroe_fuerza = obtener_minimo(heroes, "fuerza")
    print(f"------------------------------\n ---- HEROE {valor} MAS DEBIL ----")
    stark_imprimir_heroes(obtener_dato_cantidad(lista, numero_heroe_fuerza, "fuerza"))
# G
def promedio_fuerza_heroes(lista: list, valor: str, clave: str)->None:
    """Esta función recibe como parámetros una lista y utiliza otras funciones para poder llegar a sacar el promedio de fuerzas de héroes no binarios y printearlo

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    heroes = obtener_dato_cantidad(lista, valor, clave)
    promedio = calcular_promedio(heroes, "fuerza")
    print(f"El promedio de la fuerza de los heroes {valor} es: {promedio}")
# H Y I
def cantidad_superheroes_valor(lista: list, clave: str)->None:
    """Esta función recibe como parámetros una lista y se encarga de mostrar la cantidad de héroes que hay con la lista de los colores de ojos

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    todos_colores = obtener_lista_valores(lista, clave)
    titulo = clave.split("_")
    print(f"------------------------------\n HEROES X {clave}\n------------------------------")
    for color in todos_colores:
        cantidad = 0
        for i in range(len(lista)):
            color_de_ojo_heroe = obtener_datos(lista[i], clave).capitalize()
            if color_de_ojo_heroe == color:
                cantidad += 1
        print(f"Heroes con {titulo[1]} {color}: {cantidad}")
    print("------------------------------")
# J y K
def superheroe_agrupados(lista: list, clave: str):
    """Esta función recibe como parámetros una lista y utiliza otras funciones para poder agrupar a los superhéroes por color de ojo

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    todos_colores = obtener_lista_valores(lista, clave)

    for color in todos_colores:
        print(f"------------------------------\nHeroes x {clave} {color}\n------------------------------")
        for i in range(len(lista)):
            color_heroes = obtener_datos(lista[i], clave)
            if color_heroes == color:
                nombre_heroe = obtener_nombre(lista[i])
                print(f"- {nombre_heroe}")
        print("-"*30)
###################################################################################################