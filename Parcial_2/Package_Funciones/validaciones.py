import json

def validar_nombre(path,nombre_recibido)->bool:
    """Esta función recibe comó parametró una ruta que lo llama path y el nombre_recibido, se encarga
    de validar que el nombre no se encuentra ya cargado, y valida que no tenga caracteres especiales

    Argumentos:
        path (_type_): Una ruta de un archivo ya predefinido
        nombre_recibido (_type_): El nombre que introduce el usuario ya predefinido

    Retorno:
        bool: retorna bool, true o false
    """
    retorno = False
    with open(path, "r", encoding="UTF-8") as archivo:
        try:                                            # Se espera que pase esto si el archivo json se cargo correctamente
            lista_json = json.load(archivo)
            lista_jugadores = list(map(lambda jugador : jugador["nombre"],lista_json["Players"]))

            if nombre_recibido.capitalize() not in lista_jugadores and nombre_recibido.isalnum():
                retorno = True
        except:                                         # En caso de que rompa se espera que suceda esto
            if nombre_recibido.isalnum() == True:
                retorno = True

    return retorno