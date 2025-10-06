import pygame
pygame.init()  # Inicializa pygame
pygame.mixer.init()  # Inicializa el sistema de sonido

# Sonido general de clic para los botones
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
click_sound.set_volume(0.5)  # Ajusta el volumen (0.0 a 1.0)

# ----------- Clase Button Reutilizable -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound=None):
        self.rect = pygame.Rect(rect)  # Zona clickeable del botón
        self.normal = pygame.image.load(normal_path).convert_alpha()  # Imagen normal
        self.hover = pygame.image.load(hover_path).convert_alpha()  # Imagen con hover
        self.action = action  # Acción que devuelve al hacer clic
        self.sound = sound  # Sonido opcional al presionar

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()  # Obtener posición del mouse
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
            return self.action  # Devuelve la acción asignada
        return None  # Si no se clickeó el botón no hace nada

# ----------- Clase de Interfaz -----------
class Configuracion:  # Pantalla para elegir dificultad
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Fondo de la interfaz
        self.fondo = pygame.image.load("assets_PI/interfaces/configuracion/fondo/interfaz_de_configuracion2.png").convert()

        # Lista de botones con sus acciones
        self.botones = [

            Button((0, 35, 120, 67),"assets_PI/sprites/boton_back.png","assets_PI/sprites/boton_back_hover.png","main", click_sound )
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"  # Si se cierra la ventana, se sale del juego

        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion # Devuelve la acción del botón y cambia de pantalla

    def update(self):
        pass  

    def draw(self):
        self.screen.blit(self.fondo, (0, 0))  # Dibujar el fondo
        for boton in self.botones:
            boton.draw(self.screen)  # Dibujar cada botón

    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:  # Si se seleccionó alguna opción
                    return cambio

            self.update()
            self.draw()
            pygame.display.flip()  # Actualiza la pantalla con los cambios
