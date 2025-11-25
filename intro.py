import pygame
from ffpyplayer.player import MediaPlayer

def run_intro(idioma, volumen):
    pygame.init()
    try:
        pygame.mixer.init()
    except:
        print("⚠ No se pudo iniciar el audio (pero el juego continuará).")

    try:
        pygame.mixer.music.stop()
    except:
        pass

    screen = pygame.display.set_mode((1024, 768))
    clock = pygame.time.Clock()

    # Selección del video según idioma
    if idioma.lower() == "en":
        ruta_video = "assets_PI/Intro/Intro_EcoDash_dg.mp4" 
    else:
        ruta_video = "assets_PI/Intro/Intro_EcoDash_gd.mp4"

    player = MediaPlayer(ruta_video)

    try: player.set_volume(volumen)
    except: pass

    #Cargamos el sonido del botón
    try:
        click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    except:
        click_sound = None

    # Fuente del texto
    font = pygame.font.Font(None, 40)

    # Rectángulo base del botón
    boton_rect = pygame.Rect(800, 700, 180, 50)

    # Tiempo inicial
    start_time = pygame.time.get_ticks()
    alpha = 255

    # Para animar fade out global
    fade_out = False
    fade_opacity = 0  # 0 → sin fade, 255 → negro total

    running = True

    last_frame_surface = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.close_player()
                pygame.quit()
                return "salir"

            # Salto con clic
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(pygame.mouse.get_pos()):
                    if click_sound: click_sound.play()
                    fade_out = True  # Iniciar fade
            

            # Salto con ESC/ESPACIO
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_SPACE]:
                    if click_sound: click_sound.play()
                    fade_out = True

        # ---------------- VIDEO --------------------
        frame, val = player.get_frame()

        # ⚠ Evitar EOF hasta que el fade o el botón lo digan
        if val == 'eof':
            frame = None  # no actualizamos más frames, pero NO salimos
            fade_out = True

        # Si hay un frame nuevo, lo guardamos
        if frame is not None:
            img, t = frame
            w, h = img.get_size()
            last_frame_surface = pygame.image.frombuffer(img.to_bytearray()[0], (w, h), "RGB")

        # Dibujamos el último frame válido o un fondo negro
        if last_frame_surface is not None:
            screen.blit(pygame.transform.scale(last_frame_surface, screen.get_size()), (0, 0))
        else:
            screen.fill((0, 0, 0))

        # ---------------- BOTÓN --------------------
        mouse_pos = pygame.mouse.get_pos()
        elapsed = (pygame.time.get_ticks() - start_time) / 1000

        # Opacidad después de 5s
        if elapsed > 5:
            alpha = max(120, alpha - 1.2)
            alpha = int(alpha)


        # Hover animado (suave)
        hovering = boton_rect.collidepoint(mouse_pos)
        grow = 8 if hovering else 0

        # Superficie con alpha
        boton_surface = pygame.Surface(
            (boton_rect.width + grow, boton_rect.height + grow), pygame.SRCALPHA
        )

        # Fondo con transparencia
        fondo_alpha = min(255, alpha + (40 if hovering else 0)) 
        boton_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(
            boton_surface,
            (0, 0, 0, fondo_alpha),
            (0, 0, boton_rect.width + grow, boton_rect.height + grow),
            border_radius=18,
        )


        # Posición centrada
        boton_x = boton_rect.x - grow // 2
        boton_y = boton_rect.y - grow // 2

        # Borde semitransparente
        border_color = (255, 255, 255, int(alpha))
        pygame.draw.rect(
            boton_surface,
            border_color,
            (0, 0, boton_rect.width + grow, boton_rect.height + grow),
            width=3,
            border_radius=18,
        )

        screen.blit(boton_surface, (boton_x, boton_y))

        # 🏷 Texto transparente
        texto = font.render("Saltar", True, (255, 255, 255))
        texto.set_alpha(alpha)
        text_rect = texto.get_rect(center=(boton_x + (boton_rect.width + grow)//2,
                                           boton_y + (boton_rect.height + grow)//2))
        screen.blit(texto, text_rect)

        # --------------- FADE OUT -------------------
        if fade_out:
            fade_opacity += 8  # Velocidad del fade
            fade_layer = pygame.Surface(screen.get_size())
            fade_layer.set_alpha(fade_opacity)
            fade_layer.fill((0, 0, 0))
            screen.blit(fade_layer, (0, 0))

            if fade_opacity >= 255:
                player.close_player()
                return "continuar"

        pygame.display.flip()
        clock.tick(60)

    player.close_player()
    return "continuar"