
matriz_uno = [[1, 2],
              [3, 4],
              [5, 6]]

matriz_dos = [[7, 8, 9],
              [1, 2, 3]]

def mostrar_matriz(matriz: list)->None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end="")
        print("")

matriz_resultado = [[0]* 3 for _ in range(3)]

def multiplicacion(matriz_uno: list, matriz_dos: list)->list:
    for i in range(len(matriz_uno)):
        for j in range(len(matriz_dos[0])):
            sumatoria = 0
            for k in range(len(matriz_uno[0])):
                sumatoria += matriz_uno[i][k] * matriz_dos[k][j]
            matriz_resultado[i][j] = sumatoria
    return matriz_resultado

mostrar_matriz(multiplicacion(matriz_uno, matriz_dos))