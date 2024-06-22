import json

def validar_nombre(path,nombre_recibido):
    retorno = False
    with open(path, "r", encoding="UTF-8") as archivo:
        try:                                            # Se espera que pase esto si el archivo json se cargo correctamente
            lista_json = json.load(archivo)
            lista_jugadores = list(map(lambda jugador : jugador["nombre"],lista_json["Players"]))

            if nombre_recibido not in lista_jugadores and nombre_recibido.isalnum():
                retorno = True
        except:                                         # En caso de que rompa se espera que suceda esto
            if nombre_recibido.isalnum() == True:
                retorno = True

    return retorno