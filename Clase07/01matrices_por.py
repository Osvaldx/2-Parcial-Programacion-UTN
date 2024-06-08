validado = False
# --------------------------------------------------------------------------------------------------------------- #
# FUNCION PARA MOSTRAR MATRIZ ORDENADO
def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end="")
        print("")
# --------------------------------------------------------------------------------------------------------------- #
# PRIMERA MATRIZ!
numero_filas_primera_matriz = input("Ingrese las filas que desea para la primera matriz: ")
numero_filas_primera_matriz = int(numero_filas_primera_matriz)

numero_columnas_primera_matriz = input("Ingrese las columnas que desea para la primera matriz: ")
numero_columnas_primera_matriz = int(numero_columnas_primera_matriz)

primera_matriz = [[0] * numero_columnas_primera_matriz for _ in range(numero_filas_primera_matriz)]
mostrar_matriz(primera_matriz)
# --------------------------------------------------------------------------------------------------------------- #
# SEGUNDA MATRIZ!
numero_filas_segunda_matriz = input("Ingrese las filas que desea para la segunda matriz: ")
numero_filas_segunda_matriz = int(numero_filas_segunda_matriz)

numero_columnas_segunda_matriz = input("Ingrese las columnas que desea para la segunda matriz: ")
numero_columnas_segunda_matriz = int(numero_columnas_segunda_matriz)

segunda_matriz = [[0] * numero_columnas_segunda_matriz for _ in range(numero_filas_segunda_matriz)]
mostrar_matriz(segunda_matriz)
# --------------------------------------------------------------------------------------------------------------- #
if numero_columnas_primera_matriz == numero_filas_segunda_matriz:
    resultado_matriz = [[0] * numero_filas_primera_matriz for _ in range(numero_columnas_segunda_matriz)]
    validado = True
    mostrar_matriz(resultado_matriz)
else:
    print("La matriz ingresada no es posible de multiplicar")
# --------------------------------------------------------------------------------------------------------------- #
if validado == True:
    # PRIMERA MATRIZ:
    for i in range(len(primera_matriz)):
        for j in range(len(primera_matriz[i])):
            primera_matriz[i][j] = int(input(f"Ingrese un numero para la fila {i + 1} y la columna {j + 1}: "))
    # SEGUNDA MATRIZ:
    for i in range(len(segunda_matriz)):
        for j in range(len(segunda_matriz[i])):
            segunda_matriz[i][j] = int(input(f"Ingrese un numero para fila {i + 1} y la columna {j + 1}: "))
    # --------------------------------------------------------------------------------------------------------------- #
    # RESULTADO MATRIZ:
    for i in range(len(primera_matriz)):
        for j in range(len(segunda_matriz[0])):
            for k in range(len(primera_matriz[0])):
                resultado_matriz[i][j] += primera_matriz[i][k] * segunda_matriz[k][j]
    # --------------------------------------------------------------------------------------------------------------- #
    mostrar_matriz(resultado_matriz)