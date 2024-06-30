import pygame
import json
import random
from .colores import *
from .configuracion import *

# #################################################################################################### #
# VENTANA DEL MENU 1
# #################################################################################################### #
def ventana_menu_print_nombre(ventana:tuple,texto:str,font:pygame.font,color_texto:pygame.color,x,y)->None:
    """Esta función recibe comó parametró una ventana, un texto, una fuente, un color y posiciónes de (x,y)
    se encarga de mostrar en pantalla el texto que se recibe por parametro

    Argumentos:
        ventana (tuple): una ventana de pygame ya predefinida e inicializada
        texto (str): un texto ya predefinido
        font (pygame.font): una fuente para el texto
        color_texto (pygame.color): el color del texto
        x (_type_): posición X
        y (_type_): posición Y
    
    Return:
        __Type__: None
    """
    mostrar_pantalla = font.render(texto,True,color_texto)
    ventana.blit(mostrar_pantalla,((x + 10),(y + 10)))
# ---------------------------------------------------------------------------------------------------- #
def ventana_menu_rectangulo_nombre(ventana:tuple,click:str)->None:
    """Esta función recibe comó parametró una ventana y un str.
    esta funcion se encarga de blitear en pantlla un figura rectangular en la cual el usurio ingresara su nombre, 
    si este es repetido se coloreare de color rojo el borde de ese rectangulo.

    Argumentos:
        ventana (tuple): una tupla ya predefinida con su parametros de altura y ancho
        click (str): un str determinante para el color del rectangulo
    
    Return:
        __Type__: None
    """
    color_borde = NEGRO
    if click == "True":
        color_borde = VERDE_OSCURO
    elif click == "AusenciaNICK":
        color_borde = ROJO
        ventana.blit(texto_nombre_repetido2, (458,558))
        ventana.blit(texto_nombre_repetido, (455,555))
    pygame.draw.rect(ventana, GRIS, (rect_x,rect_y,rect_ancho,rect_alto),0,5)
    pygame.draw.rect(ventana, color_borde, (rect_x,rect_y,rect_ancho,rect_alto),5,5)
# ---------------------------------------------------------------------------------------------------- #
def crear_json_players(path:str,nombre_recibido:str)->None:
    """Esta funcion recibe como parametro una ruta de acceso y un caracter str.
    Se encarga de leer un archivo json y de sobreesceribirlo con un diccionario.

    Argumentos:
        path (str): un ruta ya predefinida del archivo
        nombre_recibido (_type_): un nombre ya predefinido
    
    Return:
        __Type__: None
    """
    with open(path, "r", encoding="UTF-8") as archivo:
        try:
            lista_players = [json.load(archivo)]
        except:
            lista_players = []

    nombre_recibido = nombre_recibido.capitalize()
    dato_user = {
            "nombre": nombre_recibido,
            "dinero": 0,
            "puntos": 0,
        }
    
    if lista_players == []:
        formato = {
            "Players": []
        }
        lista_players.append(formato)
        lista_players[0]["Players"].append(dato_user)
    else:
        lista_players[0]["Players"].append(dato_user)
    
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(lista_players[0],archivo,indent=4,ensure_ascii=False)
# ---------------------------------------------------------------------------------------------------- #
def ventana_menu_dibujar_todo(ventana:tuple,titulo:pygame.surface,boton_play:pygame.surface,boton_play_rect,nombre_recibido:str,font_texto,click:str)->None:
    """Esta función recibe como parametro una ventana, un titulo, un botoplay, propiedades del rectangulo, un nombre, font_texto y click
    Se encarga de mostrar en pantalla todos los bliteo que suceden en la interación del usuario y el programa

    Argumentos:
        ventana (tuple): Una ventana ya predefnida e inicializada
        titulo (_type_): Un surface
        boton_play (_type_): Un surface
        boton_play_rect (_type_): Un surface
        nombre_recibido (_type_): Una string ya predefinida
        font_texto (_type_): fuente ya predeterminada para el texto
        click (_type_): Una string ya predefinida
    
    Return:
        __Type__: None
    """
    fondito = pygame.image.load(path + "imagenes/fondo22.jpg")
    fondito = pygame.transform.scale(fondito,(1300,800))
    ventana.blit(fondito,(0,0))
    ventana.blit(titulo, (333,80))
    ventana.blit(boton_play, (boton_play_rect.x,boton_play_rect.y))
    ventana.blit(texto_ingresar_nombre2, (436,434))
    ventana.blit(texto_ingresar_nombre, (433,430))
    ventana_menu_rectangulo_nombre(ventana,click)
    ventana_menu_print_nombre(ventana,nombre_recibido,font_texto,NEGRO,rect_x,rect_y)
# #################################################################################################### #
# VENTANA DE JUEGO 2
# #################################################################################################### #
def leer_del_csv(path:str,lista_preguntas:list,lista_respuestas:list)->None:
    """Esta función recibe como parametros un path, una lista de preguntas y lista de respuestas:
    Se encarga de leer y extraer del csv las preguntas y respuestas y despues ir agregandolas en las listas
    que se recibio por parametros que se encuentran vacias

    Argumentos:
        path (str): una ruta ya predeterminada
        lista_preguntas (_type_): una lista vacia
        lista_respuestas (_type_): una lista vacia
    
    Return:
        __Type__: None
    """
    
    with open(path, "r", encoding="UTF-8") as archivo:
        lineas_del_archivo = archivo.readlines()
        lista_del_archivo_random = []
        copia_lineas_archivo = lineas_del_archivo.copy()
        copia_lineas_archivo.pop(0)
        while True:
            if copia_lineas_archivo != []:
                texto_completo = random.choice(copia_lineas_archivo)
                lista_del_archivo_random.append(texto_completo)
                copia_lineas_archivo.remove(texto_completo)
            else:
                break

    for i in range(1,len(lista_del_archivo_random)):
        datos = lista_del_archivo_random[i]
        datos = datos.split(",")

        preguntas = datos[0]

        respuestas_correctas = datos[1]
        respuestas_correctas = respuestas_correctas.replace("\n","")

        no_respuestas = datos[2]
        no_respuestas = no_respuestas.replace("-", ",")
        no_respuestas = no_respuestas.replace("\n","")
        no_respuestas_separadas = no_respuestas.split(",")

        if len(lista_preguntas) <= 12:
            lista_preguntas.append(preguntas)
            lista_respuestas.append(no_respuestas_separadas)

        no_respuestas_separadas.append(respuestas_correctas)

#---------------------------------------------------------------------------------------------
       
def dividir_texto(texto:str)->list[str]:
    """Esta funcion reciebe como parametro un str.
    se encanrga de dividir ese str en base a un parametro pasado, en este caso un @

    Argumentos:
        texto (str): Un texto en formato string ya predefinido

    Returns:
        list: Retorna una lista con el texto dividido
    """
    retorno = texto
    validar_arroba = texto.count("@")
    if validar_arroba > 0:
        lista_del_texto_modificado = texto.split("@")
        retorno = lista_del_texto_modificado
    
    return retorno
    
#--------------------------------------------------------------------------------------------------

def actualizacion_puntos(path,numero:int,nombre_jugador:str,tiempo_transcurrido,tiempo_inicial,clave:str)->list:
    """Esta funcion recebi como parametro un ruta de acceso, un numero, el nombre del jugador, el tiempo  y una key.
    Se encarga de asignarle un puntaje a los jugadore segun el tiempo que haya tardado en contestar la pregunta.
    Argumentos:
        path (_type_): Un ruta de archivo ya predefiinido
        numero (int): Un número ya predefinido que se recibio por parametro
        nombre_jugador (_type_): el nombre ya ingresado anteriormente
        tiempo_transcurrido (_type_): es el timepo que le llevo a el usuario contestas la pregunta
        tiempo_inicial (_type_): se inicializa un tiempo del cual se va descontato de a segundo de manera descendente
        clave (_type_): esta clave se utiliza para poder separar los distitnos funciones que se hacen si actualizar o reiniciar puntos

    Returns:
        _type_: la lista de los jugadores que sera utilizada mas adelante
    """
    with open(path, "r", encoding="UTF-8") as archivo:
        lista_jugadores = json.load(archivo)

    for jugador in lista_jugadores["Players"]:
        if nombre_jugador.capitalize() == jugador["nombre"]:
            if clave == "actualizar_puntos":
                jugador["dinero"] = numero
                tiempo_record = (int(tiempo_inicial) // 1000) - int(tiempo_transcurrido)
                
                if tiempo_record <= 3:
                    jugador["puntos"] += 5 # Hace referencia a lo que falta del cronometro para llegar a 30
                elif tiempo_record <= 6:
                    jugador["puntos"] += 3
                elif tiempo_record <= 8:
                    jugador["puntos"] += 1
                elif tiempo_record <= 12:
                    jugador["puntos"] += 0.5
                elif tiempo_record <= 16:
                    jugador["puntos"] += 0.25
                elif tiempo_record <= 18:
                    jugador["puntos"] += 0.05
                else:
                    jugador["puntos"] += 0.01
            elif clave == "reiniciar_puntos":
                jugador["dinero"] = numero
                jugador["puntos"] = numero
    
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(lista_jugadores,archivo,indent=4,ensure_ascii=False)
    
    return lista_jugadores
# ---------------------------------------------------------------------------------------------------- #
def ventana_juego_dibujar_todo(ventana:tuple,box_seleccionada,box_no_seleccionada,ubicacion_seleccionada,texto_cronometro,bandera_reloj,texto_pregunta_dividido_1,texto_pregunta_dividido_2,lista_ubicaciones_fijas,ubicacion_respuesta_elegida,opcion_respuesta,tabla_dinero,digito_banco,retirarse,opcion_si_seleccionado,opcion_no_seleccionado,nombre_recibido)->bool| str:
    """Esta función se encarga de dibujar todo en pantalla y pegar imagenes dependiendo los eventos que vayan sucendiendo con la interacción del usuario
    recibe como parametros varios Surfaces, imagenes, fonts, textos, banderas, y tuplas

    Args:
        ventana (tuple): una surface ya predefinida
        box_seleccionada (_type_): una surface predefinida
        box_no_seleccionada (_type_): una surface predefinida
        ubicacion_seleccionada (_type_): la ubicacion de algun surface
        texto_cronometro (_type_): el temporizado con su fuente predeterminada
        bandera_reloj (_type_): una bandera booleano
        texto_pregunta_dividido_1 (_type_): una parte de la pregunta 
        texto_pregunta_dividido_2 (_type_): la otro parte de la preguta para que se blite de manera correcta en la ventana
        lista_ubicaciones_fijas (_type_): una lista de tuplas en la cual se encuentran las ubicaciones de las preguntas
        ubicacion_respuesta_elegida (_type_): la ubicacion de respuesta eligida por el usuario
        opcion_respuesta (_type_): Ubicación de la respuesta correcta
        tabla_dinero (_type_): la lista de los premios
        digito_banco (_type_): muestra el dinero que el usuario posee
        retirarse (_type_): Es una string que recibe si o no en string
        opcion_si_seleccionado (_type_): Es un booleano que le da opcion de retirarse del juego
        opcion_no_seleccionado (_type_): Es un booleano que le da opcion de retirarse del juego
        nombre_recibido (_type_): es el nombre ya predeterminado

    Returns:
        _type_: Bool | str
    """
    retorno = False
    ventana.fill(AMARILLO_PASTEL_APAGADO)
    ventana.blit(fondo_juego, (100,30))
    pygame.draw.rect(ventana,MARRON,(100,30,1000,600),10)
    ventana.blit(box_pregunta,(340,480))
    font_opciones = pygame.font.Font(path + "fonts/prstartk.ttf", 15)
    
    for ubicacion_opcion in lista_ubicaciones_fijas:
        (ubicacion_x,ubicacion_y) = ubicacion_opcion[0]
        
        if (ubicacion_x,ubicacion_y) == ubicacion_seleccionada:
            ventana.blit(box_seleccionada,((ubicacion_x,ubicacion_y)))
        else:
            ventana.blit(box_no_seleccionada,((ubicacion_x,ubicacion_y)))
        
        texto_de_opcion = font_opciones.render(ubicacion_opcion[1],True,NEGRO)
        if retirarse != True:
            ventana.blit(texto_de_opcion,(ubicacion_x + 45 ,ubicacion_y + 30))

    if ubicacion_respuesta_elegida != None:
        for ubicacion_respuesta in lista_ubicaciones_fijas:
            if ubicacion_respuesta_elegida == ubicacion_respuesta[0]:
                if retirarse != True:
                    if opcion_respuesta == ubicacion_respuesta[1]:
                        retorno = True
                    else:
                        retorno = "equivocado"
                    break

    ventana.blit(tabla_dinero, (923,30))
    ventana.blit(titulo_premios,(980,42))
    ventana.blit(CRONOMETRO_imagen,(10,30))
    if retirarse != True:
        ventana.blit(texto_cronometro, (42,80))
        ventana.blit(texto_pregunta_dividido_1, (390,515))
        ventana.blit(texto_pregunta_dividido_2, (390,540))
    ventana.blit(cuadro_dinero,(20,650))
    texto_dinero_banco = font_dinero.render("BANCO:",True,BLANCO)
    texto_dinero_digito = font_dinero.render(digito_banco,True,BLANCO)
    ventana.blit(texto_dinero_banco, (50,675))
    ventana.blit(texto_dinero_digito, (50,700))

    if retirarse == True:
        texto_retirarse = font_globito.render("¿Desea retirarse?",True,NEGRO)
        ventana.blit(globo_mensaje, (580,200))
        if opcion_si_seleccionado == True:
            ventana.blit(opcion_si_globo_presionado,(610,255))
        else:
            ventana.blit(opcion_si_globo_normal, (610,255))
        if opcion_no_seleccionado == True:
            ventana.blit(opcion_no_globo_presionado,(690,255))
        else:
            ventana.blit(opcion_no_globo_normal,(690,255))

        ventana.blit(texto_retirarse, (588,230))

    if (bandera_reloj == True) or bandera_reloj == "fallo":
        actualizacion_puntos(path + "archivos/jugadores.json",0,nombre_recibido,0,0,"reiniciar_puntos")
        ventana.fill(NEGRO)
        ventana.blit(texto_game_over, (230,150))
        ventana.blit(imagen_de_calavera,(325,250))

    if retorno == True or retorno == "equivocado":
        pygame.display.update()
        return retorno
# #################################################################################################### #
def leer_json(ruta_json:str)->list[dict]:
    """Esta función recibe como parametros la ruta del json y se necarga de solo leerlo y retornar los jugadores

    Argumentos:
        ruta_json (str): una ruta ya predefinida

    Returns:
        list[dict]: la lista de jugadores
    """
    with open(ruta_json, "r") as archivo:
        contenido = json.load(archivo)
    return contenido["Players"]

def ordenar_scores(lista_participantes:list, opcion_ordenar:str, que_ordenar:str)->list:
    """Esta funcion receibe una lista, la opcion a ordenar y que debe ordenar.
    Esta funcion la utilzamos para realizar el top de juagores en base a los puntos

    Args:
        lista_participantes (_type_): lista establecida del json
        opcion_ordenar (str): Desc
        que_ordenar (str): puntos

    Returns:
        list:la lista de jugadores ya ordenada
    """
    intercambio = False
    for j in range(len(lista_participantes)):             
        intercambio = False                
        for i in range(len(lista_participantes)-1 -j): 
            if opcion_ordenar == "Asc":     
                if lista_participantes[i][que_ordenar] > lista_participantes[i+1][que_ordenar]:        
                    auxiliar = lista_participantes[i]
                    lista_participantes[i] = lista_participantes[i+1]
                    lista_participantes[i+1] = auxiliar
                    intercambio =  True
            else:
                if lista_participantes[i][que_ordenar] < lista_participantes[i+1][que_ordenar]:        
                    auxiliar = lista_participantes[i]
                    lista_participantes[i] = lista_participantes[i+1]
                    lista_participantes[i+1] = auxiliar
                    intercambio =  True

        if intercambio==False:             
            break
    return lista_participantes
#--------------------------------------------------------------------------------------------

def dibujar_botones(ventana:tuple)->None:
    """Esta funcion recibe como parametro una superficie y se encarga de blitear los botones y los textos necesarios

    Args:
        ventana (tuple): una surface predefinida
    """
    ventana.blit(texto_volver_menu,(520,570))
    ventana.blit(boton_menu,(502,580))
    ventana.blit(texto_salir,(610,660))
    ventana.blit(boton_salir,(598,618))
    ventana.blit(texto_opciones,(450,530))
# #################################################################################################### #
def dibujar_todo_ganador(ventana:tuple)->None:
    """Esta función recibe como parametros una ventana y se encarga de blitear o mostrar todo el contenido
    en pantalla para el usuario

    Argumentos:
        ventana (tuple): una Surface ya predefinida
    """
    ventana.blit(fondo_ganador,(0,0))
    ventana.blit(texto_you_win, (440,465))
    ventana.blit(boton_scores,(470,590))
    ventana.blit(texto_puntos,(588,650))