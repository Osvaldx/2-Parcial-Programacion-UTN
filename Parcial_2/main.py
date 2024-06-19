import pygame
from colores import *
import json
pygame.init()

alto = 800 # Y
ancho = 1200 # X
dimensiones = (ancho, alto)

ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("MILLONES")

logo = pygame.image.load("Parcial_2/imagenes/dolar.png")
pygame.display.set_icon(logo)

ventana.fill(AMARILLO_PASTEL)

titulo = pygame.image.load("Parcial_2/imagenes/titulo.png")
titulo = pygame.transform.scale(titulo, (550,450))
ventana.blit(titulo, (305,40))

boton_play = pygame.image.load("Parcial_2/imagenes/botonjugar.png")
boton_play = pygame.transform.scale(boton_play, (150,150))
ventana.blit(boton_play, (515,480))


#boton de play-----------------------------------------
play = pygame.font.SysFont("Ravie",30, True)
#-------------------------------------------------------

bandera = True
while bandera:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        print(evento)
        if evento.type == pygame.QUIT:
            bandera = False

    pygame.display.update() #aca se va actuializando



pygame.quit()



# pygame.draw.line(PANTALLA, (STAR_CORDS), (END_CORDS), GROSOR)
#