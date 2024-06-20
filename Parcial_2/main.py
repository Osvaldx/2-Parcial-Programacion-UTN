from Package_Funciones.funciones import *

pygame.init()

ventana = pygame.display.set_mode(ventana_dimensiones)
pygame.display.set_caption("MILLONES")

logo = pygame.image.load("2repo/Parcial_2/imagenes/dolar.png")
pygame.display.set_icon(logo)
###########################################
menu_de_juego = ventana_principal(ventana)

if menu_de_juego == True:
    ventana_de_juego(ventana)

###########################################

pygame.quit()