# select_character_menu.py
import pygame
import sys

pygame.init()
pygame.mixer.init()
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
click_sound.set_volume(0.5)

# Crear ventana
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

# Clase general para botones
class Button:
    def __init__(self, x, y, image, image_hover=None, sound=None, action=None):
        self.image = image
        self.image_hover = image_hover if image_hover else image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = sound
        self.action = action  # ESTA ES LA CLAVE

    def draw(self, screen, pos_mouse=None):
        if pos_mouse and self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.sound:
                self.sound.play()
            return self.action  # DEVUELVE LA ACCIÓN
        return None


class Select_character:
    def __init__(self, screen):
        self.screen = screen
        self.posiciones = [443, 675]
        self.indice_actual = 0
        self.personaje_seleccionado = None

        # Cargar imágenes
        self.background = pygame.image.load("assets_PI/interfaces/eleguir_personaje/fondo/select_character_background.png")
        self.next_img = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/next_button.png")
        self.next_hover = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/next_buttonh.png")
        self.select_img = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/select.png")
        self.back = pygame.image.load("assets_PI/sprites/boton_back.png")
        self.back_hover = pygame.image.load("assets_PI/sprites/boton_back_hover.png")

        # Botones con acciones reales
        self.next_button = Button(906, 670, self.next_img, self.next_hover, click_sound, action="seleccion_dificultad")
        self.back_button = Button(0, 2, self.back, self.back_hover, click_sound, action="main")
        self.select_button = Button(self.posiciones[self.indice_actual], 297, self.select_img, None, click_sound, action="seleccion_personaje")

    def run(self):
        running = True
        while running:
            pos_mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Botones
                result = self.next_button.clicked(event) or self.back_button.clicked(event) or self.select_button.clicked(event)
                if result:
                    return result  # AHORA DEVUELVE LA ACCIÓN CORRECTAMENTE

                # Mover selector con teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.indice_actual = (self.indice_actual + 1) % len(self.posiciones)
                    elif event.key == pygame.K_LEFT:
                        self.indice_actual = (self.indice_actual - 1) % len(self.posiciones)
                    elif event.key == pygame.K_RETURN:
                        self.personaje_seleccionado = self.indice_actual
                        print(f"Personaje {self.personaje_seleccionado + 1} seleccionado!")

            # Actualiza botón select visualmente
            self.select_button.rect.x = self.posiciones[self.indice_actual]

            # Dibujar
            self.screen.blit(self.background, (0, 0))
            self.next_button.draw(self.screen, pos_mouse)
            self.back_button.draw(self.screen, pos_mouse)
            self.select_button.draw(self.screen)

            pygame.display.flip()
