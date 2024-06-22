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

def ventana_juego_dibujar_todo(ventana:tuple,box_seleccionada,box_no_seleccionada,ubicacion_seleccionada,texto_cronometro,bandera_reloj):
    imagen_de_calavera = pygame.image.load("2repo\Parcial_2\imagenes\calavera.png")
    imagen_de_calavera= pygame.transform.scale(imagen_de_calavera, (500, 500))

    fuente_game_over = pygame.font.Font("2repo/Parcial_2/fonts/m04.TTF",80)
    texto_game_over = fuente_game_over.render("GAME OVER", False, (167,54,0))
    texto_game_over = fuente_game_over.render("GAME OVER", False, (255,0,0))

    fondo_juego = pygame.image.load("2repo/Parcial_2/imagenes/fondojuego.jpg")
    fondo_juego = pygame.transform.scale(fondo_juego, (1000,600))

    box_pregunta = pygame.image.load("2repo/Parcial_2/imagenes/pregunta.png")

    CRONOMETRO_imagen = pygame.image.load("2repo/Parcial_2/imagenes/cronometro.png")#hace que no se acumulen las cosas
    CRONOMETRO_imagen = pygame.transform.scale(CRONOMETRO_imagen,(90,110))

    tabla_dinero = pygame.image.load("2repo/Parcial_2/imagenes/tabla.png")
    tabla_dinero = pygame.transform.scale(tabla_dinero, (250,400))

    ventana.fill(AMARILLO_PASTEL_APAGADO)
    ventana.blit(fondo_juego, (100,30))
    pygame.draw.rect(ventana,MARRON,(100,30,1000,600),10)
    ventana.blit(box_pregunta,(350,480))
    ubicaciones = {
        (600,600),
        (290,600),
        (290,690),
        (600,690),
    }
    for (ubicacion_x,ubicacion_y) in ubicaciones:
        if (ubicacion_x,ubicacion_y) == ubicacion_seleccionada:
            ventana.blit(box_seleccionada,(ubicacion_x,ubicacion_y))
        else:
            ventana.blit(box_no_seleccionada,(ubicacion_x,ubicacion_y))

    ventana.blit(tabla_dinero, (923,126))
    ventana.blit(CRONOMETRO_imagen,(10,30))
    ventana.blit(texto_cronometro, (42,80))
    if bandera_reloj == True:
        ventana.fill((0,0,0))
        ventana.blit(texto_game_over, (230,150))
        ventana.blit(imagen_de_calavera,(325,250))
# #################################################################################################### #