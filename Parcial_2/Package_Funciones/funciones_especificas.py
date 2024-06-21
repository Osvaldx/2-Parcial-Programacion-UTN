import pygame
import json
from .colores import *
from .config import *

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
    
    if lista_players == []:
        formato = {
            "Players": []
        }
        lista_players.append(formato)
        dato_user = {
            "nombre": nombre_recibido,
            "dinero": 320000,
            "score": 800,
        }
        lista_players[0]["Players"].append(dato_user)
    else:
        dato_user = {
            "nombre": nombre_recibido,
            "dinero": 444777,
            "score": 450,
        }
        lista_players[0]["Players"].append(dato_user)
    
    with open(path, "w", encoding="UTF-8") as archivo:
        json.dump(lista_players[0],archivo,indent=4,ensure_ascii=False)
# ---------------------------------------------------------------------------------------------------- #
def ventana_menu_dibujar_todo(ventana:tuple,titulo,boton_play,nombre_recibido,font_texto,cord_x_botonplay,cord_y_botonplay,click):
    ventana.fill(AMARILLO_PASTEL)
    ventana.blit(titulo, (330,100))
    ventana.blit(boton_play, (cord_x_botonplay,cord_y_botonplay))
    ventana_menu_rectangulo_nombre(ventana,click)
    ventana_menu_print_nombre(ventana,nombre_recibido,font_texto,NEGRO,rect_x,rect_y)
# #################################################################################################### #
# VENTANA DE JUEGO 2
# #################################################################################################### #
def leer_del_csv(path:str,lista_preguntas,lista_correctas)->None:
    archivo = open(path, "r", encoding="utf-8")
    lineas_del_archivo = archivo.readlines()
    archivo.close
 
    for i in range(1,len(lineas_del_archivo)):
        datos = lineas_del_archivo[i]
        datos = datos.split(",")
        preguntas = datos[0]
        respuestas_correctas = datos[1]
        respuestas_correctas = respuestas_correctas.replace("\n","")

        lista_preguntas.append(preguntas)
        lista_correctas.append(respuestas_correctas)

def ventana_juego_dibujar_todo(ventana:tuple,fondo_juego,CRONOMETRO_imagen,texto_cronometro):
    ventana.blit(fondo_juego, (100,30))
    box_pregunta = pygame.draw.rect(ventana, CELESTE,(box_pregunta_x,box_pregunta_y,box_pregunta_width,box_pregunta_high),0,20)
    box_pregunta_borde = pygame.draw.rect(ventana, NEGRO,(box_pregunta_x,box_pregunta_y,box_pregunta_width,box_pregunta_high),7,20)

    variables = [
        (box_respuesta_correcta_x, box_respuesta_correcta_y),
        (box_respuesta_incorrecta_1_x, box_respuesta_incorrecta_1_y),
        (box_respuesta_incorrecta_2_x, box_respuesta_incorrecta_2_y),
        (box_respuesta_incorrecta_3_x, box_respuesta_incorrecta_3_y),
    ]

    for (rectangulo_x,rectangulo_y) in variables:
        rectangulo_opciones = pygame.draw.rect(ventana, CELESTE, (rectangulo_x, rectangulo_y, box_respuesta_width, box_respuesta_high), 0, 20)
        rectangulo_opciones_bordes = pygame.draw.rect(ventana, NEGRO, (rectangulo_x, rectangulo_y, box_respuesta_width, box_respuesta_high), 6, 20)
    
    ventana.blit(CRONOMETRO_imagen,(50,25))
    ventana.blit(texto_cronometro, (82,75))
# #################################################################################################### #