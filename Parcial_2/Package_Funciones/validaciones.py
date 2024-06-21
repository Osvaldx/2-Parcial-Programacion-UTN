def validar_nombre(nombre_ingresado):
    retorno = True
    while (nombre_ingresado.isalnum() == False) or (nombre_ingresado == ""):
        retorno = False
        break
    
    return retorno