import os
import pygame

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
        # Rectángulo de colisión/posicionamiento
        self.rect = pygame.Rect(rect)
        # Imágenes normal y hover con canal alpha
        self.normal = pygame.image.load(normal_path).convert_alpha()
        self.hover = pygame.image.load(hover_path).convert_alpha()
        # Acción que reporta al hacer click
        self.action = action
        # Sonido opcional al click
        self.sound = sound

    def draw(self, screen):
        # Dibuja según si el mouse está encima
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
        # Devuelve la acción si hacen click dentro del botón
        if self.rect.collidepoint(pos):
            if self.sound:
                self.sound.play()
            return self.action
        return None

# ------------------ CLASE CONFIGURACIÓN ------------------
class Configuracion:
    # --- MODIFICADO: Acepta el idioma y volumen actual ---
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        # --- MODIFICADO: Usa los valores que recibe ---
        self.idioma = idioma_actual
        self.volumen = volumen_actual # <-- USA EL VOLUMEN RECIBIDO

        # Medidas ventana actuales
        self.W, self.H = self.screen.get_size()

        # --------- FONDO (una sola vez por frame) ---------
        self.fondo = pygame.image.load(os.path.join(
            BASE_DIR, "assets_PI", "interfaces", "configuracion", "fondo", "fondo_paisaje.png"
        )).convert()
        self.fondo = pygame.transform.scale(self.fondo, (self.W, self.H))

        # --------- PANEL DE MADERA (SIN paisaje) ----------
        self.panel = pygame.image.load(os.path.join(
            BASE_DIR, "assets_PI", "interfaces", "configuracion", "fondo", "setting.png"
        )).convert_alpha()
        # Centramos el panel en la pantalla
        self.panel_rect = self.panel.get_rect(center=(self.W // 2, self.H // 2))

        # --- AÑADIDO: Cargar fuentes una vez ---
        try:
            # Fuente para el TÍTULO
            font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "tu_fuente.ttf") 
            self.font_titulo = pygame.font.Font(font_titulo_path, 64) 
        except FileNotFoundError:
            self.font_titulo = pygame.font.Font(None, 72)
            
        try:
            # Fuente para el BOTÓN
            font_boton_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "tu_fuente_pixel.ttf") 
            self.font_boton = pygame.font.Font(font_boton_path, 32) 
        except FileNotFoundError:
            self.font_boton = pygame.font.Font(None, 40)


        # --------- VOLÚMEN Y CONTROLES ----------
        pygame.mixer.music.set_volume(self.volumen) # Ajusta el volumen inicial
        
        self.dragging_slider = False
        self.slider_click_rect = pygame.Rect(0, 0, 0, 0) 

        # --- Cargamos las imágenes con su tamaño original ---
        # Iconos volumen
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

        # --- Obtenemos los tamaños REALES de las imágenes ---
        self.BW = self.barra_vacia.get_width()
        self.BH = self.barra_vacia.get_height()
        self.KNOB_W = self.icono_slider.get_width()
        self.KNOB_H = self.icono_slider.get_height()
        self.FLAG_W = self.bandera_es.get_width()
        self.FLAG_H = self.bandera_es.get_height()
        self.CLOSE_W = self.icono_cerrar.get_width()
        self.CLOSE_H = self.icono_cerrar.get_height()

        # --------- POSICIONES ABSOLUTAS ----------
        self.ICON_VOL_POS   = (189, 144)        # volumen icono
        self.BARRA_POS      = (228, 231)        # barra de volumen (esquina sup izq)
        self.BANDERA_ES_POS = (201, 375)        # España
        self.BANDERA_UK_POS = (540, 375)        # Reino Unido
        self.CERRAR_POS     = (975, 249)        # botón cerrar
        self.BACK_POS       = (36, 42)          # botón atrás
        
        # Calculamos la Y del slider para que esté centrado verticalmente con la barra
        self.SLIDER_Y = self.BARRA_POS[1] + (self.BH // 2) - (self.KNOB_H // 2)
        
        # --------- BOTÓN BACK ----------
        self.botones = [
            Button(
                rect=(self.BACK_POS[0], self.BACK_POS[1], 96, 40), # Asegúrate que 96x40 es el tamaño
                normal_path=os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),
                hover_path=os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),
                action="main",
                sound=click_sound
            )
        ]

    # ------------------ EVENTOS ------------------
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"

        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging_slider = False

        if event.type == pygame.MOUSEMOTION:
            if self.dragging_slider:
                self.volumen = (event.pos[0] - self.BARRA_POS[0]) / self.BW
                self.volumen = max(0.0, min(1.0, self.volumen))
                pygame.mixer.music.set_volume(self.volumen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Botón volver
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion

            # Click en el knob para arrastrar
            if self.slider_click_rect.collidepoint(event.pos):
                self.dragging_slider = True
                click_sound.play()
                return 

            # Click directo sobre la barra
            barra_rect = pygame.Rect(self.BARRA_POS[0], self.BARRA_POS[1], self.BW, self.BH)
            if barra_rect.collidepoint(event.pos):
                self.dragging_slider = True
                self.volumen = (event.pos[0] - self.BARRA_POS[0]) / self.BW
                self.volumen = max(0.0, min(1.0, self.volumen))
                pygame.mixer.music.set_volume(self.volumen)
                click_sound.play()

            # Banderas
            es_rect = pygame.Rect(self.BANDERA_ES_POS[0], self.BANDERA_ES_POS[1], self.FLAG_W, self.FLAG_H)
            uk_rect = pygame.Rect(self.BANDERA_UK_POS[0], self.BANDERA_UK_POS[1], self.FLAG_W, self.FLAG_H)
            if es_rect.collidepoint(event.pos):
                self.idioma = "es"; click_sound.play()
            elif uk_rect.collidepoint(event.pos):
                self.idioma = "en"; click_sound.play()

            # Cerrar (X)
            close_rect = pygame.Rect(self.CERRAR_POS[0], self.CERRAR_POS[1], self.CLOSE_W, self.CLOSE_H)
            if close_rect.collidepoint(event.pos):
                click_sound.play()
                return "main" 

    # ------------------ ACTUALIZAR ------------------
    def update(self):
        pass

    # ------------------ DIBUJAR ------------------
    def draw(self):
        # Fondo
        self.screen.blit(self.fondo, (0, 0))

        # Panel de madera
        self.screen.blit(self.panel, self.panel_rect)

        # --- Título dinámico con coordenadas fijas ---
        titulo_texto = "SETTINGS" if self.idioma == "en" else "CONFIGURACIÓN"
        texto_surface = self.font_titulo.render(titulo_texto, True, (0, 0, 0)) # Color negro
        coordenadas_titulo = (345, 153) 
        self.screen.blit(texto_surface, coordenadas_titulo)
        # --- FIN Título dinámico ---


        # Icono de volumen
        if self.volumen == 0:
            icono_vol = self.icono_volumen_mute
        elif self.volumen < 0.5:
            icono_vol = self.icono_volumen_medio
        else:
            icono_vol = self.icono_volumen_alto
        self.screen.blit(icono_vol, self.ICON_VOL_POS)

        # Barra y fill
        barra_x, barra_y = self.BARRA_POS
        self.screen.blit(self.barra_vacia, (barra_x, barra_y))
        ancho_lleno = int(self.BW * self.volumen)
        self.screen.blit(self.barra_llena, (barra_x, barra_y),
                          pygame.Rect(0, 0, ancho_lleno, self.BH))

        # Knob del slider
        slider_range = self.BW - self.KNOB_W
        slider_x = self.BARRA_POS[0] + int(slider_range * self.volumen)
        self.screen.blit(self.icono_slider, (slider_x, self.SLIDER_Y))
        
        # Actualizamos el rectángulo de click del knob
        self.slider_click_rect.topleft = (slider_x, self.SLIDER_Y)
        self.slider_click_rect.size = self.icono_slider.get_size()

        # Banderas
        self.screen.blit(self.bandera_es, self.BANDERA_ES_POS)
        self.screen.blit(self.bandera_en, self.BANDERA_UK_POS)

        # Botón cerrar (X)
        self.screen.blit(self.icono_cerrar, self.CERRAR_POS)

        # --- MODIFICADO: Botón volver con texto dinámico ---
        for boton in self.botones:
            boton.draw(self.screen) # Dibuja el fondo (normal o hover)
            
            # --- AÑADIDO: Texto dinámico encima del botón ---
            if boton.action == "main": # Identifica el botón "main"
                texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
                
                # Renderizar (usamos la fuente de botón cargada en __init__)
                texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0)) # Color negro
                
                # --- MODIFICADO: Usar coordenadas fijas (53, 66) ---
                coordenadas_boton_texto = (53, 66)
                
                # Dibujar el texto
                self.screen.blit(texto_boton_surf, coordenadas_boton_texto)
            
            
        # Actualizar pantalla
        pygame.display.flip()

    # ------------------ LOOP PRINCIPAL ------------------
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    self.running = False 
                    # --- MODIFICADO: Devuelve la acción, idioma Y VOLUMEN ---
                    return cambio, self.idioma, self.volumen
            
            self.update()
            self.draw() 
            clock.tick(60)
        
        # --- MODIFICADO: Devuelve la acción, idioma Y VOLUMEN ---
        return "salir", self.idioma, self.volumen

# ------------------ EJECUCIÓN PRINCIPAL ------------------
if __name__ == '__main__':
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Menú de Configuración")
    
    # --- Simulación del estado guardado ---
    idioma_actual = "es"
    volumen_actual = 0.5 
    
    running_main = True
    while running_main:
        print(f"Estás en el 'menú principal' (simulado). Idioma: {idioma_actual}, Vol: {volumen_actual}")
        
        # --- MODIFICADO: Pasa el idioma y volumen guardados ---
        cfg = Configuracion(screen, idioma_actual, volumen_actual)
        
        # --- MODIFICADO: Recibe TRES valores ---
        accion_salida, idioma_nuevo, volumen_nuevo = cfg.run() 
        
        # --- MODIFICADO: Actualiza el estado guardado ---
        idioma_actual = idioma_nuevo
        volumen_actual = volumen_nuevo 
        
        if accion_salida == "main":
            print(f"Volviendo al menú principal... Idioma: {idioma_actual}, Vol: {volumen_actual}")
            continue 
        elif accion_salida == "salir":
            print("Cerrando el juego...")
            running_main = False 
            
    pygame.quit()