from Package_Input.input import get_init
from Package_Arrays.Especificas import *

# ------------------------------------------------------------- #
def ingreso_numeros(lista: list)->list:
    """Esta funcion recibe como parametros una lista y se encarga de reemplazar los 10 numeros por lo que ingrese el usuario

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        list: Retorna la lista con los numeros reemplazados
    """

    for i in range(len(lista)):
        if lista[i] == -1:
            lista[i] = get_init("Ingrese 10 numeros: ", "[ERROR] El numero no se encuentra en el rango permitido", -1000, 1000, 3)

    print(lista)
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def cantidad_positivos_negativos(lista: list)-> None:
    """Esta funcion recibe como parametros una lista y se encarga de contar la cantidad de numeros negativos y positivos que hay

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: Retorna none ya que la funcion usa un print
    """
    cantidad_positivos = 0
    cantidad_negativos = 0

    for i in range(len(lista)):
        if determinar_positividad_negatividad(lista[i]) == True:
            cantidad_positivos += 1
        elif determinar_positividad_negatividad(lista[i]) == False:
            cantidad_negativos += 1

    print(f"""
- Cantidad de positivos: {cantidad_positivos}
- Cantidad de negativos: {cantidad_negativos}
""")
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def sumatoria_numeros_pares(lista: list)-> None:
    """Esta funcion recibe como parametro una lista y se encarga de sumar los numeros pares de esta lista

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: Retorna none ya que la funcion usa un print
    """
    suma_pares = 0

    for i in range(len(lista)):
        if determinar_par_impar(lista[i]) == True:
            suma_pares += lista[i]

    print(f"""
- La suma de los numeros pares es: {suma_pares}
""")
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def mayor_numero_impar(lista: list)-> int:
    """Esta funcion recibe como parametros una lista y se encarga de mostrar el numero mayor impar

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        int: Retorna un numero entero
    """
    mayor_impar = 0

    for i in range(len(lista)):
        if determinar_par_impar(lista[i]) == False:
            if lista[i] == 0 or lista[i] > mayor_impar:
                mayor_impar = lista[i]
    
    print(f"El mayor numero impar es: {mayor_impar}")
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def imprime_numeros_ingresados(lista: list)-> list:
    """Esta funcion recibe como parametros una lista y se encarga de imprimir los numeros que se encuentran en ella

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        list: Retorna la misma lista en un print
    """

    for i in range(len(lista)):
        print(lista[i])
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def imprime_numeros_pares(lista: list)-> list:
    """Esta funcion recibe como parametros una lista y se encarga de imprimir solo los numeros pares de esta

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        list: Retorna una lista pero de numeros pares
    """

    for i in range(len(lista)):
        if determinar_par_impar(lista[i]) == True:
            print(lista[i])
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def imprime_numeros_indices_impar(lista: list)-> list:
    """Esta funcion recibe como parametros una lista y se encarga de imprimir los indices impares de la lista

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        list: Retorna una lista de indices impares
    """

    for i in range(len(lista)):
        if determinar_par_impar(i) == False:
            print(lista[i])
# ------------------------------------------------------------- #

