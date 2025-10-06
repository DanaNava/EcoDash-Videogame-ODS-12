import pygame

pygame.init()  # Inicializa pygame
pygame.mixer.init()  # Inicializa el sistema de sonido
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
click_sound.set_volume(0.5)  # Ajusta el volumen del clic

# ----------- Clase Button Reutilizable -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound = None):
        self.rect = pygame.Rect(rect)  # Área interactiva del botón
        self.normal = pygame.image.load(normal_path).convert_alpha()  # Imagen normal
        self.hover = pygame.image.load(hover_path).convert_alpha()  # Imagen cuando el mouse pasa encima
        self.action = action  # Acción que devuelve cuando se clickea
        self.sound = sound  # Sonido opcional del botón

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()  # Posición del mouse
        # Si el mouse está encima, mostrar imagen hover
        if self.rect.collidepoint(mouse_pos):
            screen.blit(self.hover, self.rect)
        else:
            screen.blit(self.normal, self.rect)

    def check_click(self, pos):
       if self.rect.collidepoint(pos):  # Detecta clic dentro del botón
            if self.sound:   # Reproducir sonido al hacer clic
                self.sound.play()
            return self.action  # Devuelve la acción asociada
       return None


# ----------- Clase Selección de Nivel -----------
class Seleccion_nivel:
    def __init__(self, screen):
        self.screen = screen
        self.running = True  # Controla el bucle interno

        # Fondo de la pantalla
        self.fondo = pygame.image.load("assets_PI/interfaces/eleguir_nivel/fondo/fondo_interfaz_Seleccion_de_nivel.png").convert()

        # Botones de selección de nivel + botón de volver
        self.botones = [
            Button((175, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1_hover.png","nivel1", click_sound),

            Button((409, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2_hover.png","nivel2", click_sound),

            Button((634, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3_hover.png","nivel3", click_sound),

            Button((0, 2, 120, 67),"assets_PI/sprites/boton_back.png","assets_PI/sprites/boton_back_hover.png","seleccion_dificultad", click_sound)
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
                    return accion  # Devuelve el estado a cambiar en el main

    def update(self):
        pass  

    def draw(self):
        self.screen.blit(self.fondo, (0, 0))  # Dibuja el fondo
        for boton in self.botones:
            boton.draw(self.screen)  # Renderiza cada botón

    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio  # Sale si se pulsa algo

            self.update()
            self.draw()
            pygame.display.flip()  # Actualiza la pantalla
