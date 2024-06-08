print("Bienvenido al cuadrado magico!!")

numero_dimension = input("Ingrese la dimension de su cuadrado (mxn): ")
numero_dimension = int(numero_dimension)

M = numero_dimension *(numero_dimension ** 2 + 1)/2
# ----------------------------------------------------------------------- #
def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end="")
        print("")
# ----------------------------------------------------------------------- #
matriz = [[0] * numero_dimension for _ in range(numero_dimension)]
mostrar_matriz(matriz)
# ----------------------------------------------------------------------- #
# INGRESO DE NUMEROS A LA MATRIZ #
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f"Ingrese el numero para la fila {i + 1} y la columna {j + 1}: "))
        mostrar_matriz(matriz)
# ----------------------------------------------------------------------- #
# SUMA DE FILAS
suma_filas = 0
for i in range(len(matriz[0])):
    suma_filas += matriz[0][i]
# ----------------------------------------------------------------------- #
# SUMA DE COLUMNAS
suma_columnas = 0
for j in range(len(matriz[0])):
    suma_columnas += matriz[j][0]
# ----------------------------------------------------------------------- #
# SUMA DE DIAGONAL (IZQ - DER):
suma_diagonal_izq_der = 0
for i in range(len(matriz)):
    suma_diagonal_izq_der += matriz[i][i]
# ----------------------------------------------------------------------- #
# SUMA DE DIAGONAL (DER - IZQ)
suma_diagonal_der_izq = 0
for i in range(len(matriz)):
    suma_diagonal_der_izq += matriz[i][len(matriz) -1 -i]
# ----------------------------------------------------------------------- #
if suma_filas and suma_columnas == M and suma_diagonal_izq_der == suma_diagonal_der_izq == M:
    print("SII ES UN CUADRADO MAGICO :))")
    mostrar_matriz(matriz)
else:
    print("NO ES UN CUADRADO MAGICO :(")
    mostrar_matriz(matriz)
# ----------------------------------------------------------------------- #