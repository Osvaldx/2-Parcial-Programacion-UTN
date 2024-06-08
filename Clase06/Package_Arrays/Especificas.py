
# ------------------------------------------------------------- #
def determinar_positividad_negatividad(numero: int)-> bool:
    """Esta funcion recibe como parametros un numero y devuelve si el numero es positivo o negativo con un booleano

    Argumentos:
        numero (int): El numero que se manda a comprobar su positividad o negatividad

    Retorna:
        bool: Retorna un booleano porque es True o False
    """
    positivo = False
    if numero > 0:
        positivo = True
    else:
        positivo = False
    
    return positivo
# ------------------------------------------------------------- #

# ------------------------------------------------------------- #
def determinar_par_impar(numero: int)-> bool:
    """Esta funcion recibe como parametros un numero y devuelve si el numero es par o impar con un booleano

    Argumentos:
        numero (int): El numero que se manda a comprobar si es par o impar

    Retorna:
        bool: Retorna un booleano porque es True o False
    """
    par = False
    if numero % 2 == 0:
        par = True
    else:
        par = False

    return par
# ------------------------------------------------------------- #
