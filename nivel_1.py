import pygame

def run_level1():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 1")

    # -----------------------------
    # CARGA DE IMÁGENES
    # -----------------------------
    fondo = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_2.png").convert_alpha()
    capa_delante = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_fondo_2.png").convert_alpha()
    capa_delante_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_izquierda_fondo.png").convert_alpha()

    personaje = pygame.image.load(
        "assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha1.png"
    ).convert_alpha()
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 80, 80)
    hitbox.center = personaje_draw_rect.center

    # Objetos recogibles
    botella_image = pygame.image.load("assets_PI/basura/inorganica/botella agua.png").convert_alpha()
    botella_rect = botella_image.get_rect(topleft=(627, 377))
    objetos = [
        {"nombre": "botella", "imagen": botella_image, "rect": botella_rect},
    ]

    # Colisiones con el fondo y objetos inmovibles
    colisiones = [
        pygame.Rect(9, 150, 14, 601),  # pared izquierda
        pygame.Rect(10, 737, 1005, 17),  # pared abajo
        pygame.Rect(1003, 11, 10, 734),  # pared derecha
        pygame.Rect(690, 17, 21, 450),  # pared bodega izquierda
        pygame.Rect(261, 15, 9, 250),  # pared esquina izquierda
        pygame.Rect(26, 146, 239, 140),  # pared esquina arriba
        pygame.Rect(719, 184, 66, 5),  # cajas
        pygame.Rect(872, 82, 122, 85),  # estanteria
        pygame.Rect(700, 336, 144, 120),  # pared abajo bodega_1
        pygame.Rect(767, 500, 43, 1),  # perchero
        pygame.Rect(935, 336, 79, 120),  # pared abajo bodega_2
        pygame.Rect(400, 58, 289, 73),  # pared arriba sala
        pygame.Rect(421, 219, 70, 71),  # sofa rojo
        pygame.Rect(645, 220, 43, 52),  # mesa con tele
        pygame.Rect(950, 577, 20, 26),  # sofa azul
        pygame.Rect(178, 530, 120, 20),  # mesa redonda_arriba
        pygame.Rect(176, 572, 120, 20),  # mesa redonda_abajo
        pygame.Rect(217, 451, 42, 60),  # silla arriba
        pygame.Rect(127, 545, 35, 1),  # silla izquierda
        pygame.Rect(311, 544, 35, 1),  # silla derecha
        pygame.Rect(215, 600, 42, 9),  # silla abajo
        pygame.Rect(284, 155, 20, 35),  # bote azul
        pygame.Rect(341, 156, 20, 35),  # bote verde
        pygame.Rect(793, 179, 20, 20),  # bote rojo
    ]

    inventario = []
    velocidad = 5
    clock = pygame.time.Clock()
    running = True

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

        # Movimiento del jugador
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hitbox.x -= velocidad
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hitbox.x += velocidad
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            hitbox.y -= velocidad
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            hitbox.y += velocidad

        # Colisiones con objetos inmovibles
        for rect in colisiones:
            if hitbox.colliderect(rect):
                hitbox.x = old_hitbox.x
                hitbox.y = old_hitbox.y
                break

        # Mantener la imagen centrada en la hitbox
        personaje_draw_rect.center = hitbox.center

        # Recoger objetos
        for obj in objetos[:]:
            if hitbox.colliderect(obj["rect"]) and keys[pygame.K_e]:
                inventario.append(obj)
                objetos.remove(obj)
                print(f"Recogido: {obj['nombre']}")  # para verificar

        # -----------------------------
        # DIBUJAR TODO
        # -----------------------------
        screen.blit(fondo, (0, 0))  # fondo primero

        # Objetos recogibles
        for obj in objetos:
            screen.blit(obj["imagen"], obj["rect"])

        # Personaje
        screen.blit(personaje, personaje_draw_rect)

        # Capas delante
        screen.blit(capa_delante, (709, 334))
        screen.blit(capa_delante_2, (814, 418))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
