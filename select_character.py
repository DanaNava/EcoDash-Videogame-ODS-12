# Para iniciar cualquier proyecto en pygame 
import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

background = pygame.image.load("select_character_background.png")
selector = pygame.image.load("selector_character.png")
selector_hover = pygame.image.load("selector_characterh.png")
nextinterface = pygame.image.load("next_button.png")
nextinterface_hover = pygame.image.load("next_buttonh.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background, (0, 0))

    # Actualizar pantalla
    pygame.display.flip()