import os
import pygame
import math

# ------------------ INICIO PYGAME ------------------
pygame.init()
pygame.mixer.init()

# ------------------ RUTAS ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ------------------ SONIDOS ------------------
# Sonido click para botones
click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "sonido_click.wav"))
click_sound.set_volume(0.5)

# ------------------ CLASE BOTÓN ------------------
class Button:
    def __init__(self, rect, normal_path, hover_path, action=None, sound=None):
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

# ------------------ CLASE NUBES ------------------
class Nubes:
    def __init__(self, imagen, velocidad, pantalla):
        self.imagen = imagen
        self.velocidad = velocidad
        self.screen = pantalla
        self.x = 0
        self.w = self.imagen.get_width()

    def update(self):
        self.x += self.velocidad
        if self.x >= self.w:
            self.x = 0

    def draw(self):
        self.screen.blit(self.imagen, (self.x - self.w, 0))
        self.screen.blit(self.imagen, (self.x, 0))

# ------------------ CLASE CONFIGURACIÓN ------------------
class Configuracion:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        self.idioma = idioma_actual
        self.volumen = volumen_actual

        # Medidas ventana
        self.W, self.H = self.screen.get_size()

        # --------- FONDOS ---------
        self.background = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "azul.png")).convert_alpha()
        self.nubes = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "nubes.png")).convert_alpha()
        self.verde = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "verdee.png")).convert_alpha()

        
        # Instancia de nubes
        self.nubes_obj = Nubes(self.nubes, velocidad=1, pantalla=self.screen)

        # --------- PANEL DE MADERA ---------
        # Cargar panel
        self.panel = pygame.image.load(os.path.join(
    BASE_DIR, "assets_PI", "interfaces", "configuracion", "fondo", "setting.png")).convert_alpha()

# Escalar un poco más grande (20% más)
        panel_w = int(self.panel.get_width() * 1.1)
        panel_h = int(self.panel.get_height() * 1.1)
        self.panel = pygame.transform.scale(self.panel, (panel_w, panel_h))

# Centrarlo en la ventana
        self.panel_rect = self.panel.get_rect(center=(self.W // 2, self.H // 2))
        
        # --- Fuentes ---
        try:
            self.font_titulo = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf"), 64)
        except FileNotFoundError:
            self.font_titulo = pygame.font.Font(None, 72)

        try:
            self.font_boton = pygame.font.Font(os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf"), 20)
        except FileNotFoundError:
            self.font_boton = pygame.font.Font(None, 40)

        # --------- VOLÚMEN Y CONTROLES ----------
        self.dragging_slider = False
        self.slider_click_rect = pygame.Rect(0, 0, 0, 0)

        # Iconos de volumen
        self.icono_volumen_alto = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "volumen_alto.png")).convert_alpha()
        self.icono_volumen_medio = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "volumen_medio.png")).convert_alpha()
        self.icono_volumen_mute = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "volumen_muteado.png")).convert_alpha()

        # Slider y barra
        self.icono_slider = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "slider.png")).convert_alpha()
        self.barra_vacia = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "barra_vacia.png")).convert_alpha()
        self.barra_llena = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "barra_llena.png")).convert_alpha()

        # Banderas
        self.bandera_es = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "bandera_españa.png")).convert_alpha()
        self.bandera_en = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "bandera_inglaterra.png")).convert_alpha()

        # Cerrar (X)
        self.icono_cerrar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "boton_cerrar.png")).convert_alpha()

        # Hover banderas
        try:
            self.bandera_es_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "bandera_españa_hover.png")).convert_alpha()
            self.bandera_en_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "configuracion", "botones", "bandera_inglaterra_hover.png")).convert_alpha()
        except pygame.error:
            self.bandera_es_hover = self.bandera_es.copy()
            pygame.draw.rect(self.bandera_es_hover, (255, 255, 0), self.bandera_es_hover.get_rect(), 5)
            self.bandera_en_hover = self.bandera_en.copy()
            pygame.draw.rect(self.bandera_en_hover, (255, 255, 0), self.bandera_en_hover.get_rect(), 5)

        # Temporizador parpadeo
        self.tiempo_parpadeo = pygame.time.get_ticks()
        self.mostrar_seleccion = True

        # Tamaños de elementos
        self.BW = self.barra_vacia.get_width()
        self.BH = self.barra_vacia.get_height()
        self.KNOB_W = self.icono_slider.get_width()
        self.KNOB_H = self.icono_slider.get_height()
        self.FLAG_W = self.bandera_es.get_width()
        self.FLAG_H = self.bandera_es.get_height()
        self.CLOSE_W = self.icono_cerrar.get_width()
        self.CLOSE_H = self.icono_cerrar.get_height()

        # Posiciones
        self.ICON_VOL_POS = (189, 145)
        self.BARRA_POS = (228, 255)
        self.BANDERA_ES_POS = (201, 355)
        self.BANDERA_UK_POS = (540, 355)
        self.CERRAR_POS = (975, 249)
        self.BACK_POS = (36, 42)

        self.SLIDER_Y = self.BARRA_POS[1] + (self.BH // 2) - (self.KNOB_H // 2)

        # Botón Back
        self.botones = [Button(
            rect=(self.BACK_POS[0], self.BACK_POS[1], 96, 50),
            normal_path=os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),
            hover_path=os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),
            action="main",
            sound=click_sound
        )]

    # ------------------ EVENTOS ------------------
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"
        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging_slider = False
        if event.type == pygame.MOUSEMOTION and self.dragging_slider:
            self.volumen = (event.pos[0] - self.BARRA_POS[0]) / self.BW
            self.volumen = max(0.0, min(1.0, self.volumen))
            pygame.mixer.music.set_volume(self.volumen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion
            if self.slider_click_rect.collidepoint(event.pos):
                self.dragging_slider = True
                click_sound.play()
            barra_rect = pygame.Rect(self.BARRA_POS[0], self.BARRA_POS[1], self.BW, self.BH)
            if barra_rect.collidepoint(event.pos):
                self.dragging_slider = True
                self.volumen = (event.pos[0] - self.BARRA_POS[0]) / self.BW
                self.volumen = max(0.0, min(1.0, self.volumen))
                pygame.mixer.music.set_volume(self.volumen)
                click_sound.play()
            es_rect = pygame.Rect(self.BANDERA_ES_POS[0], self.BANDERA_ES_POS[1], self.FLAG_W, self.FLAG_H)
            uk_rect = pygame.Rect(self.BANDERA_UK_POS[0], self.BANDERA_UK_POS[1], self.FLAG_W, self.FLAG_H)
            if es_rect.collidepoint(event.pos):
                self.idioma = "es"; click_sound.play()
            elif uk_rect.collidepoint(event.pos):
                self.idioma = "en"; click_sound.play()
            close_rect = pygame.Rect(self.CERRAR_POS[0], self.CERRAR_POS[1], self.CLOSE_W, self.CLOSE_H)
            if close_rect.collidepoint(event.pos):
                click_sound.play()
                return "main"

    # ------------------ ACTUALIZAR ------------------
    def update(self):
        self.nubes_obj.update()

    # ------------------ DIBUJAR ------------------
    def draw(self):
        # Fondo
        self.screen.blit(self.background, (0, 0))
        self.nubes_obj.draw()
        self.screen.blit(self.verde, (0, 0))

        # Panel
        self.screen.blit(self.panel, self.panel_rect)

        # Título
        if self.idioma == "en":
            titulo_texto = "SETTINGS"
            coordenadas_titulo = (380, 153)
        else:
            titulo_texto = "CONFIGURACIÓN"
            coordenadas_titulo = (345, 153)
        texto_surface = self.font_titulo.render(titulo_texto, True, (0, 0, 0))
        self.screen.blit(texto_surface, coordenadas_titulo)

        # Volumen
        if self.volumen == 0:
            icono_vol = self.icono_volumen_mute
        elif self.volumen < 0.5:
            icono_vol = self.icono_volumen_medio
        else:
            icono_vol = self.icono_volumen_alto
        self.screen.blit(icono_vol, self.ICON_VOL_POS)

        # Barra y slider
        barra_x, barra_y = self.BARRA_POS
        self.screen.blit(self.barra_vacia, (barra_x, barra_y))
        ancho_lleno = int(self.BW * self.volumen)
        self.screen.blit(self.barra_llena, (barra_x, barra_y), pygame.Rect(0, 0, ancho_lleno, self.BH))
        slider_range = self.BW - self.KNOB_W
        slider_x = self.BARRA_POS[0] + int(slider_range * self.volumen)
        self.screen.blit(self.icono_slider, (slider_x, self.SLIDER_Y))
        self.slider_click_rect.topleft = (slider_x, self.SLIDER_Y)
        self.slider_click_rect.size = self.icono_slider.get_size()

        # Banderas
        mouse_pos = pygame.mouse.get_pos()
        es_rect = pygame.Rect(self.BANDERA_ES_POS[0], self.BANDERA_ES_POS[1], self.FLAG_W, self.FLAG_H)
        uk_rect = pygame.Rect(self.BANDERA_UK_POS[0], self.BANDERA_UK_POS[1], self.FLAG_W, self.FLAG_H)
        if es_rect.collidepoint(mouse_pos):
            self.screen.blit(self.bandera_es_hover, self.BANDERA_ES_POS)
        elif self.idioma == "es" and self.mostrar_seleccion:
            self.screen.blit(self.bandera_es_hover, self.BANDERA_ES_POS)
        else:
            self.screen.blit(self.bandera_es, self.BANDERA_ES_POS)
        if uk_rect.collidepoint(mouse_pos):
            self.screen.blit(self.bandera_en_hover, self.BANDERA_UK_POS)
        elif self.idioma == "en" and self.mostrar_seleccion:
            self.screen.blit(self.bandera_en_hover, self.BANDERA_UK_POS)
        else:
            self.screen.blit(self.bandera_en, self.BANDERA_UK_POS)

        # Botones
        self.screen.blit(self.icono_cerrar, self.CERRAR_POS)
        for boton in self.botones:
            boton.draw(self.screen)
            if boton.action == "main":
                texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
                texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0))
                coordenadas_boton_texto = (57, 57)
                self.screen.blit(texto_boton_surf, coordenadas_boton_texto)

        pygame.display.flip()

    # ------------------ LOOP PRINCIPAL ------------------
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            ahora = pygame.time.get_ticks()
            if ahora - self.tiempo_parpadeo > 500:
                self.mostrar_seleccion = not self.mostrar_seleccion
                self.tiempo_parpadeo = ahora
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    self.running = False
                    return cambio, self.idioma, self.volumen
            self.update()
            self.draw()
            clock.tick(60)
        return "salir", self.idioma, self.volumen
