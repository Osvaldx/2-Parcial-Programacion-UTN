from .funciones_especificas import *
from .validaciones import *
import pygame

##################################################################################################################################
def ventana_menu(ventana:tuple)->bool:
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
                    if validar_nombre(nombre_recibido) == True:
                        crear_json_players("2repo/Parcial_2/archivos/jugadores.json",nombre_recibido)
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

        ventana_menu_dibujar_todo(ventana,titulo,boton_play,nombre_recibido,font_nombre_texto,cord_x_botonplay,cord_y_botonplay,click)
        pygame.display.update() #aca se va actuializando

##################################################################################################################################
def ventana_de_juego(ventana):
    ventana.fill(AMARILLO_PASTEL)
    lista_preguntas = []
    lista_correctas = []

    leer_del_csv("2repo/Parcial_2/archivos/preguntas.csv",lista_preguntas,lista_correctas)

    fondo_juego = pygame.image.load("2repo/Parcial_2/imagenes/fondojuego.jpg")
    fondo_juego = pygame.transform.scale(fondo_juego, (1000,600))

    font_cronometro = pygame.font.Font("2repo/Parcial_2/fonts/Retro Gaming.ttf", 20)
    clock = pygame.time.Clock() #se nivelan los fps
    tiempo_incial = 30000
    tiempo_referencia = pygame.time.get_ticks()

    CRONOMETRO_imagen = pygame.image.load("2repo/Parcial_2/imagenes/cronometro.png")#hace que no se acumulen las cosas
    CRONOMETRO_imagen = pygame.transform.scale(CRONOMETRO_imagen,(90,110))
    
    bandera = True
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            print(evento)
            if evento.type == pygame.QUIT:
                bandera = False
        

        tiempo_actual = pygame.time.get_ticks()
        tiempo_trascurrido = (tiempo_incial - (tiempo_actual - tiempo_referencia))/1000
        tiempo_trascurrido = round(tiempo_trascurrido)
        tiempo_trascurrido = str(tiempo_trascurrido) #PARA PODER PONERLE UN FUENTE A ELECCION

        if tiempo_trascurrido == "0":
            bandera = False

        texto_cronometro = font_cronometro.render(tiempo_trascurrido, True, (0,0,0))

        ventana_juego_dibujar_todo(ventana,fondo_juego,CRONOMETRO_imagen,texto_cronometro)
        clock.tick(60)
        pygame.display.update()