import pygame
from .colores import *
from .config import *

def print_nombre(ventana:tuple,texto,font,color_texto,x,y):
    mostrar_pantalla = font.render(texto,True,color_texto)
    ventana.blit(mostrar_pantalla,((x + 10),(y + 10)))

def rectangulo_nombre(ventana:tuple,click:str):
    color_borde = NEGRO
    if click == "True":
        color_borde = VERDE_OSCURO
    elif click == "AusenciaNICK":
        color_borde = RED
    pygame.draw.rect(ventana, GRIS, (rect_x,rect_y,rect_width,rect_high),0,3)
    pygame.draw.rect(ventana, color_borde, (rect_x,rect_y,rect_width,rect_high),5,3)

def dibujar_todo(ventana:tuple,titulo,boton_play,nombre_recibido,font_texto,cord_x_botonplay,cord_y_botonplay,click):
    ventana.fill(AMARILLO_PASTEL)
    ventana.blit(titulo, (330,100))
    ventana.blit(boton_play, (cord_x_botonplay,cord_y_botonplay))
    rectangulo_nombre(ventana,click)
    print_nombre(ventana,nombre_recibido,font_texto,NEGRO,rect_x,rect_y)