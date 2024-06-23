from .funciones_especificas import *
from .validaciones import *
import pygame

##################################################################################################################################
def ventana_menu(ventana:tuple)->bool:
    pygame.mixer.music.load("2repo/Parcial_2/music/MENU.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    boton_play = boton_play_normal
    boton_play_rect = boton_play.get_rect()
    boton_play_rect.topleft = (515,600)
    input_activado = False

    font_size_nombre = 25
    font_nombre_texto = pygame.font.Font("2repo/Parcial_2/fonts/Retro Gaming.TTF",font_size_nombre)
    nombre_recibido = ""

    pos_x = 0
    pos_y = 0
    
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
                if (pos_x <= (boton_play_rect.x + boton_play_rect.width) and pos_x >= boton_play_rect.x) and (pos_y <= (boton_play_rect.y + boton_play_rect.width) and pos_y >= boton_play_rect.y):
                    boton_play_rect.x = 505
                    boton_play_rect.y = 590
                    boton_play = boton_play_grande
                else:
                    boton_play_rect.x = 515
                    boton_play_rect.y = 600
                    boton_play = boton_play_normal

            elif evento.type == pygame.MOUSEBUTTONUP:
                boton_play_rect.x = 515
                boton_play_rect.y = 600
                boton_play = boton_play_normal
                if (pos_x <= (boton_play_rect.x + 125) and pos_x >= boton_play_rect.x) and (pos_y <= (boton_play_rect.y + 125) and pos_y >= boton_play_rect.y):
                    if validar_nombre("2repo/Parcial_2/archivos/jugadores.json",nombre_recibido) == True:
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
                        input_activado = False
                        click = "False"
                    else:
                        if len(nombre_recibido) <= 8:
                            nombre_recibido += evento.unicode
                        else:
                            nombre_recibido = nombre_recibido

        ventana_menu_dibujar_todo(ventana,titulo,boton_play,boton_play_rect,nombre_recibido,font_nombre_texto,click)
        pygame.display.update() #aca se va actuializando

##################################################################################################################################
def ventana_de_juego(ventana):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("2repo/Parcial_2/music/RELOJ.mp3")
    pygame.mixer.music.set_volume(0.5)
    lista_preguntas = []
    lista_correctas = []

    leer_del_csv("2repo/Parcial_2/archivos/preguntas.csv",lista_preguntas,lista_correctas)

    for i in range(len(lista_preguntas)):
        font_pregunta = pygame.font.Font("2repo/Parcial_2/fonts/Pixel12x10Mono-v1.1.0.ttf", 30)
        texto_pregunta = font_pregunta.render(lista_preguntas[i],True,NEGRO)
        box_opciones_rect = box_no_seleccionada.get_rect()

        font_cronometro = pygame.font.Font("2repo/Parcial_2/fonts/Retro Gaming.ttf", 20)
        clock = pygame.time.Clock() #se nivelan los fps
        tiempo_incial = 30000
        tiempo_referencia = pygame.time.get_ticks()
        bandera_reloj = False
        
        fuente = pygame.font.Font("2repo\\Parcial_2\\fonts\\Retro Gaming.ttf",25)

        ubicacion_seleccionada = None
        bandera = True
        while bandera:
            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                print(evento)
                if evento.type == pygame.QUIT:
                    bandera = False
                    return False
                elif evento.type == pygame.MOUSEMOTION:
                    mouse_x,mouse_y = evento.pos
                    ubicacion_seleccionada = None
                    for (ubicacion_x,ubicacion_y) in ubicaciones:
                        box_opciones_rect = box_no_seleccionada.get_rect(topleft=(ubicacion_x,ubicacion_y))
                        if (mouse_x <= (box_opciones_rect.x + box_opciones_rect.width) and mouse_x >= box_opciones_rect.x) and (mouse_y <= (box_opciones_rect.y + box_opciones_rect.height) and mouse_y >= box_opciones_rect.y):
                            ubicacion_seleccionada = (ubicacion_x,ubicacion_y)
                            break
            
            tiempo_actual = pygame.time.get_ticks()
            if bandera_reloj == False:
                tiempo_trascurrido = (tiempo_incial - (tiempo_actual - tiempo_referencia))/1000
                tiempo_trascurrido = round(tiempo_trascurrido)
                tiempo_trascurrido = str(tiempo_trascurrido) #PARA PODER PONERLE UN FUENTE A ELECCION
                if tiempo_trascurrido == "8":
                    pygame.mixer.music.play(0)
                elif tiempo_trascurrido == "0":
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("2repo/Parcial_2/music/GAMEOVER.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play(0,0,0)
                    bandera_reloj = True
            else:
                tiempo_trascurrido = "0"
                pygame.time.delay(5000)
                break
            
            if int(tiempo_trascurrido) >= 9:
                color_cronometro = NEGRO
            else:
                color_cronometro = RED

            texto_cronometro = font_cronometro.render(tiempo_trascurrido, True, color_cronometro)


            ventana_juego_dibujar_todo(ventana,box_seleccionada,box_no_seleccionada,ubicacion_seleccionada,texto_cronometro,bandera_reloj,texto_pregunta)

            y_de_matriz_score = 202
            x_matriz_score= 979
            for i in range(len(lista_premios)):
                texto = fuente.render(lista_premios[i][1], False, NEGRO)
                ventana.blit(texto,(x_matriz_score,y_de_matriz_score))
                y_de_matriz_score += 53

            clock.tick(60)
            pygame.display.update()