import random
import colorama
from colorama import *
from random import randint

# -------------------------------------------------------------- #
def generar_legajos(matriz:list, minimo:int, maximo:int)-> None:
    """Esta funcion recibe como parametros una matriz y 2 números maximos y minimos para poder generar numeros de legajos alazar entre ese rango

    Argumentos:
        matriz (list): Una matriz ya predefinida
        minimo (int): El numero minimo que se usara para el rango
        maximo (int): El numero maximo que se usara para el rango

    Retorno:
        None: No retorna nada solo reemplaza los numeros en la matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(minimo, maximo)
# -------------------------------------------------------------- #
def validar_legajo(numero:int, matriz:list)-> bool:
    """Esta funcion recibe como parametros un numero entero y una matriz como lista

    Argumentos:
        numero (int): El numero que ingreso el usuario
        matriz (list): Una matriz ya predefinida

    Retorna:
        bool: Retorna un booleano solo devuelve True o False
    """
    valido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                valido = True
    return valido
# -------------------------------------------------------------- #
def validar_linea(numero: int, matriz: list)->bool:
    """Esta funcion recibe como parametros un numero entero y una matriz y valida que el numero se encuentre adentro de la matriz

    Argumentos:
        numero (int): El numero que ingreso el usuario
        matriz (list): Una matriz ya predefinida

    Retorna:
        bool: Retorna un booleano solo devuelve True o False
    """
    valido = False
    for i in range(len(matriz)):
        if matriz[i][0] == numero:
            valido = True
    return valido
# -------------------------------------------------------------- #
def validar_coche(coche: int, matriz: list)->bool:
    """Esta funcion recibe como parametros un numero entero y una matriz como lista y valida que el numero ingresado no se salga de la longitud de la matriz

    Argumentos:
        numero (int): El numero que ingreso el usuario
        matriz (list): Una matriz ya predefinida

    Retorna:
        bool: Retorna un booleano solo devuelve True o False
    """
    valido = True
    coche_longitud = len(matriz[0])
    if coche >= coche_longitud or coche == 0:
        valido = False
    return valido
# -------------------------------------------------------------- #
def mostrar_matriz(matriz:list)-> None:
    """Esta funcion recibe como parametros una matriz lista y muestra con un print la matriz

    Argumentos:
        matriz (list): Una matriz ya predefinida
    
    Retorna:
        None: No retorna nada ya que usa un print
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:8}", end="")
        print("")
# -------------------------------------------------------------- #
def mostrar_lineas(matriz: list)->None:
    """Esta funcion recibe como parametros una matriz lista que muestra solo las lineas de colectivos

    Argumentos:
        matriz (list): Una matriz ya predefinida

    Retorna:
        None: No retorna nada ya que usa un print
    """
    for j in range(len(matriz)):
        print(f"{matriz[j][0]:4}", end="")
    print("")
# -------------------------------------------------------------- #
def mostrar_coches(linea: int, matriz: list)->None:
    """Esta funcion recibe como parametros un numero entero y una lista y muestra los numeros de la fila

    Argumentos:
        linea (int): Un numero entero que se le pide al usuario
        matriz (list): Una matriz ya predefinida
    
    Retorna:
        None: No retorna nada ya que usa un print
    """
    for i in range(len(matriz)):
        if matriz[i][0] == linea:
            for j in range(1, len(matriz[i])):
                print(f"{matriz[i][j]:4}", end="")
            print("")
# -------------------------------------------------------------- #
def validar_recaudacion(recaudacion:int )->bool:
    """Esta funcion recibe como parametros un numero entero y valida si el numero esta por encima de 0

    Argumentos:
        recaudacion (int): Un numero entero que se le pide al usuario

    Returns:
        bool: Retorna un booleano solo devuelve True o False
    """
    valido = False
    if recaudacion > 0:
        valido = True
    return valido
# -------------------------------------------------------------- #
def agregar_recaudacion(matriz_colectivos: list, linea: int, coche:int)->None:
    """Esta funcion recibe como parametros una matriz lista y 2 numeros enteros, le pide al usuario la recaudacion y valida, para despues poder reemplazarlo en la matriz

    Argumentos:
        matriz_colectivos (list): Una matriz ya predefinida
        linea (int): Un numero entero que se le pide al usuario
        coche (int): Un numero entero que se le pide al usuario

    Retorno:
        None: no retorna nada solo reemplaza valores en la matriz
    """
    continuar = "si"
    while continuar:
        recaudacion = int(input(Fore.LIGHTMAGENTA_EX + "Ingrese la recaudacion del dia: "))
        recaudacion_valido = validar_recaudacion(recaudacion)

        while recaudacion_valido == False:
            recaudacion = int(input(Fore.LIGHTRED_EX + "[ERROR] Ingrese nuevamente la recaudacion del dia: "))
            recaudacion_valido = validar_recaudacion(recaudacion)
        
        for i in range(len(matriz_colectivos)):
            for j in range(len(matriz_colectivos[i])):
                if matriz_colectivos[i][j] == linea:
                    indice_linea = i
        matriz_colectivos[indice_linea][coche] += recaudacion
        continuar = input(Fore.LIGHTGREEN_EX + "Desea seguir ingresando recaudaciones? si/no: ")
        if continuar == "no":
            break
# --------------------------------------------------------------- #