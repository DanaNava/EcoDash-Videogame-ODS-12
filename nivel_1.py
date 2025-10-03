import pygame
import sys

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

    # -----------------------------
    # BASURA
    # -----------------------------
    platano = pygame.image.load("assets_PI/basura/organica/banano.png").convert_alpha()
    agua = pygame.image.load("assets_PI/basura/inorganica/botella agua.png").convert_alpha()
    foco = pygame.image.load("assets_PI/basura/residuos_peligrosos/Foquito item-a975.png").convert_alpha()
    lata = pygame.image.load("assets_PI/basura/inorganica/lata.png").convert_alpha()
    manzana = pygame.image.load("assets_PI/basura/organica/manzene.png").convert_alpha()
    bateria = pygame.image.load("assets_PI/basura/residuos_peligrosos/batería item -9c3f.png").convert_alpha()

    basura = [
        {"imagen": platano, "rect": platano.get_rect(topleft=(200, 350)), "nombre": "Plátano", "tipo": "organica"},
        {"imagen": agua, "rect": agua.get_rect(topleft=(620, 400)), "nombre": "Botella de agua", "tipo": "inorganica"},
        {"imagen": foco, "rect": foco.get_rect(topleft=(420, 640)), "nombre": "Foco", "tipo": "peligrosa"},
        {"imagen": lata, "rect": lata.get_rect(topleft=(920, 280)), "nombre": "Lata", "tipo": "inorganica"},
        {"imagen": manzana, "rect": manzana.get_rect(topleft=(360, 250)), "nombre": "Manzana", "tipo": "organica"},
        {"imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600)), "nombre": "Batería", "tipo": "peligrosa"}
    ]

    botes = [
        {"nombre": "Azul", "tipo": "inorganica", "rect": pygame.Rect(284, 155, 20, 35)},
        {"nombre": "Verde", "tipo": "organica", "rect": pygame.Rect(341, 156, 20, 35)},
        {"nombre": "Rojo", "tipo": "peligrosa", "rect": pygame.Rect(793, 179, 20, 20)}
    ]

    colisiones = [
        pygame.Rect(9, 150, 14, 601),
        pygame.Rect(10, 737, 1005, 17),
        pygame.Rect(1003, 11, 10, 734),
        pygame.Rect(690, 17, 21, 450),
        pygame.Rect(261, 15, 9, 250),
        pygame.Rect(26, 146, 239, 140),
        pygame.Rect(719, 184, 66, 5),
        pygame.Rect(872, 82, 122, 85),
        pygame.Rect(700, 336, 144, 120),
        pygame.Rect(767, 500, 43, 1),
        pygame.Rect(935, 336, 79, 120),
        pygame.Rect(400, 58, 289, 73),
        pygame.Rect(421, 219, 70, 71),
        pygame.Rect(645, 220, 43, 52),
        pygame.Rect(950, 577, 20, 26),
        pygame.Rect(178, 530, 120, 20),
        pygame.Rect(176, 572, 120, 20),
        pygame.Rect(217, 451, 42, 60),
        pygame.Rect(127, 545, 35, 1),
        pygame.Rect(311, 544, 35, 1),
        pygame.Rect(215, 600, 42, 9),
        pygame.Rect(284, 155, 20, 35),  # bote azul
        pygame.Rect(341, 156, 20, 35),  # bote verde
        pygame.Rect(793, 179, 20, 20)  # bote rojo
    ]

    # -----------------------------
    # ANIMACIONES
    # -----------------------------
    frames_dano = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha2.png").convert_alpha()
    ]

    frames_muerte = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte5.png").convert_alpha()
    ]

    pantalla_perdida = pygame.image.load("assets_PI/interfaces/perdida/game over 2.0.png").convert_alpha()

    animando_dano = False
    animando_muerte = False
    frame_actual_dano = 0
    frame_actual_muerte = 0
    tiempo_frame = 0
    duracion_frame = 100

    # -----------------------------
    # VARIABLES
    # -----------------------------
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 2000
    fuente = pygame.font.Font(None, 36)
    velocidad = 5
    clock = pygame.time.Clock()
    running = True
    prev_keys = pygame.key.get_pressed()
    errores = 0

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

        # Movimiento
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            hitbox.x -= velocidad
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            hitbox.x += velocidad
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            hitbox.y -= velocidad
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            hitbox.y += velocidad

        for rect in colisiones:
            if hitbox.colliderect(rect):
                hitbox.x = old_hitbox.x
                hitbox.y = old_hitbox.y
                break

        personaje_draw_rect.center = hitbox.center

        # Edge detection
        pressed_e = keys[pygame.K_e] and not prev_keys[pygame.K_e]
        pressed_q = keys[pygame.K_q] and not prev_keys[pygame.K_q]

        # Recoger objetos
        if pressed_e:
            for obj in basura[:]:
                if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                    if objeto_en_mano is None:
                        objeto_en_mano = obj
                        basura.remove(obj)
                        mensaje = f"Recogiste: {obj['nombre']}"
                    else:
                        mensaje = "Ya tienes un objeto en la mano"
                    mensaje_tiempo = pygame.time.get_ticks()
                    break

        # Tirar basura
        if pressed_q:
            if objeto_en_mano is None:
                mensaje = "No tienes ningún objeto en la mano"
                mensaje_tiempo = pygame.time.get_ticks()
            else:
                proximity = hitbox.inflate(24, 24)
                tiro_valido = False

                for bote in botes:
                    if proximity.colliderect(bote["rect"]):
                        tiro_valido = True
                        if objeto_en_mano["tipo"] == bote["tipo"]:
                            mensaje = f"Tiraste {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                            objeto_en_mano = None
                        else:
                            errores += 1
                            mensaje = f"No puedes tirar {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            objeto_en_mano = None
                        mensaje_tiempo = pygame.time.get_ticks()
                        break

                if not tiro_valido:
                    mensaje = "No hay un bote cerca"
                    mensaje_tiempo = pygame.time.get_ticks()

        # -----------------------------
        # DIBUJAR
        # -----------------------------
        screen.fill((0, 0, 0))
        screen.blit(fondo, (0, 0))

        for obj in basura:
            screen.blit(obj["imagen"], obj["rect"])

        screen.blit(personaje, personaje_draw_rect)
        screen.blit(capa_delante, (709, 334))
        screen.blit(capa_delante_2, (814, 418))

        # Mensaje
        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
            mensaje_rect = pygame.Rect(12, 12, 500, 36)
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            texto = fuente.render(mensaje, True, (255, 255, 255))
            screen.blit(texto, (20, 20))
        else:
            mensaje = ""

        # Animación de daño
        if animando_dano:
            ahora = pygame.time.get_ticks()
            if ahora - tiempo_frame >= duracion_frame:
                frame_actual_dano += 1
                tiempo_frame = ahora
                if frame_actual_dano >= len(frames_dano):
                    animando_dano = False
                    frame_actual_dano = 0
            if animando_dano:
                frame = frames_dano[frame_actual_dano]
                screen.blit(frame, personaje_draw_rect.topleft)

        # Animación de muerte y pantalla de pérdida
        if errores >= 3:
            animando_muerte = True
            frame_actual_muerte = 0
            tiempo_frame = pygame.time.get_ticks()
            errores = -1  # evitar repetir la animación

        if animando_muerte:
            ahora = pygame.time.get_ticks()
            if ahora - tiempo_frame >= duracion_frame:
                frame_actual_muerte += 1
                tiempo_frame = ahora
                if frame_actual_muerte >= len(frames_muerte):
                    # Animación terminada -> mostrar pantalla de pérdida
                    screen.blit(pantalla_perdida, (0, 0))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    running = False
            else:
                frame = frames_muerte[frame_actual_muerte]
                screen.blit(frame, personaje_draw_rect.topleft)

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys

        pygame.quit()