from Package_Funciones.funciones import *

pygame.init()

alto = 800 # Y
ancho = 1200 # X
dimensiones = (ancho, alto)

ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("MILLONES")

logo = pygame.image.load("2repo/Parcial_2/imagenes/dolar.png")
pygame.display.set_icon(logo)

###########################################
menu_de_juego = ventana_principal(ventana)

if menu_de_juego == True:
    ventana_de_juego(ventana)

###########################################

pygame.quit()