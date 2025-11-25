import pygame
import sys
import random
import os
from ffpyplayer.player import MediaPlayer 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ========== SISTEMA DE VIDEO INICIAL ==========
def mostrar_video_inicial(volumen, idioma="es"):
    """Muestra el video al inicio según el idioma y espera a que el usuario haga clic para continuar"""
    pygame.init()
    try:
        pygame.mixer.init()
    except:
        print("⚠ No se pudo iniciar el audio (pero el juego continuará).")

    screen = pygame.display.set_mode((1024, 768))
    clock = pygame.time.Clock()

    # Determinar el video según el idioma
    if idioma == "en":
        video_path = "assets_PI/tutorial/video_tutorial_ingles.mp4"
        texto_boton = "GO TO LEVEL"
    else:  # español por defecto
        video_path = "assets_PI/tutorial/video_tutorial.mp4"
        texto_boton = "IR AL NIVEL"

    # Cargar el video del tutorial según idioma
    player = MediaPlayer(video_path)
    print(f"🔍 Cargando video tutorial en {idioma.upper()}...") 

    # SPRITE DEL BOTÓN SIGUIENTE
    try:
        sprite_boton_siguiente = pygame.image.load("assets_PI/tutorial/siguiente.png").convert_alpha()
        sprite_boton_siguiente_hover = pygame.image.load("assets_PI/tutorial/siguiente_hover.png").convert_alpha()
        
        escala_boton = 3.0
        ancho_original = sprite_boton_siguiente.get_width()
        alto_original = sprite_boton_siguiente.get_height()
        nuevo_ancho = int(ancho_original * escala_boton)
        nuevo_alto = int(alto_original * escala_boton)
        
        sprite_boton_siguiente = pygame.transform.scale(sprite_boton_siguiente, (nuevo_ancho, nuevo_alto))
        sprite_boton_siguiente_hover = pygame.transform.scale(sprite_boton_siguiente_hover, (nuevo_ancho, nuevo_alto))
        
        boton_rect = sprite_boton_siguiente.get_rect()
        boton_rect.bottomright = (1000, 730)
        
        tiene_sprite = True
        print("Sprite del botón cargado correctamente")
        
    except Exception as e:
        print(f"⚠ No se pudo cargar el sprite del botón: {e}")
        boton_rect = pygame.Rect(800, 700, 180, 50)
        tiene_sprite = False
        sprite_boton_siguiente = None
        sprite_boton_siguiente_hover = None

    # Para animar fade out global
    fade_out = False
    fade_opacity = 0

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
                    fade_out = True

            # Salto con ESC/ESPACIO
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_ESCAPE, pygame.K_SPACE]:
                    fade_out = True

        # ---------------- VIDEO SIMPLIFICADO --------------------
        frame, val = player.get_frame()
        
        if frame is not None:
            img, timestamp = frame
            w, h = img.get_size()
            last_frame_surface = pygame.image.frombuffer(img.to_bytearray()[0], (w, h), "RGB")
        
        if val == 'eof':
            frame = None

        # Dibujar el frame (siempre que haya uno)
        if last_frame_surface is not None:
            screen.blit(pygame.transform.scale(last_frame_surface, screen.get_size()), (0, 0))
        else:
            screen.fill((0, 0, 0))

        # ---------------- BOTÓN CON SPRITE --------------------
        mouse_pos = pygame.mouse.get_pos()
        hovering = boton_rect.collidepoint(mouse_pos)
        
        if tiene_sprite:
            if hovering:
                escala_hover = 1.05
                ancho_hover = int(sprite_boton_siguiente.get_width() * escala_hover)
                alto_hover = int(sprite_boton_siguiente.get_height() * escala_hover)
                sprite_hover = pygame.transform.scale(sprite_boton_siguiente_hover, (ancho_hover, alto_hover))
                rect_hover = sprite_hover.get_rect(center=boton_rect.center)
                screen.blit(sprite_hover, rect_hover)
            else:
                screen.blit(sprite_boton_siguiente, boton_rect)
                
            if hovering:
                font = pygame.font.Font(None, 40)
                texto = font.render(texto_boton, True, (255, 255, 255))
                texto_rect = texto.get_rect(midbottom=(boton_rect.centerx, boton_rect.top - 10))
                screen.blit(texto, texto_rect)

        # --------------- FADE OUT -------------------
        if fade_out:
            fade_opacity += 8
            fade_layer = pygame.Surface(screen.get_size())
            fade_layer.set_alpha(fade_opacity)
            fade_layer.fill((0, 0, 0))
            screen.blit(fade_layer, (0, 0))

            if fade_opacity >= 255:
                player.close_player()
                return "continuar"

        pygame.display.flip()
        clock.tick(30)  # Reducir FPS para mejor sync

    player.close_player()
    return "continuar"
# ========== FIN SISTEMA DE VIDEO INICIAL ==========

# ========== SISTEMA DE PAUSA ==========
class SistemaPausa:
    def __init__(self, pantalla, idioma="es"):
        self.pantalla = pantalla
        self.juego_pausado = False
        self.musica_pausada = False
        self.return_value = None
        self.idioma = idioma
        
        
        # Botón de pausa en esquina superior derecha
        self.boton_pausa_rect = pygame.Rect(910, 20, 160, 160)
        self.boton_reanudar_rect = pygame.Rect(0, 0, 120, 120)
        self.boton_reiniciar_rect = pygame.Rect(0, 0, 120, 120)
        self.boton_menu_rect = pygame.Rect(0, 0, 120, 120)
        
        # Estados hover
        self.boton_pausa_hover = False
        self.boton_reanudar_hover = False
        self.boton_reiniciar_hover = False
        self.boton_menu_hover = False
        
        try:
            self.sprite_boton_pausa = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "minipausa.png")).convert_alpha()
            self.sprite_boton_pausa_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "minipausa_hover.png")).convert_alpha()
            
            # Escalar botón de pausa pequeño
            escala = 3.0
            nuevo_ancho = int(self.sprite_boton_pausa.get_width() * escala)
            nuevo_alto = int(self.sprite_boton_pausa.get_height() * escala)
            self.sprite_boton_pausa = pygame.transform.scale(self.sprite_boton_pausa, (nuevo_ancho, nuevo_alto))
            self.sprite_boton_pausa_hover = pygame.transform.scale(self.sprite_boton_pausa_hover, (nuevo_ancho, nuevo_alto))
            
            # Cargar otros sprites
            self.sprite_boton_reanudar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "volver.png")).convert_alpha()
            self.sprite_boton_reanudar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "volver_hover.png")).convert_alpha()
            self.sprite_boton_reiniciar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "reinicio.png")).convert_alpha()
            self.sprite_boton_reiniciar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "reinicio_hover.png")).convert_alpha()
            self.sprite_boton_menu = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "almenu.png")).convert_alpha()
            self.sprite_boton_menu_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "almenu_hover.png")).convert_alpha()
            self.sprite_fondo_pausa = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "pausa", "interfaz_de_pausa.png")).convert_alpha()

            # Escalar botones del menú de pausa
            escala_menu = 4.0
            botones_menu = ['reanudar', 'reiniciar', 'menu']
            for sprite_name in botones_menu:
                sprite_normal = getattr(self, f'sprite_boton_{sprite_name}')
                sprite_hover = getattr(self, f'sprite_boton_{sprite_name}_hover')

                if sprite_normal and sprite_hover:
                    nuevo_ancho = int(sprite_normal.get_width() * escala_menu)
                    nuevo_alto = int(sprite_normal.get_height() * escala_menu)
                    setattr(self, f'sprite_boton_{sprite_name}', pygame.transform.scale(sprite_normal, (nuevo_ancho, nuevo_alto)))
                    setattr(self, f'sprite_boton_{sprite_name}_hover', pygame.transform.scale(sprite_hover, (nuevo_ancho, nuevo_alto)))

        except: 
            self.sprite_boton_pausa = None
            self.sprite_boton_pausa_hover = None
            self.sprite_boton_reanudar = None
            self.sprite_boton_reanudar_hover = None
            self.sprite_boton_reiniciar = None
            self.sprite_boton_reiniciar_hover = None
            self.sprite_boton_menu = None
            self.sprite_boton_menu_hover = None
            self.sprite_fondo_pausa = None

    def manejar_eventos(self, event, nivel_instance):
        mouse_pos = pygame.mouse.get_pos()
        self.boton_pausa_hover = self.boton_pausa_rect.collidepoint(mouse_pos)
        
        if self.juego_pausado:
            ancho_pantalla, alto_pantalla = self.pantalla.get_size()
            ancho_pausa = 800
            alto_pausa = 400
            x_pausa = (ancho_pantalla - ancho_pausa) // 2 +50
            y_pausa = (alto_pantalla - alto_pausa) // 2 +50

            boton_ancho = 180
            boton_alto = 180
            espacio_entre_botones = 30
            total_ancho_botones = (boton_ancho * 3) + (espacio_entre_botones * 2)
            inicio_x = x_pausa + (ancho_pausa - total_ancho_botones) // 2
            pos_y = y_pausa + (alto_pausa - boton_alto) // 2

            self.boton_reanudar_rect = pygame.Rect(inicio_x, pos_y, boton_ancho, boton_alto)
            self.boton_reiniciar_rect = pygame.Rect(inicio_x + boton_ancho + espacio_entre_botones, pos_y, boton_ancho, boton_alto)
            self.boton_menu_rect = pygame.Rect(inicio_x + (boton_ancho + espacio_entre_botones) * 2, pos_y, boton_ancho, boton_alto)
            
            self.boton_reanudar_hover = self.boton_reanudar_rect.collidepoint(mouse_pos)
            self.boton_reiniciar_hover = self.boton_reiniciar_rect.collidepoint(mouse_pos)
            self.boton_menu_hover = self.boton_menu_rect.collidepoint(mouse_pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.juego_pausado:
                    self.reanudar()
                else:
                    self.pausar()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
            if self.juego_pausado:
                if self.boton_reanudar_rect.collidepoint(pos):
                    self.reanudar()
                elif self.boton_reiniciar_rect.collidepoint(pos):
                    self.reiniciar_nivel(nivel_instance)
                elif self.boton_menu_rect.collidepoint(pos):
                    self.ir_al_menu(nivel_instance)
            else:
                if self.boton_pausa_rect.collidepoint(pos):
                    self.pausar()

    def pausar(self):
        self.juego_pausado = True
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.musica_pausada = True

    def reanudar(self):
        self.juego_pausado = False
        if self.musica_pausada:
            pygame.mixer.music.unpause()
            self.musica_pausada = False

    def reiniciar_nivel(self, nivel_instance):
        self.juego_pausado = False
        self.return_value = "tutorial"

    def ir_al_menu(self, nivel_instance):
        self.juego_pausado = False
        self.return_value = "main"

    def dibujar(self):
        if not self.juego_pausado:
            if self.sprite_boton_pausa:
                if self.boton_pausa_hover and self.sprite_boton_pausa_hover:
                    self.pantalla.blit(self.sprite_boton_pausa_hover, self.boton_pausa_rect)
                else:
                    self.pantalla.blit(self.sprite_boton_pausa, self.boton_pausa_rect)
        else:
            ancho_pantalla, alto_pantalla = self.pantalla.get_size()
            ancho_pausa = 800
            alto_pausa = 400
            x_pausa = (ancho_pantalla - ancho_pausa) // 2
            y_pausa = (alto_pantalla - alto_pausa) // 2

            fondo_pausa = pygame.Surface((ancho_pausa, alto_pausa), pygame.SRCALPHA)
            fondo_pausa.fill((0, 0, 0, 200))
            self.pantalla.blit(fondo_pausa, (x_pausa, y_pausa))
            pygame.draw.rect(self.pantalla, (255, 255, 255), (x_pausa, y_pausa, ancho_pausa, alto_pausa), 3)
            
            if self.sprite_fondo_pausa:
                fondo_escalado = pygame.transform.scale(self.sprite_fondo_pausa, (ancho_pausa, alto_pausa))
                self.pantalla.blit(fondo_escalado, (x_pausa, y_pausa))
            
            # Dibujar botones con textos
            if self.sprite_boton_reanudar:
                if self.boton_reanudar_hover and self.sprite_boton_reanudar_hover:
                    self.pantalla.blit(self.sprite_boton_reanudar_hover, self.boton_reanudar_rect)
                else:
                    self.pantalla.blit(self.sprite_boton_reanudar, self.boton_reanudar_rect)
            
            if self.sprite_boton_reiniciar:
                if self.boton_reiniciar_hover and self.sprite_boton_reiniciar_hover:
                    self.pantalla.blit(self.sprite_boton_reiniciar_hover, self.boton_reiniciar_rect)
                else:
                    self.pantalla.blit(self.sprite_boton_reiniciar, self.boton_reiniciar_rect)
            
            if self.sprite_boton_menu:
                if self.boton_menu_hover and self.sprite_boton_menu_hover:
                    self.pantalla.blit(self.sprite_boton_menu_hover, self.boton_menu_rect)
                else:
                    self.pantalla.blit(self.sprite_boton_menu, self.boton_menu_rect)
            
            # Dibujar textos de los botones
            font = pygame.font.Font(None, 36)
            
            
# ========== FIN SISTEMA DE PAUSA ==========

def run_tutorial(idioma="es", volumen=0.5):
    # -----------------------------
    # MOSTRAR VIDEO INICIAL
    # -----------------------------
    resultado_video = mostrar_video_inicial(volumen, idioma)
    if resultado_video == "salir":
        pygame.quit()
        return "salir"
    
    # -----------------------------
    # INICIALIZACIÓN DEL JUEGO
    # -----------------------------
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Tutorial")

    sistema_pausa = SistemaPausa(screen, idioma)

    # -----------------------------
    # CARGA DE IMÁGENES
    # -----------------------------
    fondo = pygame.transform.scale(pygame.image.load("assets_PI/tutorial/semituto.png").convert_alpha(), (1024, 768))
    
    # Pantalla de victoria y barras de vida
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")

    # Posturas estáticas para quieto
    quieto_derecha = pygame.image.load("assets_PI/personajes/femenino/posturas/personaje_PI_femenino_derecha.png").convert_alpha()
    quieto_izquierda = pygame.image.load("assets_PI/personajes/femenino/posturas/personaje_PI_femenino_izquierda.png").convert_alpha()
    quieto_detras = pygame.image.load("assets_PI/personajes/femenino/posturas/personaje_PI_femenino_detras.png").convert_alpha()
    quieto_delante = pygame.image.load("assets_PI/personajes/femenino/posturas/personaje_PI_femenino_delante.png").convert_alpha()

    # Escalar imágenes
    win = pygame.transform.scale(w, (1024, 768))
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))
    cronometro = pygame.image.load("assets_PI/sprites/Cronometro_PI.png").convert_alpha()

    # Botes
    organico = pygame.image.load("assets_PI/botes/bote organico.png").convert_alpha()
    inorganico = pygame.image.load("assets_PI/botes/bote inorganico.png").convert_alpha()
    peligroso = pygame.image.load("assets_PI/botes/bote peligro (1).png").convert_alpha()

    # Cargar botones
    boton_menu = pygame.image.load("assets_PI/interfaces/perdida/boton_menu.png").convert_alpha()
    boton_menu_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_menu_hover.png").convert_alpha()

    boton_win_menu_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_hover_pantalla_victoria.png")
    boton_win_menu = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_pantalla_victoria.png")
    boton_win = pygame.transform.scale(boton_win_menu, (650, 200))
    boton_win_hover = pygame.transform.scale(boton_win_menu_hover, (650, 200))

    rect_menu_victoria = boton_win_menu.get_rect(center=(515, 570))

    rect_menu = boton_menu.get_rect(center=(515, 550))

    # Personaje inicial
    personaje = quieto_delante
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 70, 70)
    hitbox.center = personaje_draw_rect.center
    
    # ESCALAR PERSONAJE
    escala_personaje = 2.0

    def escalar_frames(lista_frames, escala):
        return [pygame.transform.scale(frame, 
                                      (int(frame.get_width() * escala), 
                                       int(frame.get_height() * escala))) 
                for frame in lista_frames]

    # Escalar posturas estáticas del personaje
    quieto_derecha = pygame.transform.scale(quieto_derecha, 
                                           (int(quieto_derecha.get_width() * escala_personaje), 
                                            int(quieto_derecha.get_height() * escala_personaje)))
    quieto_izquierda = pygame.transform.scale(quieto_izquierda, 
                                             (int(quieto_izquierda.get_width() * escala_personaje), 
                                              int(quieto_izquierda.get_height() * escala_personaje)))
    quieto_detras = pygame.transform.scale(quieto_detras, 
                                          (int(quieto_detras.get_width() * escala_personaje), 
                                           int(quieto_detras.get_height() * escala_personaje)))
    quieto_delante = pygame.transform.scale(quieto_delante, 
                                           (int(quieto_delante.get_width() * escala_personaje), 
                                            int(quieto_delante.get_height() * escala_personaje)))

    # Actualizar personaje y hitbox después de escalar
    personaje = quieto_delante
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 70 * escala_personaje, 70 * escala_personaje)
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
    # BASURA CON ANIMACIONES
    # -----------------------------
    
    # Cargar frames de animación para cada basura
    frames_periodico = [
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande4.png").convert_alpha()
    ]
    
    frames_manzana = [
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene4.png").convert_alpha()
    ]
    
    frames_foco = [
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a975.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a976.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a977.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a978.png").convert_alpha()
    ]
    
    # ESCALAR BOTES
    escala_botes = 2.0
    organico_escalado = pygame.transform.scale(organico, 
                                            (int(organico.get_width() * escala_botes), 
                                             int(organico.get_height() * escala_botes)))
    inorganico_escalado = pygame.transform.scale(inorganico, 
                                              (int(inorganico.get_width() * escala_botes), 
                                               int(inorganico.get_height() * escala_botes)))
    peligroso_escalado = pygame.transform.scale(peligroso, 
                                             (int(peligroso.get_width() * escala_botes), 
                                              int(peligroso.get_height() * escala_botes)))

    # BOTES CON COLISIONES MEJORADAS
    botes = [
        {
            "imagen": inorganico_escalado, 
            "nombre": "Inorganico", 
            "tipo": "inorganica", 
            "rect": inorganico_escalado.get_rect(topleft=(800, 150)),
            "colision": inorganico_escalado.get_rect(topleft=(800, 150)).inflate(-60, -80)  # Colisión más ajustada
        },
        {
            "imagen": organico_escalado, 
            "nombre": "Organico", 
            "tipo": "organica", 
            "rect": organico_escalado.get_rect(topleft=(150, 550)),
            "colision": organico_escalado.get_rect(topleft=(150, 550)).inflate(-60, -80)
        },
        {
            "imagen": peligroso_escalado, 
            "nombre": "Residuos peligrosos", 
            "tipo": "peligrosa", 
            "rect": peligroso_escalado.get_rect(topleft=(700, 550)),
            "colision": peligroso_escalado.get_rect(topleft=(700, 550)).inflate(-60, -80)
        }
    ]

    # Escalar basuras
    escala_basura = 2.0
    frames_periodico = [pygame.transform.scale(frame, 
                                            (int(frame.get_width() * escala_basura), 
                                             int(frame.get_height() * escala_basura))) 
                    for frame in frames_periodico]
    frames_manzana = [pygame.transform.scale(frame, 
                                          (int(frame.get_width() * escala_basura), 
                                           int(frame.get_height() * escala_basura))) 
                    for frame in frames_manzana]
    frames_foco = [pygame.transform.scale(frame, 
                                       (int(frame.get_width() * escala_basura), 
                                        int(frame.get_height() * escala_basura))) 
                for frame in frames_foco]

    # BASURAS EN POSICIONES ALEATORIAS SIN SUPERPOSICIÓN
    def generar_posicion_aleatoria(posiciones_existentes):
        while True:
            x = random.randint(150, 850)
            y = random.randint(150, 600)
            
            # Verificar que no se superponga con otras basuras
            superposicion = False
            for pos in posiciones_existentes:
                distancia = ((x - pos[0]) ** 2 + (y - pos[1]) ** 2) ** 0.5
                if distancia < 100:
                    superposicion = True
                    break
            
            # Verificar que no esté dentro de ningún bote
            nueva_pos_rect = pygame.Rect(x, y, 50, 50)  # Área de la basura
            for bote in botes:
                # Usar la hitbox del bote (que vamos a reducir)
                if bote["colision"].colliderect(nueva_pos_rect):
                    superposicion = True
                    break
            
            if not superposicion:
                return (x, y)

    posiciones_basura = []
    basura = []
    
    # Crear cada basura con posición única
    tipos_basura = [
        {"frames": frames_periodico, "nombre": "Periodico", "tipo": "inorganica"},
        {"frames": frames_manzana, "nombre": "Manzana", "tipo": "organica"},
        {"frames": frames_foco, "nombre": "Foco", "tipo": "peligrosa"}
    ]
    
    for tipo in tipos_basura:
        pos = generar_posicion_aleatoria(posiciones_basura)
        posiciones_basura.append(pos)
        
        basura.append({
            "frames": tipo["frames"],
            "rect": tipo["frames"][0].get_rect(topleft=pos),
            "nombre": tipo["nombre"],
            "tipo": tipo["tipo"],
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        })

    # SISTEMA DE COLISIONES MEJORADO
    colisiones = [
        pygame.Rect(0, 0, 1024, 1),     # Borde superior
        pygame.Rect(0, 767, 1024, 305), # Borde inferior  
        pygame.Rect(0, 0, 1, 768),      # Borde izquierdo
        pygame.Rect(1023, 0, 1, 768),   # Borde derecho
    ]

    # Añadir colisiones de botes al sistema de colisiones
    colisiones_botes = [bote["colision"] for bote in botes]
    todas_colisiones = colisiones + colisiones_botes

    # -----------------------------
    # ANIMACIONES DEL PERSONAJE
    # -----------------------------
    frames_dano = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_recibir_daño_derecha/Pi_personaje_m_animacion_recibir_daño_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_recibir_daño_derecha/Pi_personaje_m_animacion_recibir_daño_derecha2.png").convert_alpha()
    ]

    frames_muerte_derecha = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_derecha/Pi_personaje_m_animacion_muerte_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_derecha/Pi_personaje_m_animacion_muerte_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_derecha/Pi_personaje_m_animacion_muerte_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_derecha/Pi_personaje_m_animacion_muerte_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_derecha/Pi_personaje_m_animacion_muerte_derecha5.png").convert_alpha()
    ]

    frames_muerte_izquierda = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_izquierda/Pi_personaje_m_animacion_muerte_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_izquierda/Pi_personaje_m_animacion_muerte_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_izquierda/Pi_personaje_m_animacion_muerte_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_izquierda/Pi_personaje_m_animacion_muerte_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_muerte_izquierda/Pi_personaje_m_animacion_muerte_izquierda5.png").convert_alpha()
    ]

    frames_muerte_delante = frames_muerte_derecha
    frames_muerte_detras = frames_muerte_derecha

    frames_caminar_delante = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_delante/Pi_personaje_m_animacion_caminar_delante6.png").convert_alpha()
    ]

    frames_caminar_derecha = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_derecha/Pi_personaje_m_animacion_caminar_derecha6.png").convert_alpha()
    ]

    frames_caminar_detras = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_detras/Pi_personaje_m_animacion_caminar_detras6.png").convert_alpha(),
    ]

    frames_caminar_izquierda = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_caminar_izquierda/Pi_personaje_m_animacion_caminar_izquierda6.png").convert_alpha()
    ]

    # ANIMACIONES DE QUIETO
    frames_quieto_detras = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_detras/Pi_personaje_m_animacion_quieto_detras9.png").convert_alpha()
    ]

    frames_quieto_derecha = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_derecha/Pi_personaje_m_animacion_quieto_derecha9.png").convert_alpha()
    ]

    frames_quieto_izquierda = [
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/femenino/animaciones/Pi_personaje_m_animacion_quieto_izquierda/Pi_personaje_m_animacion_quieto_izquierda9.png").convert_alpha()
    ]   

    frames_quieto_delante = [quieto_delante]

    # ESCALAR TODAS LAS ANIMACIONES DEL PERSONAJE
    frames_dano = escalar_frames(frames_dano, escala_personaje)
    frames_muerte_derecha = escalar_frames(frames_muerte_derecha, escala_personaje)
    frames_muerte_izquierda = escalar_frames(frames_muerte_izquierda, escala_personaje)
    frames_muerte_delante = escalar_frames(frames_muerte_delante, escala_personaje)
    frames_muerte_detras = escalar_frames(frames_muerte_detras, escala_personaje)
    frames_caminar_delante = escalar_frames(frames_caminar_delante, escala_personaje)
    frames_caminar_derecha = escalar_frames(frames_caminar_derecha, escala_personaje)
    frames_caminar_detras = escalar_frames(frames_caminar_detras, escala_personaje)
    frames_caminar_izquierda = escalar_frames(frames_caminar_izquierda, escala_personaje)
    frames_quieto_detras = escalar_frames(frames_quieto_detras, escala_personaje)
    frames_quieto_derecha = escalar_frames(frames_quieto_derecha, escala_personaje)
    frames_quieto_izquierda = escalar_frames(frames_quieto_izquierda, escala_personaje)
    frames_quieto_delante = escalar_frames(frames_quieto_delante, escala_personaje)

    pantalla_perdida = pygame.image.load("assets_PI/interfaces/perdida/game over 2.0.png").convert_alpha()

    # Banderas para activar animaciones
    animando_dano = False
    animando_muerte = False
    animacion_correr_izquierda = False
    animacion_correr_derecha = False
    animacion_correr_detras = False
    animacion_correr_delante = False
    animando_quieto = False
    tiempo_fin_animacion = None

    # Banderas para señalar el frame inicial de las animaciones
    frame_actual_dano = 0
    frame_actual_muerte = 0
    frame_actual_correr_izquierda = 0
    frame_actual_correr_derecha = 0
    frame_actual_correr_delante = 0
    frame_actual_correr_detras = 0
    frame_actual_quieto_derecha = 0
    frame_actual_quieto_izquierda = 0
    frame_actual_quieto_detras = 0
    frame_actual_quieto_delante = 0

    # Establecer la duracion de cada frame
    tiempo_frame = 0
    duracion_frame = 100
    duracion_frame_movimiento = 80
    duracion_frame_quieto = 200

    # -----------------------------
    # VARIABLES
    # -----------------------------
    
    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 3000
    fuente = pygame.font.Font(None, 32)
    
    # velocidad del juego y personaje
    velocidad = 5
    clock = pygame.time.Clock()
    
    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo - SISTEMA MEJORADO CON PAUSA
    tiempo_total = 200
    inicio_tiempo = pygame.time.get_ticks()
    tiempo_pausa_acumulado = 0
    tiempo_ultima_pausa = 0
    tiempo_visual = tiempo_total 
    fuente_tiempo = pygame.font.SysFont("dejavusansmono", 35)

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
    
    # Sprite que aparece sobre el personaje
    sprite_sobre_cabeza = pygame.image.load("assets_PI/tutorial/tecla_enter.png").convert_alpha()
    sprite_sobre_cabeza = pygame.transform.scale(sprite_sobre_cabeza, (110, 110))
    sprite_visible = False

    # -----------------------------
    # FUNCIONES PARA PANTALLAS DE FINAL
    # -----------------------------
    def mostrar_pantalla_perdida():
        pygame.mixer.music.load("assets_PI/sonidos/musica de perdida.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        sonido_morir.play()

        # Definir el rectángulo del botón con tamaño aumentado
        ancho_boton = 600  # Aumentar el ancho
        alto_boton = 200   # Aumentar el alto
        # COORDENADAS PARA CENTRAR EL BOTÓN:
        x_pos = (screen.get_width() - ancho_boton) // 2  # Centrado horizontal
        y_pos = (screen.get_height() - alto_boton) // 2  # Centrado vertical
        
        rect_menu_victoria = pygame.Rect(x_pos, y_pos, ancho_boton, alto_boton)


        while True:
            screen.fill((0, 0, 0))
            screen.blit(pantalla_perdida, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            # Botones
            if rect_menu.collidepoint(mouse_pos):
                screen.blit(boton_win_hover, rect_menu)
            else:
                screen.blit(boton_menu, rect_menu)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_menu.collidepoint(mouse_pos):
                        pygame.mixer.music.stop()
                        return "main"

    def mostrar_pantalla_victoria():
        pygame.mixer.music.load("assets_PI/musica/musica_victoria.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # Definir el rectángulo del botón con tamaño aumentado
        ancho_boton = 600  # Aumentar el ancho
        alto_boton = 200   # Aumentar el alto
        # COORDENADAS PARA CENTRAR EL BOTÓN:
        x_pos = (screen.get_width() - ancho_boton) // 2  # Centrado horizontal
        y_pos = (screen.get_height() - alto_boton) // 2  # Centrado vertical
        
        rect_menu_victoria = pygame.Rect(x_pos, y_pos, ancho_boton, alto_boton)

        while True:
            screen.fill((0, 0, 0))
            screen.blit(win, (0, 0))

            mouse_pos = pygame.mouse.get_pos()
            if rect_menu_victoria.collidepoint(mouse_pos):
                screen.blit(boton_win_hover, rect_menu_victoria)
            else:
                screen.blit(boton_win, rect_menu_victoria)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if rect_menu_victoria.collidepoint(mouse_pos):
                        pygame.mixer.music.stop()
                        return "main"  

    # -----------------------------
    # BUCLE PRINCIPAL
    # -----------------------------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            sistema_pausa.manejar_eventos(event, None)
            
        if sistema_pausa.return_value is not None:
            return sistema_pausa.return_value
            
        if sistema_pausa.juego_pausado:
            screen.fill((0, 0, 0))
            screen.blit(fondo, (0, 0))
            screen.blit(cronometro, (15, 60))
            
            if vida_actual == 3:
                screen.blit(barra_vida, (20, -20))
            elif vida_actual == 2:
                screen.blit(barra_vida2, (20, -20))
            elif vida_actual == 1:
                screen.blit(barra_vida1, (20, -20))
                
            for obj in basura:
                frame_actual = obj["frames"][obj["frame_actual"]]
                screen.blit(frame_actual, obj["rect"])
                
            for bote in botes:
                screen.blit(bote["imagen"], bote["rect"])
                
            screen.blit(frame, personaje_draw_rect)
            
            if objeto_en_mano is not None and not animando_muerte:
                mano_x = personaje_draw_rect.centerx + 20
                mano_y = personaje_draw_rect.centery 
                screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))
            
            minutos = tiempo_visual // 60
            segundos_restantes = tiempo_visual % 60
            tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"
            color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)
            texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
            screen.blit(texto_tiempo, (17, 85))
            
            sistema_pausa.dibujar()
            
            pygame.display.flip()
            clock.tick(60)
            continue

        # ========== CÓDIGO NORMAL (cuando NO está pausado) ==========
        tiempo_actual = pygame.time.get_ticks()
        if sistema_pausa.juego_pausado:
            if tiempo_ultima_pausa == 0:
                tiempo_ultima_pausa = tiempo_actual
        else:
            if tiempo_ultima_pausa > 0:
                tiempo_pausa_acumulado += tiempo_actual - tiempo_ultima_pausa
                tiempo_ultima_pausa = 0
        tiempo_transcurrido = (tiempo_actual - inicio_tiempo - tiempo_pausa_acumulado) // 1000
        tiempo_restante = max(0, tiempo_total - tiempo_transcurrido)
        
        if not sistema_pausa.juego_pausado:
            tiempo_visual = tiempo_restante

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

        # MOVIMIENTO CON COLISIONES MEJORADAS
        if not animando_muerte and not tiempo_fin_animacion:
            moving = False
            if not animando_dano:
                if keys[pygame.K_LEFT]:
                    hitbox.x -= velocidad
                    animacion_correr_izquierda = True
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "izquierda"
                    frame_actual_quieto_izquierda = 0
                elif keys[pygame.K_RIGHT]:
                    hitbox.x += velocidad
                    animacion_correr_derecha = True
                    animacion_correr_izquierda = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "derecha"
                    frame_actual_quieto_derecha = 0
                elif keys[pygame.K_UP]:
                    hitbox.y -= velocidad
                    animacion_correr_detras = True
                    animacion_correr_delante = False
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    moving = True
                    ultima_direccion = "detras"
                    frame_actual_quieto_detras = 0
                elif keys[pygame.K_DOWN]:
                    hitbox.y += velocidad
                    animacion_correr_delante = True
                    animacion_correr_detras = False
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    moving = True
                    ultima_direccion = "delante"
                    frame_actual_quieto_delante = 0
                else:
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    animando_quieto = True

            if moving:
                if not pygame.mixer.get_busy():
                    sonido_caminar.play()

            # VERIFICAR COLISIONES CON BOTES Y BORDES
            for rect in todas_colisiones:
                if hitbox.colliderect(rect):
                    hitbox.x = old_hitbox.x
                    hitbox.y = old_hitbox.y
                    break

        personaje_draw_rect.center = hitbox.center
        
        # VERIFICAR INTERACCIÓN CON BASURA Y BOTES
        basura_cerca = False
        bote_cerca = False
        
        if objeto_en_mano is None:
            # Verificar basura para recoger
            for obj in basura:
                distancia = ((hitbox.centerx - obj["rect"].centerx) ** 2 + 
                            (hitbox.centery - obj["rect"].centery) ** 2) ** 0.5
                if distancia < 100:
                    basura_cerca = True
                    break
        else:
            # Verificar botes para tirar - USANDO HITBOX DE COLISIÓN
            for bote in botes:
                distancia = ((hitbox.centerx - bote["colision"].centerx) ** 2 + 
                            (hitbox.centery - bote["colision"].centery) ** 2) ** 0.5
                if distancia < 100:
                    bote_cerca = True
                    break

        sprite_visible = basura_cerca or bote_cerca

        pressed_enter = keys[pygame.K_RETURN] and not prev_keys[pygame.K_RETURN]

        # Recoger objetos
        if pressed_enter and objeto_en_mano is None:
            for obj in basura[:]:
                if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                    sonido_recoger.play()
                    obj["animando"] = False
                    objeto_en_mano = {
                        "imagen": obj["frames"][0],
                        "nombre": obj["nombre"],
                        "tipo": obj["tipo"]
                    }
                    basura.remove(obj)
                    sprite_visible = False
                    # Mensaje traducido según idioma
                    if idioma == "en":
                        mensaje = f"You picked up: {obj['nombre']}"
                    else:
                        mensaje = f"Recogiste: {obj['nombre']}"
                    break
            else:
                if not any(hitbox.inflate(12, 12).colliderect(obj["rect"]) for obj in basura):
                    if idioma == "en":
                        mensaje = "No objects to pick up nearby"
                    else:
                        mensaje = "No hay objetos para recoger cerca"
                    mensaje_tiempo = pygame.time.get_ticks()

        # Tirar basura
        elif pressed_enter and objeto_en_mano is not None:
            proximity = hitbox.inflate(24, 24)
            tiro_valido = False
            bote_correcto_encontrado = False
            bote_actual = None
            bote_mas_cercano = None
            distancia_minima = float('inf')

            for bote in botes:
                if proximity.colliderect(bote["colision"]):
                    distancia = ((hitbox.centerx - bote["rect"].centerx) ** 2 + 
                               (hitbox.centery - bote["rect"].centery) ** 2) ** 0.5
                    
                    if distancia < distancia_minima:
                        distancia_minima = distancia
                        bote_mas_cercano = bote

            if bote_mas_cercano:
                bote_actual = bote_mas_cercano
                tiro_valido = True

                if objeto_en_mano["tipo"] == bote_actual["tipo"]:
                    bote_correcto_encontrado = True
                    # Mensaje traducido según idioma
                    if idioma == "en":
                        mensaje = f"✓ You threw {objeto_en_mano['nombre']} in {bote_actual['nombre']} bin"
                    else:
                        mensaje = f"✓ Tiraste {objeto_en_mano['nombre']} en bote {bote_actual['nombre']}"
                    objeto_en_mano = None
                    sonido_tirar_correcto.play()
                else:
                    errores += 1
                    # Mensaje traducido según idioma
                    if idioma == "en":
                        mensaje = f"✗ You can't throw {objeto_en_mano['nombre']} in {bote_actual['nombre']} bin"
                    else:
                        mensaje = f"✗ No puedes tirar {objeto_en_mano['nombre']} en bote {bote_actual['nombre']}"
                    animando_dano = True
                    frame_actual_dano = 0
                    tiempo_frame = pygame.time.get_ticks()
                    sonido_tirar_incorrecto.play()
                    
                    vida_actual -= 1
                    if vida_actual < 0:
                        vida_actual = 0

                mensaje_tiempo = pygame.time.get_ticks()
            else:
                if idioma == "en":
                    mensaje = "No bin nearby"
                else:
                    mensaje = "No hay un bote cerca"
                mensaje_tiempo = pygame.time.get_ticks()
                sprite_visible = False

        # ACTUALIZAR ANIMACIONES DE BASURA
        tiempo_actual = pygame.time.get_ticks()
        
        for obj in basura:
            if obj["animando"]:
                tiempo_transcurrido = tiempo_actual - obj["tiempo_ultimo_frame"]
                
                if obj["frame_actual"] == 0:
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 1
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 1:
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 2
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 2:
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 3
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 3:
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 0
                        obj["tiempo_ultimo_frame"] = tiempo_actual

        # -----------------------------
        # DIBUJAR
        # -----------------------------
        screen.fill((0, 0, 0))
        screen.blit(fondo, (0, 0))
        screen.blit(cronometro, (15, 60))

        if vida_actual == 3:
            screen.blit(barra_vida, (20, -20))
        elif vida_actual == 2:
            screen.blit(barra_vida2, (20, -20))
        elif vida_actual == 1:
            screen.blit(barra_vida1, (20, -20))

        for obj in basura:
            frame_actual = obj["frames"][obj["frame_actual"]]
            screen.blit(frame_actual, obj["rect"])

        for bote in botes:
            screen.blit(bote["imagen"], bote["rect"])

        # Actualizar animación del personaje
        ahora = pygame.time.get_ticks()
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
                
                if ultima_direccion == "derecha":
                    frame = frames_quieto_derecha[frame_actual_quieto_derecha]
                elif ultima_direccion == "izquierda":
                    frame = frames_quieto_izquierda[frame_actual_quieto_izquierda]
                elif ultima_direccion == "detras":
                    frame = frames_quieto_detras[frame_actual_quieto_detras]
                elif ultima_direccion == "delante":
                    frame = frames_quieto_derecha[frame_actual_quieto_derecha]
                else:
                    frame = quieto_delante

            else:
                posturas_quieto = {
                    "derecha": quieto_derecha,
                    "izquierda": quieto_izquierda,
                    "detras": quieto_detras,
                    "delante": quieto_delante
                }
                frame = posturas_quieto.get(ultima_direccion, quieto_delante)
        else:
            posturas_quieto = {
                "derecha": quieto_derecha,
                "izquierda": quieto_izquierda,
                "detras": quieto_detras,
                "delante": quieto_delante
            }
            frame = posturas_quieto.get(ultima_direccion, quieto_delante)

        personaje_draw_rect = frame.get_rect(center=hitbox.center)
        
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
            
            frame_dano = frames_dano[frame_actual_dano]
            rect_dano = frame_dano.get_rect(center=hitbox.center)
            screen.blit(frame_dano, rect_dano)
        else:
            screen.blit(frame, personaje_draw_rect)

        if sprite_visible:
            sprite_x = hitbox.centerx - sprite_sobre_cabeza.get_width() // 2
            sprite_y = hitbox.top - sprite_sobre_cabeza.get_height() - 10
            screen.blit(sprite_sobre_cabeza, (sprite_x, sprite_y))

        if objeto_en_mano is not None and not animando_muerte:
            mano_x = personaje_draw_rect.centerx + 20
            mano_y = personaje_draw_rect.centery 
            screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))

        if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
            texto_surface = fuente.render(mensaje, True, (255, 255, 255))
            texto_ancho = texto_surface.get_width()
            mensaje_ancho = min(texto_ancho + 20, 700)
            mensaje_rect = pygame.Rect(512 - mensaje_ancho // 2, 12, mensaje_ancho, 36)
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            pygame.draw.rect(screen, (255, 255, 255), mensaje_rect, 2)
            screen.blit(texto_surface, (mensaje_rect.x + 10, mensaje_rect.y + 5))
        else:
            mensaje = ""

        tiempo_actual = pygame.time.get_ticks()
        segundos = (tiempo_actual - inicio_tiempo) // 1000
        tiempo_restante = max(0, tiempo_total - segundos)

        if tiempo_restante <= 30 and not musica_cambiada:
            pygame.mixer.music.load("assets_PI/musica/musica_apresurada.ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        color_tiempo = (255, 0, 0) if tiempo_restante <= 30 else (255, 255, 255)
        minutos = tiempo_restante // 60
        segundos_restantes = tiempo_restante % 60
        tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"
        texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
        cronometro = pygame.transform.scale(cronometro, (150, 90))
        screen.blit(texto_tiempo, (17, 85))
        
        sistema_pausa.dibujar()

        if ganar(basura, objeto_en_mano):
            resultado = mostrar_pantalla_victoria()
            pygame.mixer.music.stop()
            return resultado

        if errores >= 3:
            if not animando_muerte and not tiempo_fin_animacion:
                animando_muerte = True
                frame_actual_muerte = 0
                tiempo_frame_muerte = pygame.time.get_ticks()
                tiempo_fin_animacion = None
                sonido_morir.play()
                sonido_caminar.stop()

            if animando_muerte:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_frame_muerte >= duracion_frame:
                    frame_actual_muerte += 1
                    tiempo_frame_muerte = ahora

                    if frame_actual_muerte >= 5:
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = 4

                if ultima_direccion == "izquierda":
                    frames_muerte = frames_muerte_izquierda
                else:
                    frames_muerte = frames_muerte_derecha

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
                    pygame.mixer.music.stop()
                    return resultado
        
                else:
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
        
        if tiempo_restante <= 0 and not muerte_por_tiempo:
            muerte_por_tiempo = True
            errores = 3

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys
        
    if hasattr(sistema_pausa, 'return_value') and sistema_pausa.return_value:
        return sistema_pausa.return_value
    return None    

# Solo para pruebas independientes
if __name__ == "__main__":
    run_tutorial()