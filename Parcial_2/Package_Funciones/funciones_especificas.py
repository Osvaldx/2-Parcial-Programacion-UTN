import pygame
import json
import random
from .colores import *
from .configuracion import *

# #################################################################################################### #
# VENTANA DEL MENU 1
# #################################################################################################### #
def ventana_menu_print_nombre(ventana:tuple,texto,font,color_texto,x,y):
    mostrar_pantalla = font.render(texto,True,color_texto)
    ventana.blit(mostrar_pantalla,((x + 10),(y + 10)))
# ---------------------------------------------------------------------------------------------------- #
def ventana_menu_rectangulo_nombre(ventana:tuple,click:str):
    color_borde = NEGRO
    if click == "True":
        color_borde = VERDE_OSCURO
    elif click == "AusenciaNICK":
        color_borde = RED
        ventana.blit(texto_nombre_repetido, (405,555))
    pygame.draw.rect(ventana, GRIS, (rect_x,rect_y,rect_width,rect_high),0,5)
    pygame.draw.rect(ventana, color_borde, (rect_x,rect_y,rect_width,rect_high),5,5)
# ---------------------------------------------------------------------------------------------------- #
def crear_json_players(path:str,nombre_recibido):
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
def ventana_menu_dibujar_todo(ventana:tuple,titulo,boton_play,boton_play_rect,nombre_recibido,font_texto,click):
    ventana.fill(AMARILLO_PASTEL)
    ventana.blit(titulo, (330,100))
    ventana.blit(boton_play, (boton_play_rect.x,boton_play_rect.y))
    ventana.blit(texto_ingresar_nombre, (430,440))
    ventana_menu_rectangulo_nombre(ventana,click)
    ventana_menu_print_nombre(ventana,nombre_recibido,font_texto,NEGRO,rect_x,rect_y)
# #################################################################################################### #
# VENTANA DE JUEGO 2
# #################################################################################################### #
def leer_del_csv(path:str,lista_preguntas,lista_respuestas)->None:
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
def dividir_texto(texto:str):
    retorno = texto
    validar_arroba = texto.count("@")
    if validar_arroba > 0:
        texto_modificado = texto.split("@")
        retorno = texto_modificado
    
    return retorno

def actualizacion_puntos(path,numero:int,nombre_jugador,tiempo_transcurrido,tiempo_inicial):
    with open(path, "r", encoding="UTF-8") as archivo:
        lista_jugadores = json.load(archivo)

    for jugador in lista_jugadores["Players"]:
        if nombre_jugador.capitalize() == jugador["nombre"]:
            jugador["dinero"] = numero
            tiempo_record = (int(tiempo_inicial) // 1000) - int(tiempo_transcurrido)
            
            if tiempo_record <= 2:
                jugador["puntos"] += 5 # Hace referencia a lo que falta del cronometro para llegar a 30
            elif tiempo_record <= 3:
                jugador["puntos"] += 3
            elif tiempo_record <= 5:
                jugador["puntos"] += 1
            elif tiempo_record <= 8:
                jugador["puntos"] += 0.5
            elif tiempo_record <= 12:
                jugador["puntos"] += 0.25
            elif tiempo_record <= 15:
                jugador["puntos"] += 0.05
            else:
                jugador["puntos"] += 0.01
    
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(lista_jugadores,archivo,indent=4,ensure_ascii=False)
# ---------------------------------------------------------------------------------------------------- #
def ventana_juego_dibujar_todo(ventana:tuple,box_seleccionada,box_no_seleccionada,ubicacion_seleccionada,texto_cronometro,bandera_reloj,texto_pregunta_dividido_1,texto_pregunta_dividido_2,lista_ubicaciones_fijas,ubicacion_respuesta_elegida,opcion_respuesta,tabla_dinero):
    retorno = False
    ventana.fill(AMARILLO_PASTEL_APAGADO)
    ventana.blit(fondo_juego, (100,30))
    pygame.draw.rect(ventana,MARRON,(100,30,1000,600),10)
    box_pregunta = pygame.image.load("2repo/Parcial_2/imagenes/pregunta.png")
    box_pregunta = pygame.transform.scale(box_pregunta,(500,106))
    ventana.blit(box_pregunta,(340,480))
    font_opciones = pygame.font.Font(path + "fonts/prstartk.ttf", 15)

    for ubicacion_opcion in lista_ubicaciones_fijas:
        (ubicacion_x,ubicacion_y) = ubicacion_opcion[0]
        
        if (ubicacion_x,ubicacion_y) == ubicacion_seleccionada:
            ventana.blit(box_seleccionada,((ubicacion_x,ubicacion_y)))
        else:
            ventana.blit(box_no_seleccionada,((ubicacion_x,ubicacion_y)))

        texto_de_opcion = font_opciones.render(ubicacion_opcion[1],True,NEGRO)
        ventana.blit(texto_de_opcion,(ubicacion_x + 45 ,ubicacion_y + 30))

    if ubicacion_respuesta_elegida != None:
        for ubicacion_respuesta in lista_ubicaciones_fijas:
            if ubicacion_respuesta_elegida == ubicacion_respuesta[0]:
                if opcion_respuesta == ubicacion_respuesta[1]:
                    retorno = True
                else:
                    retorno = "equivocado"
                break

    ventana.blit(tabla_dinero, (923,30))
    ventana.blit(titulo_premios,(980,42))
    ventana.blit(CRONOMETRO_imagen,(10,30))
    ventana.blit(texto_cronometro, (42,80))
    ventana.blit(texto_pregunta_dividido_1, (390,515))
    ventana.blit(texto_pregunta_dividido_2, (390,540))

    if (bandera_reloj == True) or bandera_reloj == "fallo":
        ventana.fill(NEGRO)
        ventana.blit(texto_game_over, (230,150))
        ventana.blit(imagen_de_calavera,(325,250))

    if retorno == True or retorno == "equivocado":
        pygame.display.update()
        return retorno
# #################################################################################################### #