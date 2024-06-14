from Package_Funciones.peliculas import *

# Nahuel Romano Osvaldo

lista_peliculas = []

cargar_peliculas(lista_peliculas)
lista_peliculas = sacar_peliculas_repetidas(lista_peliculas)
seteo_ids_eliminadas()

while True:
    mostrar_menu("menu_principal")

    opciones = input("Ingrese una de las opciones: ")
    opciones = validacion_input(opciones)

    match opciones:
        case 1:
            pelicula = crear_pelicula(lista_peliculas)
            dar_de_alta(lista_peliculas, pelicula)
        case 2:
            print(modificar(lista_peliculas))
        case 3:
            print(eliminar(lista_peliculas))
        case 4:
            opciones_mostrar_peliculas(lista_peliculas)
        case 5:
            ordenar_peliculas(lista_peliculas)
        case 6:
            print(buscar_pelicula_titulo(lista_peliculas))
        case 7:
            mostrar_promedios(lista_peliculas)
        case 8:
            mostrar_porcentajes(lista_peliculas)
        case 9:
            mostrar_por_genero(lista_peliculas)
        case 10:
            guardar_al_salir(lista_peliculas)
            break
        case _:
            print("[!] INGRESE UNA OPCION VALIDA")