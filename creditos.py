import pygame
import sys
import os 

pygame.init()   # Inicializa pygame
pygame.mixer.init()   # Inicializa sistema de sonido

# Ruta base para encontrar los assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sonido para los botones
try:
    click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI/sonidos/sonido_click.wav"))
    click_sound.set_volume(0.5)
except pygame.error:
    print("No se pudo cargar 'sonido_click.wav'")
    click_sound = None

# ----------- Clase Button Reutilizable -----------
# (Copiada de tus otros archivos para consistencia)
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound = None):
        self.rect = pygame.Rect(rect)   # Área interactiva del botón
        # Manejo de error si no se encuentra la imagen
        try:
            self.normal = pygame.image.load(normal_path).convert_alpha()
            self.hover = pygame.image.load(hover_path).convert_alpha()
        except pygame.error:
            print(f"Error cargando imagen de botón: {normal_path}")
            self.normal = pygame.Surface((rect[2], rect[3])) # Crea una superficie negra
            self.normal.fill((0,0,0))
            self.hover = self.normal
            
        self.action = action   # Acción que devuelve cuando se clickea
        self.sound = sound   # Sonido opcional del botón

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

# ----------- Clase Pantalla de Créditos -----------
class Creditos:
    def __init__(self, screen, idioma_actual, volumen_actual):
        self.screen = screen
        self.running = True
        self.idioma = idioma_actual
        self.volumen = volumen_actual # Lo guardamos por si acaso

        # --- Cargar Fondo ---
        try:
            fondo_path = os.path.join(BASE_DIR, "assets_PI/interfaces/creditos/fondo/creditos.png") # Nombre corregido
            self.fondo = pygame.image.load(fondo_path).convert()
        except pygame.error:
            print("No se encontró 'creditos.png', usando fondo negro.")
            self.fondo = pygame.Surface(self.screen.get_size())
            self.fondo.fill((0, 0, 0)) # Fondo negro si falla

        # --- Cargar Fuentes ---
        try:
            font_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "tu_fuente_pixel.ttf")
            self.font_titulo = pygame.font.Font(font_path, 48) # Para "DESARROLLADORES"
            self.font_nombres = pygame.font.Font(font_path, 30) # Para la lista de nombres
            self.font_boton = pygame.font.Font(font_path, 32) # Para el botón "Volver"
        except FileNotFoundError:
            print("Fuente pixel no encontrada, usando fuentes por defecto.")
            self.font_titulo = pygame.font.Font(None, 55)
            self.font_nombres = pygame.font.Font(None, 36)
            self.font_boton = pygame.font.Font(None, 40)

        # --- Botón de Volver ---
        self.boton_volver = Button((0, 2, 120, 67),
                                   os.path.join(BASE_DIR, "assets_PI/sprites/boton_back.png"),
                                   os.path.join(BASE_DIR, "assets_PI/sprites/boton_back_hover.png"),
                                   "main", 
                                   click_sound)
        
        # --- Lista de Nombres (con acentos) ---
        self.nombres = [
            "Ibarra Heredia Alan Alejandro",
            "Nava Montiel Dana Paola",
            "Escobar Núñez Cristian Alexander",
            "Martínez Zúñiga Carolina",
            "Salgado Zepeda David",
            "Vázquez Atanacio Diego Alejandro"
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
        self.screen.blit(self.fondo, (0, 0)) # 1. Dibujar el fondo

        # 2. Dibujar el botón "Volver"
        self.boton_volver.draw(self.screen)
        texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
        texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0))
        self.screen.blit(texto_boton_surf, (18, 25)) # Coordenadas fijas para el texto del botón

        # --- MODIFICADO: Título en dos líneas con coordenadas dinámicas ---
        if self.idioma == "en":
            titulo_str_1 = "GAME"
            titulo_str_2 = "DEVELOPERS"
            coordenadas_titulo_1 = (460, 180) # <-- Coordenadas para Inglés
        else:
            titulo_str_1 = "DESARROLLADORES"
            titulo_str_2 = "del JUEGO"
            coordenadas_titulo_1 = (291, 183) # <-- Coordenadas para Español
            
        titulo_surf_1 = self.font_titulo.render(titulo_str_1, True, (0,0,0)) # Color negro
        titulo_surf_2 = self.font_titulo.render(titulo_str_2, True, (0,0,0)) # Color negro

        # Posicionar la primera línea en las coordenadas dinámicas
        titulo_rect_1 = titulo_surf_1.get_rect(topleft=coordenadas_titulo_1)
        
        # Posicionar la segunda línea centrada debajo de la primera
        titulo_rect_2 = titulo_surf_2.get_rect(centerx=titulo_rect_1.centerx, top=titulo_rect_1.bottom + 5) # 5px padding

        self.screen.blit(titulo_surf_1, titulo_rect_1)
        self.screen.blit(titulo_surf_2, titulo_rect_2)

        # 4. Lista de nombres en (315, 387)
        start_x = 315 # Coordenada X fija
        start_y = 387 # Coordenada Y fija
        line_height = 45 # Espacio entre nombres

        for i, nombre in enumerate(self.nombres):
            nombre_surf = self.font_nombres.render(nombre, True, (0,0,0)) # Color negro
            # Alinear todos los nombres a la izquierda en X=315
            nombre_rect = nombre_surf.get_rect(topleft=(start_x, start_y + (i * line_height)))
            self.screen.blit(nombre_surf, nombre_rect)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio # Devuelve "main" o "salir"

            self.draw()
            pygame.display.flip()
        
        return "salir" 

# Para probar este archivo de forma independiente
if __name__ == '__main__':
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Prueba de Créditos")
    
    # Simulación de estado global
    idioma_actual = "es"
    volumen_actual = 0.5
    
    pantalla_creditos = Creditos(screen, idioma_actual, volumen_actual)
    resultado = pantalla_creditos.run()
    
    print(f"Pantalla de créditos cerró con: {resultado}")
    pygame.quit()
    sys.exit()