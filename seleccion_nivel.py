import pygame
import os

pygame.init()
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "sonido_click.wav"))
click_sound.set_volume(0.5)


# ----------- Clase Button -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound=None):
        self.rect = pygame.Rect(rect)
        self.normal = pygame.image.load(normal_path).convert_alpha()
        self.hover = pygame.image.load(hover_path).convert_alpha()
        self.action = action
        self.sound = sound

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.sound:
                self.sound.play()
            return self.action
        return None


# ----------- Clase Selección de Nivel -----------
class Seleccion_nivel:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True

        self.idioma = idioma_actual
        self.volumen = volumen_actual

        # Fuentes
        try:
            self.font_boton = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 19)
        except:
            self.font_boton = pygame.font.Font(None, 40)

        try:
            self.font_titulo = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf"), 66)
        except:
            self.font_titulo = pygame.font.Font(None, 60)

        # ------- FONDO ANIMADO --------
        self.fondo = pygame.image.load(os.path.join(
            BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "BUB.png"
        )).convert_alpha()

        self.fondo_x = 0
        self.fondo_vel = 0.1

        # Fondo adelante
        self.fondo_frente = pygame.image.load(os.path.join(
            BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "selenive.png"
        )).convert_alpha()

        # Botones
        self.botones = [
            Button((175, 345, 213, 84),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel1.png"),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel1_hover.png"),
                "nivel1", click_sound),

            Button((409, 345, 213, 84),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel2.png"),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel2_hover.png"),
                "nivel2", click_sound),

            Button((634, 345, 213, 84),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel3.png"),
                os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones",
                             "boton_interfaz_eleguir_nivel_nivel3_hover.png"),
                "nivel3", click_sound),

            Button((58, 40, 120, 67),
                os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),
                os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),
                "seleccion_dificultad", click_sound)
        ]

    # -------- eventos --------
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"

        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion

    # -------- update fondo --------
    def update(self):
        self.fondo_x += self.fondo_vel

        if self.fondo_x > self.fondo.get_width():
            self.fondo_x = 0

    # -------- draw --------
    def draw(self):
        # ------- DIBUJAR FONDO ANIMADO --------
        self.screen.blit(self.fondo, (self.fondo_x, 0))
        self.screen.blit(self.fondo, (self.fondo_x - self.fondo.get_width(), 0))

        # ------- DIBUJAR FONDO ADELANTE --------
        self.screen.blit(self.fondo_frente, (0, 0))

        # ------- DIBUJAR BOTONES --------
        for boton in self.botones:
            boton.draw(self.screen)

        # ------- AHORA SÍ: TEXTO ARRIBA DEL TODO --------
        titulo = "LEVEL SELECTION" if self.idioma == "en" else "SELECCIÓN DE NIVEL"
        self.screen.blit(self.font_titulo.render(titulo, True, (0, 0, 0)), (290, 120))

        # Etiquetas de los botones
        for boton in self.botones:
            if boton.action == "seleccion_dificultad":
                self.screen.blit(self.font_boton.render("VOLVER" if self.idioma=="es" else "BACK", True, (0,0,0)), (78, 55))
            if boton.action == "nivel1":
                self.screen.blit(self.font_boton.render("NIVEL 1" if self.idioma=="es" else "LEVEL 1", True, (0,0,0)), (204, 369))
            if boton.action == "nivel2":
                self.screen.blit(self.font_boton.render("NIVEL 2" if self.idioma=="es" else "LEVEL 2", True, (0,0,0)), (438, 369))
            if boton.action == "nivel3":
                self.screen.blit(self.font_boton.render("NIVEL 3" if self.idioma=="es" else "LEVEL 3", True, (0,0,0)), (663, 369))

    # -------- loop --------
    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio

            self.update()
            self.draw()
            pygame.display.flip()
