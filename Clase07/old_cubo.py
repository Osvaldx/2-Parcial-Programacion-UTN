print("Bienvenido a el cuadrado magico!")

numero_dimension = input("Ingrese las dimensiones (numero_dimension x numero_dimension) del cuadrado: ")
numero_dimension = int(numero_dimension)

M = numero_dimension *(numero_dimension ** 2 + 1)/2
# --------------------------------------------------------------------------------------------------------------- #
def mostrar_matriz(matriz: list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end="")
        print("")
# --------------------------------------------------------------------------------------------------------------- #
matriz = [[0] * numero_dimension for _ in range(numero_dimension)]
mostrar_matriz(matriz)
# --------------------------------------------------------------------------------------------------------------- #
# SUMA EN FILAS
suma_filas_valida = True
for i in range(len(matriz)):
    suma_filas = 0
    for j in range(len(matriz[i])):
        numero_ingresado = int(input(f"Ingrese el numero para la fila {i + 1} y la columna {j + 1}: "))
        matriz[i][j] = numero_ingresado
        mostrar_matriz(matriz)
        suma_filas += numero_ingresado
    if suma_filas != M:
        suma_filas_valida = False
# --------------------------------------------------------------------------------------------------------------- #
# SUMA EN COLUMNAS
suma_columnas_valida = True
for j in range(len(matriz[0])):
    suma_columnas = 0
    for i in range(len(matriz)):
        suma_columnas += matriz[i][j]
    if suma_columnas != M:
        suma_columnas_valida = False
# --------------------------------------------------------------------------------------------------------------- #
# SUMA EN DIAGONALES (IZQ - DERC)
suma_izquierda  = 0
for i in range(len(matriz)):
    suma_izquierda += matriz[i][i]
# --------------------------------------------------------------------------------------------------------------- #
# SUMA EN DIAGONALES (DERC - IZQ)
suma_derecha = 0
for i in range(len(matriz)):
    suma_derecha += matriz[i][len(matriz) -1 -i]
# --------------------------------------------------------------------------------------------------------------- #
if suma_filas_valida and suma_columnas_valida and suma_derecha == M and suma_izquierda == M:
    print("El CUADRADO ES MAGICO!!")
    mostrar_matriz(matriz)
else:
    print("EL CUADRADO NO ES MAGICO :(((( ")
    mostrar_matriz(matriz)
# --------------------------------------------------------------------------------------------------------------- #