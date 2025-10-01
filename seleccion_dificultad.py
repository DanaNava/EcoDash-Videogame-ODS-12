import pygame

class MiInterfaz:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.cambio = None
        # Aquí cargas tus imágenes, botones, fuentes, etc.
        self.fondo = pygame.image.load("assets_PI/interfaces/eleguir_dificultad/fondo/fondo_interfaz_elegir_dificultad.png").convert()  
       
        self.botones = [{
                "rect": pygame.Rect(199, 303, 237, 96),
                "normal": pygame.image.load("assets_PI/interfaces/eleguir_dificultad/botones/boton_interfaz_eleguir_dificultad_facil.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/interfaces/eleguir_dificultad/botones/boton_interfaz_eleguir_dificultad_facil_hover.png").convert_alpha()
            },
            {
                "rect": pygame.Rect(197, 475, 235, 97),
                "normal": pygame.image.load("assets_PI/interfaces/eleguir_dificultad/botones/boton_interfaz_eleguir_dificultad_medio.png").convert_alpha(),
                "hover": pygame.image.load("assets_PI/interfaces/eleguir_dificultad/botones/boton_interfaz_eleguir_dificultad_medio_hover.png").convert_alpha()
            }]  

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, boton in enumerate(self.botones):
                if boton["rect"].collidepoint(mouse_pos):
                   if i == 0:
                    self.cambio = "facil"
                   elif i == 1:
                    self.cambio = "medio"

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





