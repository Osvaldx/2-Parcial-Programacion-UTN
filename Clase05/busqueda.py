
################### BUSQUEDA NUMERO ###################
lista = [2, 56, -2, 7, 61, 12]
busqueda = 61

def buscar_numero(lista: list, numero: int)->int:
    retorno = -1

    for i in range(len(lista)):
        if busqueda == lista[i]:
            retorno = i
    return retorno
    
buscar_numero(lista, 7)

################### SUMA DE POSITIVOS ###################

def sumar_positivos(lista: list)->int:
    acumulador_sumas = 0

    for i in range(len(lista)):
        if lista[i] > 0:
            acumulador_sumas += lista[i]

    return acumulador_sumas

print(sumar_positivos(lista))

################### NUMERO MAXIMO ###################

def numero_maximo(lista: list)-> int:
    for i in range(len(lista)):
        if i == 0 or lista[i] > numero_maximo:
            numero_maximo = lista[i]
            indice_maximo = [i]

    print(f"El numero maximo es {numero_maximo}, el indice del numero maximo es {indice_maximo}")

numero_maximo(lista)

################### BUSQUEDA Y REEMPLAZO ###################

def buscar_reemplazar(lista: list,  numero_buscado: int, reemplazo: int)-> None:
    for i in range(len(lista)):
        if lista[i] == numero_buscado:
            lista[i] = reemplazo

    return lista
    
def mostrar_lista(lista: list)-> None:
    for i in range(len(lista)):
        print(lista[i])

mostrar_lista(buscar_reemplazar(lista, 7, 11))