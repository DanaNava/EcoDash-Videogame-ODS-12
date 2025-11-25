import pygame
import os # <-- AÑADIDO

pygame.init()   # Inicializa pygame
pygame.mixer.init()   # Inicializa el sistema de sonido

# --- AÑADIDO ---
# Ruta base para encontrar los assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sonido general de clic para los botones
click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "sonido_click.wav"))
click_sound.set_volume(0.5)   # Ajusta el volumen (0.0 a 1.0)

# ----------- Clase Button Reutilizable -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound=None):
        self.rect = pygame.Rect(rect)   # Zona clickeable del botón
        self.normal = pygame.image.load(normal_path).convert_alpha()   # Imagen normal
        self.hover = pygame.image.load(hover_path).convert_alpha()   # Imagen con hover
        self.action = action   # Acción que devuelve al hacer clic
        self.sound = sound   # Sonido opcional al presionar

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()   # Obtener posición del mouse
        # Si el mouse está encima del botón, mostrar hover, si no la imagen normal
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
        # Revisa si se hizo clic dentro del botón
        if self.rect.collidepoint(pos):
            if self.sound:   # Reproducir sonido al hacer clic si se configuró
                self.sound.play()
            return self.action   # Devuelve la acción asignada
        return None   # Si no se clickeó el botón no hace nada

# ----------- Clase de Interfaz -----------
class Seleccion_dificultad:   # Pantalla para elegir dificultad
    # --- MODIFICADO: Acepta el idioma y volumen actual ---
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        
        # --- AÑADIDO: Guarda el idioma y volumen ---
        self.idioma = idioma_actual
        self.volumen = volumen_actual # <-- AÑADIDO

        # --- ¡¡¡MODIFICADO AQUÍ!!! ---
        # --- Cargar la fuente para el botón "Volver" (Texto Normal) ---
        try:
            font_boton_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf") 
            self.font_boton = pygame.font.Font(font_boton_path, 19) # Tamaño más pequeño
        except FileNotFoundError:
            print("ERROR: No se encontró 'Pixel.ttf'")
            self.font_boton = pygame.font.Font(None, 40)

        # --- Cargar fuente para el TÍTULO ---
        try:
            font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf") 
            self.font_titulo = pygame.font.Font(font_titulo_path, 110) # Ajusta el tamaño
        except FileNotFoundError:
            print("ERROR: No se encontró 'Stay Pixel DEMO.tff'")
            self.font_titulo = pygame.font.Font(None, 60)

        # --- Cargar fuente para OPCIONES (Texto Normal) ---
        try:
            font_opcion_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf") 
            self.font_opcion = pygame.font.Font(font_opcion_path, 25) # Ajusta el tamaño
        except FileNotFoundError:
            print("ERROR: No se encontró 'Pixel.ttf'")
            self.font_opcion = pygame.font.Font(None, 48)
        # --- FIN DE LA MODIFICACIÓN ---

        # Fondo de la interfaz (ahora sin texto)
        self.fondo = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "tabla.png")).convert_alpha()
        self.nube = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "BUB.png")).convert_alpha()
        self.azul = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "Fondo_animado", "azul.png")).convert_alpha()

        # --- AÑADIDO: posiciones para animar las nubes ---
        self.nube_x = 0
        self.nube_vel = 0.1  # ← MISMA VELOCIDAD, AHORA HACIA LA DERECHA

        # Lista de botones con sus acciones (ahora sin texto)
        self.botones = [
            Button((152, 313, 333, 97),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_dificultad", "botones", "boton_interfaz_eleguir_dificultad_facil.png"),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_dificultad", "botones", "boton_interfaz_eleguir_dificultad_facil_hover.png"),"facil", click_sound ),

            Button((152, 482, 330, 98),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_dificultad", "botones", "boton_interfaz_eleguir_dificultad_medio.png"),os.path.join(BASE_DIR, "assets_PI", "interfaces", "eleguir_dificultad", "botones", "boton_interfaz_eleguir_dificultad_medio_hover.png"),"medio", click_sound ),

            # Este es el botón de "volver"
            Button((40, 35, 120, 67),os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back.png"),os.path.join(BASE_DIR, "assets_PI", "sprites", "boton_back_hover.png"),"select_character", click_sound )
        ]

    def handle_event(self, event):
        if event.type == (pygame.QUIT):
            self.running = False
            return "salir"   # Si se cierra la ventana, se sale del juego

        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion # Devuelve la acción del botón y cambia de pantalla

    def update(self):

        # --- ANIMACIÓN DE NUBES (scroll infinito) ---
        self.nube_x += self.nube_vel   # ← AHORA HACIA LA DERECHA

        # Cuando sale por la derecha, reinicia
        if self.nube_x >= 1280:
            self.nube_x = 0

    def draw(self):

        # --- ORDEN CORRECTO DE CAPAS ---
        self.screen.blit(self.azul, (0,0))   # Capa más atrás

        # NUBES animadas (dos para loop perfecto)
        self.screen.blit(self.nube, (self.nube_x, 0))
        self.screen.blit(self.nube, (self.nube_x - 1280, 0))  # ← ahora hace loop hacia la DERECHA

        self.screen.blit(self.fondo, (0,0))  # Adelante (tabla)
        # --------------------------------

        # --- AÑADIDO: Dibujar TÍTULO dinámico ---
        titulo_str = "DIFFICULTY" if self.idioma == "en" else "DIFICULTAD"
        titulo_surf = self.font_titulo.render(titulo_str, True, (0, 0, 0)) # Color negro
        self.screen.blit(titulo_surf, (300, 165)) # Coordenadas que diste
        # --- FIN TÍTULO ---

        # Textos para los botones (se dibujarán encima)
        texto_facil_str = "BEGINNER" if self.idioma == "en" else "PRINCIPIANTE"
        texto_facil_surf = self.font_opcion.render(texto_facil_str, True, (0, 0, 0))
        
        texto_medio_str = "CHALLENGER" if self.idioma == "en" else "Retador"
        texto_medio_surf = self.font_opcion.render(texto_medio_str, True, (0, 0, 0))

        # Bucle para dibujar botones y sus textos
        for boton in self.botones:
            boton.draw(self.screen)   # Dibujar cada botón

            # --- Lógica para dibujar texto en el botón "Back" ---
            if boton.action == "select_character":
                texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
                texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0)) # Color negro
                coordenadas_boton_texto = (58, 49) 
                self.screen.blit(texto_boton_surf, coordenadas_boton_texto)
            
            # --- AÑADIDO: Lógica para dibujar texto "PRINCIPIANTE" ---
            elif boton.action == "facil":
                self.screen.blit(texto_facil_surf, (195, 345)) # Coordenadas que diste
            
            # --- AÑADIDO: Lógica para dibujar texto "INTERMEDIO" ---
            elif boton.action == "medio":
                self.screen.blit(texto_medio_surf, (192, 519)) # Coordenadas que diste

    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:   # Si se seleccionó alguna opción
                    return cambio

            self.update()
            self.draw()
            pygame.display.flip()   # Actualiza la pantalla con los cambios
