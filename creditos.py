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

# -------- Clase Créditos con fondos y tabla --------
class Creditos:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        self.idioma = idioma_actual
        self.volumen = volumen_actual
        pygame.mixer.music.set_volume(self.volumen)

        ancho_ventana, alto_ventana = screen.get_size()

        # --- Fondo BUB (atrás) ---
        try:
            fondo_path = r"C:\EcoDash-Videogame-ODS-12\assets_PI\interfaces\Fondo_animado\BUB.png"
            self.fondo = pygame.image.load(fondo_path).convert_alpha()
            self.fondo = pygame.transform.scale(self.fondo, (ancho_ventana, alto_ventana))
        except pygame.error:
            self.fondo = pygame.Surface((ancho_ventana, alto_ventana))
            self.fondo.fill((0,0,0))

        # --- Fondo Verdi (medio) ---
        try:
            fondo_frente_path = r"C:\EcoDash-Videogame-ODS-12\assets_PI\interfaces\Fondo_animado\verdi.png"
            self.fondo_frente = pygame.image.load(fondo_frente_path).convert_alpha()
            self.fondo_frente = pygame.transform.scale(self.fondo_frente, (ancho_ventana, alto_ventana))
            self.fondo_frente.set_alpha(200)  # Transparencia parcial para que se vea BUB
        except pygame.error:
            self.fondo_frente = pygame.Surface((ancho_ventana, alto_ventana))
            self.fondo_frente.fill((50,50,50))

        # --- Tabla (delante) ---
        try:
            tabla_path = r"C:\EcoDash-Videogame-ODS-12\assets_PI\interfaces\Fondo_animado\tablon.png"
            self.tabla = pygame.image.load(tabla_path).convert_alpha()
            self.tabla = pygame.transform.scale(self.tabla, (ancho_ventana, alto_ventana))
            # si quieres ver el fondo detrás de la tabla, ajusta alpha:
            # self.tabla.set_alpha(230)
        except pygame.error:
            self.tabla = pygame.Surface((ancho_ventana, alto_ventana))
            self.tabla.fill((100,100,100))

        # --- Botón de Volver ---
        self.boton_volver = Button(
            (0,2,120,67),
            os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),
            os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),
            "main",
            click_sound
        )

        # Fuentes
        try:
            self.font_titulo = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf"), 48)
        except:
            self.font_titulo = pygame.font.Font(None, 55)

        try:
            self.font_nombres = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 15)
            self.font_boton = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 20)
        except:
            self.font_nombres = pygame.font.Font(None, 36)
            self.font_boton = pygame.font.Font(None, 40)

        # Lista de nombres
        self.nombres = [
            "Ibarra Heredia Alan Alejandro",
            "Nava Montiel Dana Paola",
            "Escobar Núñez Cristian Alexander",
            "Martínez Zúñiga Carolina",
            "Salgado Zepeda David",
            "Vazquez Atanacio Diego Alejandro"
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
        # 1. Fondo BUB (atrás)
        self.screen.blit(self.fondo, (0,0))

        # 2. Fondo Verdi (medio) con transparencia
        self.screen.blit(self.fondo_frente, (0,0))

        # 3. Tabla encima
        self.screen.blit(self.tabla, (0,0))

        # 4. Botón Volver
        self.boton_volver.draw(self.screen)
        texto_boton_str = "BACK" if self.idioma=="en" else "VOLVER"
        texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0,0,0))
        self.screen.blit(texto_boton_surf, (14,18))

        # 5. Título
        if self.idioma=="en":
            titulo_str_1 = "GAME"
            titulo_str_2 = "DEVELOPERS"
            coord_titulo_1 = (420,183)
        else:
            titulo_str_1 = "DESARROLLADORES"
            titulo_str_2 = "del JUEGO"
            coord_titulo_1 = (350,183)

        titulo_surf_1 = self.font_titulo.render(titulo_str_1, True, (0,0,0))
        titulo_surf_2 = self.font_titulo.render(titulo_str_2, True, (0,0,0))
        titulo_rect_1 = titulo_surf_1.get_rect(topleft=coord_titulo_1)
        titulo_rect_2 = titulo_surf_2.get_rect(centerx=titulo_rect_1.centerx, top=titulo_rect_1.bottom+5)
        self.screen.blit(titulo_surf_1, titulo_rect_1)
        self.screen.blit(titulo_surf_2, titulo_rect_2)

        # 6. Lista de nombres
        start_x, start_y, line_height = 315, 387, 45
        for i, nombre in enumerate(self.nombres):
            nombre_surf = self.font_nombres.render(nombre, True, (0,0,0))
            self.screen.blit(nombre_surf, (start_x, start_y + i*line_height))

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
