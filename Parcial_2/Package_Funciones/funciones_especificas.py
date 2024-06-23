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
            "score": 0,
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
    ventana_menu_rectangulo_nombre(ventana,click)
    ventana_menu_print_nombre(ventana,nombre_recibido,font_texto,NEGRO,rect_x,rect_y)
# #################################################################################################### #
# VENTANA DE JUEGO 2
# #################################################################################################### #
def leer_del_csv(path:str,lista_preguntas,lista_respuestas)->None:
    with open(path, "r", encoding="UTF-8") as archivo:
        lineas_del_archivo = archivo.readlines()

    for i in range(1,len(lineas_del_archivo)):
        datos = lineas_del_archivo[i]
        datos = datos.split(",")

        preguntas = datos[0]

        respuestas_correctas = datos[1]
        respuestas_correctas = respuestas_correctas.replace("\n","")

        no_respuestas = datos[2]
        no_respuestas = no_respuestas.replace("-", ",")
        no_respuestas = no_respuestas.replace("\n","")
        no_respuestas_separadas = no_respuestas.split(",")

        lista_preguntas.append(preguntas)
        lista_respuestas.append(no_respuestas_separadas)

        no_respuestas_separadas.append(respuestas_correctas)
# ---------------------------------------------------------------------------------------------------- #
def ventana_juego_dibujar_todo(ventana:tuple,box_seleccionada,box_no_seleccionada,ubicacion_seleccionada,texto_cronometro,bandera_reloj,texto_pregunta,texto_opciones,lista_ubicaciones_fijas):
    ventana.fill(AMARILLO_PASTEL_APAGADO)
    ventana.blit(fondo_juego, (100,30))
    pygame.draw.rect(ventana,MARRON,(100,30,1000,600),10)
    ventana.blit(box_pregunta,(350,480))
    font_opciones = pygame.font.Font("2repo/Parcial_2/fonts/prstartk.ttf", 15)

    for ubicacion_opcion in lista_ubicaciones_fijas:
        (ubicacion_x,ubicacion_y) = ubicacion_opcion[0]
        
        if (ubicacion_x,ubicacion_y) == ubicacion_seleccionada:
            ventana.blit(box_seleccionada,((ubicacion_x,ubicacion_y)))
        else:
            ventana.blit(box_no_seleccionada,((ubicacion_x,ubicacion_y)))

        texto_de_opcion = font_opciones.render(ubicacion_opcion[1],True,NEGRO)
        ventana.blit(texto_de_opcion,(ubicacion_x + 80 ,ubicacion_y + 30))

    ventana.blit(tabla_dinero, (923,126))
    ventana.blit(CRONOMETRO_imagen,(10,30))
    ventana.blit(texto_cronometro, (42,80))
    ventana.blit(texto_pregunta, (363,518))
    if bandera_reloj == True:
        ventana.fill(NEGRO)
        ventana.blit(texto_game_over, (230,150))
        ventana.blit(imagen_de_calavera,(325,250))
# #################################################################################################### #