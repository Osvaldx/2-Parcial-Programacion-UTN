from data_stark import lista_personajes
from funciones_menu import *

def stark_marvel_app(lista: list):
    """Esta función recibe como parámetro es una lista y utiliza otras funciones para poder hacer funcionar el menú y validar lo que tenga

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    validacion = False
    while True:
        opciones = stark_menu_principal()

        if opciones == False:
            print("Ingrese nuevamente una opcion")
            opciones = stark_menu_principal()

        match opciones:
            case 1:
                validacion = True
                stark_normalizar_datos(lista)
            case 2:
                if validacion == True:
                    nombre_superheroes_nb(lista, "NB", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 3:
                if validacion == True:
                    superheroe_alto(lista, "F", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 4:
                if validacion == True:
                    superheroe_alto(lista, "M", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 5:
                if validacion == True:
                    superheroe_mas_debil(lista, "M", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 6:
                if validacion == True:
                    superheroe_mas_debil(lista, "NB", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 7:
                if validacion == True:
                    promedio_fuerza_heroes(lista, "NB", "genero")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 8:
                if validacion == True:
                    cantidad_superheroes_valor(lista, "color_ojos")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 9:
                if validacion == True:
                    cantidad_superheroes_valor(lista, "color_pelo")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 10:
                if validacion == True:
                    superheroe_agrupados(lista, "color_ojos")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 11:
                if validacion == True:
                    superheroe_agrupados(lista, "inteligencia")
                else:
                    print("NORMALICE LOS DATOS! OPCION 1")
            case 12:
                print("ADIOS!")
                break

stark_marvel_app(lista_personajes)