from Package_Funciones.funciones import *

pygame.init()

ventana = pygame.display.set_mode(ventana_dimensiones)
pygame.display.set_caption("MILLONES")

logo = pygame.image.load("2repo/Parcial_2/imagenes/dolar.png")
pygame.display.set_icon(logo)
###########################################
while True:
    menu_juego = ventana_menu(ventana)
    if menu_juego == True:
        juego_continuar = ventana_de_juego(ventana)
    else:
        break
###########################################

pygame.quit()