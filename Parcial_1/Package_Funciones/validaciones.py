# --------------------------------------- #
def validacion_titulo(lista: list, clave: str)->str:
    """Esta funcion recibe como parametros una lista y una clave en formato string y se encarga de validar
    que el titulo en base a ciertas caracteristicas

    Argumentos:
        lista (list): Una lista ya predefinida
        clave (str): Una clave en string

    Retorna:
        str: Una string que seria el titulo
    """
    while True:
        titulo = input("Ingrese el titulo de la pelicula: ")
        longitud_titulo = len(titulo)
        bandera_encontrada = False

        while longitud_titulo > 30 or titulo == "":
            print(f"[!] EL TITULO NO PUEDE SER TAN LARGO O ESTAR VACIO")
            titulo = input("Ingrese nuevamente el titulo de la pelicula: ")
            longitud_titulo = len(titulo)
        
        if clave == "crear":
            for i in range(len(lista)):
                if titulo.upper() == lista[i]["titulo"].upper():
                    print("[!] EL TITULO INGRESADO YA EXISTE!")
                    bandera_encontrada = True
        
        if bandera_encontrada == False:
            return titulo
# --------------------------------------- #
def validacion_genero(ingreso_genero: str)->str:
    """Esta función valida que el género ingresado esté en una lista predefinida de géneros

    Argumentos:
        ingreso_genero (str): El género ingresado por el usuario

    Retorna:
        str: El género validado
    """
    lista_generos = ["Acción", "Aventura", "Animación", "Biográfico", "Comedia", "Comedia romántica","Comedia dramática", "Crimen",
"Documental", "Drama", "Fantasía", "Histórico","Infantil", "Musical", "Misterio", "Policíaco", "Romance", "Ciencia ficción",
"Suspenso", "Terror", "Western", "Bélico", "Deportivo", "Noir", "Experimental","Familiar", "Superhéroes", "Espionaje",
"Artes marciales", "Fantástico","Catástrofe", "Melodrama", "Erótico", "Cine independiente", "Zombies","Vampiros", "Cyberpunk",
"Steampunk", "Distopía", "Utopía", "Road Movie","Docuficción", "Mockumentary", "Gótico", "Slasher", "Adolescente", "Culto","Maravilloso"]
    
    while True:
        for genero in lista_generos:
            if ingreso_genero == genero:
                return ingreso_genero

        print("[!] EL GENERO INGRESADO NO ESTA DISPONIBLE")
        ingreso_genero = input("Ingrese nuevamente un genero: ")
# --------------------------------------- #
def validacion_anio(anio: str)->int:
    """Esta función valida que el año ingresado sea un número y esté dentro del rango válido (1888-2024)

    Argumentos:
        anio (str): El año ingresado por el usuario en formato string

    Retorna:
        int: El año validado
    """
    while anio.isnumeric() == False or int(anio) < 1888 or int(anio) > 2024:
        print("[!] EL AÑO DEBE SER MAYOR A 1888 Y SOLO DEBE SER NUMEROS")
        anio = input("Ingrese nuevamente el año de lanzamiento: ")
    
    anio = int(anio)
    return anio
# --------------------------------------- #
def validacion_duracion(duracion: str)->int:
    """Esta función valida que la duración ingresada sea un número positivo

    Argumentos:
        duracion (str): La duración ingresada por el usuario en formato string

    Retorna:
        int: La duración validada en minutos
    """
    while duracion.isnumeric() == False or int(duracion) <= 0:
        print(f"[!] LA DURACION NO PUEDE SER {duracion}")
        duracion = input("Ingrese nuevamente la duracion de la pelicula (en minutos): ")
    
    duracion = int(duracion)
    return duracion
# --------------------------------------- #
def validacion_atp(atp: str)->bool:
    """Esta función valida que el valor ingresado para la aptitud de todo público sea "Si" o "No"

    Argumentos:
        atp (str): El valor ingresado por el usuario ("Si" o "No")

    Retorna:
        bool: True si es apta para todo público, False en caso contrario
    """
    while atp != "Si" and atp != "No":
        print(f"[!] INGRESE UNA OPCION CORRECTA")
        atp = input("La pelicula es apta para todo publico (Si/No): ").capitalize()
    
    if atp == "Si":
        retorno = True
    elif atp == "No":
        retorno = False
    
    return retorno
# --------------------------------------- #
def validacion_plataformas()->str:
    """Esta función valida las plataformas ingresadas por el usuario, asegurándose de que no contengan 
    números y no excedan los 20 caracteres

    Retorna:
        str: Una lista de las plataformas validadas
    """
    lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
    lista_plataformas = []
    bandera = True

    while bandera == True:
        plataforma_validada = False
        while plataforma_validada == False:
            plataforma = input("Ingrese las plataforma disponible de la pelicula: ").capitalize()

            if plataforma not in lista_plataformas:
                conteo = 0
                for numero in lista_numeros:
                    conteo += plataforma.count(numero)
                
                longitud_palabra = len(plataforma)
                if conteo == 0 and longitud_palabra <= 20 and plataforma != "":
                    lista_plataformas.append(plataforma)
                    plataforma_validada = True
                else:
                    print("[!] LA PLATAFORMA NO PUEDE TENER NUMEROS O PASAR DE LOS 20 CARACTERES")
            else:
                print("[!] ESA PLATAFORMA YA ESTA AGREGADA A ESA PELICULA")
        
        if plataforma_validada == True:
            continuar = input("Desea agregar otra plataforma? Si/No: ").capitalize()
            while continuar != "Si" and continuar != "No":
                print("[!] INGRESE UNA OPCION CORRECTA!")
                continuar = input("Desea agregar otra plataforma? Si/No: ").capitalize()
            
            if continuar == "No":
                bandera = False
    
    return lista_plataformas
# --------------------------------------- #
def validacion_input(opcion: str)->bool | int:
    """Esta función valida que la opción ingresada sea un número

    Argumentos:
        opcion (str): La opción ingresada por el usuario en formato string

    Retorna:
        bool | int: Retorna el número validado o False si la validación falla
    """
    retorno = False

    if opcion.isnumeric() == True:
        retorno = int(opcion)
    
    return retorno
# --------------------------------------- #
def validacion_asc_des(opcion: str)->str:
    """Esta función valida que la opción ingresada sea "ascendente" o "descendente"

    Argumentos:
        opcion (str): La opción ingresada por el usuario en formato string

    Retorna:
        str: La opción validada
    """
    while opcion != "ascendente" and opcion != "descendente":
        print("[!] LA OPCION INGRESADA NO ERA VALIDA")
        opcion = input("Ingrese nuevamente una de las opciones: ").lower()
    
    return opcion
# --------------------------------------- #