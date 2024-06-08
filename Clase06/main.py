from Package_Arrays.Array_Generales import *

lista = [-1] * 10

valido = False
msj_invalido = "DEBE PASAR POR LA OPCION [A] PARA UTILIZAR ESTA OPCION"

while True:
    print(""" Seleccione alguna de las opciones:\n 
    [A]. Ingreso de 10 numeros enteros entre -1000 y 1000.
    [B]. Mostrar la cantidad de números positivos y negativos.
    [C]. Mostrar la sumatoria de los números pares.
    [D]. Informar el mayor de los números impares.
    [E]. Imprimir todos los números ingresados.
    [F]. Imprimir todos los números pares.
    [G]. Imprimir los números de los índices impares.
    [H]. Salir
    """)

    opciones = input("Opcion: ")

    match opciones:
        case "A":
            valido = True
            ingreso_numeros(lista)
        case "B":
            if valido == True:
                cantidad_positivos_negativos(lista)
            else:
                print(msj_invalido)
        case "C":
            if valido == True:
                sumatoria_numeros_pares(lista)
            else:
                print(msj_invalido)
        case "D":
            if valido == True:
                mayor_numero_impar(lista)
            else:
                print(msj_invalido)
        case "E":
            if valido == True:
                imprime_numeros_ingresados(lista)
            else:
                print(msj_invalido)
        case "F":
            if valido == True:
                imprime_numeros_pares(lista)
            else:
                print(msj_invalido)
        case "G":
            if valido == True:
                imprime_numeros_indices_impar(lista)
            else:
                print(msj_invalido)
        case "H":
            break