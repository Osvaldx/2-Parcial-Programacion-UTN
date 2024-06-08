import colorama
from colorama import *
from Package_Funciones.Generales import *
from Package_Funciones.Especificas import generar_legajos

validacion = False
F = 3
C = 5

matriz_legajos = [[0] * F for _ in range(C)]
generar_legajos(matriz_legajos, 1000, 9999)

matriz_colectivos = [[100, 0, 0, 0, 0, 0],
                     [98, 0, 0, 0, 0, 0],
                     [10, 0, 0, 0, 0, 0]]
# --------------------------------------------------------------------- #
while True:
    print(Fore.GREEN + """ Seleccione alguna de las opciones:\n 
    [1]. Cargar Planilla
    [2]. Mostrar la recaudación de todos los coches y líneas.
    [3]. Calcular y mostrar recaudación por línea.
    [4]. Calcular y mostrar recaudación por coche.
    [5]. Calcular y mostrar la recaudación total.
    [6]. Salir
    """)

    opciones = input(Fore.LIGHTYELLOW_EX + "Ingrese una de las opciones: ")

    match opciones:
        case "1":
            validacion = True
            cargar_planilla(matriz_legajos, matriz_colectivos)
        case "2":
            if validacion == True:
                mostrar_matriz(matriz_colectivos)
            else:
                print(Fore.RED + "[ERROR] Ingrese por la opcion A!")
        case "3":
            if validacion == True:
                calcular_recaudacion_linea(matriz_colectivos)
            else:
                print(Fore.RED + "[ERROR] Ingrese por la opcion A!")
        case "4":
            if validacion == True:
                calcular_recaudacion_coche(matriz_colectivos)
            else:
                print(Fore.RED + "[ERROR] Ingrese por la opcion A!")
        case "5":
            if validacion == True:
                calcular_recaudacion_total(matriz_colectivos)
            else:
                print(Fore.RED + "[ERROR] Ingrese por la opcion A!")
        case "6":
            print("Adios :)")
            break
        case _:
            print(Fore.LIGHTRED_EX + "[ERROR] Ingrese una opcion valida: ")