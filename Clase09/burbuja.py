lista = [3, 2, 2, 3, 1]

def bubble_sort(lista: list)->None:
    for i in range(len(lista)):
        intercambio = False
        for j in range(len(lista) -1 -i):
            if lista[j] > lista[j+1]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
                intercambio = True
        if intercambio == False:
            break

bubble_sort(lista)
print(lista)