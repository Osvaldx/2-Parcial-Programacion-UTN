from .funciones_especificas import *
from functools import reduce
import json

# ------------------------------------------------------------------------------------ #
def opciones_menu(clave: str)->int:
    if clave == "numeros":
        opcion = input("Ingrese una de las opciones: ")
        while not opcion.isnumeric():
            opcion = input("Ingrese nuevamente una de las opciones: ")
        opcion = int(opcion)
    elif clave == "letras":
        opcion = input("Ingrese una de las opciones: ").lower()
        while not opcion.isalpha():
            opcion = input("Ingrese nuevamente una de las opciones: ")
    
    return opcion
# ------------------------------------------------------------------------------------ #
def leer_csv_json(lista: list):
    mostrar_menu("jsonycsv")
    tipo_archivo_usuario = opciones_menu("numeros")

    match tipo_archivo_usuario:
        case 1:
            archivo_ingresado = input("Ingrese el nombre del archivo con su extension: ")
            validar_extension = archivo_ingresado
            validar_extension = validar_extension.split(".")
            if (validar_extension[0] == archivo_ingresado) or (validar_extension[1] != "json"):
                print("NO ES UN ARCHIVO JSON")
            else:
                path = f"Clase15/Practica_ABM_Archivos/{archivo_ingresado}"
                with open(path, "r", encoding="UTF-8") as archivo:
                    empleados = json.load(archivo)
                    lista.append(empleados)
        case 2:
            archivo_ingresado = input("Ingrese el nombre del archivo con su extension: ")
            validar_extension = archivo_ingresado
            validar_extension = validar_extension.split(".")
            if (validar_extension[0] == archivo_ingresado) or (validar_extension[1] != "csv"):
                print("NO ES UN ARCHIVO CSV")
            else:
                path = f"Clase15/Practica_ABM_Archivos/{archivo_ingresado}"
                with open(path, "r", encoding='UTF-8') as archivo:
                    empleados = archivo.readlines()
                    formato = {
                        "empleados": []
                    }
                    lista.append(formato)
                    for i in range(1, len(empleados)):
                        datos = empleados[i]
                        datos = datos.split(",")

                        identidad = datos[0]
                        identidad = int(identidad)
                        nombre = datos[1]
                        apellido = datos[2]
                        puesto = datos[3]
                        salario = datos[4]
                        salario = salario.replace("\n", "")
                        salario = int(salario)

                        empleado = {
                            "id": identidad,
                            "nombre": nombre,
                            "apellido": apellido,
                            "puesto": puesto,
                            "salario": salario,
                        }
                        lista[0]["empleados"].append(empleado)
        case _:
            print("REINTENTAR")
# ------------------------------------------------------------------------------------ #
def crear_usuario()->dict:
    nombre = input("Ingrese su Nombre: ").capitalize()
    while validar_nombre_apellido(nombre) == False:
        nombre = input("Ingrese nuevamente su Nombre: ").capitalize()

    apellido = input("Ingrese su Apellido: ").capitalize()
    while validar_nombre_apellido(apellido) == False:
        apellido = input("Ingrese nuevamente su Apellido: ").capitalize()

    puesto = input("Ingrese su Puesto: ").capitalize()
    while validar_puesto(puesto) == False:
        puesto = input("Ingrese nuevamente su Puesto: ").capitalize()

    salario = input("Ingrese el monto de su Salario: ")
    while validar_salario(salario) == False:
        salario = input("Ingrese nuevamente el monto de su Salario: ")
    salario = int(salario)

    empleado = {
        "id": "",
        "nombre": nombre,
        "apellido": apellido,
        "puesto": puesto,
        "salario": salario
    }

    return empleado
# ------------------------------------------------------------------------------------ #
def dar_de_alta(lista: list, diccionario: dict, identificacion: int)->None:
    if lista != []:
        lista_entera = lista[0]["empleados"]
        id_maximo = 0
        for i in range(len(lista_entera)):
            if id_maximo == 0 or lista_entera[i]["id"] > id_maximo:
                id_maximo = lista_entera[i]["id"]
        identificacion = id_maximo + 1
        diccionario["id"] = identificacion
        lista[0]["empleados"].append(diccionario)
        print(f"- Se agrego al empleado con la ID: {identificacion} correctamente!")
    else:
        diccionario["id"] = identificacion
        lista[0]["empleados"].append(diccionario)
# ------------------------------------------------------------------------------------ #
def mostrar_menu(clave: str):
    if clave == "principal":
        print("""
            - [1] Leer desde CSV / JSON.
            - [2] Dar de alta.
            - [3] Modificar.
            - [4] Eliminar.
            - [5] Mostrar empleados x CATEGORIA.
            - [6] Mostrar Analistas con sueldo mayor a $500000.
            - [7] Calcular salario promedio.
            - [8] Ordenar empleados.
            - [9] Guardar Cambios.
            - [10] Salir.
            """)
    elif clave == "submenu_mostrar":
        print("""Que desea modificar:
            - [a] Empleados con determinado PUESTO.
            - [b] Empleados con determinado SALARIO.
            - [c] Empleados con determinado APELLIDO.
            """)
    elif clave == "submenu_mostrar_puesto":
        print("""Puestos:
            - Gerente
            - Supervisor
            - Analista
            - Encargado
            - Asistente
            """)
    elif clave == "submenu":
        print("""Que desea modificar:
            - [1] Nombre
            - [2] Apellido
            - [3] Puesto
            - [4] Salario
            """)
    elif clave == "jsonycsv":
        print("""Que tipo de archivo cargara?
          - [1] JSON
          - [2] CSV""")
    elif clave == "ordernar_listado":
        print("""De que manera desea ordenar los empleados:
            - [1] Nombre
            - [2] Apellido
            - [3] Salario
            """)
    elif clave == "ascendente_descendente":
        print("""De que manera desea ordenar los empleados:
            - Ascendente
            - Descendente
            """)
# ------------------------------------------------------------------------------------ #
def mostrar_empleados_p_s_a(lista: list):
    mostrar_menu("submenu_mostrar")
    opciones = opciones_menu("letras")
    match opciones:
        case "a":
            mostrar_menu("submenu_mostrar_puesto")
            opcion_puesto = input("Ingrese una de los puestos: ").capitalize()
            while validar_puesto(opcion_puesto) == False:
                opcion_puesto = input("Ingrese nuevamente su Puesto: ").capitalize()
            # --------------------------------------- #
            if opcion_puesto == "Gerente":
                lista_gerentes = []
                formato = {
                    "gerentes": []
                }
                lista_gerentes.append(formato)
                lista_gerentes[0]["gerentes"] = list(filter(lambda empleados : empleados["puesto"] == "Gerente", lista[0]["empleados"]))
                print("*"*30, "\n - LISTA DE GERENTES - ")
                mostrar_empleados(lista_gerentes, "gerentes", "False")
            # --------------------------------------- #
            elif opcion_puesto == "Supervisor":
                lista_supervisores = []
                formato = {
                    "supervisores": []
                }
                lista_supervisores.append(formato)
                lista_supervisores[0]["supervisores"] = list(filter(lambda empleados : empleados["puesto"] == "Supervisor", lista[0]["empleados"]))
                print("*"*30, "\n - LISTA DE SUPERVISORES - ")
                mostrar_empleados(lista_supervisores, "supervisores", "False")
            # --------------------------------------- #
            elif opcion_puesto == "Analista":
                lista_analistas = []
                formato = {
                    "analistas": []
                }
                lista_analistas.append(formato)
                lista_analistas[0]["analistas"] = list(filter(lambda empleados : empleados["puesto"] == "Analista", lista[0]["empleados"]))
                print("*"*30, "\n - LISTA DE ANALISTAS - ")
                mostrar_empleados(lista_analistas, "analistas", "False")
            # --------------------------------------- #
            elif opcion_puesto == "Encargado":
                lista_encargados = []
                formato = {
                    "encargados": []
                }
                lista_encargados.append(formato)
                lista_encargados[0]["encargados"] = list(filter(lambda empleados : empleados["puesto"] == "Encargado", lista[0]["empleados"]))
                print("*"*30, "\n - LISTA DE ENCARGADO - ")
                mostrar_empleados(lista_encargados, "encargados", "False")
            # --------------------------------------- #
            elif opcion_puesto == "Asistente":
                lista_asistentes = []
                formato = {
                    "asistentes": []
                }
                lista_asistentes.append(formato)
                lista_asistentes[0]["asistentes"] = list(filter(lambda empleados : empleados["puesto"] == "Asistente", lista[0]["empleados"]))
                print("*"*30, "\n - LISTA DE ASISTENTES - ")
                mostrar_empleados(lista_asistentes, "asistentes", "False")
            # --------------------------------------- #
            else:
                print("INGRESE UN PUESTO QUE EXISTA")
            # --------------------------------------- #
        case "b":
            salario_determinado = input("Ingrese el salario a buscar: ")
            while validar_salario(salario_determinado) == False:
                salario_determinado = input("Ingrese nuevamente el salario a buscar: ")
            salario_determinado = int(salario_determinado)
            empleado_salario = []
            formato = {
                "salarios_determinado": []
            }
            empleado_salario.append(formato)
            empleado_salario[0]["salarios_determinado"] = filter(lambda empleado : empleado["salario"] == salario_determinado,lista[0]["empleados"])
            print("*"*30, "\n - LISTA DE EMPLEADOS X SUELDO DETERMINADO - ")
            mostrar_empleados(empleado_salario, "salarios_determinado", "False")
        case "c":
            apellido_determinado = input("Ingrese el apellido a buscar: ").capitalize()
            while validar_nombre_apellido(apellido_determinado) == False:
                apellido_determinado = input("Ingrese nuevamente el apellido a buscar: ").capitalize()
            empleado_apellido = []
            formato = {
                "empleado": []
            }
            empleado_apellido.append(formato)
            empleado_apellido[0]["empleado"] = filter(lambda empleado : empleado["apellido"] == apellido_determinado,lista[0]["empleados"])
            print("*"*30, "\n - LISTA DE EMPLEADOS X APELLIDO DETERMINADO - ")
            mostrar_empleados(empleado_apellido, "empleado", "False")
# ------------------------------------------------------------------------------------ #
def modificar(lista: list[dict], id_persona: int)->None:
    mensaje = ""
    for empleado in lista[0]["empleados"]:
        if id_persona == empleado["id"]:
            continuar = True
            while continuar:
                mostrar_menu("submenu")
                opcion = opciones_menu("numeros")
                match opcion:
                    case 1:
                        nombre_nuevo = input("Ingrese el nuevo nombre: ")
                        while validar_nombre_apellido(nombre_nuevo) == False:
                            nombre_nuevo = input("Ingrese nuevamente el nuevo nombre: ")
                        empleado["nombre"] = nombre_nuevo
                        mensaje += "[+] Se modifico el Nombre correctamente\n"
                    case 2:
                        apellido_nuevo = input("Ingrese el nuevo apellido: ")
                        while validar_nombre_apellido(apellido_nuevo) == False:
                            apellido_nuevo = input("Ingrese nuevamente el nuevo apellido: ")
                        empleado["apellido"] = apellido_nuevo
                        mensaje += "[+] Se modifico el Apellido correctamente\n"
                    case 3:
                        puesto_nuevo = input("Ingrese el nuevo puesto: ")
                        while validar_puesto(puesto_nuevo) == False:
                            puesto_nuevo = input("Ingrese nuevamente el nuevo puesto: ")
                        empleado["puesto"] = puesto_nuevo
                        mensaje += "[+] Se modifico el Puesto correctamente\n"
                    case 4:
                        salario_nuevo = input("Ingrese el nuevo salario: ")
                        while validar_salario(salario_nuevo) == False:
                            salario_nuevo = input("Ingrese nuevamente el nuevo salario: ")
                        empleado["salario"] = salario_nuevo
                        mensaje += "[+] Se modifico el Salario correctamente\n"
                    case _:
                        print("INGRESE UNA OPCION VALIDA")
                
                continuar_modificando = input("Desea continuar modificando? si/no: ")
                if continuar_modificando == "no":
                    continuar = False

    return mensaje
# ------------------------------------------------------------------------------------ #
def mostrar_empleados(lista: list[dict],clave: str,guardar: str)->None:
    print("*"*30)
    for empleado in lista[0][clave]:
        print(f"""- ID: {empleado['id']}
- Nombre: {empleado['nombre']}
- Apellido: {empleado['apellido']}
- Puesto: {empleado['puesto']}
- Salario: {empleado['salario']}
""")
        print("*"*30)

    if guardar == "True":
        with open("Clase15\Practica_ABM_Archivos\empleados.json", "w", encoding="UTF-8") as archivo:
            json.dump(lista[0], archivo, indent=4, ensure_ascii=False)
        
        with open("Clase15\Practica_ABM_Archivos\empleados.csv", "w", encoding="UTF-8") as archivo:
            archivo.write("ID,Nombre,Apellido,Puesto,Salario\n")
            for empleado in lista[0]["empleados"]:
                identidad = empleado["id"]
                nombre = empleado["nombre"]
                apellido = empleado["apellido"]
                puesto = empleado["puesto"]
                salario = empleado["salario"]
                archivo.write(f"{identidad},{nombre},{apellido},{puesto},{salario}\n")
# ------------------------------------------------------------------------------------ #
def eliminar(lista: list, id_persona: int)->str:
    mensaje = "Esa ID no existe"
    for empleado in lista[0]['empleados']:
        if id_persona == empleado["id"]:
            lista[0]['empleados'].pop(id_persona - 1)
            mensaje = f"El empleado con la ID {id_persona} fue eliminado"
            break
    
    return mensaje
# ------------------------------------------------------------------------------------ #
def mostrar_gerentes(lista: list):
    lista_gerentes = []
    formato = {
        "gerentes": []
    }
    lista_gerentes.append(formato)
    lista_gerentes[0]["gerentes"] += filter(lambda empleados : empleados["puesto"] == "Gerente", lista[0]["empleados"])

    print("*"*30, "\n - LISTA DE GERENTES - ")
    mostrar_empleados(lista_gerentes, "gerentes", "False")
    
    with open("Clase15\Practica_ABM_Archivos\gerentes.json", "w", encoding="UTF-8") as archivo:
        json.dump(lista_gerentes[0], archivo, indent=4, ensure_ascii=False)
    
    with open("Clase15\Practica_ABM_Archivos\gerentes.csv", "w", encoding="UTF-8") as archivo:
        archivo.write("ID,Nombre,Apellido,Puesto,Salario\n")
        for persona in lista_gerentes[0]["gerentes"]:
            identidad = persona["id"]
            nombre = persona["nombre"]
            apellido = persona["apellido"]
            puesto = persona["puesto"]
            salario = persona["salario"]

            archivo.write(f"{identidad},{nombre},{apellido},{puesto},{salario}\n")
# ------------------------------------------------------------------------------------ #
def empleados_analistas(lista: list):
    lista_analistas = []
    formato = {
        "analistas": []
    }
    lista_analistas.append(formato)
    lista_analistas[0]["analistas"] += filter(lambda empleados : empleados["puesto"] == "Analista" and empleados["salario"] > 500000, lista[0]["empleados"])

    print("*"*30,"\n - LISTA DE ANALISTAS (SUELDO > 500.000)")
    mostrar_empleados(lista_analistas, "analistas", "False")
# ------------------------------------------------------------------------------------ #
def salario_promedio(lista: list)->str:
    suma = reduce(lambda acumulador, sueldo : acumulador + sueldo["salario"], lista[0]["empleados"],0)
    longitud_lista = len(lista[0]["empleados"])

    promedio = suma / longitud_lista
    mensaje = f"El salario promedio es {promedio}"

    with open("Clase15\Practica_ABM_Archivos\salario_promedio.txt", "w") as archivo:
        archivo.write(mensaje)

    return mensaje
# ------------------------------------------------------------------------------------ #
def ordenar_empleados(lista: list):
    mostrar_menu("ascendente_descendente")
    opcion_asc_des = input("Ingrese una de las opciones: ").lower()
    while opcion_asc_des != "ascendente" and opcion_asc_des != "descendente":
        opcion_asc_des = input("Ingrese nuevamente una de las opciones: ").lower()
    
    mostrar_menu("ordernar_listado")
    opciones = opciones_menu("numeros")

    match opciones:
        case 1:
            bubble_sort(lista, "empleados", "nombre", opcion_asc_des)
            print("*"*30, f"\n - EMPLEADOS ORDENADOS X NOMBRE ({opcion_asc_des})")
            mostrar_empleados(lista, "empleados", "False")
        case 2:
            bubble_sort(lista, "empleados", "apellido", opcion_asc_des)
            print("*"*30, f"\n - EMPLEADOS ORDENADOS X APELLIDO ({opcion_asc_des})")
            mostrar_empleados(lista, "empleados", "False")
        case 3:
            bubble_sort(lista, "empleados", "salario", opcion_asc_des)
            print("*"*30, f"\n - EMPLEADOS ORDENADOS X SALARIO ({opcion_asc_des})")
            mostrar_empleados(lista, "empleados", "False")
# ------------------------------------------------------------------------------------ #