def multiplicar_matrices(A, B):
    # A es una matriz de 3x2 y B es una matriz de 2x3
    # El resultado será una matriz de 3x3
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            suma = 0
            for k in range(len(A[0])):
                suma += A[i][k] * B[k][j]
            resultado[i][j] = suma
            
    return resultado

# Ejemplo de matrices
primera_matriz = [[1, 2], [3, 4], [5, 6]]  # Matriz de 3x2
segunda_matriz = [[7, 8, 9], [1, 2, 3]]  # Matriz de 2x3

# Llamada a la función
resultado_matriz = multiplicar_matrices(primera_matriz, segunda_matriz)

# Mostrar el resultado
for fila in resultado_matriz:
    print(fila)
