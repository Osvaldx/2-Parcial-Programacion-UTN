######################################################################################################

def validate_number(numero:int | float, minimo:int | float, maximo:int | float) -> bool:
    """esta funcion se encarga de validar si el numero se encuentra en el rango permitido

    Args:
        numero (int | float): es el numero que ingreso el usuario
        minimo (int | float): el numero minimo del rango que se permite
        maximo (int | float): el numero maximo del rango que se permite

    Returns:
        bool: se espera una respuesta booleana de True o False
    """
    valido = False
    if numero > minimo and numero < maximo:
        valido = True

    return valido

######################################################################################################

def validate_length(palabra:str, longitud:int) -> bool:
    """Esta funcion valida si la palabra tiene la longitud permitida

    Args:
        palabra (str): es la palabra que el usuario ingreso
        longitud (int): la longitud establecida para las palabras

    Returns:
        bool: se espera una respuesta booleana de True o False
    """
    valido = False
    cantidad_palabra = len(palabra)

    if cantidad_palabra > longitud:
        valido = True
    
    return valido

######################################################################################################