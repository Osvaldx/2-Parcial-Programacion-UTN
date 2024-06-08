from .funciones_especificas import *

def opciones_menu()->int:
    """Esta funcion se encarga de validar la opcion ingresada por el usuario y parcearlo a entero

    Retorna:
        int: Un numero entero
    """
    opcion = input("Ingrese una de las opciones: ")
    while not opcion.isnumeric():
        opcion = input("Ingrese nuevamente una de las opciones: ")
    opcion = int(opcion)
    
    return opcion

def crear_usuario()->dict:
    """Esta función se encarga de pedirle al usuario datos a completar para crear un usuario en la lista de empleados en formato diccionario

    Retorno:
        dict: Un diccionario con los datos ingresados
    """
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

def dar_de_alta(lista: list, diccionario: dict, identificacion: int)->None:
    """Esta función recibe como parámetros una lista y un diccionario de tipo dict eh un número entero representado como id Se encarga de colocarle id de correspondiente a cada nuevo empleado

    Argumentos:
        lista (list): Una lista ya predefinida
        diccionario (dict): Un diccionario ya predefinido
        identificacion (int): Un numero ya predefinido
    """
    diccionario["id"] = identificacion
    lista.append(diccionario)
    # if identificacion == 1:
    #     diccionario["id"] = identificacion
    #     lista.append(diccionario)
    # else:
    #     longitud_lista = len(lista)
    #     if longitud_lista < lista[longitud_lista - 1]["id"]:
    #         diccionario["id"] = longitud_lista
    #         lista.append(diccionario)
    #     else:
    #         diccionario["id"] = identificacion
    #         lista.append(diccionario)

def mostrar_menu(clave: str):
    # Esta funcion se encarga de imprimir el menu o submenu
    if clave == "principal":
        print("""
            - [1] Dar de alta.
            - [2] Modificar.
            - [3] Eliminar.
            - [4] Mostrar todos.
            - [5] Mostrar gerentes.
            - [6] Calcular salario promedio.
            - [7] SALIR
            """)
    else:
        print("""Que desea modificar:
            - [1] Nombre
            - [2] Apellido
            - [3] Puesto
            - [4] Salario
            """)

def modificar(lista: list[dict], id_persona: int)->None:
    """Esta función recibe como parámetros una lista Que tiene diccionarios y un número representado como idea de persona se encarga de comparar y actualizar datos qué hay en los diccionarios de esta lista

    Argumentos:
        lista (list[dict]): Una lista ya predefinida
        id_persona (int): Un numero ya predefinido

    Retorno:
        None: No retorna nada
    """
    mensaje = ""
    for i in range(len(lista)):
        if id_persona == lista[i]["id"]:
            continuar = True
            while continuar:
                mostrar_menu("submenu")
                opcion = opciones_menu()
                match opcion:
                    case 1:
                        nombre_nuevo = input("Ingrese el nuevo nombre: ")
                        while validar_nombre_apellido(nombre_nuevo) == False:
                            nombre_nuevo = input("Ingrese nuevamente el nuevo nombre: ")
                        lista[i]["nombre"] = nombre_nuevo
                        mensaje += "[+] Se modifico el Nombre correctamente\n"
                    case 2:
                        apellido_nuevo = input("Ingrese el nuevo apellido: ")
                        while validar_nombre_apellido(apellido_nuevo) == False:
                            apellido_nuevo = input("Ingrese nuevamente el nuevo apellido: ")
                        lista[i]["apellido"] = apellido_nuevo
                        mensaje += "[+] Se modifico el Apellido correctamente\n"
                    case 3:
                        puesto_nuevo = input("Ingrese el nuevo puesto: ")
                        while validar_puesto(puesto_nuevo) == False:
                            puesto_nuevo = input("Ingrese nuevamente el nuevo puesto: ")
                        lista[i]["puesto"] = puesto_nuevo
                        mensaje += "[+] Se modifico el Puesto correctamente\n"
                    case 4:
                        salario_nuevo = input("Ingrese el nuevo salario: ")
                        while validar_salario(salario_nuevo) == False:
                            salario_nuevo = input("Ingrese nuevamente el nuevo salario: ")
                        lista[i]["salario"] = salario_nuevo
                        mensaje += "[+] Se modifico el Salario correctamente\n"
                    case _:
                        print("INGRESE UNA OPCION VALIDA")
                
                continuar_modificando = input("Desea continuar modificando? si/no: ")
                if continuar_modificando == "no":
                    continuar = False

    return mensaje

def mostrar_empleados(lista: list[dict])->None:
    """ Esta función recibe como parámetros una lista con diccionarios y se encarga de mostrar y darle formato a cada diccionario"""
    print("*"*30)
    for i in range(len(lista)):
        print(f"""
- ID: {lista[i]["id"]}
- Nombre: {lista[i]["nombre"]}
- Apellido: {lista[i]["apellido"]}
- Puesto: {lista[i]["puesto"]}
- Salario: {lista[i]["salario"]}
""")
        print("*"*30)

def eliminar(lista: list, id_persona: int):
    """Esta función recibe como parámetros una lista y un número representado como ide de persona y se encarga de eliminarlo con un método de lista

    Argumentos:
        lista (list): Una lista ya predefinida
        id_persona (int): Un numero ya predefinido
    """
    lista.pop(id_persona - 1)

def mostrar_gerentes(lista: list):
    """Esta función recibe como parámetros una lista y se encarga de separarlos y agrupar a solo los gerentes de esa lista para después mostrarlos en pantalla

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    lista_gerentes = []
    for i in range(len(lista)):
        if lista[i]["puesto"] == "Gerente":
            lista_gerentes.append(lista[i])
    
    mostrar_empleados(lista_gerentes)

def salario_promedio(lista: list)->str:
    """Esta función recibe como parámetros una lista y se encarga de hacer una suma de todo los salarios que se encuentran adentro de esta para poder calcular el promedio

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        str: Retorna una string que seria el mensaje
    """
    suma = 0
    longitud_lista = len(lista)
    for i in range(len(lista)):
        suma += lista[i]["salario"]
    
    promedio = suma / longitud_lista
    mensaje = f"El salario promedio es {promedio}"

    return mensaje