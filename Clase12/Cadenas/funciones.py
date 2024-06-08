from data import Video

def normalizar_objetos(lista_videos: list[Video])->None:
    for i in range(len(lista_videos)):
        lista_videos[i].dividir_titulo()
        lista_videos[i].obtener_codigo_url()
        lista_videos[i].formatear_fecha()
    print("NORMALIZACION DE OBJETOS LISTA!")

def mostrar_temas(lista_videos: list[Video])->None:
    for i in range(len(lista_videos)):
        lista_videos[i].mostrar_tema()

def orderna_lista(lista_videos: list[Video])->None:
    for i in range(len(lista_videos)):
        for j in range(len(lista_videos) -1 -i):
            if lista_videos[j].sesion > lista_videos[j+1].sesion:
                aux = lista_videos[j]
                lista_videos[j] = lista_videos[j+1]
                lista_videos[j+1] = aux
    print("TEMAS ORDENADOSS!!")

def promedio_vistas(lista_videos: list[Video])->None:
    suma = 0
    for i in range(len(lista_videos)):
        vistas = lista_videos[i].vistas
        suma += int(vistas)
    promedio = suma / len(lista_videos)
    cantidad_k = promedio / 1000
    print(f"El promedio de vistas en K es: {round(cantidad_k)}k")

def maxima_reproduccion(lista_videos: list[Video])->None:
    bandera = False

    for i in range(len(lista_videos)):
        vistas = lista_videos[i].vistas
        vistas = int(vistas)
        if bandera == False or vistas > num_max:
            num_max = lista_videos[i].vistas
            bandera = True
    print(f"El video con mas reproducciones tiene: {num_max} reproducciones")

def busqueda_por_codigo(lista_videos: list[Video])->None:
    for i in range(len(lista_videos)):
        buscar = lista_videos[i].url_youtube
        buscar = buscar.count("nick")
        if buscar >= 1:
            lista_videos[i].mostrar_tema()

def listar_por_colaborador(lista_videos: list[Video])->None:
    colaborador = input("Ingrese el nombre de un colaborador: ")
    while not colaborador.isalpha():
        colaborador = input("Ingrese nuevamente el nombre de un colaborador: ")

    for i in range(len(lista_videos)):
        buscar = lista_videos[i].url_youtube
        buscar = buscar.count(colaborador)
        if buscar >= 1:
            lista_videos[i].mostrar_tema()