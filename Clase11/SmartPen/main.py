from class_boligrafo import *

lapicera_uno = Boligrafo("Azul", "Fino")
lapicera_dos = Boligrafo("Rojo", "Grueso")

continuar = False

while True:
    print(""" Seleccione alguna de las opciones:\n
    [1]. Lapicera 1.
    [2]. Lapicera 2.
    [3]. Escribir texto.
    [4]. Recargar Lapicera.
    [5]. Salir
    """)

    opciones = int(input("Ingrese una opcion: "))

    match opciones:
        case 1:
            continuar = True
            seleccionado = lapicera_uno
            print("LAPICERA 1 SELECCIONADO")
        case 2:
            continuar = True
            seleccionado = lapicera_dos
            print("LAPICERA 2 SELECCIONADO")
        case 3:
            if continuar == True:
                texto = input("Ingrese el texto: ")
                print(seleccionado.escribir(texto))
            else:
                print("DEBE SELECCIONAR ALGUNA LAPICERA PARA USAR ESTA OPCION")
        case 4:
            if continuar == True:
                recarga = int(input("Ingrese cuanto desea recargar: "))
                print(seleccionado.recargar(recarga))
            else:
                print("DEBE SELECCIONAR ALGUNA LAPICERA PARA USAR ESTA OPCION")
        case 5:
            print("Adios!")
            break