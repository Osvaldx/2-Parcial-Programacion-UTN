from .funciones_especificas import *
from .validaciones import *
import pygame

##################################################################################################################################
def ventana_menu(ventana:tuple)->bool:
    musica_juego.stop()
    musica_menu.set_volume(0.3)
    musica_menu.play(-1)

    boton_play = boton_play_normal
    boton_play_rect = boton_play.get_rect()
    boton_play_rect.topleft = (515,600)
    input_activado = False

    nombre_recibido = ""

    pos_x = 0
    pos_y = 0
    
    bandera = True
    retorno = None
    click = "False"
    while bandera:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                bandera = False

            elif evento.type == pygame.MOUSEMOTION:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]
                if (pos_x >= boton_play_rect.x and pos_x <= (boton_play_rect.x + boton_play_rect.width)) and (pos_y >= boton_play_rect.y and pos_y <= (boton_play_rect.y + boton_play_rect.width)):
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
                if (pos_x >= boton_play_rect.x and pos_x <= (boton_play_rect.x + 125)) and (pos_y >= boton_play_rect.y and pos_y <= (boton_play_rect.y + 125)):
                    if validar_nombre(path + "archivos/jugadores.json",nombre_recibido) == True:
                        crear_json_players(path + "archivos/jugadores.json",nombre_recibido)
                        bandera = False
                        retorno = True
                        return retorno,nombre_recibido
                    else:
                        click = "AusenciaNICK"
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if (pos_x >= rect_x and pos_x <= (rect_x + rect_width)) and (pos_y >= rect_y and pos_y <= (rect_y + rect_high)):
                    input_activado = True
                    click = "True"
            elif evento.type == pygame.KEYDOWN:
                if input_activado == True:
                    if evento.key == pygame.K_BACKSPACE:
                        longitud_nombre = len(nombre_recibido)
                        nombre_recibido = nombre_recibido[0:longitud_nombre - 1]
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
        
    return retorno,nombre_recibido
##################################################################################################################################
def ventana_de_juego(ventana,nombre_recibido):
    musica_menu.stop()
    musica_juego.set_volume(0.15)
    musica_juego.play(-1)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path + "music/RELOJ.mp3")
    pygame.mixer.music.set_volume(0.5)
    seleccion_opcion.set_volume(0.5)

    lista_preguntas = []
    lista_respuesta = []

    leer_del_csv(path + "archivos/preguntas.csv", lista_preguntas, lista_respuesta)

    opcion_si_globo_normal_rect = opcion_si_globo_normal.get_rect()
    opcion_si_globo_normal_rect.topleft = (610,255)

    opcion_no_globo_normal_rect = opcion_no_globo_normal.get_rect()
    opcion_no_globo_normal_rect.topleft = (690,255)

    retorno = None
    retirarse = False
    for i in range(len(lista_preguntas)):
        longitud_premios = len(lista_premios)
        digito_banco = lista_premios[longitud_premios -i -1][1]
        tiempo_record = 0
        ubicacion_respuesta_elegida = None
        paso_nivel = False
        font_pregunta = pygame.font.Font(path + "fonts/prstartk.ttf", 16)

        texto_de_pregunta = dividir_texto(lista_preguntas[i])
        texto_pregunta_dividido_1 = font_pregunta.render(texto_de_pregunta[0], True, NEGRO)
        texto_pregunta_dividido_2 = font_pregunta.render(texto_de_pregunta[1], True, NEGRO)

        box_opciones_rect = box_no_seleccionada.get_rect()

        texto_opciones = lista_respuesta[i]
        opcion_respuesta = lista_respuesta[i][3]
        lista_texto_copia = texto_opciones.copy()
        lista_ubicaciones_fijas = []
        
        tabla_dinero = pygame.image.load(tablas_dinero[i])

        for j in range(len(ubicaciones)):
            opcion_random = random.choice(lista_texto_copia)
            slots = (ubicaciones[j], opcion_random)
            lista_ubicaciones_fijas.append(slots)
            lista_texto_copia.remove(opcion_random)

        font_cronometro = pygame.font.Font(path + "fonts/Retro Gaming.ttf", 20)
        clock = pygame.time.Clock()  # se nivelan los fps
        tiempo_incial = 30000
        tiempo_referencia = pygame.time.get_ticks()
        bandera_reloj = False

        ubicacion_seleccionada = None
        contador_musica = 0
        opcion_si_seleccionado = False
        opcion_no_seleccionado = False
        bandera = True
        while bandera:
            lista_eventos = pygame.event.get()
            for evento in lista_eventos:
                if evento.type == pygame.QUIT:
                    retorno = False
                    bandera = False
                elif evento.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = evento.pos
                    ubicacion_seleccionada = None
                    for (ubicacion_x, ubicacion_y) in ubicaciones:
                        box_opciones_rect = box_no_seleccionada.get_rect(topleft=(ubicacion_x, ubicacion_y))
                        if (mouse_x >= box_opciones_rect.x and mouse_x <= (box_opciones_rect.x + box_opciones_rect.width)) and (mouse_y >= box_opciones_rect.y and mouse_y <= (box_opciones_rect.y + box_opciones_rect.height)):
                            ubicacion_seleccionada = (ubicacion_x,ubicacion_y)
                            break

                    if ubicacion_seleccionada != None:
                        contador_musica += 1
                        if contador_musica == 1:
                            seleccion_opcion.play(0)
                    else:
                        contador_musica = 0

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if (mouse_x >= box_opciones_rect.x and mouse_x <= (box_opciones_rect.x + box_opciones_rect.width)) and (mouse_y >= box_opciones_rect.y and mouse_y <= (box_opciones_rect.y + box_opciones_rect.height)):
                        ubicacion_respuesta_elegida = (ubicacion_x, ubicacion_y)
                    if retirarse == True:
                        if (mouse_x >= opcion_si_globo_normal_rect.x and mouse_x <= (opcion_si_globo_normal_rect.x + opcion_si_globo_normal_rect.width)) and (mouse_y >= opcion_si_globo_normal_rect.y and mouse_y <= (opcion_si_globo_normal_rect.y + opcion_si_globo_normal_rect.height)):
                            opcion_si_seleccionado = True
                        if (mouse_x >= opcion_no_globo_normal_rect.x and mouse_x <= (opcion_no_globo_normal_rect.x + opcion_no_globo_normal_rect.width)) and (mouse_y >= opcion_no_globo_normal_rect.y and mouse_y <= (opcion_no_globo_normal_rect.y + opcion_no_globo_normal_rect.height)):
                            opcion_no_seleccionado = True

                elif evento.type == pygame.MOUSEBUTTONUP:
                    if retirarse == True:
                        if (mouse_x >= opcion_si_globo_normal_rect.x and mouse_x <= (opcion_si_globo_normal_rect.x + opcion_si_globo_normal_rect.width)) and (mouse_y >= opcion_si_globo_normal_rect.y and mouse_y <= (opcion_si_globo_normal_rect.y + opcion_si_globo_normal_rect.height)):
                            opcion_si_seleccionado = False
                            return True
                        if (mouse_x >= opcion_no_globo_normal_rect.x and mouse_x <= (opcion_no_globo_normal_rect.x + opcion_no_globo_normal_rect.width)) and (mouse_y >= opcion_no_globo_normal_rect.y and mouse_y <= (opcion_no_globo_normal_rect.y + opcion_no_globo_normal_rect.height)):
                            opcion_no_seleccionado = False
                            retirarse = False
                            tiempo_referencia = pygame.time.get_ticks()

            
            tiempo_actual = pygame.time.get_ticks()
            if bandera_reloj == False or bandera_reloj == "fallo":
                tiempo_trascurrido = (tiempo_incial - (tiempo_actual - tiempo_referencia)) // 1000
                tiempo_trascurrido = str(tiempo_trascurrido)  # PARA PODER PONERLE UN FUENTE A ELECCION
                if tiempo_trascurrido == "8":
                    pygame.mixer.music.play(0)
                elif tiempo_trascurrido == "0" or bandera_reloj == "fallo":
                    musica_juego.stop()
                    pygame.mixer.music.stop()
                    sonido_gameover.set_volume(1.0)
                    sonido_gameover.play(0)
                    bandera_reloj = True
            else:
                tiempo_trascurrido = "0"
                pygame.time.delay(5000)
                bandera = False
                retorno = True
            
            if int(tiempo_trascurrido) >= 9:
                color_cronometro = NEGRO
            else:
                color_cronometro = RED

            texto_cronometro = font_cronometro.render(tiempo_trascurrido, True, color_cronometro)
            tiempo_record = tiempo_trascurrido

            siguiente_nivel = ventana_juego_dibujar_todo(ventana, box_seleccionada, box_no_seleccionada, ubicacion_seleccionada, texto_cronometro, bandera_reloj, texto_pregunta_dividido_1,texto_pregunta_dividido_2, lista_ubicaciones_fijas, ubicacion_respuesta_elegida, opcion_respuesta, tabla_dinero, digito_banco, retirarse, opcion_si_seleccionado, opcion_no_seleccionado)
            y_de_matriz_score = 102
            x_matriz_score = 979
            for k in range(len(lista_premios) -1):
                texto = fuente.render(lista_premios[k][1], False, NEGRO)
                if bandera_reloj == False:
                    ventana.blit(texto, (x_matriz_score, y_de_matriz_score))
                y_de_matriz_score += 53

            if siguiente_nivel == True:
                longitud = len(lista_premios)
                indice = longitud -i -1 -1 # se duplica el -1 debido a que el banco y la lista de premios tiene $0 la ultima
                actualizacion_puntos(path + "archivos/jugadores.json",lista_premios[indice][2],nombre_recibido,tiempo_record,tiempo_incial)
                paso_nivel = True
                bandera = False
                pygame.mixer.music.stop()
                retirarse = True
            elif siguiente_nivel == "equivocado":
                bandera_reloj = "fallo"

            clock.tick(120)
            pygame.display.update()
            ubicacion_respuesta_elegida = None
        
        if paso_nivel == False:
            return retorno