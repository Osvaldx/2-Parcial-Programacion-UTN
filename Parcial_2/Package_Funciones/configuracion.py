import pygame
pygame.init()

################################
# CONFIGURACION DE VENTANA
ventana_ancho = 1200 # X
ventana_alto = 800 # Y
ventana_dimensiones = (ventana_ancho,ventana_alto)
################################
# CONFIGURACION DE TITULO
titulo_width = 500
titulo_high = 320
dimensiones_titulo = (titulo_width,titulo_high)
################################
# CONFIGURACION DE BOTONES
boton_play_normal_width = 125
boton_play_normal_high = 125
dimnesiones_boton_normal = (boton_play_normal_width,boton_play_normal_high)

boton_play_grande_width = 150
boton_play_grande_high = 150
dimensiones_boton_grande = (boton_play_grande_width,boton_play_grande_high)
################################
# CONFIGURACION DE RECTANGULO
rect_x = 478
rect_y = 480
rect_width = 200
rect_high = 50
################################
# CONFIGURACION DE RECTANGULOS OPCIONES:
ubicaciones = [
        (600,600),
        (290,600),
        (290,690),
        (600,690),
    ]
################################
# LISTA PREMIOS TABLA
lista_premios = [ 
    ["6", "  1 Millon"],
    ["5", "$800.000"],
    ["4", "$600.000"],
    ["3", "$300.000"],
    ["2", "$100.000"],
    ["1", " $50.000"],
]
################################
# CARGA DE IMGS:
titulo = pygame.image.load("2repo/Parcial_2/imagenes/titulo.png")
titulo = pygame.transform.scale(titulo, dimensiones_titulo)

boton_play_normal = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
boton_play_normal = pygame.transform.scale(boton_play_normal, dimnesiones_boton_normal)

boton_play_grande = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
boton_play_grande = pygame.transform.scale(boton_play_grande, dimensiones_boton_grande)

imagen_de_calavera = pygame.image.load("2repo\Parcial_2\imagenes\calavera.png")
imagen_de_calavera= pygame.transform.scale(imagen_de_calavera, (500, 500))

fuente_game_over = pygame.font.Font("2repo/Parcial_2/fonts/m04.TTF",80)
texto_game_over = fuente_game_over.render("GAME OVER", False, (167,54,0))
texto_game_over = fuente_game_over.render("GAME OVER", False, (255,0,0))

fondo_juego = pygame.image.load("2repo/Parcial_2/imagenes/fondojuego.jpg")
fondo_juego = pygame.transform.scale(fondo_juego, (1000,600))

box_no_seleccionada = pygame.image.load("2repo/Parcial_2/imagenes/opciones.png")
box_no_seleccionada = pygame.transform.scale(box_no_seleccionada, (270,80))

box_seleccionada = pygame.image.load("2repo/Parcial_2/imagenes/opcion_seleccionada.png")
box_seleccionada = pygame.transform.scale(box_seleccionada, (270,80))

box_pregunta = pygame.image.load("2repo/Parcial_2/imagenes/pregunta.png")

CRONOMETRO_imagen = pygame.image.load("2repo/Parcial_2/imagenes/cronometro.png")#hace que no se acumulen las cosas
CRONOMETRO_imagen = pygame.transform.scale(CRONOMETRO_imagen,(90,110))

tabla_dinero = pygame.image.load("2repo/Parcial_2/imagenes/tabla.png")
tabla_dinero = pygame.transform.scale(tabla_dinero, (250,400))

################################