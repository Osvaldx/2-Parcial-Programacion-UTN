import json
from .funciones_especificas import *

##################################################################################################################################
def ventana_principal(ventana:tuple)->bool:
    titulo = pygame.image.load("2repo/Parcial_2/imagenes/titulo.png")
    titulo = pygame.transform.scale(titulo, dimensiones_titulo)

    boton_play_normal = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
    boton_play_normal = pygame.transform.scale(boton_play_normal, dimnesiones_boton_normal)

    boton_play_grande = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
    boton_play_grande = pygame.transform.scale(boton_play_grande, dimensiones_boton_grande)

    boton_play = boton_play_normal
    input_activado = False

    font_size_nombre = 25
    font_nombre_texto = pygame.font.Font("2repo/Parcial_2/fonts/Retro Gaming.TTF",font_size_nombre)
    nombre_recibido = ""

    cord_x_botonplay = 515
    cord_y_botonplay = 600
    
    bandera = True
    click = "False"
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
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
                boton_play = boton_play_normal
                if (pos_x <= (cord_x_botonplay + 125) and pos_x >= cord_x_botonplay) and (pos_y <= (cord_y_botonplay + 125) and pos_y >= cord_y_botonplay):
                    if nombre_recibido != "":
                        bandera = False
                        return True
                    else:
                        click = "AusenciaNICK"
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if (pos_x <= (rect_x + rect_width) and pos_x >= rect_x) and (pos_y <= (rect_y + rect_high) and pos_y >= rect_y):
                    input_activado = True
                    click = "True"
            elif evento.type == pygame.KEYDOWN:
                if input_activado == True:
                    if evento.key == pygame.K_BACKSPACE:
                        nombre_recibido = nombre_recibido[:-1]
                    elif evento.key == pygame.K_RETURN:
                        print(nombre_recibido)
                        input_activado = False
                        # nombre_recibido = ""
                        click = "False"
                    else:
                        if len(nombre_recibido) <= 8:
                            nombre_recibido += evento.unicode
                        else:
                            nombre_recibido = nombre_recibido

        dibujar_todo(ventana,titulo,boton_play,nombre_recibido,font_nombre_texto,cord_x_botonplay,cord_y_botonplay,click)
        pygame.display.update() #aca se va actuializando

##################################################################################################################################
def ventana_de_juego(ventana:tuple):
    ventana.fill(AMARILLO_PASTEL)

    bandera = True
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            print(evento)
            if evento.type == pygame.QUIT:
                bandera = False
        
        pygame.display.update()