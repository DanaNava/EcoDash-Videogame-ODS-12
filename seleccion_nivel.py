import pygame

pygame.init()
pygame.mixer.init()
click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
click_sound.set_volume(0.5)  # Ajusta el volumen (0.0 a 1.0)


# ----------- Clase Button Reutilizable -----------
class Button:
    def __init__(self, rect, normal_path, hover_path, action, sound = None):
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
            if self.sound:   # reproducir sonido al hacer clic
                self.sound.play()
            return self.action
       return None


# ----------- Clase Selección de Nivel -----------
class Seleccion_nivel:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Fondo
        self.fondo = pygame.image.load("assets_PI/interfaces/eleguir_nivel/fondo/fondo_interfaz_Seleccion_de_nivel.png").convert()

        # Botones
        self.botones = [
            Button((175, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1_hover.png","nivel1", click_sound),

            Button((409, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2_hover.png","nivel2", click_sound),

            Button((634, 345, 213, 84),"assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3.png","assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3_hover.png","nivel3", click_sound),

            Button((0, 2, 120, 67),"assets_PI/sprites/boton_back.png","assets_PI/sprites/boton_back_hover.png","seleccion_dificultad", click_sound)
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return "salir"

        if event.type == pygame.MOUSEBUTTONDOWN:
            for boton in self.botones:
                accion = boton.check_click(event.pos)
                if accion:
                    return accion

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.fondo, (0, 0))
        for boton in self.botones:
            boton.draw(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                cambio = self.handle_event(event)
                if cambio:
                    return cambio

            self.update()
            self.draw()
            pygame.display.flip()
