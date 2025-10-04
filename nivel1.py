# Importar pygame
import pygame
import sys

# Funcion en donde ocurre todo el nivel 1
def run_level1():
    #Inicia pygame
    pygame.init()
    # Para sonidos
    pygame.mixer.init() 
    # Crear pantalla
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Trash Hunters')
    


    # --------------------------------------------
    # --------------- IMAGENES -------------------
    #---------------------------------------------
    background = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_2.png")
    capa_delante = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_fondo_2.png")
    capa_delante_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_izquierda_fondo.png")
    capa_delante_3 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_arriba.png")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")

    # Escalar imagenes
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))
    win = pygame.transform.scale(w, (1024, 768))

    # ------------- Botones -------------
    boton_win_intentar = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria.png")
    boton_win_intentar_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria_hover.png")
    boton_win_menu = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_pantalla_victoria.png")
    boton_win_menu_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_hover_pantalla_victoria.png")
    boton_reintentar = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez.png").convert_alpha()
    boton_reintentar_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez_hover.png").convert_alpha()
    boton_menu = pygame.image.load("assets_PI/interfaces/perdida/boton_menu.png").convert_alpha()
    boton_menu_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_menu_hover.png").convert_alpha()

    # Posiciones botones
    rect_reintentar_victoria = boton_win_intentar.get_rect(center=(515, 487))
    rect_menu_victoria = boton_win_menu.get_rect(center=(515, 570))
    rect_reintentar = boton_reintentar.get_rect(center=(515, 467))
    rect_menu = boton_menu.get_rect(center=(515, 550))

    #------------ Personaje --------------
    personaje = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_delante.png")
    # Hitbox del personaje
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 50, 50)
    hitbox.center = personaje_draw_rect.center

    #---------------------------------------------
    #----------------- MÚSICA --------------------
    #---------------------------------------------

    # Musica de fondo del nivel 1
    pygame.mixer.music.load("assets_PI/musica/musica_nivel.wav")
    #Para la intensidad del volumen 
    pygame.mixer.music.set_volume(0.5)
    #Bucle de la musica
    pygame.mixer.music.play(-1)
    
    # Efectos de sonidos 
    sonido_caminar = pygame.mixer.Sound("assets_PI/sonidos/pasos_madera.wav")
    sonido_dano = pygame.mixer.Sound("assets_PI/sonidos/recibir_daño.wav")
    sonido_morir = pygame.mixer.Sound("assets_PI/sonidos/morir.wav")
    sonido_recoger = pygame.mixer.Sound("assets_PI/sonidos/recoger_basura.wav")
    sonido_tirar_correcto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_bien.wav")
    sonido_tirar_incorrecto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_error.wav")
    
    # Intensidad del volumen
    sonido_caminar.set_volume(1)
    sonido_dano.set_volume(0.1)
    sonido_morir.set_volume(0.6)
    sonido_recoger.set_volume(0.4)
    sonido_tirar_correcto.set_volume(0.5)
    sonido_tirar_incorrecto.set_volume(1)


    # -------------- Basura ---------------
    platano = pygame.image.load("assets_PI/basura/organica/banano.png")
    agua = pygame.image.load("assets_PI/basura/inorganica/botella agua.png")
    foco = pygame.image.load("assets_PI/basura/residuos_peligrosos/Foquito item-a975.png")
    lata = pygame.image.load("assets_PI/basura/inorganica/lata.png")
    manzana = pygame.image.load("assets_PI/basura/organica/manzene.png")
    bateria = pygame.image.load("assets_PI/basura/residuos_peligrosos/batería item -9c3f.png")
    
    # Coordenadas de la basura
    basura = [
         {"nombre": "Plátano", "tipo": "organica", "imagen": platano, "rect": platano.get_rect(topleft=(200, 350))},
         {"nombre": "Agua", "tipo": "inorganica", "imagen": agua, "rect": agua.get_rect(topleft=(620, 400))},
         {"nombre": "Foco", "tipo": "peligrosa", "imagen": foco, "rect": foco.get_rect(topleft=(420, 640))},
         {"nombre": "Lata", "tipo": "inorganica", "imagen": lata, "rect": lata.get_rect(topleft=(920, 280))},
         {"nombre": "Manzana", "tipo": "organica", "imagen": manzana, "rect": manzana.get_rect(topleft=(360, 250))},
         {"nombre": "Batería", "tipo": "peligrosa", "imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600))}
      ]
    
    #-------------- Botes ----------------
    botes = [
        {"nombre": "Azul", "tipo": "inorganica", "rect": pygame.Rect(284, 155, 20, 35)},
        {"nombre": "Verde", "tipo": "organica", "rect": pygame.Rect(341, 156, 20, 35)},
        {"nombre": "Rojo", "tipo": "peligrosa", "rect": pygame.Rect(793, 179, 20, 20)}
    ]



    #-------------------------------------------
    #-------------- COLISIONES -----------------
    #-------------------------------------------

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
    ]
    
    #---------------------------------------------------
    # ---------------- ANIMACIONES ---------------------
    #---------------------------------------------------

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



    #------------------------------------------
    #-------------- VARIABLES -----------------
    #------------------------------------------

    # Variables de animaciones
    animando_dano = False
    animando_muerte = False
    tiempo_fin_animacion = None
    frame_actual_dano = 0
    frame_actual_muerte = 0
    tiempo_frame = 0
    duracion_frame = 100

    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 2000
    fuente = pygame.font.Font(None, 36)


    channel_walk = pygame.mixer.Channel(0)
    
    # Velocidad del personaje
    velocidad = 5
    
    # Variable de la velocidad del juego
    clock = pygame.time.Clock()

    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo
    tiempo = 120
    inicio_tiempo = pygame.time.get_ticks()
    fuente_tiempo =pygame.font.Font(None, 48)

    # Variable indicadora para cambiar la musica
    musica_cambiada = False

    # Funcion para ganar
    def ganar(basura, objeto_en_mano):
        return len(basura) == 0 and objeto_en_mano is None

    # Variable para el bucle del juego
    running = True

    # Variable que detecta nuevas pulsaciones
    prev_keys = pygame.key.get_pressed()

    # Contador de errores del jugador
    errores = 0

    # --------------------------------------------------
    # --------------- BUCLE DEL JUEGO ------------------
    # --------------------------------------------------

    # Bucle que mantiene el juego corriendo hasta que se cierre
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False

        # Variable para detectar las teclas que se presionan
        teclas = pygame.key.get_pressed()
        # Variable que guarda la ultima posicion del personaje
        old_hitbox = hitbox.copy()

        #------------Movimiento del personaje--------------
        if teclas[pygame.K_LEFT]:
           hitbox.x -= velocidad        
        if teclas[pygame.K_RIGHT]:
           hitbox.x += velocidad
        if teclas[pygame.K_UP]:
           hitbox.y -= velocidad
        if teclas[pygame.K_DOWN]:
           hitbox.y += velocidad

        # Sonido al caminar
        if teclas[pygame.K_LEFT] or teclas[pygame.K_RIGHT] or teclas[pygame.K_UP] or teclas[pygame.K_DOWN]:
           if not pygame.mixer.get_busy():
              sonido_caminar.play()

        #----------------Colisiones--------------------
        # For que detecta las colisiones
        for rect in colisiones:
            if hitbox.colliderect(rect):
               hitbox.x = old_hitbox.x 
               hitbox.y = old_hitbox.y                           
               break

        # Hitbox centrado con el personaje
        personaje_draw_rect.center = hitbox.center 

        # Detectar pulsaciones nuevas (edge detection)
        pressed_e = teclas[pygame.K_e] and not prev_keys[pygame.K_e]
        pressed_q = teclas[pygame.K_q] and not prev_keys[pygame.K_q]   

        #-------------Recoger y tirar basura--------------
        # Recoger basura (presionar tecla E)
        if pressed_e:
           for obj in basura[:]:
               if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                  if objeto_en_mano is None:
                        objeto_en_mano = obj
                        basura.remove(obj)
                        mensaje = f"Recogiste: {obj['nombre']}"
                        sonido_recoger.play()
                  else:
                       mensaje = "Ya tienes un objeto en la mano"
                       mensaje_tiempo = pygame.time.get_ticks()
                       break
    
        # Tirar basura (presionar tecla Q)
        if pressed_q:
           if objeto_en_mano is None:
              mensaje = "No tienes ningún objeto en la mano"
              mensaje_tiempo = pygame.time.get_ticks()
           else:
                proximity = hitbox.inflate(24, 24)
                tiro_valido = False

            #-----------Basura en los botes------------

            # For para tirar la basura estando un bote cerca
                for bote in botes:
                    # Si se tira correctamente    
                    if proximity.colliderect(bote["rect"]):
                       tiro_valido = True
                       if objeto_en_mano["tipo"] == bote["tipo"]:
                          mensaje = f"Tiraste {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                          objeto_en_mano = None
                          sonido_tirar_correcto.play()
        
                    # Error al tirarla
                       else:
                          errores += 1
                          mensaje = f"No puedes tirar {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                          animando_dano = True
                          frame_actual_dano = 0
                          tiempo_frame_dano = pygame.time.get_ticks()
                          objeto_en_mano = None
                          sonido_tirar_incorrecto.play()
        
                          # Cambio en la barra de vida
                          vida_actual -= 1
                          if vida_actual < 0:
                             vida_actual = 0
                          elif vida_actual == 2:
                               vida_actual = 2
                          elif vida_actual == 1:
                               vida_actual = 1
        
                       mensaje_tiempo = pygame.time.get_ticks()
                       break

                # Si se tira y no hay un bote cerca              
                if not tiro_valido: 
                    mensaje = "No hay un bote cerca"
                    mensaje_tiempo = pygame.time.get_ticks()


        #-------------------------------------------------------
        #--------------- DIBUJAR EN LA PANTALLA ----------------
        #-------------------------------------------------------

        #------------Fondo de nivel 1------------
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        #-------------Barra de vida--------------    
        if vida_actual == 3:
           screen.blit(barra_vida, (20, -20))
        elif vida_actual == 2:
             screen.blit(barra_vida2, (20, -20))
        elif vida_actual == 1:
             screen.blit(barra_vida1, (20, -20))         

        #------Dibujar la basura en el mapa------
        for obj in basura:
            screen.blit(obj["imagen"], obj["rect"].topleft)

        #-----------Dibujar personaje------------
        screen.blit(personaje, personaje_draw_rect)

        #-------Dibujar basura en la mano--------
        if objeto_en_mano is not None:
           mano_x = personaje_draw_rect.centerx + 20
           mano_y = personaje_draw_rect.centery 
           screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))


        #----------Dibujar capas encima-----------
        screen.blit(capa_delante, (938, 424))
        screen.blit(capa_delante_2, (816, 423))
        screen.blit(capa_delante_3, (698, 333))

        # ----------------Mensaje----------------
        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
           mensaje_rect = pygame.Rect(12, 12, 500, 36)
           pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
           texto = fuente.render(mensaje, True, (255, 255, 255))
           screen.blit(texto, (20, 20))
        else:
            mensaje = ""
    
        #-----------Animación de daño------------
        if animando_dano:
            ahora = pygame.time.get_ticks()
            if ahora - tiempo_frame_dano >= duracion_frame:
               frame_actual_dano += 1
               tiempo_frame_dano = ahora
               if frame_actual_dano >= len(frames_dano):
                   animando_dano = False
                   frame_actual_dano = 0
            if animando_dano:
               frame = frames_dano[frame_actual_dano]
               frame_rect = frame.get_rect(center = personaje_draw_rect.center)
               screen.blit(frame, frame_rect.topleft)  

        #-----------------Tiempo------------------
        tiempo_actual = pygame.time.get_ticks()
        segundos = (tiempo_actual - inicio_tiempo)  // 1000
        tiempo_restante = max(0, tiempo - segundos)

        # Musica si queda poco tiempo
        if tiempo_restante <= 20 and not musica_cambiada:
            pygame.mixer.music.load("assets_PI/musica/musica_apresurada.ogg")  # tu nuevo archivo
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        # Variable 
        color_tiempo = (255,0,0) if tiempo_restante <= 20 else (255,255,255)

        pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
        texto_tiempo = fuente_tiempo.render(f" {tiempo_restante}", True, color_tiempo)
        screen.blit(texto_tiempo, (20, 90))

        #-----------Pantallas de ganar y perder--------------
        # Funcion pantalla ganar
        def mostrar_pantalla_victoria():
            pygame.mixer.music.load("assets_PI/musica/musica_victoria.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

            while True:
                screen.fill((0, 0, 0))
                screen.blit(win, (0, 0))

                # Variable para detectar cuando pasa el mouse
                mouse_pos = pygame.mouse.get_pos()

                #-------Botonoes pantalla ganar-------
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_win_intentar, rect_reintentar_victoria)
                else:
                    screen.blit( boton_win_intentar_hover, rect_reintentar_victoria)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_win_menu, rect_menu_victoria)
                else:
                    screen.blit(boton_win_menu_hover, rect_menu_victoria)

                #--------Actualizar pantalla---------
                pygame.display.flip()

                # For para quitar el juego o presionar un boton
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            run_level1()
                        elif rect_menu.collidepoint(mouse_pos):
                            return 

        # Funcion pantalla perder
        def mostrar_pantalla_perdida():
            pygame.mixer.music.load("assets_PI/sonidos/musica de perdida.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

            while True:
                  screen.fill((0, 0, 0))
                  screen.blit(pantalla_perdida, (0, 0))

                  # Variable para detectar cuando pasa el mouse  
                  mouse_pos = pygame.mouse.get_pos()

                  #-------Botonoes pantalla perder-------
                  if rect_reintentar.collidepoint(mouse_pos):
                      screen.blit(boton_reintentar_hover, rect_reintentar)
                  else: 
                      screen.blit(boton_reintentar, rect_reintentar)

                  if rect_menu.collidepoint(mouse_pos):
                      screen.blit(boton_menu_hover, rect_menu)
                  else:
                      screen.blit(boton_menu, rect_menu)

                  #--------Actualizar pantalla---------  
                  pygame.display.flip()

                  # For para quitar el juego o presionar un boton
                  for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                           run_level1()
                        elif rect_menu.collidepoint(mouse_pos):
                             return 
                         
        # Ganar
        if ganar(basura, objeto_en_mano):
           mostrar_pantalla_victoria()

        #--------------------------------------------------------
        #--------------------Animaciones-------------------------
        #--------------------------------------------------------

        #Animacion de muerte y pantalla de perdida
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
               screen.blit(background, (0, 0))
               screen.blit(frames_muerte[frame_actual_muerte], personaje_draw_rect.topleft)
               pygame.display.flip()
               clock.tick(60)

           elif tiempo_fin_animacion:
               ahora = pygame.time.get_ticks()
               if ahora - tiempo_fin_animacion >= 1500:
                   mostrar_pantalla_perdida()
               else:
                   screen.fill((0, 0, 0))
                   screen.blit(background, (0, 0))
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
                screen.blit(background, (0, 0))
                screen.blit(frames_muerte[frame_actual_muerte], personaje_draw_rect.topleft)
                pygame.display.flip()
                clock.tick(60)
            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    mostrar_pantalla_perdida()
                else:
                    screen.fill((0, 0, 0))
                    screen.blit(background, (0, 0))
                    screen.blit(frames_muerte[-1], personaje_draw_rect.topleft)
                    pygame.display.flip()
                    clock.tick(60)

        pygame.display.flip()
        clock.tick(60) 

        # Actualizar las teclas presionadas
        prev_keys = teclas

    pygame.quit()
             
if __name__ == "__main__":
    run_level1()