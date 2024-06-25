import pygame
from .colores import *
pygame.init()

################################
# PATH:
path = "2repo/Parcial_2/"
################################
# MUSICAS DEL JUEGO
musica_menu = pygame.mixer.Sound(path + "music/MENU.mp3")
sonido_gameover = pygame.mixer.Sound(path + "music/GAMEOVER.mp3")
musica_juego = pygame.mixer.Sound(path + "music/ENJUEGO.mp3")
seleccion_opcion = pygame.mixer.Sound(path + "music/SELECCION_MENU.mp3")
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
# CONFIGURACION DE RECTANGULO INGRESAR NOMBRE
rect_x = 478
rect_y = 500
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
    ["12", "  1 Millon", 1000000],
    ["11", "$800.000", 800000],
    ["10", "$650.000", 650000],
    ["9", "$500.000", 500000],
    ["8", "$350.000", 350000],
    ["7", "$300.000", 300000],
    ["6", "$200.000", 200000],
    ["5", "$150.000", 150000],
    ["4", "$100.000", 100000],
    ["3", "$75.000", 75000],
    ["2", "$50.000", 50000],
    ["1", " $10.000", 10000],
]
################################
tablas_dinero = ['2repo/Parcial_2/imagenes/tabla.png',
                    '2repo/Parcial_2/imagenes/tabla2.png',
                    '2repo/Parcial_2/imagenes/tabla3.png',
                    '2repo/Parcial_2/imagenes/tabla4.png',
                    '2repo/Parcial_2/imagenes/tabla5.png',
                    '2repo/Parcial_2/imagenes/tabla6.png',
                    '2repo/Parcial_2/imagenes/tabla7.png',
                    '2repo/Parcial_2/imagenes/tabla8.png',
                    '2repo/Parcial_2/imagenes/tabla9.png',
                    '2repo/Parcial_2/imagenes/tabla10.png',
                    '2repo/Parcial_2/imagenes/tabla11.png',
                    '2repo/Parcial_2/imagenes/tabla12.png']
################################
# CARGA DE IMGS:
titulo = pygame.image.load("2repo/Parcial_2/imagenes/titulo.png")
titulo = pygame.transform.scale(titulo, dimensiones_titulo)

boton_play_normal = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
boton_play_normal = pygame.transform.scale(boton_play_normal, dimnesiones_boton_normal)

font_nombre_texto = pygame.font.Font(path + "fonts/Retro Gaming.TTF",25)
texto_ingresar_nombre = font_nombre_texto.render("INGRESA TU NOMBRE",True,NEGRO)
texto_nombre_repetido = font_nombre_texto.render("ESE NOMBRE YA EXISTE!",True,RED)

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

CRONOMETRO_imagen = pygame.image.load("2repo/Parcial_2/imagenes/cronometro.png")#hace que no se acumulen las cosas
CRONOMETRO_imagen = pygame.transform.scale(CRONOMETRO_imagen,(90,110))

fuente = pygame.font.Font(path + "fonts/Retro Gaming.ttf", 25)
titulo_premios = fuente.render("PREMIOS",True,NEGRO)
################################