#0.0
def stark_normalizar_datos(lista: list)->None:
    """Esta funcion recibe como parametros una lista y se encarga de parcear los datos de la lista

    Argumentos:
        lista (list): Recibe una lista ya predefinida

    Retorno:
        None: no retorna nada
    """
    # ACA VERIFICO SI EL DATO ESTA PARSEADO O NO
    retorno = False
    if lista != []:
        for i in range(len(lista)):
            if lista[i] == {}:
                pass
            dato_modificado = False
            tipo_de_dato = type(lista[i]["fuerza"])
            if tipo_de_dato != int:
                lista[i]["fuerza"] = int(lista[i]["fuerza"])
                dato_modificado = True

            tipo_de_dato = type(lista[i]["altura"])
            if tipo_de_dato != float:
                lista[i]["altura"] = float(lista[i]["altura"])
                dato_modificado = True

            tipo_de_dato = type(lista[i]["peso"])
            if tipo_de_dato != float:
                lista[i]["peso"] = float(lista[i]["peso"])
                dato_modificado = True
        # ACA VOY A VERIFICAR
        if dato_modificado == True:
            print("DATOS NORMALIZADOS")
            retorno = True
        else:
            print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")

    return retorno
#1.1  
def obtener_datos(diccionario: dict, clave: str)->str | None:
    """Esta funcion recibe como parametros un diccionario de tipo dict y una clave tipo str, se encarga de obtener el valor del dict y la key

    Argumentos:
        diccionario (dict): Un diccionario ya predefinido
        clave (str): Una clave ya predefinida

    Retorna:
        str | None: retorna tanto una string como nada
    """
    retorno = False
    if diccionario != {}:
        valor_clave = diccionario.get(clave)
        if valor_clave != None:
            retorno = valor_clave
    
    return retorno
#1.2
def obtener_nombre(diccionario: dict)->str:
    """Esta funcion recibe como parametros un diccionario y se encarga de buscar en ese diccionario el valor de la key nombre

    Argumentos:
        diccionario (dict): Un diccionario ya predefinido

    Retorno:
        str: Retorna una string que es un mensaje
    """
    retorno = False
    if diccionario != {}:
        valor_clave = obtener_datos(diccionario, "nombre")
        if valor_clave != None:
            mensaje = f"Nombre: {valor_clave}"
            retorno = mensaje
        
    return retorno
#2
def obtener_nombre_y_dato(diccionario: dict, key:str)-> str:
    """Esta funcion recibe como parametros un diccionario y una key, y se encarga de llamar a otras funciones para obtener el nombre y dato que se encuentra en el diccionario

    Argumentos:
        diccionario (dict): Un diccionario ya predefinido
        key (str): Una key ya predefinida

    Retorna:
        str: Una string que seria un mensaje
    """
    retorno = False
    if diccionario != {}:
        dato = obtener_datos(diccionario, key)
        nombre = obtener_nombre(diccionario)

        formato = f"- {nombre} | {key}: {dato}"

        if diccionario.get(key) != False or nombre != False:
            retorno = formato
    
    return retorno
#3.1
def obtener_maximo(lista: list, key: str)-> int | float:
    """Recibe como parametros una lista y una key de tipo str, y se encarga de recorrer la lista y encontrar el valor maximo de la key ingresada

    Argumentos:
        lista (list): Una lista ya predefinida
        key (str): Una key ya predefinida

    Retorna:
        int | float: Retorna un entero o un float
    """
    retorno = False
    if lista != []:
        bandera = False
        for i in range(len(lista)):
            tipo_dato = type(lista[i][key])
            if tipo_dato == int or tipo_dato == float:
                if bandera == False or lista[i][key] > num_max:
                    num_max = lista[i][key]
                    bandera = True
        if bandera == True:
            retorno = num_max
    
    return retorno
#3.2
def obtener_minimo(lista: list, key: str)-> int | float:
    """_summary_

    Args:
        lista (list): _description_
        key (str): _description_

    Returns:
        int | float: _description_
    """
    retorno = False
    if lista != []:
        bandera = False
        for i in range(len(lista)):
            tipo_dato = type(lista[i][key])
            if tipo_dato == int or tipo_dato == float:
                if bandera == False or lista[i][key] < num_min:
                    num_min = lista[i][key]
                    bandera = True
        if bandera == True:
            retorno = num_min
    
    return retorno
#3.3
def obtener_dato_cantidad(lista: list, dato: int | float | str, key: str)-> list:
    """Esta funcion recibe como parametros una lista, un dato de cualquier tipo y una key de tipo str, se encarga de guardar en una lista todos los heroes con ese tipo de key y dato igual

    Argumentos:
        lista (list): Una lista ya predefinida
        dato (int | float | str): Una dato ya predefinido
        key (str): Una key ya predefinida

    Retorna:
        list: Una lista con todos los heroes
    """
    lista_heroes = []
    for i in range(len(lista)):
        if lista[i].get(key) == dato:
            lista_heroes.append(lista[i])
    return lista_heroes
#3.4
def stark_imprimir_nombre_heroes(lista: list)-> None:
    """Recibe como parametros una lista y se encarga de recorrer la lista para poder imprimir los nombres de los heroes

    Argumentos:
        lista (list): Una lista ya predefinida
    """
    if lista != []:
        print("-"*30)
        for i in range(len(lista)):
            print(obtener_nombre(lista[i]))
    print("-"*30)
#3.4 (agregado)
def stark_imprimir_heroes(lista: list)-> None:
    """Recibe como parametros una lista y se encarga de imprimir los diccionarios que se encuentran adentro de la lista

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorno:
        None: No retorna nada
    """
    if lista != []:
        for i in range(len(lista)):
            diccionario = lista[i]
            print("-"*30)
            for j in diccionario:
                print(f"- {j}: {diccionario[j]}")
        print("-"*30)
    else:
        return False
#4.1
def sumar_dato_heroe(lista: list, key: str, )-> int | float:
    """Recibe como parametros una lista y una key de tipo string, esta funcion se encarga de sumar todos los datos de los diccionarios de la lista con su respectiva key

    Args:
        lista (list): _description_
        key (str): _description_

    Returns:
        int | float: _description_
    """
    suma_datos = 0
    for i in range(len(lista)):
        if lista[i] != {}:
            suma_datos += lista[i][key]
    return suma_datos
#4.2
def dividir(dividendo: int | float, divisor: int | float)-> int | float:
    """Esta función recibe como parámetros un dividiendo que es un tipo de dato entero o float y un divisor que es un tipo de dato entero o float y se encarga de hacer una división con los parámetros recibidos

    Argumentos:
        dividendo (int | float): Un numero entero o float ya predefinido
        divisor (int | float): Un numero entero o float ya predefinido

    Retorna:
        int | float: Un entero o float
    """
    retorno = False
    if divisor != 0:
        division = dividendo / divisor
        retorno = division
    
    return retorno
#4.3
def calcular_promedio(lista: list, key: str)-> int | float:
    """Esta función recibe como parámetros una lista de tipo list y una key de tipo string y se encarga de calcular el promedio con los parámetros recibidos utilizando otras funciones

    Argumentos:
        lista (list): Recibe una lista ya predefinida
        key (str): Recibe una key ya predefinida

    Retorno:
        int | float: Retorna una entero o float
    """
    suma_dato_total = sumar_dato_heroe(lista, key)
    longitud_lista = len(lista)
    promedio = dividir(suma_dato_total, longitud_lista)
    
    return promedio
#4.4
def mostrar_promedio_dato(lista: list, key: str)->bool:
    """Esta función recibe como parámetros una lista y una que hay de tipo string y se encarga de validar los tipos de datos de que hay en esa lista con los diccionarios con su respectiva key qué es un entero float

    Argumentos:
        lista (list): Una lista ya predefinida
        key (str): Una key ya predefinida

    Retorno:
        bool: Retorna una booleano True o False
    """
    retorno = False
    if lista != []:
        for i in range(len(lista)):
            tipo_dato = type(lista[i].get(key))
            if tipo_dato == int or tipo_dato == float:
                retorno = True
    return retorno
#5.1
def imprimir_menu()->None:
    # Esta funcion solo printea el menu de opciones
    print(f"""
        1) NORMALIZAR DATOS
        2) NOMBRES DE LOS SUPERHEROES [NB]
        3) SUPERHEROE MAS ALTA [F]
        4) SUPERHEROE MAS ALTO [M]
        5) SUPERHEROE MAS DEBIL [M]
        6) SUPERHEROE MAS DEBIL DEL [NB]
        7) PROMEDIO DE FUERZA DE HEROES [NB]
        8) SUPERHEROES COLOR DE OJOS
        9) SUPERHEROES DE COLOR DE PELOS
        10) SUPERHEROES AGRUPADOS POR COLOR DE OJOS
        11) SUPERHEROES AGRUPADOS POR TIPO DE INTELIGENCIA\n
        12) SALIR""")
#5.2
def validar_entero(numero: str)->bool:
    """Esta función recibe como parámetros un número en formato string y se encarga de validar si es un número o no

    Argumentos:
        numero (str): Un numero ya predefinido

    Returns:
        bool: Retorna un booleano True o False
    """
    retorno = False
    if numero.isnumeric() == True:
        retorno = True
    return retorno
#5.3
def stark_menu_principal()->int:
    """Esta función se encarga de llamar a la función de imprimir menú y le pide al usuario que ingrese un input y se encarga de validar de que sea una de las opciones correspondientes el menú

    Retorna:
        int: Un numero entero
    """
    retorno = False
    imprimir_menu()
    numero_opciones = input("Ingrese una de las opciones: ")
    validacion = validar_entero(numero_opciones)
    
    if validacion == True:
        numero_opciones = int(numero_opciones)
        retorno = numero_opciones
    
    return retorno
# opcion agregada
def obtener_lista_valores(lista: list, key: str)->list:
    """Esta función recibe como parámetro una lista y una key de formato string y se encarga de recorrer la lista Y en cada índice utilizarla que ingresada por parámetro para poder capturar el valor y guardarlo en una lista y después setearlo

    Argumentos:
        lista (list): Una lista ya predefinida
        key (str): Una key ya predefinida

    Retorna:
        list: Retorna una lista con todos los valores
    """
    lista_valores = []
    for i in range(len(lista)):
        lista_valores.append(obtener_datos(lista[i], key))

    lista_valores_set = set(lista_valores)
    return lista_valores_set