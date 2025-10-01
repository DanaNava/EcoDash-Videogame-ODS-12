import pygame

def run_level1():
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 1")

    fondo = pygame.image.load("assets_PI/diseyo_nivel/nivel1/FINALL.png")
    personaje = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_delante.png")
    personaje_rect = personaje.get_rect(center=(489, 420))
    capa_delante = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta.png")
    
    velocidad = 5  # Velocidad de movimiento
    running = True
    clock = pygame.time.Clock()
    
    colisiones = [
        # EJEMPLOS (BORRARLOS Y PONER LOS TUYOS)
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
        pygame.Rect(793,179, 20, 20) #bote rojo
    ]

    overlay = pygame.Surface((1024, 768), pygame.SRCALPHA)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        keys = pygame.key.get_pressed()

        old_pos = personaje_rect.copy()
        
           
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            personaje_rect.x -= velocidad
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            personaje_rect.x += velocidad
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            personaje_rect.y -= velocidad
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            personaje_rect.y += velocidad

        for rect in colisiones:
            if personaje_rect.colliderect(rect):
                personaje_rect = old_pos

        pygame.draw.rect(screen, (255, 0, 0), colisiones[15], 2)
        pygame.draw.rect(screen, (255, 0, 0), colisiones[3], 2)

        screen.blit(fondo, (0, 0))
        screen.blit(personaje, personaje_rect)
        screen.blit(capa_delante, (841,335))  
        pygame.display.flip()
        clock.tick(60)
