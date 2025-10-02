# Importar pygame
import pygame
import sys
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

#Imagenes
background = pygame.image.load("nivel1.png")
personaje = pygame.image.load("personaje_default.png")

# Posicion del personaje
personaje_x = 115
personaje_y = 525

# Velocidad del personaje
velocidad = 10

# Bucle del juego
while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# Variable para detectar las teclas que se presionan
      teclas = pygame.key.get_pressed()
# Movimiento del personajito con las teclas
      if teclas[pygame.K_LEFT]:
            personaje_x -= velocidad
        
      if teclas[pygame.K_RIGHT]:
            personaje_x += velocidad

      if teclas[pygame.K_UP]:
            personaje_y -= velocidad

      if teclas[pygame.K_DOWN]:
            personaje_y += velocidad


# Imagen de fondo a la pantalla
      screen.blit(background, (0, 0))

        
# Dibujar personaje
      screen.blit(personaje, (personaje_x, personaje_y))

# Actualizar pantalla
      pygame.display.flip()