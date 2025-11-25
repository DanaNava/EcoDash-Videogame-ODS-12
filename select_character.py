import pygame
import sys
import os 
import math

pygame.init()   # Inicializa pygame
pygame.mixer.init()  # Inicializa sistema de sonido

# --- AÑADIDO ---
# Ruta base para encontrar los assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Sonido para los botones
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
click_sound.set_volume(0.5)

# Crear ventana 
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

# Clase general para botones reutilizable
class Button:
    def __init__(self, x, y, image, image_hover=None, sound=None, action=None):
        self.image = image   # Imagen normal
        self.image_hover = image_hover if image_hover else image   # Imagen hover (si no hay, usa la normal)
        self.rect = self.image.get_rect(topleft=(x, y))   # Posición y tamaño del botón
        self.sound = sound   # Sonido al hacer clic
        self.action = action   # Acción que devuelve al pulsarlo

    def draw(self, screen, pos_mouse=None):
        # Cambia la imagen si el mouse está encima
        if pos_mouse and self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def clicked(self, event):
        # Detecta clic del mouse sobre el botón
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if self.sound:
                self.sound.play()   # Reproduce el sonido si está disponible
            return self.action   # Devuelve la acción asignada
        return None


class Select_character:
    def __init__(self, screen, idioma_actual, volumen_actual): 
        self.screen = screen
        self.posiciones = [443, 740]  # Izquierda: hombre (0), Derecha: mujer (1)
        self.indice_actual = 0  # 0 = hombre, 1 = mujer
        self.personaje_seleccionado = None
        self.idioma = idioma_actual
        self.volumen = volumen_actual

        # Cargar fuentes
        try:
            font_boton_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf") 
            self.font_boton = pygame.font.Font(font_boton_path, 20)
        except FileNotFoundError:
            print("ERROR: No se encontró 'Pixel.ttf'")
            self.font_boton = pygame.font.Font(None, 40)
            
        try:
            font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf") 
            self.font_titulo = pygame.font.Font(font_titulo_path, 52)
        except FileNotFoundError:
            print("ERROR: No se encontró 'Stay Pixel DEMO.ttf'")
            self.font_titulo = pygame.font.Font(None, 60)

        # Cargar imágenes
        self.background = pygame.image.load("assets_PI/interfaces/Fondo_animado/azul.png")
        self.personaje = pygame.image.load("assets_PI/interfaces/Fondo_animado/personajes.png")
        self.nube = pygame.image.load("assets_PI/interfaces/Fondo_animado/BUB.png")
        
        self.next_img = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/next_button.png")
        self.next_hover = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/next_buttonh.png")
        self.select_img = pygame.image.load("assets_PI/interfaces/eleguir_personaje/botones/select.png")
        self.back = pygame.image.load("assets_PI/sprites/boton_back.png")
        self.back_hover = pygame.image.load("assets_PI/sprites/boton_back_hover.png")

        # Botones
        self.next_button = Button(906, 670, self.next_img, self.next_hover, click_sound, action="seleccion_dificultad")
        self.back_button = Button(0, 2, self.back, self.back_hover, click_sound, action="main")
        self.select_button = Button(self.posiciones[self.indice_actual], 297, self.select_img, None, click_sound, action="seleccion_personaje")

    def run(self):
        running = True

        # --- NUEVO: Variables para animar la nube ---
        nube_x = 0               # Posición horizontal inicial de la nube
        velocidad_nube = 1       # Velocidad de movimiento de la nube

        while running:
            pos_mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Comprobar clic en botones
                result = self.next_button.clicked(event) or self.back_button.clicked(event) or self.select_button.clicked(event)
                if result:
                    # Cuando se presiona cualquier botón, guardamos el personaje actualmente seleccionado
                    self.personaje_seleccionado = self.indice_actual  # 0 = hombre, 1 = mujer
                    print(f"Personaje seleccionado: {'Hombre' if self.personaje_seleccionado == 0 else 'Mujer'}")
                    
                    # Devolvemos tanto la acción como el personaje seleccionado
                    return {
                        "accion": result, 
                        "personaje": self.personaje_seleccionado
                    }

                # Controles con teclado para mover el selector
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.indice_actual = 1  # Mover a mujer
                    elif event.key == pygame.K_LEFT:
                        self.indice_actual = 0  # Mover a hombre

            # Actualizar posición visual del botón de selección
            self.select_button.rect.x = self.posiciones[self.indice_actual]

            # --- NUEVO: Mover la nube horizontalmente ---
            nube_x += velocidad_nube
            if nube_x >= self.nube.get_width():
                nube_x = 0

            # Dibujado
            self.screen.blit(self.background, (0, 0))
            # --- NUEVO: Dibujar nube en loop infinito ---
            self.screen.blit(self.nube, (nube_x - self.nube.get_width(), 0))
            self.screen.blit(self.nube, (nube_x, 0))

            self.screen.blit(self.personaje, (0, 0))
            
            # Texto dinámico para el título
            titulo_texto_str = "CHOOSE YOUR CHARACTER" if self.idioma == "en" else "ESCOGE TU PERSONAJE"
            titulo_texto_surf = self.font_titulo.render(titulo_texto_str, True, (0, 0, 0))
            coordenadas_titulo = (240, 81)
            self.screen.blit(titulo_texto_surf, coordenadas_titulo)

            # Botones
            self.next_button.draw(self.screen, pos_mouse)
            self.back_button.draw(self.screen, pos_mouse)
            self.select_button.draw(self.screen)

            # Texto dinámico para el botón "Back"
            texto_boton_str = "BACK" if self.idioma == "en" else "VOLVER"
            texto_boton_surf = self.font_boton.render(texto_boton_str, True, (0, 0, 0))
            coordenadas_boton_texto = (15, 18)
            self.screen.blit(texto_boton_surf, coordenadas_boton_texto)

            pygame.display.flip()
