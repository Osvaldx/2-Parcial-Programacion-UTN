def counting_sort(lista: list)->list:
    # NUMERO MAXIMO Y MINIMO DE LA LISTA
    for i in range(len(lista)):
        if i == 0 or lista[i] > num_max:
            num_max = lista[i]
        if i == 0 or lista[i] < num_min:
            num_min = lista[i]

    # PARTE DE CONTEO    
    conteo = [0] * (num_max + 1)
    
    for i in range(len(lista)):
        for j in range(len(conteo)):
            if lista[i] == j:
                conteo[j] += 1
    # SUMA ACUMULATIVA
    sumas = [0] * (num_max + 1)

    for i in range(len(conteo)):
        for j in range(len(sumas)):
            if i == 0:
                sumas[j] = conteo[i]
                i += 1
    
    print(sumas)




lista = [0, 5, 3, 5 ,7 ,0 ,3, 4, 2, 14]
counting_sort(lista)