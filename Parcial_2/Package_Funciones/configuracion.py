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
musica_ganador = pygame.mixer.Sound(path + "music/GANADOR_FINAL.mp3")
musica_tabla_puntos = pygame.mixer.Sound(path + "music/TABLA_PUNTOS.mp3")
################################
# CONFIGURACION DE VENTANA
ventana_ancho = 1200 # X
ventana_alto = 800 # Y
ventana_dimensiones = (ventana_ancho,ventana_alto)
################################
# CONFIGURACION DE TITULO
titulo_ancho = 500
titulo_alto = 320
dimensiones_titulo = (titulo_ancho,titulo_alto)
################################
# CONFIGURACION DE BOTONES
boton_play_normal_ancho = 125
boton_play_normal_alto = 125
dimnesiones_boton_normal = (boton_play_normal_ancho,boton_play_normal_alto)

boton_play_grande_ancho = 150
boton_play_grande_alto = 150
dimensiones_boton_grande = (boton_play_grande_ancho,boton_play_grande_alto)
################################
# CONFIGURACION DE RECTANGULO INGRESAR NOMBRE
rect_x = 480
rect_y = 500
rect_ancho = 200
rect_alto = 50
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
    ["0", " $0", 0]
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
                    '2repo/Parcial_2/imagenes/tabla12.png',
                    'FIN_PREGUNTAS']
################################
# CARGA DE IMGS:
titulo = pygame.image.load("2repo/Parcial_2/imagenes/titulo.png")
titulo = pygame.transform.scale(titulo, dimensiones_titulo)

boton_play_normal = pygame.image.load("2repo/Parcial_2/imagenes/botonjugar.png")
boton_play_normal = pygame.transform.scale(boton_play_normal, dimnesiones_boton_normal)

font_nombre_texto = pygame.font.Font(path + "fonts/Retro Gaming.TTF",25)
font_texto_error = pygame.font.Font(path + "fonts/Retro Gaming.TTF",18)
texto_ingresar_nombre = font_nombre_texto.render("INGRESA TU NOMBRE",True,NEGRO)
texto_ingresar_nombre2 = font_nombre_texto.render("INGRESA TU NOMBRE",True,VERDE_PASTEL)
texto_nombre_repetido = font_texto_error.render("ESE NOMBRE YA EXISTE!",True,ROJO_FUERTE)
texto_nombre_repetido2 = font_texto_error.render("ESE NOMBRE YA EXISTE!",True,BLANCO)

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

cuadro_dinero = pygame.image.load(path + "imagenes/dinerocuadro.png")
cuadro_dinero = pygame.transform.scale(cuadro_dinero,(230,100))

font_dinero = pygame.font.Font(path + "fonts/prstartk.ttf",15)

globo_mensaje = pygame.image.load(path + "imagenes/globomensaje.png")
globo_mensaje = pygame.transform.scale(globo_mensaje, (180,120))

box_pregunta = pygame.image.load("2repo/Parcial_2/imagenes/pregunta.png")
box_pregunta = pygame.transform.scale(box_pregunta,(500,106))
#####################################################
# OPCION DE RETIRARSE CONFIGURACIONES:
ancho_boton = 50
alto_boton = 30
dimensiones_botones_sino = (ancho_boton,alto_boton)

font_globito = pygame.font.Font(path + "fonts/prstartk.ttf",10)

opcion_si_globo_normal = pygame.image.load(path + "imagenes/opcionsi.png")
opcion_si_globo_normal = pygame.transform.scale(opcion_si_globo_normal,dimensiones_botones_sino)

opcion_si_globo_presionado = pygame.image.load(path + "imagenes/opcionsi_presionado.png")
opcion_si_globo_presionado = pygame.transform.scale(opcion_si_globo_presionado,dimensiones_botones_sino)

opcion_no_globo_normal = pygame.image.load(path + "imagenes/opcionno.png")
opcion_no_globo_normal = pygame.transform.scale(opcion_no_globo_normal,dimensiones_botones_sino)

opcion_no_globo_presionado = pygame.image.load(path + "imagenes/opcionno_presionado.png")
opcion_no_globo_presionado = pygame.transform.scale(opcion_no_globo_presionado,dimensiones_botones_sino)

####################################################
# CONFIGURACIONES PANTALLA PUNTOS:

boton_menu = pygame.image.load(path + "imagenes/boton_menu.png")
boton_menu_ancho = 75
boton_menu_alto = 40
dimensiones_boton_menu = (boton_menu_ancho,boton_menu_alto)
boton_menu = pygame.transform.scale(boton_menu, dimensiones_boton_menu)

boton_salir = pygame.image.load(path + "imagenes/boton_salir.png")
boton_salir_ancho = 75
boton_salir_alto = 40
dimensiones_boton_salir = (boton_salir_ancho,boton_salir_alto)
boton_salir = pygame.transform.scale(boton_salir, dimensiones_boton_salir)

fuente_opciones = pygame.font.Font(path + "fonts/prstartk.ttf", 15)
texto_opciones = fuente_opciones.render("¡CLICKE ALGUN BOTON!",True,NEGRO)
fuente_texto = pygame.font.Font(path + "fonts/prstartk.ttf", 10)
texto_volver_menu = fuente_texto.render("MENU",True,VERDE)
texto_salir = fuente_texto.render("SALIR",True,ROJO)

####################################################
# CONFIGURACIONES GANADOR:
fuente_you_fin = pygame.font.Font(path + "fonts/upheavtt.ttf", 90)

fondo_ganador = pygame.image.load(path + "imagenes/pantallaganador.png")
fondo_ganador = pygame.transform.scale(fondo_ganador, ventana_dimensiones)

texto_you_win = fuente_you_fin.render("YOU WIN", False, AMARILLO_DORADO)

boton_scores = pygame.image.load(path + "imagenes/boton_score.png")
boton_scores_ancho = 300
boton_scores_alto = 140
dimensiones_boton_scores = (boton_scores_ancho,boton_scores_alto)
boton_scores = pygame.transform.scale(boton_scores, dimensiones_boton_scores)

fuente_puntos = pygame.font.Font(path + "fonts/upheavtt.ttf", 15)
texto_puntos = fuente_puntos.render("Puntos", False, BEIGE)
####################################################