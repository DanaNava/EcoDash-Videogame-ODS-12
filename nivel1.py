# Importar pygame
import pygame
import sys
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Trash Hunters')

#Imagenes
background = pygame.image.load("FINALL.png")
personaje = pygame.image.load("PI_personaje_m_ver_delante.png")

platano = pygame.image.load("banano.png")
agua = pygame.image.load("botella agua.png")
foco = pygame.image.load("Foquito item-a975.png")
lata = pygame.image.load("lata.png")
manzana = pygame.image.load("manzene.png")
bateria = pygame.image.load("batería item -9c3f.png")

# Coordenadas de cada objeto
basura = [
     {"imagen": platano, "rect": platano.get_rect(topleft = (200, 350))},
     {"imagen": agua, "rect": agua.get_rect(topleft=(620, 400))},
     {"imagen": foco, "rect": foco.get_rect(topleft=(420, 640))},
     {"imagen": lata, "rect": lata.get_rect(topleft=(920, 280))},
     {"imagen": manzana, "rect": manzana.get_rect(topleft=(360, 250))},
     {"imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600))}
]

# Posicion del personaje
personaje_x = 100
personaje_y = 300

# Velocidad del personaje
velocidad = 5

# Variable de la velocidad del juego
clock = pygame.time.Clock()

# Hitbox del personajito
personaje_rect = personaje.get_rect(topleft = (personaje_x, personaje_y))

# Objetos con los que el personaje hara colision
colisiones = [
        pygame.Rect(9, 150, 14, 601), #pared izquierda
        pygame.Rect(10, 737, 1005, 17), #pared abajo
        pygame.Rect(1003, 11, 10, 734), #pared derecha
        pygame.Rect(690,17, 21, 450), #pared bodega izquierda
        pygame.Rect(261,15, 9, 250), #pared esquina izquierda
        pygame.Rect(26,146, 239, 140), #pared esquina arriba
        pygame.Rect(719,184, 66, 5), #cajas
        pygame.Rect(872,82, 122, 85), #estanteria
        pygame.Rect(708,336, 134, 120), #pared abajo bodega_1
        pygame.Rect(767,500, 43, 1), #perchero
        pygame.Rect(924,336, 79, 120), #pared abajo bodega_2
        pygame.Rect(400,58, 289, 73), #pared arriba sala
        pygame.Rect(421,219, 70, 71), #sofa rojo
        pygame.Rect(645,220, 43, 52), #mesa con tele
        pygame.Rect(950,577, 20, 26), #sofa zul
        pygame.Rect(178,530, 120, 20), #mesa redonda_arriba
        pygame.Rect(176,572, 120, 20), #mesa redonda_abajo
        pygame.Rect(217,451, 42, 60), #silla arriba
        pygame.Rect(127,545, 35, 1), #silla IZQUIERDA
        pygame.Rect(311,544, 35, 1), #silla derecha
        pygame.Rect(215,600, 42, 9), #silla abajo
        pygame.Rect(284,155, 20, 35), #bote azul
        pygame.Rect(341,156, 20, 35), #bote VERDE
        pygame.Rect(793,179, 20, 20), #bote rojo
        pygame.Rect(215,370, 20, 20), #platano
        pygame.Rect(370, 260, 20, 20), # manzana
        pygame.Rect(640, 415, 15, 30), # botella de agua
        pygame.Rect(935, 290, 25, 25), # lata
        pygame.Rect(65, 610, 15, 25), # batería
        pygame.Rect(435, 650, 20, 20) # foco
]

# Bucle del juego
while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# Variable que guarda la ultima posicion del personaje
      old_rect = personaje_rect.copy()

# Variable para detectar las teclas que se presionan
      teclas = pygame.key.get_pressed()

# Movimiento del personajito con las teclas
      if teclas[pygame.K_LEFT]:
            personaje_x -= velocidad
        
      if teclas[pygame.K_RIGHT]:
            personaje_x += velocidad

      if teclas[pygame.K_UP]:
            personaje_y -= velocidad

      if teclas[pygame.K_DOWN]:
            personaje_y += velocidad

# El hitbox del personaje se mueve con el 
      personaje_rect.topleft = (personaje_x, personaje_y)

# For que detecta colisiones
      for rect in colisiones:
           if personaje_rect.colliderect(rect):
                personaje_rect = old_rect #Esto hace que vuelva a la posicion anterior
                                          #de la colision mientras el evento (colision) 
                                          # se mantenga en true
                personaje_x, personaje_y = old_rect.topleft 

# Imagen de fondo a la pantalla
      screen.blit(background, (0, 0))

# Dibujar la basura en el mapa
      for obj in basura:
           screen.blit(obj["imagen"], obj["rect"].topleft)
        
# Dibujar personaje
      screen.blit(personaje, (personaje_x, personaje_y))

      for rect in colisiones:
        pygame.draw.rect(screen, (255, 0, 0), rect, 2)

# Actualizar pantalla
      pygame.display.flip()

# Velocidad a la que va a correr el juego
      clock.tick(60) 