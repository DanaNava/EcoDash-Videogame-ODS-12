# Para iniciar cualquier proyecto en pygame 
import pygame
import sys
pygame.init()

# Colorcitos
negro = (   0,   0,   0)
blanco = (255, 255, 255)
verde = (  0, 255,   0)
rojo = (255,   0,   0)
azul = (  0,   0, 255)

# Crear ventana
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

#Imagen de fondo
background = pygame.image.load("background1.png").convert()
imagen_redimensionada = pygame.transform.scale(background, (1024, 768))
start_img = pygame.image.load("start1.png")
start_hover = pygame.image.load("start1h.png")
tutorial = pygame.image.load("tutorial.png")
tutorial_hover = pygame.image.load("tutorialh.png")
configuracion = pygame.image.load("configuracion.png")
configuracion_hover = pygame.image.load("configuracionh.png")
creditos = pygame.image.load("creditos.png")
creditos_hover = pygame.image.load("creditosh.png")


# clase boton
class Button():
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

start_button = Button(403, 315, start_img, start_hover)

# Otro boton
class Button2():
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

tutorial_button = Button2(404, 537, tutorial, tutorial_hover)

# Otro boton
class Button3():
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

configuracion_button = Button3(10, 666, configuracion, configuracion_hover)

# Otro boton
class Button4():
    def __init__(self, x, y, image, image_hover):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            screen.blit(self.image_hover, self.rect)
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

creditos_button = Button4(925, 676, creditos, creditos_hover)


# Crear el bucle del juego
while True:
    pos_mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Condicion que detectara que se clickeo un boton y actualizara su estado
    if start_button.clicked(event):
        #! Iniciar nueva interfaz aqui
        print("Inicia el jueguito aqui")

    if tutorial_button.clicked(event):
        #! Iniciar nueva interfaz aqui
        print("Iniciar tutorial aqui")

    if configuracion_button.clicked(event):
        #! Iniciar nueva interfaz aqui
        print("Abrir configuracion aqui")

    if creditos_button.clicked(event):
        #! Iniciar nueva interfaz aqui
        print("Abrir creditos aqui")

    # Poner fondo en la pantalla
    screen.blit(imagen_redimensionada, (0, 0))

    # Inicia zona de diseños y dibujos

    start_button.draw(pos_mouse)
    tutorial_button.draw(pos_mouse)
    configuracion_button.draw(pos_mouse)
    creditos_button.draw(pos_mouse)
    
    # Actualizar pantalla
    pygame.display.flip()
