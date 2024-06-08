
matriz = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" | ")
    print("")