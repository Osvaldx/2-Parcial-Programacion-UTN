from Package_Funciones.validaciones import *
from Package_Funciones.especificas import *
import json

def crear_pelicula(lista: list)->dict:
    """Esta función recibe como parámetros una lista y se encarga te pedirle al usuario datos necesarios 
    para poder llenarlos y darle un formato de diccionario

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        dict: un diccionario con todos los datos pedidos al usuario
    """
    titulo = validacion_titulo(lista, "crear")

    mostrar_menu("tipos_generos")
    genero = input("Ingrese uno de los generos: ")
    genero = validacion_genero(genero)
    
    anio_lanzamiento = input("Ingrese el año de lanzamiento: ")
    anio_lanzamiento = validacion_anio(anio_lanzamiento)
    
    duracion = input("Ingrese la duracion de la pelicula (en minutos): ")
    duracion = validacion_duracion(duracion)
    
    apta_todo_publico = input("La pelicula es apta para todo publico (Si/No): ")
    apta_todo_publico = apta_todo_publico.capitalize()
    apta_todo_publico = validacion_atp(apta_todo_publico)
    
    plataformas = validacion_plataformas()

    formato = {
        "id": "",
        "titulo": titulo,
        "genero": genero,
        "año_lanzamiento": anio_lanzamiento,
        "duracion": duracion,
        "atp": apta_todo_publico,
        "plataformas": plataformas,
    }

    return formato
# ------------------------------------------------------------------------------------ #
def dar_de_alta(lista: list, diccionario: dict)->None:
    """Esta funcion recibe como parametros una lista y un diccionario y se encarga
    de asignarle una ID al diccionario que le llego por parametro y agregarlo a la lista

    Argumentos:
        lista (list): Una lista ya predefinida
        diccionario (dict): Un diccionario ya predefinido

    Returns:
        None: No retorna nada
    """
    if lista != []:
        id_maxima = sacar_id_maxima(lista)

        with open("Parcial_1/Package_Funciones/ids_eliminadas.txt", "r") as archivo:
            texto = archivo.readlines()
            if texto != []:
                lista_nueva = []
                for linea in texto:
                    linea = linea.replace("\n", "")
                    linea = int(linea)
                    lista_nueva.append(linea)

                while (id_maxima + 1) in lista_nueva:
                    id_maxima += 1
                
                id_maxima += 1
            else:
                id_maxima += 1

        diccionario["id"] = id_maxima
        lista.append(diccionario)

    else:
        diccionario["id"] = 1
        lista.append(diccionario)
# ------------------------------------------------------------------------------------ #
def modificar(lista: list)->str:
    """Esta funcion recibe como parametros una lista y se encarga de modificar los diccionarios dependiendo de
    que dato quieren cambiar, titulo, genero, duracion, etc

    Argumentos:
        lista (list): Una lista ya predenida con las peliculas

    Retorna:
        str: Retorna un mensaje de los cambios que se hicieron
    """

    if lista != []:
        pelicula_modificar = validacion_titulo(lista, "no crear")
        
        mensaje = "[!] No hay ninguna pelicula con ese titulo :("

        for i in range(len(lista)):
            if pelicula_modificar.upper() == lista[i]["titulo"].upper():
                mensaje = ""
                bandera = True
                while bandera:
                    mostrar_menu("modificar_menu")

                    opciones = input("Ingrese una opcion: ")
                    opciones = validacion_input(opciones)

                    match opciones:
                        case 1:
                            nuevo_titulo = validacion_titulo(lista, "crear")
                            lista[i]["titulo"] = nuevo_titulo
                            mensaje += "[+] TITULO MODIFICADO CON EXITO!\n"
                        case 2:
                            mostrar_menu("tipos_generos")
                            new_genero = input("Ingrese el nuevo genero: ")
                            new_genero = validacion_genero(new_genero)
                            lista[i]["genero"] = new_genero
                            mensaje += "[+] GENERO MODIFICADO CON EXITO!\n"
                        case 3:
                            nuevo_anio = input("Ingrese el nuevo año de lanzamiento: ")
                            nuevo_anio = validacion_anio(nuevo_anio)
                            lista[i]["año_lanzamiento"] = nuevo_anio
                            mensaje += "[+] AÑO DE LANZAMIENTO MODIFICADO CON EXITO!\n"
                        case 4:
                            nueva_duracion = input("Ingrese la nueva duracion de la pelicula (en minutos): ")
                            nueva_duracion = validacion_duracion(nueva_duracion)
                            lista[i]["duracion"] = nueva_duracion
                            mensaje += "[+] DURACION MODIFICADA CON EXITO!\n"
                        case 5:
                            nuevo_atp = input("El ATP nuevo es apto para todo publico Si/No: ")
                            nuevo_atp = nuevo_atp.capitalize()
                            nuevo_atp = validacion_atp(nuevo_atp)
                            lista[i]["atp"] = nuevo_atp
                            mensaje += "[+] ATP MODIFICADA CON EXITO!\n"
                        case 6:
                            nueva_plataforma = validacion_plataformas()
                            lista[i]["plataformas"] = nueva_plataforma
                            mensaje += "[+] PLATAFORMA MODIFICADA CON EXITO!"
                        case _:
                            print("[!] OPCION INVALIDA")
                    
                    continuar = input("Desea seguir modificando datos? Si/No: ")
                    continuar = continuar.capitalize()

                    while continuar != "Si" and continuar != "No":
                        print("[!] OPCION INVALIDA")
                        continuar = input("Desea seguir modificando datos? Si/No: ")
                        continuar = continuar.capitalize()

                    if continuar == "No":
                        bandera = False
    else:
        mensaje = "[!] ERROR, La lista se encuentra vacia."
    
    return mensaje
# ------------------------------------------------------------------------------------ #
def eliminar(lista: list)->str:
    """Esta funcion recibe como parametros una lista y se encarga de pedirle al usuario que
    pelicula desea eliminar mediante el titulo, cuando se elimina la pelicula se guarda en un txt
    la id de esa pelicula eliminada

    Argumentos:
        lista (list): Una lista ya predefnida

    Retorna:
        str: Una string dependiendo el caso
    """
    if lista != []:
        titulo_pelicula = input("Ingrese el titulo de la pelicula a ELIMINAR: ")
        mensaje = "[!] No hay ninguna pelicula con ese titulo"
        indice_eliminar = ""
        
        for i in range(len(lista)):
            if titulo_pelicula.upper() == lista[i]['titulo'].upper():
                mensaje = f"[+] SE ELIMINO CON EXITO LA PELICULA: {titulo_pelicula} ID: {lista[i]['id']}"
                indice_eliminar = i
                with open("Parcial_1/Package_Funciones/ids_eliminadas.txt", "a") as archivo:
                    archivo.write(f"{lista[i]['id']}\n")
        
        if indice_eliminar != "":
            lista.pop(indice_eliminar)
    
    else:
        mensaje = "[!] ERROR, La lista se encuentra vacia."
    
    return mensaje
# ------------------------------------------------------------------------------------ #
def opciones_mostrar_peliculas(lista: list)->None:
    """Esta funcion recibe como parametros una lista ya predefinida, se encarga de mostrar
    las peliculas por el dato que el usuario ingresa, se encarga de filtrar

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    if lista != []:
        while True:
            mostrar_menu("mostrar_pelis")

            opciones = input("Ingrese una de las opciones: ")
            opciones = opciones.lower()

            match opciones:
                case "a":
                    mostrar_peliculas(lista)
                case "b":
                    mostrar_menu("tipos_generos")
                    determinado_genero = input("Ingrese el tipo de genero de las peliculas a mostrar: ")
                    determinado_genero = validacion_genero(determinado_genero)

                    lista_generos = list(filter(lambda pelicula : pelicula["genero"] == determinado_genero,lista))
                    
                    if lista_generos != []:
                        mostrar_peliculas(lista_generos)
                    else:
                        print("[!] No hay peliculas con ese genero :(")
                case "c":
                    determinado_anio = input("Ingrese el año de las peliculas a mostrar: ")
                    determinado_anio = validacion_anio(determinado_anio)

                    lista_anios = list(filter(lambda pelicula : pelicula["año_lanzamiento"] == determinado_anio,lista))
                    
                    if lista_anios != []:
                        mostrar_peliculas(lista_anios)
                    else:
                        print("[!] No hay peliculas con ese año :(")
                case "d":
                    lista_atp = list(filter(lambda pelicula : pelicula["atp"] == True,lista))
                    
                    mostrar_peliculas(lista_atp)
                case "e":
                    lista_no_atp = list(filter(lambda pelicula : pelicula["atp"] == False,lista))
                    
                    mostrar_peliculas(lista_no_atp)
                case "f":
                    determinada_plataforma = input("Ingrese la plataforma a filtrar de peliculas: ")
                    lista_pelis_plataforma = []

                    for i in range(len(lista)):
                        for plataforma in lista[i]["plataformas"]:
                            if determinada_plataforma.upper() == plataforma.upper():
                                lista_pelis_plataforma.append(lista[i])
                    
                    if lista_pelis_plataforma != []:
                        mostrar_peliculas(lista_pelis_plataforma)
                    else:
                        print("[!] NO SE ENCONTRO NINGUNA PLATAFORMA CON ESE NOMBRE")
                case "g":
                    break
                case _:
                    print("[!] INGRESE UNA OPCION VALIDA")
    
    else:
        print("[!] ERROR, La lista se encuentra vacia.")
# ------------------------------------------------------------------------------------ #
def ordenar_peliculas(lista: list)->None:
    """Esta funcion recibe como parametros una lista ya predefinida y se encarga de ofrecer
    al usuario ordenar (llama a funciones de ordenamiento) las peliculas de forma ascendente o descendente, por categorias
    titulo, genero, año, etc.

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    if lista != []:
        bandera = False
        while True:
            if bandera == False:
                mostrar_menu("ascendente_descendente")
                opcion_asc_des = input("Ingrese una de las opciones: ")
                opcion_asc_des = opcion_asc_des.lower()
                opcion_asc_des = validacion_asc_des(opcion_asc_des)
                bandera = True
            
            mostrar_menu("menu_ordenar_pelis")
            opciones = input("Ingrese una de las opciones: ")
            opciones = opciones.lower()

            match opciones:
                case "a":
                    bubble_sort(lista, "titulo", opcion_asc_des)
                    mostrar_peliculas(lista)
                case "b":
                    bubble_sort(lista, "genero", opcion_asc_des)
                    mostrar_peliculas(lista)
                case "c":
                    bubble_sort(lista, "año_lanzamiento", opcion_asc_des)
                    mostrar_peliculas(lista)
                case "d":
                    bubble_sort(lista, "duracion", opcion_asc_des)
                    mostrar_peliculas(lista)
                case "e":
                    break
                case _:
                    print("[!] OPCION NO VALIDA")

    else:
        print("[!] ERROR, La lista se encuentra vacia.")
# ------------------------------------------------------------------------------------ #
def buscar_pelicula_titulo(lista: list)->str:
    """Esta funcion recibe como parametros una lista y se encarga de pedirle al usuario la pelicula que desea
    mostrar

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorno:
        str: Un mensaje dependiendo lo que sucede
    """
    if lista != []:
        titulo_a_buscar = validacion_titulo(lista, "no crear")
        pelicula = []
        mensaje = "[!] ESE TITULO NO EXISTE!"

        for i in range(len(lista)):
            if titulo_a_buscar.upper() == lista[i]["titulo"].upper():
                pelicula.append(lista[i])
                mostrar_peliculas(pelicula)
                mensaje = "[+] PELICULA ENCONTRADA Y MOSTRADA CON EXITO!"
                break
    
    else:
        mensaje = "[!] ERROR, La lista se encuentra vacia."
    
    return mensaje
# ------------------------------------------------------------------------------------ #
def mostrar_promedios(lista: list)->None:
    """Esta funcion recibe como parametros una lista, se encarga de ofrecerle al usuario
    si quiere ver el promedio por año o por duracion de las peliculas

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    if lista != []:
        while True:
            mostrar_menu("promedio_peliculas")

            opcion = input("Ingrese una de las opciones: ")
            opcion = opcion.lower()

            match opcion:
                case "a":
                    promedio = sacar_promedio(lista, "año_lanzamiento")
                    print(f"[+] EL PROMEDIO de Año de lanzamiento en las peliculas es: {promedio}")
                case "b":
                    promedio = sacar_promedio(lista, "duracion")
                    print(f"[+] EL PROMEDIO de Duracion en las peliculas es: {promedio} m")
                case "c":
                    break
                case _:
                    print("[!] OPCION NO VALIDA")
    else:
        print("[!] ERROR, La lista se encuentra vacia.")
# ------------------------------------------------------------------------------------ #
def mostrar_porcentajes(lista: list)->None:
    """Esta funcion recibe como parametros una lista y se encarga de mostrar los porcentajes
    del genero ingresado o de los ATP

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    if lista != []:
        while True:
            mostrar_menu("porcentaje_peliculas")

            opcion = input("Ingrese una de las opciones: ")
            opcion = opcion.lower()

            match opcion:
                case "a":
                    mostrar_menu("tipos_generos")
                    genero_ingresado = input("Ingrese el genero que desea ver su porcentaje: ")
                    genero_ingresado = validacion_genero(genero_ingresado)

                    porcentaje = porcentaje_genero(lista, "genero", genero_ingresado)
                    print(f"[+] El porcentaje del genero {genero_ingresado} es: {porcentaje}%")
                case "b":
                    porcentaje_atp_si = porcentaje_genero(lista, "atp", True)
                    porcentaje_atp_no = porcentaje_genero(lista, "atp", False)

                    print(f"[+] El porcentaje del ATP Si (Apto para todo publico) es {porcentaje_atp_si}%")
                    print(f"[+] El porcentaje del ATP No (No Apto para todo publico) es {porcentaje_atp_no}%")
                case "c":
                    break
                case _:
                    print("[!] OPCION NO VALIDA")
    else:
        print("[!] ERROR, La lista se encuentra vacia.")
# ------------------------------------------------------------------------------------ #
def guardar_al_salir(lista: list)->None:
    """Esta funcion recibe como parametros una lista y se encarga de guardar los cambios
    que sucedieron en la lista con peliculas, primero les da un formato para sobreescribirlos
    en el csv de peliculas

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    if lista != []:
        with open("Parcial_1/Package_Funciones/peliculas.csv", "w", encoding="UTF-8") as archivo:
            archivo.write("ID,Título,Género,Año de lanzamiento,Duración,ATP,Plataformas\n")
            for i in range(len(lista)):
                id = lista[i]["id"]
                titulo = lista[i]["titulo"]
                genero = lista[i]["genero"]
                anio_lanzamiento = lista[i]["año_lanzamiento"]
                duracion = lista[i]["duracion"]
                atp = lista[i]["atp"]
                plataformas = lista[i]["plataformas"]
                caracter = "-"
                plataformas = caracter.join(plataformas)

                if atp == True:
                    atp = "Si"
                else:
                    atp = "No"

                archivo.write(f"{id},{titulo},{genero},{anio_lanzamiento},{duracion},{atp},{plataformas}\n")
        
        seteo_ids_eliminadas()
# ------------------------------------------------------------------------------------ #
def mostrar_por_genero(lista: list):
    lista_generos = obtener_lista_valores(lista, "genero")
    datos_generos = {}

    with open("Parcial_1\Package_Funciones\peliculas_por_generos.json", "w", encoding="utf-8") as archivo:
        archivo.writelines(datos_generos)

    print("*"*50)
    for genero in lista_generos:
        datos_generos[genero] = []
        contador = 0
        print(f"Peliculas con genero {genero}:")
        for i in range(len(lista)):
            titulo = lista[i]['titulo']
            if lista[i]['genero'] == genero:
                contador += 1
                print(f"  - {lista[i].get('titulo')}")
                datos_generos[genero].append(titulo)
        if contador > 0:
            print(f"Total de películas de género {genero}: {contador}")
            print("*"*50)

    with open("Parcial_1\Package_Funciones\peliculas_por_generos.json", "a", encoding="utf-8") as archivo:
        json.dump(datos_generos, archivo, indent=4, ensure_ascii=False)
# ------------------------------------------------------------------------------------ #