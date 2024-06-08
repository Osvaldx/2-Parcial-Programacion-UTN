# ----------------------------------------------------- #
def validar_nombre_apellido(cadena: str)->bool:
    """Esta función recibe como parámetros una cadena de tipo string y se encarga de validar que no exceda del límite y qué sea sólo caracteres del abecedario

    Argumentos:
        cadena (str): Una string ya predefinida

    Retorna:
        bool: Una booleano true o false
    """
    retorno = False
    longitud_cadena = len(cadena)

    if longitud_cadena < 16 and cadena.isalpha() == True:
        retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_puesto(cadena: str)->bool:
    """Esta función recibe como parámetro una cadena de formato string y se encarga de validar que esa cadena se encuentra dentro de la lista de puestos

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        bool: Una booleano true o false
    """
    retorno = False
    puestos = ["Gerente","Supervisor", "Analista", "Encargado", "Asistente"]

    for i in range(len(puestos)):
        if cadena.capitalize() == puestos[i]:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_salario(cadena: str)->bool:
    """Esta función recibe como parámetros una cadena de formato string y se encarga de validar que la cadena tenga sólo números y sea superior al sueldo mínimo  establecido

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        bool: Una booleano true o false
    """
    retorno = False
    if cadena.isnumeric() == True:
        cadena = int(cadena)
        if cadena > 234315:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_id(numero: str)->bool:
    """Esta función recibe como parámetros un número en formato string y se encarga de validar qué solo tengan números y parcea una vez validada

    Argumentos:
        cadena (str): Una cadena ya predefinida

    Retorna:
        bool: Una booleano true o false
    """
    retorno = False
    if numero.isnumeric() == True:
        numero = int(numero)
        if numero > 0:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def ordenar_lista(lista: list)->None:
    """Esta función recibe como parámetros una lista y se encarga de ordenar de menor a mayor la id de cada empleado

    Argumentos:
        cadena (str): Una cadena ya predefinida
    """
    for i in range(len(lista)):
        intercambio = False
        for j in range(len(lista) -1 -i):
            if lista[j]["id"] > lista[j+1]["id"]:
                auxiliar = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = auxiliar
                intercambio = True
        if intercambio == False:
            break
# ----------------------------------------------------- #