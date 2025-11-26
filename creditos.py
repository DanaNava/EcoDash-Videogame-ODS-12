import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

# Ruta base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sonido click
click_sound_path = os.path.join(BASE_DIR, "assets_PI", "sonidos", "sonido_click.wav")
click_sound = pygame.mixer.Sound(click_sound_path)
click_sound.set_volume(0.5)

# -------- Clase Button --------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound=None):
        self.rect = pygame.Rect(rect)
        try:
            self.normal = pygame.image.load(normal_path).convert_alpha()
            self.hover = pygame.image.load(hover_path).convert_alpha()
        except pygame.error:
            self.normal = pygame.Surface((rect[2], rect[3]))
            self.normal.fill((0,0,0))
            self.hover = self.normal
        self.action = action
        self.sound = sound

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            if self.sound:
                self.sound.play()
            return self.action
        return None

# -------- Clase Créditos --------
class Creditos:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        self.idioma = idioma_actual
        self.volumen = volumen_actual
        pygame.mixer.music.set_volume(self.volumen)

        ancho_ventana, alto_ventana = screen.get_size()

        # --- Fondo BUB ---
        try:
            self.fondo = pygame.image.load("assets_PI/interfaces/Fondo_animado/BUB.png").convert_alpha()
            self.fondo = pygame.transform.scale(self.fondo, (ancho_ventana, alto_ventana))
        except pygame.error:
            self.fondo = pygame.Surface((ancho_ventana, alto_ventana))
            self.fondo.fill((0,0,0))

        # --- Fondo Verdi ---
        try:
            self.fondo_frente = pygame.image.load("assets_PI/interfaces/Fondo_animado/verdi.png").convert_alpha()
            self.fondo_frente = pygame.transform.scale(self.fondo_frente, (ancho_ventana, alto_ventana))
            self.fondo_frente.set_alpha(200)
        except pygame.error:
            self.fondo_frente = pygame.Surface((ancho_ventana, alto_ventana))
            self.fondo_frente.fill((50,50,50))

        # --- Tabla ---
        try:
            self.tabla = pygame.image.load("assets_PI/interfaces/Fondo_animado/tablon.png").convert_alpha()
            self.tabla = pygame.transform.scale(self.tabla, (ancho_ventana, alto_ventana))
        except pygame.error:
            self.tabla = pygame.Surface((ancho_ventana, alto_ventana))
            self.tabla.fill((100,100,100))

        # --- Botón Volver ---
        self.boton_volver = Button(
            (0,2,120,67),
            os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),
            os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),
            "main",
            click_sound
        )

        # --- Fuentes ---
        try:
            self.font_titulo = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf"), 48)
        except:
            self.font_titulo = pygame.font.Font(None, 40)

        try:
            self.font_nombres = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 20)
            self.font_roles = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 11)
            self.font_boton = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 20)
        except:
            self.font_nombres = pygame.font.Font(None, 25)
            self.font_roles = pygame.font.Font(None, 12)
            self.font_boton = pygame.font.Font(None, 20)

        # --- Créditos ---
        self.creditos = [
            ("--------Alan Ibarra --------", "Programador / Diseñador de personajes / Multimedia"),
            ("-----Alejandro Vazquez-----", "Programador / Artista de objetos"),
            ("--------Dana Nava--------", "Programador / Diseñador de interfaz / Director de cinemática"),
            ("-------David Salgado-------", "Diseñador de niveles / Programador / Diseñador de sonido"),
            ("-----Carolina Martínez-----", "Programador / Diseñador UIX / Documentador / Traductor"),
            ("------Cristian Escobar------", "Diseñador de interfaz / Encargado de idioma / Documentador")
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"
        if event.type == pygame.MOUSEBUTTONDOWN:
            accion = self.boton_volver.check_click(event.pos)
            if accion:
                return accion

    def draw(self):
        # Fondo
        self.screen.blit(self.fondo, (0,0))
        self.screen.blit(self.fondo_frente, (0,0))
        self.screen.blit(self.tabla, (0,0))

        # Botón Volver
        self.boton_volver.draw(self.screen)
        texto_boton = "BACK" if self.idioma == "en" else "VOLVER"
        self.screen.blit(self.font_boton.render(texto_boton, True, (0,0,0)), (14,18))

        # ---- TITULO ----
        if self.idioma == "en":
            t1 = "GAME"
            t2 = "DEVELOPERS"
            pos1 = (420, 183)
        else:
            t1 = "DESARROLLADORES"
            t2 = "del JUEGO"
            pos1 = (350, 183)

        surf1 = self.font_titulo.render(t1, True, (0,0,0))
        surf2 = self.font_titulo.render(t2, True, (0,0,0))
        r1 = surf1.get_rect(topleft=pos1)
        r2 = surf2.get_rect(centerx=r1.centerx, top=r1.bottom+5)

        self.screen.blit(surf1, r1)
        self.screen.blit(surf2, r2)

        # ---- NOMBRES Y ROLES ----
        start_y = 300
        spacing = 70

        for i, (nombre, roles) in enumerate(self.creditos):
            nombre_surf = self.font_nombres.render(nombre, True, (0,0,0))
            nombre_rect = nombre_surf.get_rect(center=(512, start_y + i*spacing))
            self.screen.blit(nombre_surf, nombre_rect)

            roles_surf = self.font_roles.render(roles, True, (0,0,0))
            roles_rect = roles_surf.get_rect(center=(512, nombre_rect.bottom + 12))
            self.screen.blit(roles_surf, roles_rect)

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio
            self.draw()
            pygame.display.flip()
            clock.tick(60)
        return "salir"

# -------- Para probar --------
if __name__ == "__main__":
    screen = pygame.display.set_mode((1024,768))
    pygame.display.set_caption("Créditos con fondos y tabla")
    idioma_actual = "es"
    volumen_actual = 0.5

    pantalla_creditos = Creditos(screen, idioma_actual, volumen_actual)
    resultado = pantalla_creditos.run()
    print(f"Cerró con: {resultado}")

    pygame.quit()
    sys.exit()
