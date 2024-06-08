# ----------------------------------------------------- #
def validar_nombre_apellido(cadena: str)->bool:
    retorno = False
    longitud_cadena = len(cadena)

    if longitud_cadena < 16 and cadena.isalpha() == True:
        retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_puesto(cadena: str)->bool:
    retorno = False
    puestos = ["Gerente","Supervisor", "Analista", "Encargado", "Asistente"]

    for i in range(len(puestos)):
        if cadena.capitalize() == puestos[i]:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_salario(cadena: str)->bool:
    retorno = False
    if cadena.isnumeric() == True:
        cadena = int(cadena)
        if cadena > 234315:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def validar_id(numero: str)->bool:
    retorno = False
    if numero.isnumeric() == True:
        numero = int(numero)
        if numero > 0:
            retorno = True
    
    return retorno
# ----------------------------------------------------- #
def bubble_sort(lista: list, clave: str, clave_ordenar: str, criterio: str)->None:
    lista_empleados = lista[0][clave]

    for i in range(len(lista_empleados)):
        intercambio = False
        for j in range(len(lista_empleados) -1 -i):
            if criterio == "ascendente":
                if lista_empleados[j][clave_ordenar] > lista_empleados[j+1][clave_ordenar]:
                    auxiliar = lista_empleados[j]
                    lista_empleados[j] = lista_empleados[j+1]
                    lista_empleados[j+1] = auxiliar
                    intercambio = True
            elif criterio == "descendente":
                if lista_empleados[j][clave_ordenar] < lista_empleados[j+1][clave_ordenar]:
                    auxiliar = lista_empleados[j]
                    lista_empleados[j] = lista_empleados[j+1]
                    lista_empleados[j+1] = auxiliar
                    intercambio = True
        if (intercambio == False):
            break
# ----------------------------------------------------- #