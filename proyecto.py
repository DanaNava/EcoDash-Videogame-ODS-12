# main_menu.py
import pygame
import sys
import math

pygame.init()
pygame.mixer.init()

# Sonido de clic
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click_main.wav")
click_sound.set_volume(0.5)

# Ventana
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

# Fondos
background = pygame.image.load("assets_PI/interfaces/Fondo_animado/azul.png").convert_alpha()
nubes = pygame.image.load("assets_PI/interfaces/Fondo_animado/nubes.png").convert_alpha()
verde = pygame.image.load("assets_PI/interfaces/Fondo_animado/verdee.png").convert_alpha()
ecodash = pygame.image.load("assets_PI/interfaces/Fondo_animado/ecodash.png").convert_alpha()  # logo

# Botones
start_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_play_interfaz_main.png")
start_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_play_hover.png")
tutorial_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_tutorial.png")
tutorial_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_tutorial_hover.png")
configuracion_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_ajustes.png")
configuracion_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_ajustes_hover.png")
creditos_img = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_creditos.png")
creditos_hover = pygame.image.load("assets_PI/interfaces/main/botones/boton_interfaz_main_creditos_hover.png")


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


class Main:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.idioma = idioma_actual
        self.volumen = volumen_actual

        self.start_button = Button(403, 315, start_img, start_hover)
        self.tutorial_button = Button(404, 537, tutorial_img, tutorial_hover)
        self.configuracion_button = Button(10, 666, configuracion_img, configuracion_hover)
        self.creditos_button = Button(925, 676, creditos_img, creditos_hover)
        self.background = background

    def run(self):
        # Variables nubes
        nubes_x = 0
        velocidad_nubes = 1

        # Variables logo (movimiento seno)
        logo_center_y = 3       # Posición vertical central del logo
        logo_amplitud = 15       # Cuánto sube y baja desde la posición central
        logo_speed = 0.02         # Velocidad del movimiento
        tiempo = 0                # Contador de tiempo para el seno

        clock = pygame.time.Clock()

        while True:
            pos_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "salir"

                if self.start_button.clicked(event):
                    click_sound.play()
                    return "select_character"

                if self.tutorial_button.clicked(event):
                    return "tutorial"

                if self.configuracion_button.clicked(event):
                    return "configuracion"

                if self.creditos_button.clicked(event):
                    return "creditos"

            # --- Mover nubes ---
            nubes_x += velocidad_nubes
            if nubes_x >= nubes.get_width():
                nubes_x = 0

            # --- Movimiento vertical logo con seno ---
            logo_y = logo_center_y + logo_amplitud * math.sin(tiempo)
            tiempo += logo_speed

            # --- Dibujar fondos ---
            self.screen.blit(background, (0, 0))
            self.screen.blit(nubes, (nubes_x - nubes.get_width(), 0))
            self.screen.blit(nubes, (nubes_x, 0))
            self.screen.blit(verde, (0, 0))

            # --- Dibujar logo ecodash ---
            self.screen.blit(ecodash, (512 - ecodash.get_width() // 2, logo_y))

            # --- Botones ---
            self.start_button.draw(self.screen, pos_mouse)
            self.tutorial_button.draw(self.screen, pos_mouse)
            self.configuracion_button.draw(self.screen, pos_mouse)
            self.creditos_button.draw(self.screen, pos_mouse)

            pygame.display.flip()
            clock.tick(60)
