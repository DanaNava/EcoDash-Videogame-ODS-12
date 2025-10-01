import pygame

class MiInterfaz:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.cambio = None
        # Aquí cargas tus imágenes, botones, fuentes, etc.
        self.fondo = pygame.image.load("assets_PI/interfaces/eleguir_nivel/fondo/fondo_interfaz_Seleccion_de_nivel.png").convert()  
       
        self.botones = [{
                "rect": pygame.Rect(175, 345, 213, 84),
                "normal": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel1_hover.png").convert_alpha()
            },
            {
                "rect": pygame.Rect(409, 345, 213, 84),
                "normal": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel2_hover.png").convert_alpha()
            },
            {
                "rect": pygame.Rect(634, 345, 213, 84),
                "normal": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/interfaces/eleguir_nivel/botones/boton_interfaz_eleguir_nivel_nivel3_hover.png").convert_alpha()
            },
            {
                "rect": pygame.Rect(0, 2, 120, 67),
                "normal": pygame.image.load("assets_PI/sprites/boton_back.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/sprites/boton_back_hover.png").convert_alpha()
            }
            ]  

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, boton in enumerate(self.botones):
                if boton["rect"].collidepoint(mouse_pos):
                    if i == 0:
                        self.cambio = "nivel 1"
                    elif i == 1:
                        self.cambio = "nivel 2"
                    elif i == 2:
                        self.cambio = "nivel 3"
                    elif i == 3:
                        self.cambio = "Seleccion_dificultad"

    def update(self):
        # Aquí actualizas animaciones, colores, etc.
        pass

    def draw(self):
        self.screen.blit(self.fondo, (0,0))
        # dibujar botones
        mouse_pos = pygame.mouse.get_pos()
        for boton in self.botones:
            if boton["rect"].collidepoint(mouse_pos):
                self.screen.blit(boton["hover"], boton["rect"].topleft)
            else:
                self.screen.blit(boton["normal"], boton["rect"].topleft)


