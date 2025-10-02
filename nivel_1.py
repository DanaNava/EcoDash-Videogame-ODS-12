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

    # Objetos recogibles con nombre para mostrar en mensaje
    platano = pygame.image.load("assets_PI/basura/organica/banano.png").convert_alpha()
    agua = pygame.image.load("assets_PI/basura/inorganica/botella agua.png").convert_alpha()
    foco = pygame.image.load("assets_PI/basura/residuos_peligrosos/Foquito item-a975.png").convert_alpha()
    lata = pygame.image.load("assets_PI/basura/inorganica/lata.png").convert_alpha()
    manzana = pygame.image.load("assets_PI/basura/organica/manzene.png").convert_alpha()
    bateria = pygame.image.load("assets_PI/basura/residuos_peligrosos/batería item -9c3f.png").convert_alpha()

    basura = [
        {"imagen": platano, "rect": platano.get_rect(topleft=(200, 350)), "nombre": "Plátano"},
        {"imagen": agua, "rect": agua.get_rect(topleft=(620, 400)), "nombre": "Botella de agua"},
        {"imagen": foco, "rect": foco.get_rect(topleft=(420, 640)), "nombre": "Foco"},
        {"imagen": lata, "rect": lata.get_rect(topleft=(920, 280)), "nombre": "Lata"},
        {"imagen": manzana, "rect": manzana.get_rect(topleft=(360, 250)), "nombre": "Manzana"},
        {"imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600)), "nombre": "Batería"}
    ]

    # Colisiones con el fondo y objetos inmovibles (si quieres que los botes bloqueen,
    # déjalos aquí; si no, puedes eliminar los 3 rects de botes)
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
        pygame.Rect(793, 179, 20, 20),  # bote rojo
    ]

    botes = [
        {"nombre": "Azul", "rect": pygame.Rect(284, 155, 20, 35)},
        {"nombre": "Verde", "rect": pygame.Rect(341, 156, 20, 35)},
        {"nombre": "Rojo", "rect": pygame.Rect(793, 179, 20, 20)}
    ]

    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 2000
    fuente = pygame.font.Font(None, 36)
    velocidad = 5
    clock = pygame.time.Clock()
    running = True

    # prev_keys para detectar pulsación nueva (edge)
    prev_keys = pygame.key.get_pressed()

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while running:
        # 1) Eventos básicos (quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) Movimiento por teclas mantenidas
        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

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

        personaje_draw_rect.center = hitbox.center

        # 3) Detectar pulsaciones nuevas (edge detection)
        pressed_e = keys[pygame.K_e] and not prev_keys[pygame.K_e]
        pressed_q = keys[pygame.K_q] and not prev_keys[pygame.K_q]

        # Recoger: solo si se pulsa E (una vez) y está cerca (inflate para comodidad)
        if pressed_e:
            for obj in basura[:]:
                # usar un área un poco mayor para facilitar recogida
                if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                    if objeto_en_mano is None:
                        objeto_en_mano = obj
                        basura.remove(obj)
                        mensaje = f"Recogiste: {obj['nombre']}"
                    else:
                        mensaje = "Ya tienes un objeto en la mano"
                    mensaje_tiempo = pygame.time.get_ticks()
                    print(mensaje)
                    break  # sólo 1 objeto por pulsación

        # Tirar: pulsa Q (una vez) y estar cerca de un bote (inflate para proximidad)
        if pressed_q and objeto_en_mano is not None:
            proximity = hitbox.inflate(24, 24)
            for bote in botes:
                if proximity.colliderect(bote["rect"]):
                    mensaje = f"Tiraste {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                    objeto_en_mano = None
                    mensaje_tiempo = pygame.time.get_ticks()
                    print(mensaje)
                    break

        # 4) DIBUJAR (limpiar todo con fill para evitar zonas sin cubrir)
        screen.fill((0, 0, 0))        # limpia toda la ventana
        screen.blit(fondo, (0, 0))    # luego dibuja el fondo

        # Objetos recogibles
        for obj in basura:
            screen.blit(obj["imagen"], obj["rect"])

        # Personaje
        screen.blit(personaje, personaje_draw_rect)

        # Capas delante
        screen.blit(capa_delante, (709, 334))
        screen.blit(capa_delante_2, (814, 418))

        # Mensaje con fondo sólido para que no deje "sombra"
        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
            mensaje_rect = pygame.Rect(12, 12, 500, 36)
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            texto = fuente.render(mensaje, True, (255, 255, 255))
            screen.blit(texto, (20, 20))
        else:
            mensaje = ""

        pygame.display.flip()
        clock.tick(60)

        # actualizar prev_keys para la siguiente iteración
        prev_keys = keys

    pygame.quit()

# Para probar
if __name__ == "__main__":
    run_level1()
