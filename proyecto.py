# main_menu.py
import pygame
import sys

pygame.init()

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)

# Crear ventana
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

# Cargar imágenes
background = pygame.image.load("assets_PI/interfaces/main/fondo/background1.png").convert()
background = pygame.transform.scale(background, (1024, 768))

start_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_play_interfaz_main.png")
start_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_play_hover.png")
tutorial_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_tutorial.png")
tutorial_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_tutorial_hover.png")
configuracion_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_ajustes.png")
configuracion_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_ajustes_hover.png")
creditos_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_creditos.png")
creditos_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_creditos_hover.png")


# Clase general para botones
class Button:
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)


# Clase principal de la interfaz
class Main:
    def __init__(self, screen):
        self.screen = screen
        self.start_button = Button(403, 315, start_img, start_hover)
        self.tutorial_button = Button(404, 537, tutorial_img, tutorial_hover)
        self.configuracion_button = Button(10, 666, configuracion_img, configuracion_hover)
        self.creditos_button = Button(925, 676, creditos_img, creditos_hover)
        self.background = background

    def run(self):
        while True:
            pos_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "salir"

                if self.start_button.clicked(event):
                    return "select_character"

                if self.tutorial_button.clicked(event):
                    return "tutorial"

                if self.configuracion_button.clicked(event):
                    return "configuracion"

                if self.creditos_button.clicked(event):
                    return "creditos"

            # Dibujar fondo y botones
            self.screen.blit(self.background, (0, 0))
            self.start_button.draw(self.screen, pos_mouse)
            self.tutorial_button.draw(self.screen, pos_mouse)
            self.configuracion_button.draw(self.screen, pos_mouse)
            self.creditos_button.draw(self.screen, pos_mouse)

            pygame.display.flip()
