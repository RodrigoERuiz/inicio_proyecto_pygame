# import pygame


# ANCHO = 800
# ALTO = 600

# pygame.init()

# ventana_juego = pygame.display.set_mode([ANCHO,ALTO])

# imagen_de_fondo = pygame.image.load('recursos/background.jpg')



# #fundir imagen en pantalla
# ventana_juego.blit(imagen_de_fondo,(50,50))

# #pos_img_tabla_puntajes = (ANCHO - img_tabla.get_witdh) // 2

# # fuente_titulo = pygame.font.Font()
# # txt_titulo = fuente_titulo.render()


# # font = pygame.font.SysFont('Arial Narrow',50)
# # text = font.render("HOLA MUNDO",True, (255, 0, 0))

# pygame.display.flip()

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ventana_ancho = 800
ventana_alto = 600
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Mi Juego Pygame")
imagen_de_fondo = pygame.image.load('recursos/background.jpg')
imagen_escalada = pygame.transform.scale(imagen_de_fondo, (ventana_ancho, ventana_alto))

# Color de fondo
fondo_color = (255, 255, 255)  # Blanco

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica del juego aquí
    ventana.blit(imagen_de_fondo,(0,0))


    # Actualizar la ventana
    pygame.display.flip()
