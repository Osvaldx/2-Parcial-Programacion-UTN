# ------------------------------------------------------------------------------------ #
def sacar_peliculas_repetidas(lista: list)->list:
    """Esta funcion recibe como parametros una lista y se encarga de sacar las peliculas
    repetidas

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorno:
        list: Una lista con las peliculas sin repetir
    """
    lista_titulos_vistos = []
    peliculas_sin_repetir = []

    for i in range(len(lista)):
        titulo = lista[i]["titulo"]
        if titulo not in lista_titulos_vistos:
            lista_titulos_vistos.append(titulo)
            peliculas_sin_repetir.append(lista[i])
        else:
            with open("Parcial_1/Package_Funciones/ids_eliminadas.txt", "a") as archivo:
                archivo.write(f"{lista[i]['id']}\n")
    
    return peliculas_sin_repetir
# ------------------------------------------------------------------------------------ #
def mostrar_menu(clave: str)->None:
    """Esta función recibe como parámetros una clave en formato string y lo único que se hace es mostrar el menú dependiendo la clave"""
    if clave == "menu_principal":
        print("""
            - [1] Dar de alta.
            - [2] Modificar.
            - [3] Eliminar.
            - [4] Mostrar peliculas.
            - [5] Ordenar peliculas.
            - [6] Buscar película por título.
            - [7] Calcular promedio.
            - [8] Calcular porcentaje.
            - [9] Mostrar por género.
            - [10] Salir.
            """)
    elif clave == "tipos_generos":
            print("""
------------------------------------------------- GENEROS DISPONIBLES -----------------------------------------------------
- Acción          - Comedia romántica   - Musical         - Ciencia ficción       - Western              - Noir
- Aventura        - Comedia dramática   - Misterio        - Suspenso              - Bélico               - Experimental
- Animación       - Crimen              - Policíaco       - Terror                - Deportivo            - Familiar
- Biográfico      - Documental          - Romance         - Catástrofe            - Superhéroes          - Espionaje
- Comedia         - Drama               - Fantasía        - Melodrama             - Artes marciales      - Fantástico
- Infantil        - Histórico           - Erótico         - Cine independiente    - Zombies              - Vampiros
- Cyberpunk       - Steampunk           - Distopía        - Utopía                - Road Movie           - Docuficción
- Mockumentary    - Gótico              - Slasher         - Adolescente           - Culto                - Maravilloso
---------------------------------------------------------------------------------------------------------------------------
""")
    elif clave == "modificar_menu":
        print("""
            - [1] Titulo.
            - [2] Genero.
            - [3] Año de lanzamiento.
            - [4] Duracion.
            - [5] ATP (Apto para publico).
            - [6] Plataformas.
            """)
    elif clave == "mostrar_pelis":
        print("""
            - [a] Todas las peliculas.
            - [b] De determinado género.
            - [c] De determinado año.
            - [d] Todas las ATP.
            - [e] Todas las No ATP.
            - [f] Mostrar por Plataforma.
            - [g] Salir.
            """)
    elif clave == "menu_ordenar_pelis":
        print("""
            - [a] Título.
            - [b] Género.
            - [c] Año de lanzamiento.
            - [d] Duración.
            - [e] Salir.
            """)
    elif clave == "ascendente_descendente":
        print("""De que manera desea ordenar las peliculas:
            - Ascendente
            - Descendente
            """)
    elif clave == "promedio_peliculas":
        print("""
            - [a] Año de lanzamiento.
            - [b] Duración de películas.
            - [c] Salir.
            """)
    elif clave == "porcentaje_peliculas":
        print("""
            - [a] Porcentaje por género.
            - [b] Porcentaje por ATP.
            - [c] Salir.
            """)
# ------------------------------------------------------------------------------------ #
def cargar_peliculas(lista: list)->None:
    """Esta función recibe como parámetros una lista y se encarga de abrir el archivo el cual van a estar las películas 
    para leerlas y darle un formato de diccionario y luego agregarlas a la lista

    Argumentos:
        lista (list): Una lista vacia

    Retorna:
        None: no retorna nada
    """

    with open("Parcial_1/Package_Funciones/peliculas.csv", "r", encoding="utf-8") as archivo:
        peliculas = archivo.readlines()

        for i in range(1, len(peliculas)):
            linea = peliculas[i]
            linea = linea.split(",")

            identidad = linea[0]
            identidad = int(identidad)
            titulo = linea[1]
            genero = linea[2]
            anio_lanzamiento = linea[3]
            anio_lanzamiento = int(anio_lanzamiento)
            duracion = linea[4]
            duracion = int(duracion)
            atp = linea[5]
            plataformas = linea[6]
            plataformas = plataformas.replace("\n", "")
            plataformas = plataformas.split("-")

            if atp == "Si":
                atp = True
            else:
                atp = False

            pelicula = {
                "id": identidad,
                "titulo": titulo,
                "genero": genero,
                "año_lanzamiento": anio_lanzamiento,
                "duracion": duracion,
                "atp": atp,
                "plataformas": plataformas,
            }

            lista.append(pelicula)
    
    if lista == []:
        print("[!] ERROR, El archivo esta vacio no se cargo nada.")
    else:
        print("[+] Datos cargados con exito!")
# ------------------------------------------------------------------------------------ #
def bubble_sort(lista: list, clave: str, criterio: str)->None:
    """Esta funcion recibe como parametros una lista, una clave y criterio en formatos string, se encarga
    de ordenar de menor a mayor comparando los elementos de lista uno al lado de otro, utiliza una clave
    para recibir por categoria a ordenar y un criterio para ordenarlo de ascendente o descendente

    Argumentos:
        lista (list): Una lista ya predefinida
        clave (str): Una string ya predefinida
        criterio (str): Una string ya predefinida
    
    Retorna:
        None: no retorna nada
    """
    for i in range(len(lista)):
        intercambio = False
        for j in range(len(lista) -1 -i):
            if criterio == "ascendente":
                if lista[j][clave] > lista[j+1][clave]:
                    auxiliar = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = auxiliar
                    intercambio = True

            elif criterio == "descendente":
                if lista[j][clave] < lista[j+1][clave]:
                    auxiliar = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = auxiliar
                    intercambio = True
        if (intercambio == False):
            break
# ------------------------------------------------------------------------------------ #
def sacar_id_maxima(lista: list)->int:
    """Esta función recibe como parámetros una lista Y se encarga de recorrerla para sacar el id máxima 
    de cada diccionario que se encuentra en la lista

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        int: retorna la id maxima
    """
    lista_copia = list(lista)
    bubble_sort(lista_copia, "id", "ascendente")

    bandera = False
    for i in range(len(lista_copia)):
        if bandera == False or lista_copia[i]["id"] > id_maxima:
            id_maxima = lista_copia[i]["id"]
        
    return id_maxima
# ------------------------------------------------------------------------------------ #
def mostrar_peliculas(lista: list)->None:
    """Esta funcion recibe como parametros una lista ya predefinida y se encarga de mostrar las peliculas

    Argumentos:
        lista (list): Una lista ya predefinida

    Retorna:
        None: no retorna nada
    """
    variable_titulo = "Título"
    variable_genero = "Género"
    variable_anio = "Año de lanzamiento"
    variable_duracion = "Duración"
    variable_atp = "ATP"
    variable_plataformas = "Plataformas"
    print("*"*141)
    print(f"|  {variable_titulo:^48}  |  {variable_genero:^17}  | {variable_anio:^4} | {variable_duracion:^3}  |  {variable_atp} |  {variable_plataformas:^20}  |")
    print("-"*141)
    
    for i in range(len(lista)):
        titulo = lista[i]["titulo"]
        genero = lista[i]["genero"]
        anio = lista[i]["año_lanzamiento"]
        duracion = lista[i]["duracion"]
        atp = lista[i]["atp"]
        plataformas = lista[i]["plataformas"]
        plataformas = "-".join(plataformas)
        
        if atp == True:
            atp = "Si"
        else:
            atp = "No"

        print(f"|  {titulo:^48}  |  {genero:^17}  |     {anio:^11}    |  {duracion:^4} m   |  {atp}  |  {plataformas:^20}  |")
    print("*"*141)
# ------------------------------------------------------------------------------------ #
def sacar_promedio(lista: list, clave: str)->int:
    """Esta funcion recibe como parametros una lista y una clave en formato string
    se encarga de sacar el promedio de lo que llegue en la clave

    Argumentos:
        lista (list): Una lista ya predefinida
        clave (str): Una string ya predefinida

    Retorna:
        int: Un numero entero que seria el promedio
    """
    suma = 0
    longitud_lista = len(lista)

    for i in range(len(lista)):
        suma += lista[i][clave]
    
    promedio = suma / longitud_lista
    promedio = round(promedio)

    return promedio
# ------------------------------------------------------------------------------------ #
def porcentaje_genero(lista: list,clave: str,palabra: str | bool)->float:
    """Esta funcion recibe como parametros una lista, una clave y palabra en formato string, se encarga de sacar el porcentaje
    dependiendo la clave que pasen por parametro, y saca el porcentaje

    Argumentos:
        lista (list): Una lista ya predefinida
        clave (str): Una string ya predefinida
        palabra (str | bool): Una string o bool ya predefinida

    Retorno:
        float: un numero float que seria el porcentaje
    """
    contador = 0
    longitud_lista = len(lista)

    for i in range(len(lista)):
        if palabra == lista[i][clave]:
            contador += 1
    
    porcentaje = (contador * 100) / longitud_lista
    porcentaje = round(porcentaje,2)

    return porcentaje
# ------------------------------------------------------------------------------------ #
def seteo_ids_eliminadas()->None:
    """Esta funcion se encarga de eliminar las ID repetidas de la lista de id eliminadas"""
    with open("Parcial_1/Package_Funciones/ids_eliminadas.txt", "r") as archivo:
        texto = archivo.readlines()
        texto = set(texto)
    
    with open("Parcial_1/Package_Funciones/ids_eliminadas.txt", "w") as archivo:
        archivo.writelines(texto)
# ------------------------------------------------------------------------------------ #
def obtener_lista_valores(lista: list, key: str)->list:
    lista_valor = []

    for i in range(len(lista)):
        lista_valor.append(lista[i].get(key))
    
    lista_valor = set(lista_valor)
    return lista_valor
# ------------------------------------------------------------------------------------ #