import colorama
from colorama import *
from Package_Funciones.Especificas import *
# -------------------------------------------------------------- #
def cargar_planilla(matriz_legajos: list, matriz_colectivos: list)->None:
    """Esta funcion recibe como parametros una matriz de legajos y otra de colectivos, hace que el usuario complete la planilla

    Argumentos:
        matriz_legajos (list): Una matriz ya predefinida con números de legajos alazar
        matriz_colectivos (list): Una matriz ya predefinida
    
    Retorno:
        None: No retorna nada solo printea
    """
    mostrar_matriz(matriz_legajos)
    legajo = int(input(Fore.MAGENTA + "Ingrese su N° Legajo: "))
    legajo_valido = validar_legajo(legajo, matriz_legajos)

    while legajo_valido == False:
        legajo = int(input(Fore.LIGHTRED_EX + "[ERROR] Ingrese nuevamente su N° Legajo: "))
        legajo_valido = validar_legajo(legajo, matriz_legajos)

    continuar = "si"
    while continuar:
        mostrar_lineas(matriz_colectivos)
        linea = int(input(Fore.YELLOW + "Ingrese su linea de colectivo: "))
        linea_valido = validar_linea(linea, matriz_colectivos)

        while linea_valido == False:
            linea = int(input(Fore.LIGHTRED_EX + "[ERROR] Ingrese nuevamente su linea de colectivo: "))
            linea_valido = validar_linea(linea, matriz_colectivos)
        
        coche = int(input(Fore.LIGHTCYAN_EX + "Ingrese numero de coche: "))
        coche_valido = validar_coche(coche, matriz_colectivos)

        while coche_valido == False:
            coche = int(input(Fore.LIGHTRED_EX + "[ERROR] Ingrese nuevamente numero de coche: "))
            coche_valido = validar_coche(coche, matriz_colectivos)
        
        agregar_recaudacion(matriz_colectivos, linea, coche)

        mostrar_matriz(matriz_colectivos)

        continuar = input(Fore.LIGHTGREEN_EX + "Desea seguir con otras lineas? si/no: ")
        if continuar == "no":
            break
# -------------------------------------------------------------- #
def calcular_recaudacion_linea(matriz_colectivos: list)->None:
    """Esta funcion recibe como parametros una matriz de colectivos y muesta la recaudacion total de cada linea

    Argumentos:
        matriz_colectivos (list): Una matriz ya predefinida

    Retorno:
        None: No retorna nada solo printea
    """
    for i in range(len(matriz_colectivos)):
        suma_recaudacion = 0
        for j in range(1, len(matriz_colectivos[i])):
            suma_recaudacion += matriz_colectivos[i][j]
        print(f"La recaudacion total de la linea {matriz_colectivos[i][0]} es: {suma_recaudacion}")
# -------------------------------------------------------------- #
def calcular_recaudacion_coche(matriz_colectivos: list)->None:
    """Esta funcion recibe como parametros una matriz de colectivos y muestra la recaudacion x coche de las lineas

    Argumentos:
        matriz_colectivos (list): Una matriz ya predefinida

    Retorno:
        None: No retorna nada solo printea
    """
    for i in range(len(matriz_colectivos)):
        linea_colectivo = matriz_colectivos[i][0]
        print(f"Coches de la linea {linea_colectivo}")
        for j in range(1, len(matriz_colectivos[i])):
            recaudacion = matriz_colectivos[i][j]
            print(f"  - Coche {j}: ${recaudacion}")
        print("")
# -------------------------------------------------------------- #
def calcular_recaudacion_total(matriz_colectivos: list)->None:
    """Esta funcion recibe como parametros una matriz de colectivos y muestra la recaudacion total de todos los coches y lineas

    Argumentos:
        matriz_colectivos (list): Una matriz ya predefinida

    Retorno:
        None: No retorna nada solo printea
    """
    suma_recaudacion_total = 0
    for i in range(len(matriz_colectivos)):
        for j in range(1, len(matriz_colectivos[i])):
            suma_recaudacion_total += matriz_colectivos[i][j]
    print(f"La recaudacion total de todas las lineas y coches es: {suma_recaudacion_total}")
# -------------------------------------------------------------- #
