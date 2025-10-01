# Para iniciar cualquier proyecto en pygame 
import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

#posiciones
posiciones = [443, 675]  # coordenadas X para cada personaje
indice_actual = 0  # empieza en el primer personaje

#imagenes
background = pygame.image.load("select_character_background.png")
next_interface = pygame.image.load("next_button.png")
next_interface_hover = pygame.image.load("next_buttonh.png")
select = pygame.image.load("select.png")

# clase boton para la flechita
class Button():
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, pos_mouse):
       if self.rect.collidepoint(pos_mouse):
           screen.blit(self.image_hover, self.rect)
       else:
        screen.blit(self.image, (self.rect.x, self.rect.y))

next_button = Button(906, 670, next_interface, next_interface_hover)

# clase boton para el selector de personaje
class Button2():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

select_button = Button2(432, 297, select)


while True:
    #Obtener posicion del mouse
    pos_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                indice_actual = (indice_actual + 1) % len(posiciones)
            elif event.key == pygame.K_LEFT:
                indice_actual = (indice_actual - 1) % len(posiciones)

    select_button.rect.x = posiciones[indice_actual]
    screen.blit(background, (0, 0))

    #Dibujar el botoncito
    next_button.draw(pos_mouse)
    select_button.draw()
    # Actualizar pantalla
    pygame.display.flip()