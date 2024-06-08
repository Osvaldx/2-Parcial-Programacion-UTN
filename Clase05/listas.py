mi_lista = [0] * 5

respuesta = "Si"

while respuesta == "Si":
    casilla = int(input("Ingrese la casilla que quiera: "))
    numero = int(input("Ingrese el numero que quiera: "))

    mi_lista[casilla - 1 ] = numero

    continuar = input("Desea continuar?\n Si o No\n: ")
    if continuar == "Si":
        respuesta = "Si"
    else:
        respuesta = "No"


for i in range(len(mi_lista)):
    print(mi_lista[i])