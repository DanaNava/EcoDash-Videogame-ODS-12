import pygame
import sys


def run_level1():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 1")

    # -----------------------------
    # CARGA DE IMÁGENES
    # -----------------------------
    fondo = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_3.png").convert_alpha()
    capa_delante = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_derecha.png").convert_alpha()
    capa_delante_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_izquierda_fondo.png").convert_alpha()
    capa_delante_3 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_arriba.png").convert_alpha()
    capa_delante_4 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_sillon_1.png").convert_alpha()
    capa_delante_5 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_sillon_2.png").convert_alpha()
    capa_delante_6 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_sillon_3.png").convert_alpha()
    capa_delante_7 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_sillon_4.png").convert_alpha()
    capa_delante_8 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_mesa_derecha_1.png").convert_alpha()
    capa_delante_9 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_mesa_derecha_2.png").convert_alpha()
    capa_delante_10 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_mesa_izquierda_1.png").convert_alpha()
    capa_delante_11 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_mesa_izquierda_2.png").convert_alpha()
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")


    #Escalar imagenes
    win = pygame.transform.scale(w, (1024, 768))
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))

    #Cargar botones
    boton_reintentar = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez.png").convert_alpha()
    boton_reintentar_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez_hover.png").convert_alpha()
    boton_menu = pygame.image.load("assets_PI/interfaces/perdida/boton_menu.png").convert_alpha()
    boton_menu_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_menu_hover.png").convert_alpha()

    boton_win_menu_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_hover_pantalla_victoria.png")
    boton_win_menu = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_pantalla_victoria.png")
    boton_win_intentar = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria.png")
    boton_win_intentar_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria_hover.png")


    rect_reintentar_victoria = boton_win_menu.get_rect(center=(515, 487))
    rect_menu_victoria = boton_win_intentar.get_rect(center=(515, 570))

    rect_reintentar = boton_reintentar.get_rect(center=(515, 467))
    rect_menu = boton_menu.get_rect(center=(515, 550))


    personaje = pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha1.png").convert_alpha()
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 70, 70)
    hitbox.center = personaje_draw_rect.center


    # -----------------------------
    # CARGA musica de fondo
    # -----------------------------
    pygame.mixer.music.load("assets_PI/musica/musica_nivel.wav")
    pygame.mixer.music.set_volume(0.5)  # volumen 0.0 a 1.0
    pygame.mixer.music.play(-1)  # -1 = bucle infinito

    # -----------------------------
    # CARGA efectos de sonido
    # -----------------------------
    sonido_caminar = pygame.mixer.Sound("assets_PI/sonidos/pasos_madera.wav")
    sonido_dano = pygame.mixer.Sound("assets_PI/sonidos/recibir_daño.wav")
    sonido_morir = pygame.mixer.Sound("assets_PI/sonidos/morir.wav")
    sonido_recoger = pygame.mixer.Sound("assets_PI/sonidos/recoger_basura.wav")
    sonido_tirar_correcto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_bien.wav")
    sonido_tirar_incorrecto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_error.wav")


    # Volúmenes
    sonido_caminar.set_volume(1)
    sonido_dano.set_volume(0.1)
    sonido_morir.set_volume(0.6)
    sonido_recoger.set_volume(0.4)
    sonido_tirar_correcto.set_volume(0.5)
    sonido_tirar_incorrecto.set_volume(1)


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
        pygame.Rect(9, 150, 30, 601),  # pared izquierda
        pygame.Rect(10, 725, 1005, 50),  # pared abajo
        pygame.Rect(1003, 11, 10, 734),  # pared derecha
        pygame.Rect(690, 17, 21, 450),  # pared bodega izquierda
        pygame.Rect(261, 15, 9, 250),  # pared esquina izquierda
        pygame.Rect(26, 146, 239, 140),  # pared esquina arriba
        pygame.Rect(719, 184, 66, 5),  # cajas
        pygame.Rect(872, 82, 122, 85),  # estanteria
        pygame.Rect(693, 391, 135, 75),  # pared abajo bodega_1
        pygame.Rect(767, 500, 43, 1),  # perchero
        pygame.Rect(959, 391, 40, 75),  # pared abajo bodega_2
        pygame.Rect(400, 58, 289, 73),  # pared arriba sala
        pygame.Rect(421, 219, 70, 71),  # sofa rojo
        pygame.Rect(645, 210, 43, 60),  # mesa con tele
        pygame.Rect(950, 577, 20, 26),  # sofa azul
        pygame.Rect(185, 519, 107, 20),  # mesa redonda_arriba
        pygame.Rect(176, 572, 120, 20),  # mesa redonda_abajo
        pygame.Rect(217, 451, 42, 60),  # silla arriba
        pygame.Rect(127, 545, 35, 1),  # silla izquierda
        pygame.Rect(311, 544, 35, 1),  # silla derecha
        pygame.Rect(215, 600, 42, 9),  # silla abajo
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
    tiempo_fin_animacion = None
    frame_actual_dano = 0
    frame_actual_muerte = 0
    tiempo_frame = 0
    duracion_frame = 100

    # -----------------------------
    # VARIABLES
    # -----------------------------
    
    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 2000
    fuente = pygame.font.Font(None, 36)
    
    # velocidad del juego y personaje
    velocidad = 5
    clock = pygame.time.Clock()
    
    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max
    


    # Tiempo
    tiempo = 90
    inicio_tiempo = pygame.time.get_ticks()
    fuente_tiempo =pygame.font.Font(None, 48)

    # Variable indicadora para cambiar la musica
    musica_cambiada = False

    # Verificar si gano
    def ganar(basura, objeto_en_mano):
        return len(basura) == 0 and objeto_en_mano is None

    # Variable para el while infinito, para las teclas pulsadas y un contador de errores
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

        # Al caminar
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            if not pygame.mixer.get_busy():  # Para que no se superponga
                sonido_caminar.play()

        for rect in colisiones:
            if hitbox.colliderect(rect):
                hitbox.x = old_hitbox.x
                hitbox.y = old_hitbox.y
                break

        personaje_draw_rect.center = hitbox.center

        # Edge detection
        pressed_o = keys[pygame.K_o] and not prev_keys[pygame.K_o]
        pressed_p = keys[pygame.K_p] and not prev_keys[pygame.K_p]
        pressed_z = keys[pygame.K_z] and not prev_keys[pygame.K_z]
        pressed_x = keys[pygame.K_x] and not prev_keys[pygame.K_x]

        # Recoger objetos
        if pressed_o or pressed_z:
            for obj in basura[:]:
                if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                    if objeto_en_mano is None:
                        sonido_recoger.play()
                        objeto_en_mano = obj
                        basura.remove(obj)
                        mensaje = f"Recogiste: {obj['nombre']}"
                    else:
                        mensaje = "Ya tienes un objeto en la mano"
                    mensaje_tiempo = pygame.time.get_ticks()
                    break

        # Tirar basura
        if pressed_p or pressed_x:
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
                            sonido_tirar_correcto.play()
                        else:
                            errores += 1
                            mensaje = f"No puedes tirar {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            objeto_en_mano = None
                            sonido_tirar_incorrecto.play()
                        
                        # BARRA DE VIDA
                            vida_actual -= 1
                            if vida_actual < 0:
                                vida_actual = 0
                            elif vida_actual == 2:
                                vida_actual = 2
                            elif vida_actual == 1:
                                vida_actual = 1

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

        # [Nuevo] BARRA DE VIDA ---------    
        if vida_actual == 3:
            screen.blit(barra_vida, (20, -20))
        elif vida_actual == 2:
            screen.blit(barra_vida2, (20, -20))
        elif vida_actual == 1:
            screen.blit(barra_vida1, (20, -20))           

        for obj in basura:
            screen.blit(obj["imagen"], obj["rect"])

        screen.blit(personaje, personaje_draw_rect)
     # [Nuevo] DIBUJAR OBJETO EN LA MANO -------------------
        if objeto_en_mano is not None:
            mano_x = personaje_draw_rect.centerx + 20
            mano_y = personaje_draw_rect.centery 
            screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))


        screen.blit(capa_delante, (938, 424))
        screen.blit(capa_delante_2, (816, 423))
        screen.blit(capa_delante_3, (698, 333))
        screen.blit(capa_delante_4, (425, 215))
        screen.blit(capa_delante_5, (434, 202))
        screen.blit(capa_delante_6, (449, 205))
        screen.blit(capa_delante_7, (430, 205))
        screen.blit(capa_delante_8, (244, 514))
        screen.blit(capa_delante_9, (284, 519))
        screen.blit(capa_delante_10, (192, 514))
        screen.blit(capa_delante_10, (185, 519))

        # Mensaje
        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
            mensaje_rect = pygame.Rect(520, 12, 500, 36)
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            texto = fuente.render(mensaje, True, (255, 255, 255))
            screen.blit(texto, (mensaje_rect.x + 10, mensaje_rect.y + 5))
        else:
            mensaje = ""

        # Animación de daño
        if animando_dano:
            if frame_actual_dano == 0:
                sonido_dano.play()
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

        # [Nuevo] TIEMPO-----------
        tiempo_actual = pygame.time.get_ticks()
        segundos = (tiempo_actual - inicio_tiempo)  // 1000
        tiempo_restante = max(0, tiempo - segundos)

        if tiempo_restante <= 20 and not musica_cambiada:
            pygame.mixer.music.load("assets_PI/musica/musica_apresurada.ogg")  # tu nuevo archivo
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        color_tiempo = (255, 0, 0) if tiempo_restante <= 20 else (255, 255, 255)


        # Convertir a minutos y segundos
        minutos = tiempo_restante // 60
        segundos_restantes = tiempo_restante % 60

        # Formato mm:ss con ceros (01:05)
        tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"

        pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
        texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
        screen.blit(texto_tiempo, (20, 90))

        
        def mostrar_pantalla_perdida():
            pygame.mixer.music.load("assets_PI/sonidos/musica de perdida.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

            while True:
                screen.fill((0, 0, 0))
                screen.blit(pantalla_perdida, (0, 0))

                mouse_pos = pygame.mouse.get_pos()

                # Botones
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_reintentar_hover, rect_reintentar)
                else:
                    screen.blit(boton_reintentar, rect_reintentar)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_menu_hover, rect_menu)
                else:
                    screen.blit(boton_menu, rect_menu)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            run_level1()  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            return  # volver al menú

        def mostrar_pantalla_victoria():
            pygame.mixer.music.load("assets_PI\musica\musica_victoria.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

            while True:
                screen.fill((0, 0, 0))
                screen.blit(win, (0, 0))

                mouse_pos = pygame.mouse.get_pos()

                # Botones
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_win_intentar, rect_reintentar_victoria)
                else:
                    screen.blit( boton_win_intentar_hover, rect_reintentar_victoria)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_win_menu, rect_menu_victoria)
                else:
                    screen.blit(boton_win_menu_hover, rect_menu_victoria)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            run_level1()  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            return  # volver al menú



        #ganar
        if ganar(basura, objeto_en_mano):
            mostrar_pantalla_victoria()

         
        # Animación de muerte y pantalla de pérdida
        # Animación de muerte y pantalla de pérdida
        # Animación de muerte y pantalla de pérdida
        if errores >= 3:
            if not animando_muerte and not tiempo_fin_animacion:
                animando_muerte = True
                frame_actual_muerte = 0
                tiempo_frame_muerte = pygame.time.get_ticks()
                tiempo_fin_animacion = None
                sonido_morir.play()

            if animando_muerte:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_frame_muerte >= duracion_frame:
                    frame_actual_muerte += 1
                    tiempo_frame_muerte = ahora

                    if frame_actual_muerte >= len(frames_muerte):
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = len(frames_muerte) - 1

                screen.fill((0, 0, 0))
                screen.blit(fondo, (0, 0))
                screen.blit(frames_muerte[frame_actual_muerte], personaje_draw_rect.topleft)
                pygame.display.flip()
                clock.tick(60)

            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    mostrar_pantalla_perdida()
                else:
                    screen.fill((0, 0, 0))
                    screen.blit(fondo, (0, 0))
                    screen.blit(frames_muerte[-1], personaje_draw_rect.topleft)
                    pygame.display.flip()
                    clock.tick(60)
        
        muerte_por_tiempo = False
        # Perder si se acaba el tiempo
        if tiempo_restante <= 0 and not muerte_por_tiempo:
            muerte_por_tiempo = True
            errores = 3

        if errores >= 3:
            if not animando_muerte and not tiempo_fin_animacion:
                animando_muerte = True
                frame_actual_muerte = 0
                tiempo_frame_muerte = pygame.time.get_ticks()
                tiempo_fin_animacion = None
                sonido_morir.play()

            if animando_muerte:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_frame_muerte >= duracion_frame:
                    frame_actual_muerte += 1
                    tiempo_frame_muerte = ahora

                    if frame_actual_muerte >= len(frames_muerte):
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = len(frames_muerte) - 1

                screen.fill((0, 0, 0))
                screen.blit(fondo, (0, 0))
                screen.blit(frames_muerte[frame_actual_muerte], personaje_draw_rect.topleft)
                pygame.display.flip()
                clock.tick(60)
            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    mostrar_pantalla_perdida()
                else:
                    screen.fill((0, 0, 0))
                    screen.blit(fondo, (0, 0))
                    screen.blit(frames_muerte[-1], personaje_draw_rect.topleft)
                    pygame.display.flip()
                    clock.tick(60)

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys

    pygame.quit()


if __name__ == "__main__":
    run_level1()