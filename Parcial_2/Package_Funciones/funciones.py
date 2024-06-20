import pygame
import json
from .colores import *

##################################################################################################################################
def ventana_principal(ventana)->bool:
    titulo = pygame.image.load("2repo/Parcial_2/imagenes/titulo.png")
    titulo = pygame.transform.scale(titulo, (500,320))

    boton_play_normal = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
    boton_play_normal = pygame.transform.scale(boton_play_normal, (125,125))

    boton_play_grande = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
    boton_play_grande = pygame.transform.scale(boton_play_grande, (150,150))

    cord_x_botonplay = 515
    cord_y_botonplay = 600

    boton_play = boton_play_normal

    def dibujar_todo(color="CLEAN"):
        if color == "VENTANA1":
            ventana.fill(AMARILLO_PASTEL)
            ventana.blit(titulo, (330,100))
            ventana.blit(boton_play, (cord_x_botonplay,cord_y_botonplay))
            pygame.draw.rect(ventana, BLANCO, (478,480,200,50),0,3)
            pygame.draw.rect(ventana, GREEN, (478,480,200,50),5,3)
        elif color == "VENTANA2":
            ventana.fill(BLANCO)

    bandera = True
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            print(evento)
            if evento.type == pygame.QUIT:
                bandera = False
            elif evento.type == pygame.MOUSEMOTION:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]
                if (pos_x <= (cord_x_botonplay + 125) and pos_x >= cord_x_botonplay) and (pos_y <= (cord_y_botonplay + 125) and pos_y >= cord_y_botonplay):
                    cord_x_botonplay = 505
                    cord_y_botonplay = 590
                    boton_play = boton_play_grande
                else:
                    cord_x_botonplay = 515
                    cord_y_botonplay = 600
                    boton_play = boton_play_normal
            elif evento.type == pygame.MOUSEBUTTONUP:
                cord_x_botonplay = 515
                cord_y_botonplay = 600
                if (pos_x <= (cord_x_botonplay + 125) and pos_x >= cord_x_botonplay) and (pos_y <= (cord_y_botonplay + 125) and pos_y >= cord_y_botonplay):
                    boton_play = boton_play_normal
                    dibujar_todo("VENTANA2")
                    bandera = False
                    return True

        dibujar_todo("VENTANA1")
        pygame.display.update() #aca se va actuializando

##################################################################################################################################
def ventana_de_juego(ventana):
    ventana.fill(RED)

    bandera = True
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            print(evento)
            if evento.type == pygame.QUIT:
                bandera = False
        
        pygame.display.update()