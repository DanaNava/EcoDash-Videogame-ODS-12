import pygame
import os # <-- AÑADIDO

pygame.init()   # Inicializa pygame
pygame.mixer.init()   # Inicializa el sistema de sonido

# --- AÑADIDO ---
# Ruta base para encontrar los assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "sonido_click.wav"))
click_sound.set_volume(0.5)   # Ajusta el volumen del clic

# ----------- Clase Button Reutilizable -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound = None):
        self.rect = pygame.Rect(rect)   # Área interactiva del botón
        self.normal = pygame.image.load(normal_path).convert_alpha()   # Imagen normal
        self.hover = pygame.image.load(hover_path).convert_alpha()   # Imagen cuando el mouse pasa encima
        self.action = action   # Acción que devuelve cuando se clickea
        self.sound = sound   # Sonido opcional del botón

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()   # Posición del mouse
        # Si el mouse está encima, mostrar imagen hover
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
       if self.rect.collidepoint(pos):   # Detecta clic dentro del botón
            if self.sound:   # Reproducir sonido al hacer clic
                self.sound.play()
            return self.action   # Devuelve la acción asociada
       return None


# ----------- Clase Selección de Nivel -----------
class Seleccion_nivel:
    # --- MODIFICADO: Acepta el idioma y volumen actual ---
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True   # Controla el bucle interno
        
        # --- AÑADIDO: Guarda el idioma y volumen ---
        self.idioma = idioma_actual
        self.volumen = volumen_actual # <-- AÑADIDO

        # --- ¡¡¡MODIFICADO AQUÍ!!! ---
        # --- Cargar la fuente para el botón ---
        try:
            # Fuente para el BOTÓN "Volver" y "Nivel" (Pixel.ttf)
            font_boton_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf") 
            self.font_boton = pygame.font.Font(font_boton_path, 19) # Tamaño 32
        except FileNotFoundError:
            print("ERROR: No se encontró 'Pixel.ttf'")
            self.font_boton = pygame.font.Font(None, 40)
            
        # --- Cargar la fuente para el TÍTULO ---
        try:
            # Fuente para el TÍTULO (Stay Pixel DEMO.otf)
            font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf") 
            self.font_titulo = pygame.font.Font(font_titulo_path, 52) # Tamaño 52
        except FileNotFoundError:
            print("ERROR: No se encontró 'Stay Pixel DEMO.ttf'")
            self.font_titulo = pygame.font.Font(None, 60)
        # --- FIN DE LA MODIFICACIÓN ---

        # Fondo de la pantalla (ahora sin texto)
        self.fondo = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "fondo", "fondo_interfaz_Seleccion_de_nivel.png")).convert()

        # Botones de selección de nivel + botón de volver (ahora sin texto)
        self.botones = [
            Button((175, 345, 213, 84),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel1.png"),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel1_hover.png"),"nivel1", click_sound),

            Button((409, 345, 213, 84),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel2.png"),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel2_hover.png"),"nivel2", click_sound),

            Button((634, 345, 213, 84),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel3.png"),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_nivel", "botones", "boton_interfaz_eleguir_nivel_nivel3_hover.png"),"nivel3", click_sound),

            Button((0, 2, 120, 67),os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),"seleccion_dificultad", click_sound)
        ]

    def handle_event(self, event):
        # Cerrar ventana
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"

        # Detectar clics en botones
        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion   # Devuelve el estado a cambiar en el main

    def update(self):
        pass   

    def draw(self):
        self.screen.blit(self.fondo, (0, 0))   # Dibuja el fondo

        # --- AÑADIDO: Dibujar TÍTULO dinámico ---
        titulo_str = "LEVEL SELECTION" if self.idioma == "en" else "SELECCIÓN DE NIVEL"
        titulo_surf = self.font_titulo.render(titulo_str, True, (0, 0, 0)) # Color negro
        self.screen.blit(titulo_surf, (321, 105)) # Coordenadas que diste
        # --- FIN TÍTULO ---

        # Textos para los botones (se dibujarán encima)
        texto_n1_str = "LEVEL 1" if self.idioma == "en" else "NIVEL 1"
        texto_n1_surf = self.font_boton.render(texto_n1_str, True, (0, 0, 0))
        
        texto_n2_str = "LEVEL 2" if self.idioma == "en" else "NIVEL 2"
        texto_n2_surf = self.font_boton.render(texto_n2_str, True, (0, 0, 0))
        
        texto_n3_str = "LEVEL 3" if self.idioma == "en" else "NIVEL 3"
        texto_n3_surf = self.font_boton.render(texto_n3_str, True, (0, 0, 0))


        for boton in self.botones:
            boton.draw(self.screen)   # Renderiza cada botón
            
            # --- Lógica para dibujar texto en el botón "Back" ---
            if boton.action == "seleccion_dificultad":
                texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
                texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0)) # Color negro
                coordenadas_boton_texto = (18, 19) 
                self.screen.blit(texto_boton_surf, coordenadas_boton_texto)
            
            # --- AÑADIDO: Texto para botones de Nivel ---
            elif boton.action == "nivel1":
                self.screen.blit(texto_n1_surf, (204, 369)) # Coords que diste
                
            elif boton.action == "nivel2":
                self.screen.blit(texto_n2_surf, (438, 369)) # Coords que diste
                
            elif boton.action == "nivel3":
                self.screen.blit(texto_n3_surf, (663, 369)) # Coords que diste
            
            # --- FIN AÑADIDO ---


    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio   # Sale si se pulsa algo

            self.update()
            self.draw()
            pygame.display.flip()