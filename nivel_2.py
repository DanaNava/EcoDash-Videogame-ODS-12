import pygame
import sys


def run_level1():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 2")

    # -----------------------------
    # CARGA DE IMÁGENES
    # -----------------------------
    fondo = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondo_nivel2.png").convert_alpha()
    capa_delante_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondo1_level2.png").convert_alpha()
   
    # Pantalla de vistoria y barras de vida
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")

    # Posturas estáticas para quieto (como respaldo)
    quieto_derecha = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_derecha.png").convert_alpha()
    quieto_izquierda = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_izquierda.png").convert_alpha()
    quieto_detras = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_detras.png").convert_alpha()
    quieto_delante = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_delante.png").convert_alpha()

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

    # Personaje inicial
    personaje = quieto_delante
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 70, 70)
    hitbox.center = personaje_draw_rect.center

    # -----------------------------
    # CARGA musica de fondo
    # -----------------------------
    pygame.mixer.music.load("assets_PI/musica/musica_nivel.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

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
    sonido_dano.set_volume(0.5)
    sonido_morir.set_volume(1)
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
        {"imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600)), "nombre": "Batería", "tipo": "peligrosa"},
    ]

    botes = [
        {"nombre": "Inorganico", "tipo": "inorganica", "rect": pygame.Rect(386, 403, 53, 28)},
        {"nombre": "Organico", "tipo": "organica", "rect": pygame.Rect(215, 400, 54, 24)},
        {"nombre": "Residuos peligrosos", "tipo": "peligrosa", "rect": pygame.Rect(346, 687, 52, 29)}
    ]

    colisiones = [
        #izquierda
        pygame.Rect(0, 1, 10, 241), pygame.Rect(6, 250, 11, 102), pygame.Rect(0, 373, 14, 71), pygame.Rect(0, 446, 168, 33), 
        pygame.Rect(0, 498, 4, 268),
        #abajo
        pygame.Rect(0, 762, 595, 6), pygame.Rect(609, 657, 22, 84), pygame.Rect(609, 760, 419, 6),
        #derecho
        pygame.Rect(1028, 460, 1, 308), pygame.Rect(1010, 418, 13, 23), pygame.Rect(1023, 0, 1, 407),
        #conjunto de bancas
        pygame.Rect(996, 77, 17, 40), pygame.Rect(897, 41, 75, 14), pygame.Rect(839, 72, 33, 71),
        #rejas
        pygame.Rect(837, 250, 11, 118), pygame.Rect(598, 376, 237, 4), pygame.Rect(208, 1, 630, 3), pygame.Rect(209, 30, 10, 332), 
        pygame.Rect(248, 385, 202, 7),
        #bancas no puestas 
        pygame.Rect(187, 234, 10, 87), pygame.Rect(615, 438, 11, 52), 
        #mesa para comer?
        pygame.Rect(702, 494, 18, 83), pygame.Rect(737, 529, 86, 10), pygame.Rect(850, 495, 12, 93), pygame.Rect(758, 456, 50, 25),
        #arboles y arbustos
        pygame.Rect(22, 83, 107, 60), pygame.Rect(88, 640, 45, 49)
    ]

    # -----------------------------
    # ANIMACIONES
    # -----------------------------
    frames_dano = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha2.png").convert_alpha()
    ]

    # ANIMACIONES DE MUERTE POR DIRECCIÓN
    frames_muerte_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte5.png").convert_alpha()
    ]

    frames_muerte_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda5.png").convert_alpha()
    ]

    # Para delante y detrás, usar las mismas que derecha
    frames_muerte_delante = frames_muerte_derecha
    frames_muerte_detras = frames_muerte_derecha

    frames_caminar_delante = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante6.png").convert_alpha()
    ]

    frames_caminar_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha6.png").convert_alpha()
    ]

    frames_caminar_detras = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras6.png").convert_alpha()
    ]

    frames_caminar_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda6.png").convert_alpha()
    ]

    # ANIMACIONES DE QUIETO
    frames_quieto_detras = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras9.png").convert_alpha()
    ]

    frames_quieto_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha9.png").convert_alpha()
    ]

    frames_quieto_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda9.png").convert_alpha()
    ]

    # Para delante postura estática
    frames_quieto_delante = [quieto_delante]

    pantalla_perdida = pygame.image.load("assets_PI/interfaces/perdida/game over 2.0.png").convert_alpha()

    # Banderas para activar animaciones
    animando_dano = False
    animando_muerte = False
    animacion_correr_izquierda = False
    animacion_correr_derecha = False
    animacion_correr_detras = False
    animacion_correr_delante = False

    # Bandera para animaciones de quieto
    animando_quieto = False

    # Bandera de tiempo de animaciones
    tiempo_fin_animacion = None

    # Banderas para señalar el frame inicial de las animaciones
    frame_actual_dano = 0
    frame_actual_muerte = 0
    frame_actual_correr_izquierda = 0
    frame_actual_correr_derecha = 0
    frame_actual_correr_delante = 0
    frame_actual_correr_detras = 0
    
    # Nuevos frames para animaciones de quieto
    frame_actual_quieto_derecha = 0
    frame_actual_quieto_izquierda = 0
    frame_actual_quieto_detras = 0
    frame_actual_quieto_delante = 0

    # Establecer la duracion de cada frame
    tiempo_frame = 0
    duracion_frame = 100
    duracion_frame_movimiento = 80
    duracion_frame_quieto = 200  # Más lento para animaciones de quieto

    # -----------------------------
    # VARIABLES
    # -----------------------------
    
    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 3000  # Aumentar a 3 segundos
    fuente = pygame.font.Font(None, 32)  # Fuente más pequeña
    
    # velocidad del juego y personaje
    velocidad = 5
    clock = pygame.time.Clock()
    
    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo
    tiempo = 60
    inicio_tiempo = pygame.time.get_ticks()
    fuente_tiempo = pygame.font.Font(None, 48)

    # Variable indicadora para cambiar la musica
    musica_cambiada = False

    # Verificar si gano
    def ganar(basura, objeto_en_mano):
        return len(basura) == 0 and objeto_en_mano is None

    # Variable para el while infinito, para las teclas pulsadas y un contador de errores
    running = True
    prev_keys = pygame.key.get_pressed()
    errores = 0

    # Variable para la última dirección
    ultima_direccion = "delante"

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

       # CORRECCIÓN: Bloquear completamente el movimiento durante la muerte
        if not animando_muerte and not tiempo_fin_animacion:
            moving = False
            # Movimiento
            if not animando_dano:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    hitbox.x -= velocidad
                    animacion_correr_izquierda = True
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "izquierda"
                    # Reiniciar frame de quieto cuando empieza a moverse
                    frame_actual_quieto_izquierda = 0
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    hitbox.x += velocidad
                    animacion_correr_derecha = True
                    animacion_correr_izquierda = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "derecha"
                    frame_actual_quieto_derecha = 0
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    hitbox.y -= velocidad
                    animacion_correr_detras = True
                    animacion_correr_delante = False
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    moving = True
                    ultima_direccion = "detras"
                    frame_actual_quieto_detras = 0
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    hitbox.y += velocidad
                    animacion_correr_delante = True
                    animacion_correr_detras = False
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    moving = True
                    ultima_direccion = "delante"
                    frame_actual_quieto_delante = 0
                else:
                    # Si no hay movimiento, apagar animaciones de correr
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    # Activar animación de quieto
                    animando_quieto = True

            # Al caminar
            if moving:
                if not pygame.mixer.get_busy():
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

            # Tirar basura - VERSIÓN CORREGIDA
            if pressed_p or pressed_x:
                if objeto_en_mano is None:
                    mensaje = "No tienes ningún objeto en la mano"
                    mensaje_tiempo = pygame.time.get_ticks()
                else:
                    proximity = hitbox.inflate(24, 24)
                    tiro_valido = False
                    bote_correcto_encontrado = False
                    bote_actual = None

                    # PRIMERO: Encontrar qué bote está cerca
                    for bote in botes:
                        if proximity.colliderect(bote["rect"]):
                            tiro_valido = True
                            bote_actual = bote  # Guardar referencia al bote cercano
                            break  # Solo nos interesa el bote más cercano

                    # SEGUNDO: Procesar el tiro solo si hay un bote cercano
                    if tiro_valido and bote_actual:
                        # Verificar si es el bote CORRECTO para este objeto
                        if objeto_en_mano["tipo"] == bote_actual["tipo"]:
                            # Tiro CORRECTO
                            bote_correcto_encontrado = True
                            mensaje = f"✓ Tiraste {objeto_en_mano['nombre']} en bote {bote_actual['nombre']}"
                            objeto_en_mano = None
                            sonido_tirar_correcto.play()
                        else:
                            # Tiro INCORRECTO - NO tirar pero recibir daño
                            errores += 1
                            mensaje = f"✗ No puedes tirar {objeto_en_mano['nombre']} en bote {bote_actual['nombre']}"
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            # IMPORTANTE: NO liberar el objeto - el jugador lo mantiene en la mano
                            sonido_tirar_incorrecto.play()
                
                            # BARRA DE VIDA
                            vida_actual -= 1
                            if vida_actual < 0:
                                vida_actual = 0

                        mensaje_tiempo = pygame.time.get_ticks()
                    else:
                        # No hay bote cercano
                        mensaje = "No hay un bote cerca"
                        mensaje_tiempo = pygame.time.get_ticks()

        # -----------------------------
        # DIBUJAR
        # -----------------------------
        screen.fill((0, 0, 0))
        screen.blit(fondo, (0, 0))

        # BARRA DE VIDA
        if vida_actual == 3:
            screen.blit(barra_vida, (20, -20))
        elif vida_actual == 2:
            screen.blit(barra_vida2, (20, -20))
        elif vida_actual == 1:
            screen.blit(barra_vida1, (20, -20))

        for obj in basura:
            screen.blit(obj["imagen"], obj["rect"])

        # Actualizar animación
        ahora = pygame.time.get_ticks()
       
        # --- Animaciones de movimiento ---
        if not animando_dano and not animando_muerte:
            if animacion_correr_izquierda:
                if ahora - tiempo_frame >= duracion_frame_movimiento:
                    frame_actual_correr_izquierda = (frame_actual_correr_izquierda + 1) % len(frames_caminar_izquierda)
                    tiempo_frame = ahora
                frame = frames_caminar_izquierda[frame_actual_correr_izquierda]

            elif animacion_correr_derecha:
                if ahora - tiempo_frame >= duracion_frame_movimiento:
                    frame_actual_correr_derecha = (frame_actual_correr_derecha + 1) % len(frames_caminar_derecha)
                    tiempo_frame = ahora
                frame = frames_caminar_derecha[frame_actual_correr_derecha]

            elif animacion_correr_delante:
                if ahora - tiempo_frame >= duracion_frame_movimiento:
                    frame_actual_correr_delante = (frame_actual_correr_delante + 1) % len(frames_caminar_delante)
                    tiempo_frame = ahora
                frame = frames_caminar_delante[frame_actual_correr_delante]

            elif animacion_correr_detras:
                if ahora - tiempo_frame >= duracion_frame_movimiento:
                    frame_actual_correr_detras = (frame_actual_correr_detras + 1) % len(frames_caminar_detras)
                    tiempo_frame = ahora
                frame = frames_caminar_detras[frame_actual_correr_detras]

            # --- Animaciones de quieto ---
            elif animando_quieto:
                if ahora - tiempo_frame >= duracion_frame_quieto:
                    if ultima_direccion == "derecha":
                        frame_actual_quieto_derecha = (frame_actual_quieto_derecha + 1) % len(frames_quieto_derecha)
                    elif ultima_direccion == "izquierda":
                        frame_actual_quieto_izquierda = (frame_actual_quieto_izquierda + 1) % len(frames_quieto_izquierda)
                    elif ultima_direccion == "detras":
                        frame_actual_quieto_detras = (frame_actual_quieto_detras + 1) % len(frames_quieto_detras)
                    elif ultima_direccion == "delante":
                        frame_actual_quieto_derecha = (frame_actual_quieto_derecha + 1) % len(frames_quieto_derecha)
                    tiempo_frame = ahora
                
                # Seleccionar frame de quieto según la última dirección
                if ultima_direccion == "derecha":
                    frame = frames_quieto_derecha[frame_actual_quieto_derecha]
                elif ultima_direccion == "izquierda":
                    frame = frames_quieto_izquierda[frame_actual_quieto_izquierda]
                elif ultima_direccion == "detras":
                    frame = frames_quieto_detras[frame_actual_quieto_detras]
                elif ultima_direccion == "delante":
                    frame = frames_quieto_derecha[frame_actual_quieto_derecha]
                else:
                    frame = quieto_delante  # Por defecto

            else:
                # Postura estática por defecto (como respaldo)
                posturas_quieto = {
                    "derecha": quieto_derecha,
                    "izquierda": quieto_izquierda,
                    "detras": quieto_detras,
                    "delante": quieto_delante
                }
                frame = posturas_quieto.get(ultima_direccion, quieto_delante)
        else:
            # Durante daño o muerte, usar la última postura conocida
            posturas_quieto = {
                "derecha": quieto_derecha,
                "izquierda": quieto_izquierda,
                "detras": quieto_detras,
                "delante": quieto_delante
            }
            frame = posturas_quieto.get(ultima_direccion, quieto_delante)

        # --- DIBUJAR PERSONAJE ---
        personaje_draw_rect = frame.get_rect(center=hitbox.center)
        
        # Dibujar animación de daño en la posición correcta
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
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
            
            # Dibujar frame de daño centrado correctamente
            frame_dano = frames_dano[frame_actual_dano]
            rect_dano = frame_dano.get_rect(center=hitbox.center)
            screen.blit(frame_dano, rect_dano)
        else:
            # Dibujar personaje normal
            screen.blit(frame, personaje_draw_rect)

        # DIBUJAR OBJETO EN LA MANO
        if objeto_en_mano is not None and not animando_muerte:
            mano_x = personaje_draw_rect.centerx + 20
            mano_y = personaje_draw_rect.centery 
            screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))


        screen.blit(capa_delante_2, (31, 576))

   
        # Mensaje
        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
            # Calcular el ancho del texto
            texto_surface = fuente.render(mensaje, True, (255, 255, 255))
            texto_ancho = texto_surface.get_width()
    
            # Crear rectángulo dinámico basado en el ancho del texto
            mensaje_ancho = min(texto_ancho + 20, 700)  # Máximo 700 píxeles
            mensaje_rect = pygame.Rect(512 - mensaje_ancho // 2, 12, mensaje_ancho, 36)
    
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            pygame.draw.rect(screen, (255, 255, 255), mensaje_rect, 2)  # Borde blanco
            screen.blit(texto_surface, (mensaje_rect.x + 10, mensaje_rect.y + 5))
        else:
            mensaje = ""

        # [Nuevo] TIEMPO
        tiempo_actual = pygame.time.get_ticks()
        segundos = (tiempo_actual - inicio_tiempo) // 1000
        tiempo_restante = max(0, tiempo - segundos)

        if tiempo_restante <= 30 and not musica_cambiada:
            pygame.mixer.music.load("assets_PI/musica/musica_apresurada.ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        color_tiempo = (255, 0, 0) if tiempo_restante <= 30 else (255, 255, 255)

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
            sonido_morir.play()

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
                            pygame.mixer.music.stop()
                            return "reintentar"  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main"  # volver al menú

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
                            pygame.mixer.music.stop()
                            return "reintentar"  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main" # volver al menú
            
        #ganar
        if ganar(basura, objeto_en_mano):
            resultado = mostrar_pantalla_victoria()
            if resultado == "main":
                return "main"  # Volver al menú principal
            elif resultado == "reintentar":
                return "reintentar" # Reiniciar nivel
                

         
        # -----------------------------
        # ANIMACIÓN DE MUERTE CORREGIDA
        # -----------------------------
        if errores >= 3:
            if not animando_muerte and not tiempo_fin_animacion:
                animando_muerte = True
                frame_actual_muerte = 0
                tiempo_frame_muerte = pygame.time.get_ticks()
                tiempo_fin_animacion = None
                sonido_morir.play()
                # CORRECCIÓN: Detener sonido de caminar y otros sonidos
                sonido_caminar.stop()

            if animando_muerte:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_frame_muerte >= duracion_frame:
                    frame_actual_muerte += 1
                    tiempo_frame_muerte = ahora

                    if frame_actual_muerte >= 5:  # 5 frames de animación de muerte
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = 4  # Último frame

                # CORRECCIÓN: Seleccionar animación de muerte según la dirección
                if ultima_direccion == "izquierda":
                    frames_muerte = frames_muerte_izquierda
                else:
                    frames_muerte = frames_muerte_derecha  # Para derecha, delante y detrás

                screen.fill((0, 0, 0))
                screen.blit(fondo, (0, 0))
                frame_muerte = frames_muerte[frame_actual_muerte]
                rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                screen.blit(frame_muerte, rect_muerte)
                pygame.display.flip()
                clock.tick(60)

            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    resultado = mostrar_pantalla_perdida()
                    if resultado == "main":
                        return "main"  # Volver al menú principal
                    elif resultado == "reintentar":
                        return "reintentar"  # Reiniciar nivel
        
                else:
                    # CORRECCIÓN: Mantener la última animación de muerte según dirección
                    if ultima_direccion == "izquierda":
                        frames_muerte = frames_muerte_izquierda
                    else:
                        frames_muerte = frames_muerte_derecha

                    screen.fill((0, 0, 0))
                    screen.blit(fondo, (0, 0))
                    frame_muerte = frames_muerte[-1]
                    rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                    screen.blit(frame_muerte, rect_muerte)
                    pygame.display.flip()
                    clock.tick(60)
        
        muerte_por_tiempo = False
        # Perder si se acaba el tiempo
        if tiempo_restante <= 0 and not muerte_por_tiempo:
            muerte_por_tiempo = True
            errores = 3

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys
        
    pygame.quit()

if __name__ == "__main__":
    run_level1()