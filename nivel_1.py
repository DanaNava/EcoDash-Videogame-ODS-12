import pygame
import sys
import os 
import random 

# Ruta base para encontrar los assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ========== SISTEMA DE PAUSA ==========
class SistemaPausa:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.juego_pausado = False
        self.musica_pausada = False
        self.return_value = None
        
        # Botón de pausa en esquina superior derecha
        self.boton_pausa_rect = pygame.Rect(910, 20, 60, 60)
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

            # Escalar botones del menú de pausa x2.0
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
        # Actualizar estados hover
        self.boton_pausa_hover = self.boton_pausa_rect.collidepoint(mouse_pos)
        
        # Calcular posiciones de botones del menú de pausa
        if self.juego_pausado:
            ancho_pantalla, alto_pantalla = self.pantalla.get_size()
            ancho_pausa = 800
            alto_pausa = 400
            x_pausa = (ancho_pantalla - ancho_pausa) // 2 +50
            y_pausa = (alto_pantalla - alto_pausa) // 2 +50

            # Botones en línea horizontal
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
        nivel_instance.return_value = "reintentar"
        self.return_value = "reintentar"
        nivel_instance.running = False

    def ir_al_menu(self, nivel_instance):
        self.juego_pausado = False
        nivel_instance.return_value = "main"
        self.return_value = "main"
        nivel_instance.running = False

    def dibujar(self):
        if not self.juego_pausado:
            if self.sprite_boton_pausa:
                if self.boton_pausa_hover and self.sprite_boton_pausa_hover:
                    self.pantalla.blit(self.sprite_boton_pausa_hover, self.boton_pausa_rect)
                else:
                    self.pantalla.blit(self.sprite_boton_pausa, self.boton_pausa_rect)
        else:
            # Pantalla de pausa centrada EDITAR TAMANO
            ancho_pantalla, alto_pantalla = self.pantalla.get_size()
            ancho_pausa = 800
            alto_pausa = 400
            x_pausa = (ancho_pantalla - ancho_pausa) // 2
            y_pausa = (alto_pantalla - alto_pausa) // 2

            # Fondo semi-transparente centrado
            fondo_pausa = pygame.Surface((ancho_pausa, alto_pausa), pygame.SRCALPHA)
            fondo_pausa.fill((0, 0, 0, 200))
            self.pantalla.blit(fondo_pausa, (x_pausa, y_pausa))
            pygame.draw.rect(self.pantalla, (255, 255, 255), (x_pausa, y_pausa, ancho_pausa, alto_pausa), 3)
            
            # DIBUJAR INTERFAZ DE PAUSA - AGREGAR ESTA LÍNEA
            if self.sprite_fondo_pausa:
            # Escalar y centrar el sprite de fondo
                fondo_escalado = pygame.transform.scale(self.sprite_fondo_pausa, (ancho_pausa, alto_pausa))
                self.pantalla.blit(fondo_escalado, (x_pausa, y_pausa))
            
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
# ========== FIN SISTEMA DE PAUSA ==========

# --- MODIFICADO: Acepta idioma y volumen ---
def run_level1(idioma_actual, volumen_actual):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 1")

    # SISTEMA DE PAUSA - INICIALIZAR
    sistema_pausa = SistemaPausa(screen)

    # -----------------------------
    # CARGA DE IMÁGENES (CON RUTAS CORREGIDAS)
    # -----------------------------
    fondo = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_3.png")).convert_alpha()
    capa_delante = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_derecha.png")).convert_alpha()
    capa_delante_2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "puerta_izquierda_fondo.png")).convert_alpha()
    capa_delante_3 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_arriba.png")).convert_alpha()
    capa_delante_4 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_sillon_1.png")).convert_alpha()
    capa_delante_5 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_sillon_2.png")).convert_alpha()
    capa_delante_6 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_sillon_3.png")).convert_alpha()
    capa_delante_7 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_sillon_4.png")).convert_alpha()
    capa_delante_8 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_mesa_derecha_1.png")).convert_alpha()
    capa_delante_9 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_mesa_derecha_2.png")).convert_alpha()
    capa_delante_10 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_mesa_izquierda_1.png")).convert_alpha()
    capa_delante_11 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel1", "fondo_mesa_izquierda_2.png")).convert_alpha()
    
    # Pantalla de vistoria y barras de vida
    w = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "Pantalla_victoria.jpeg"))
    bv = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_completa.png"))
    bv2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_2co.png"))
    bv1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_1co.png"))

    # Posturas estáticas para quieto (como respaldo)
    quieto_derecha = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_derecha.png")).convert_alpha()
    quieto_izquierda = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_izquierda.png")).convert_alpha()
    quieto_detras = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_detras.png")).convert_alpha()
    quieto_delante = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_delante.png")).convert_alpha()

    #Escalar imagenes
    win = pygame.transform.scale(w, (1024, 768))
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))

    #Botes
    organico = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "botes", "bote organico.png")).convert_alpha()
    inorganico = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "botes", "bote inorganico.png")).convert_alpha()
    peligroso= pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "botes", "bote peligro (1).png")).convert_alpha()

    #Cargar botones (Asumimos que las imágenes ya no tienen texto)
    boton_reintentar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_intenta_otra_vez.png")).convert_alpha()
    boton_reintentar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_intenta_otra_vez_hover.png")).convert_alpha()
    boton_menu = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_menu.png")).convert_alpha()
    boton_menu_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_menu_hover.png")).convert_alpha()

    boton_win_menu_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_menu_hover_pantalla_victoria.png"))
    boton_win_menu = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_menu_pantalla_victoria.png"))
    boton_win_intentar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_intenta_otra_vez_victoria.png"))
    boton_win_intentar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_intenta_otra_vez_victoria_hover.png"))

    rect_reintentar_victoria = boton_win_intentar.get_rect(center=(515, 487)) 
    rect_menu_victoria = boton_win_menu.get_rect(center=(515, 570)) 

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
    pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "musica", "musica_nivel.wav"))
    pygame.mixer.music.set_volume(volumen_actual) 
    pygame.mixer.music.play(-1)

    # -----------------------------
    # CARGA efectos de sonido
    # -----------------------------
    sonido_caminar = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "pasos_madera.wav"))
    sonido_dano = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "recibir_daño.wav"))
    sonido_morir = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "morir.wav"))
    sonido_recoger = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "recoger_basura.wav"))
    sonido_tirar_correcto = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "tirar_basura_sonido_bien.wav"))
    sonido_tirar_incorrecto = pygame.mixer.Sound(os.path.join(BASE_DIR, "assets_PI", "sonidos", "tirar_basura_sonido_error.wav"))

    # Volúmenes (basados en el volumen global)
    sonido_caminar.set_volume(1 * volumen_actual)
    sonido_dano.set_volume(0.5 * volumen_actual)
    sonido_morir.set_volume(1 * volumen_actual)
    sonido_recoger.set_volume(0.4 * volumen_actual)
    sonido_tirar_correcto.set_volume(0.5 * volumen_actual)
    sonido_tirar_incorrecto.set_volume(1 * volumen_actual)

    # -----------------------------
    # BASURA CON ANIMACIONES Y TRADUCCIONES
    # -----------------------------
    # Cargar frames de animación para cada basura
    frames_botella_agua = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella_agua1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella_agua2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella_agua3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella_agua4.png")).convert_alpha()
    ]
    
    frames_lata = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "lata", "lata1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "lata", "lata2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "lata", "lata3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "lata", "lata4.png")).convert_alpha()
    ]
    
    frames_periodico = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "periodico", "periodico_mas_grande1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "periodico", "periodico_mas_grande2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "periodico", "periodico_mas_grande3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "periodico", "periodico_mas_grande4.png")).convert_alpha()
    ]
    
    frames_banana = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Banana", "banano1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Banana", "banano2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Banana", "banano3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Banana", "banano4.png")).convert_alpha()
    ]
    
    frames_cascara_huevo = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Cascara_huevo", "cascara_huevo_2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Cascara_huevo", "cascara_huevo_3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Cascara_huevo", "cascara_huevo_4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Cascara_huevo", "cascara_huevo_5.png")).convert_alpha()
    ]
    
    frames_manzana = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Manzana", "manzene1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Manzana", "manzene2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Manzana", "manzene3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "organica", "Manzana", "manzene4.png")).convert_alpha()
    ]
    
    frames_bateria = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Bateria", "batería item -9c3f1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Bateria", "batería item -9c3f2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Bateria", "batería item -9c3f3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Bateria", "batería item -9c3f4.png")).convert_alpha()
    ]
    
    frames_foco = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Foco", "Foquito item-a975.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Foco", "Foquito item-a976.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Foco", "Foquito item-a977.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Foco", "Foquito item-a978.png")).convert_alpha()
    ]
    
    frames_jeringa = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Jeringa", "Jeringa1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Jeringa", "Jeringa2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Jeringa", "Jeringa3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "residuos_peligrosos", "Jeringa", "Jeringa4.png")).convert_alpha()
    ]

    # POSICIONES ALEATORIAS PARA BASURAS
    posiciones_basura = [
        (200, 350), (620, 400), (420, 640), 
        (920, 280), (360, 250), (50, 600)
    ]

    def obtener_posiciones_aleatorias(cantidad):
        return random.sample(posiciones_basura, cantidad)

    posiciones_aleatorias = obtener_posiciones_aleatorias(6)

    basura = [
        {
            "frames": frames_banana, 
            "rect": frames_banana[0].get_rect(topleft=posiciones_aleatorias[0]), 
            "nombre": {"es": "Plátano", "en": "Banana"}, 
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_botella_agua, 
            "rect": frames_botella_agua[0].get_rect(topleft=posiciones_aleatorias[1]), 
            "nombre": {"es": "Botella de agua", "en": "Water Bottle"}, 
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_foco, 
            "rect": frames_foco[0].get_rect(topleft=posiciones_aleatorias[2]), 
            "nombre": {"es": "Foco", "en": "Light Bulb"}, 
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_lata, 
            "rect": frames_lata[0].get_rect(topleft=posiciones_aleatorias[3]), 
            "nombre": {"es": "Lata", "en": "Can"}, 
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_manzana, 
            "rect": frames_manzana[0].get_rect(topleft=posiciones_aleatorias[4]), 
            "nombre": {"es": "Manzana", "en": "Apple"}, 
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_bateria, 
            "rect": frames_bateria[0].get_rect(topleft=posiciones_aleatorias[5]), 
            "nombre": {"es": "Batería", "en": "Battery"}, 
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        }
    ]

    botes = [
        {"imagen": inorganico, "nombre": {"es": "Inorgánico", "en": "Inorganic"}, "tipo": "inorganica", "rect": pygame.Rect(284, 155, 20, 35)},
        {"imagen": organico, "nombre": {"es": "Orgánico", "en": "Organic"}, "tipo": "organica", "rect": pygame.Rect(341, 156, 20, 35)},
        {"imagen": peligroso, "nombre": {"es": "Peligrosos", "en": "Hazardous"}, "tipo": "peligrosa", "rect": pygame.Rect(793, 179, 20, 20)}
    ]

    colisiones = [
        pygame.Rect(9, 150, 30, 601), pygame.Rect(10, 725, 1005, 50), pygame.Rect(1003, 11, 10, 734),
        pygame.Rect(690, 17, 21, 450), pygame.Rect(261, 15, 9, 250), pygame.Rect(26, 146, 239, 140),
        pygame.Rect(719, 184, 66, 5), pygame.Rect(872, 82, 122, 85), pygame.Rect(693, 391, 135, 75),
        pygame.Rect(767, 500, 43, 1), pygame.Rect(959, 391, 40, 75), pygame.Rect(400, 58, 289, 73),
        pygame.Rect(421, 219, 70, 71), pygame.Rect(645, 210, 43, 60), pygame.Rect(950, 577, 20, 26),
        pygame.Rect(185, 519, 107, 20), pygame.Rect(176, 572, 120, 20), pygame.Rect(217, 451, 42, 60),
        pygame.Rect(127, 545, 35, 1), pygame.Rect(311, 544, 35, 1), pygame.Rect(215, 600, 42, 9),
        pygame.Rect(284, 155, 20, 35), pygame.Rect(341, 156, 20, 35), pygame.Rect(793, 179, 20, 20)
    ]

    # -----------------------------
    # ANIMACIONES DEL PERSONAJE (CON RUTAS CORREGIDAS)
    # -----------------------------
    frames_dano = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_daño_derecha", "Pi_personaje_m_daño_derecha1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_daño_derecha", "Pi_personaje_m_daño_derecha2.png")).convert_alpha()
    ]
    frames_muerte_derecha = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte5.png")).convert_alpha()
    ]
    frames_muerte_izquierda = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda5.png")).convert_alpha()
    ]
    frames_muerte_delante = frames_muerte_derecha
    frames_muerte_detras = frames_muerte_derecha
    frames_caminar_delante = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante6.png")).convert_alpha()
    ]
    frames_caminar_derecha = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha6.png")).convert_alpha()
    ]
    frames_caminar_detras = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras6.png")).convert_alpha()
    ]
    frames_caminar_izquierda = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda6.png")).convert_alpha()
    ]

    # ANIMACIONES DE QUIETO
    frames_quieto_detras = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras6.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras7.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras8.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras9.png")).convert_alpha()
    ]
    frames_quieto_derecha = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha6.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha7.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha8.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha9.png")).convert_alpha()
    ]
    frames_quieto_izquierda = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda4.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda5.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda6.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda7.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda8.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_izquierda", "Pi_personaje_animacion_quieto_izquierda9.png")).convert_alpha()
    ]

    # Para delante postura estática
    frames_quieto_delante = [quieto_delante]

    pantalla_perdida = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "game over 2.0.png")).convert_alpha()

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
    
    # velocidad del juego y personaje
    velocidad = 5
    clock = pygame.time.Clock()
    
    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo - SISTEMA MEJORADO CON PAUSA
    tiempo_total = 60
    inicio_tiempo = pygame.time.get_ticks()
    tiempo_pausa_acumulado = 0
    tiempo_ultima_pausa = 0
    tiempo_visual = tiempo_total 
    fuente_tiempo = pygame.font.Font(None, 48)

    # --- ¡¡¡MODIFICADO AQUÍ!!! ---
    # --- Cargar las DOS fuentes ---
    try:
        # Fuente para Títulos (Game Over / Victoria)
        font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf")
        fuente_subtitulo_gameover = pygame.font.Font(font_titulo_path, 32)
        fuente_victoria_titulo = pygame.font.Font(font_titulo_path, 48) 
        fuente_victoria_subtitulo = pygame.font.Font(font_titulo_path, 35)

        # Fuente para Texto Normal (Botones / Mensajes)
        font_texto_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Pixel.ttf")
        fuente_boton_gameover = pygame.font.Font(font_texto_path, 11) 
        fuente_victoria_botones = pygame.font.Font(font_texto_path, 21)
        fuente_mensajes = pygame.font.Font(font_texto_path, 15) # Para "Recogiste: Plátano"

    except FileNotFoundError:
        print("ERROR: No se encontraron las fuentes 'Stay Pixel DEMO.ttf' o 'Pixel.ttf'. Usando fuentes por defecto.")
        # Fallback a fuentes por defecto
        fuente_subtitulo_gameover = pygame.font.Font(None, 36)
        fuente_victoria_titulo = pygame.font.Font(None, 55)
        fuente_victoria_subtitulo = pygame.font.Font(None, 38)
        
        fuente_boton_gameover = pygame.font.Font(None, 32) 
        fuente_victoria_botones = pygame.font.Font(None, 24)
        fuente_mensajes = pygame.font.Font(None, 32)
    
    # Asignar la fuente de mensajes a la variable 'fuente' que usa el resto del código
    fuente = fuente_mensajes
    # --- FIN DE LA MODIFICACIÓN ---

    # Variable indicadora para cambiar la musica
    musica_cambiada = False

    # Verificar si gano
    def ganar(basura, objeto_en_mano):
        return len(basura) == 0 and objeto_en_mano is None

    # Variable para el while infinito, para las teclas pulsadas y un contador de errores
    running = True
    return_value = None
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
                return "salir" # <-- AÑADIDO: Salir correctamente si se cierra la ventana

            # MANEJAR EVENTOS DE PAUSA
            sistema_pausa.manejar_eventos(event, sys.modules[__name__])

        # Verificar si la pausa quiere salir del nivel
        if sistema_pausa.return_value is not None:
            return sistema_pausa.return_value

        # CALCULAR TIEMPO - SISTEMA MEJORADO CON PAUSA
        tiempo_actual = pygame.time.get_ticks()
        if sistema_pausa.juego_pausado:
            if tiempo_ultima_pausa == 0:
                tiempo_ultima_pausa = tiempo_actual
        else:
            # ACTUALIZAR tiempo_visual SOLO cuando NO está en pausa
            if tiempo_ultima_pausa > 0:
                tiempo_pausa_acumulado += tiempo_actual - tiempo_ultima_pausa
                tiempo_ultima_pausa = 0
        tiempo_transcurrido = (tiempo_actual - inicio_tiempo - tiempo_pausa_acumulado) // 1000
        tiempo_restante = max(0, tiempo_total - tiempo_transcurrido)
        
        if not sistema_pausa.juego_pausado:
            tiempo_visual = tiempo_restante

        # Si el juego está pausado, saltar el resto de la lógica
        if sistema_pausa.juego_pausado:
            # Dibujar todo el juego congelado
            screen.fill((0, 0, 0))
            screen.blit(fondo, (0, 0))

            # BARRA DE VIDA
            if vida_actual == 3:
                screen.blit(barra_vida, (20, -20))
            elif vida_actual == 2:
                screen.blit(barra_vida2, (20, -20))
            elif vida_actual == 1:
                screen.blit(barra_vida1, (20, -20))

            # DIBUJAR BASURAS CON ANIMACIONES
            for obj in basura:
                frame_actual = obj["frames"][obj["frame_actual"]]
                screen.blit(frame_actual, obj["rect"])

            # Dibujar personaje congelado
            if not animando_dano and not animando_muerte:
                posturas_quieto = {
                    "derecha": quieto_derecha,
                    "izquierda": quieto_izquierda,
                    "detras": quieto_detras,
                    "delante": quieto_delante
                }
                frame = posturas_quieto.get(ultima_direccion, quieto_delante)
                personaje_draw_rect = frame.get_rect(center=hitbox.center)
                screen.blit(frame, personaje_draw_rect)

            # DIBUJAR OBJETO EN LA MANO
            if objeto_en_mano is not None and not animando_muerte:
                mano_x = personaje_draw_rect.centerx + 20
                mano_y = personaje_draw_rect.centery 
                screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))

            # Capas del fondo
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

            #Tiempo congelado - usar tiempo_visual que ya está congelado
            minutos = tiempo_visual // 60
            segundos_restantes = tiempo_visual % 60
            tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"
            color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)
            pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
            texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
            screen.blit(texto_tiempo, (20, 90))

            # DIBUJAR SISTEMA DE PAUSA
            sistema_pausa.dibujar()

            pygame.display.flip()
            clock.tick(60)
            continue

        # SI EL JUEGO NO ESTÁ PAUSADO, EJECUTAR LÓGICA NORMAL
        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

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
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    animando_quieto = True

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
                            obj["animando"] = False
                            objeto_en_mano = {
                                "imagen": obj["frames"][0],
                                "nombre": obj["nombre"],
                                "tipo": obj["tipo"]
                            }
                            basura.remove(obj)
                            # --- MODIFICADO: Mensaje dinámico ---
                            obj_nombre = obj['nombre'][idioma_actual]
                            mensaje = f"Recogiste: {obj_nombre}" if idioma_actual == "es" else f"You picked up: {obj_nombre}"
                        else:
                            mensaje = "Ya tienes un objeto en la mano" if idioma_actual == "es" else "You are already holding an item"
                        mensaje_tiempo = pygame.time.get_ticks()
                        break

            # Tirar basura - VERSIÓN CORREGIDA
            if pressed_p or pressed_x:
                if objeto_en_mano is None:
                    # --- MODIFICADO: Mensaje dinámico ---
                    mensaje = "No tienes ningún objeto en la mano" if idioma_actual == "es" else "You are not holding an item"
                    mensaje_tiempo = pygame.time.get_ticks()
                else:
                    proximity = hitbox.inflate(24, 24)
                    tiro_valido = False
                    bote_correcto_encontrado = False
                    bote_actual = None

                    for bote in botes:
                        if proximity.colliderect(bote["rect"]):
                            tiro_valido = True
                            bote_actual = bote
                            break 

                    if tiro_valido and bote_actual:
                        # --- MODIFICADO: Mensajes dinámicos ---
                        obj_nombre = objeto_en_mano['nombre'][idioma_actual]
                        bote_nombre = bote_actual['nombre'][idioma_actual]
                        
                        if objeto_en_mano["tipo"] == bote_actual["tipo"]:
                            bote_correcto_encontrado = True
                            mensaje = f"✓ Tiraste {obj_nombre} en bote {bote_nombre}" if idioma_actual == "es" else f"✓ Threw {obj_nombre} in {bote_nombre} bin"
                            objeto_en_mano = None
                            sonido_tirar_correcto.play()
                        else:
                            errores += 1
                            mensaje = f"✗ No puedes tirar {obj_nombre} en bote {bote_nombre}" if idioma_actual == "es" else f"✗ Cannot throw {obj_nombre} in {bote_nombre} bin"
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            sonido_tirar_incorrecto.play()
                            vida_actual -= 1
                            if vida_actual < 0:
                                vida_actual = 0
                        mensaje_tiempo = pygame.time.get_ticks()
                    else:
                        # --- MODIFICADO: Mensaje dinámico ---
                        mensaje = "No hay un bote cerca" if idioma_actual == "es" else "No bin is nearby"
                        mensaje_tiempo = pygame.time.get_ticks()

        # ACTUALIZAR ANIMACIONES DE BASURA
        tiempo_actual_anim = pygame.time.get_ticks()
        for obj in basura:
            if obj["animando"]:
                tiempo_transcurrido = tiempo_actual_anim - obj["tiempo_ultimo_frame"]
                if obj["frame_actual"] == 0:
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 1
                        obj["tiempo_ultimo_frame"] = tiempo_actual_anim
                elif obj["frame_actual"] == 1:
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 2
                        obj["tiempo_ultimo_frame"] = tiempo_actual_anim
                elif obj["frame_actual"] == 2:
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 3
                        obj["tiempo_ultimo_frame"] = tiempo_actual_anim
                elif obj["frame_actual"] == 3:
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 0
                        obj["tiempo_ultimo_frame"] = tiempo_actual_anim

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
            frame_actual = obj["frames"][obj["frame_actual"]]
            screen.blit(frame_actual, obj["rect"])

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
                    "derecha": quieto_derecha, "izquierda": quieto_izquierda,
                    "detras": quieto_detras, "delante": quieto_delante
                }
                frame = posturas_quieto.get(ultima_direccion, quieto_delante)
        else:
            posturas_quieto = {
                "derecha": quieto_derecha, "izquierda": quieto_izquierda,
                "detras": quieto_detras, "delante": quieto_delante
            }
            frame = posturas_quieto.get(ultima_direccion, quieto_delante)

        # --- DIBUJAR PERSONAJE ---
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
            
            if frame_actual_dano < len(frames_dano): 
                frame_dano = frames_dano[frame_actual_dano]
                rect_dano = frame_dano.get_rect(center=hitbox.center)
                screen.blit(frame_dano, rect_dano)
        
        # --- ¡¡¡AQUÍ ESTÁ EL ARREGLO!!! ---
        # --- MODIFICADO: Añadido 'and not tiempo_fin_animacion' ---
        elif not animando_muerte and not tiempo_fin_animacion:
            screen.blit(frame, personaje_draw_rect)
        # --- FIN MODIFICACIÓN ---

        # DIBUJAR OBJETO EN LA MANO
        if objeto_en_mano is not None and not animando_muerte and not tiempo_fin_animacion:
            mano_x = personaje_draw_rect.centerx + 20
            mano_y = personaje_draw_rect.centery 
            screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))

        # Capas del fondo
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
            texto_surface = fuente.render(mensaje, True, (255, 255, 255))
            texto_ancho = texto_surface.get_width()
            mensaje_ancho = min(texto_ancho + 20, 700)
            mensaje_rect = pygame.Rect(512 - mensaje_ancho // 2, 12, mensaje_ancho, 36)
            pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
            pygame.draw.rect(screen, (255, 255, 255), mensaje_rect, 2)
            screen.blit(texto_surface, (mensaje_rect.x + 10, mensaje_rect.y + 5))
        else:
            mensaje = ""

        # MOSTRAR TIEMPO
        if tiempo_restante <= 30 and not musica_cambiada:
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "musica", "musica_apresurada.ogg"))
            pygame.mixer.music.set_volume(volumen_actual) # <-- MODIFICADO
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)
        minutos = tiempo_visual // 60
        segundos_restantes = tiempo_visual % 60
        tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"

        pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
        texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
        screen.blit(texto_tiempo, (20, 90))

        # DIBUJAR BOTÓN DE PAUSA
        sistema_pausa.dibujar()

        # --- MODIFICADO: Pasa el idioma a la pantalla de pérdida ---
        def mostrar_pantalla_perdida(idioma):
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "sonidos", "musica de perdida.mp3"))
            pygame.mixer.music.set_volume(volumen_actual) # <-- MODIFICADO
            pygame.mixer.music.play(-1)
            sonido_morir.play()

            while True:
                screen.fill((0, 0, 0))
                screen.blit(pantalla_perdida, (0, 0)) # Fondo (con "GAME OVER")
                mouse_pos = pygame.mouse.get_pos()

                # --- ¡MODIFICACIÓN DE ORDEN DE DIBUJADO! ---
                
                # 1. DIBUJAR LOS BOTONES (IMAGEN VACÍA) PRIMERO
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_reintentar_hover, rect_reintentar)
                else:
                    screen.blit(boton_reintentar, rect_reintentar)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_menu_hover, rect_menu)
                else:
                    screen.blit(boton_menu, rect_menu)
                
                # 2. DIBUJAR EL TEXTO DESPUÉS (ENCIMA DE LOS BOTONES)
                # 2a. Subtítulo (en dos líneas)
                if idioma == "en":
                    subtitulo_str_1 = "THE PLANET NEEDS YOUR HELP"
                    subtitulo_str_2 = "KEEP TRYING"
                    coordenadas_titulo = (352, 320) # <-- Coordenadas para Inglés
                else:
                    subtitulo_str_1 = "EL PLANETA NECESITA TU AYUDA"
                    subtitulo_str_2 = "SIGUE INTENTANDO"
                    coordenadas_titulo = (296, 332) # <-- Coordenadas originales Español

                subtitulo1_surf = fuente_subtitulo_gameover.render(subtitulo_str_1, True, (255, 255, 255))
                subtitulo2_surf = fuente_subtitulo_gameover.render(subtitulo_str_2, True, (255, 255, 255))
                
                subtitulo1_rect = subtitulo1_surf.get_rect(topleft=coordenadas_titulo)

                subtitulo2_rect = subtitulo2_surf.get_rect(centerx=subtitulo1_rect.centerx + 20, top=subtitulo1_rect.bottom + 5)
                screen.blit(subtitulo1_surf, subtitulo1_rect)
                screen.blit(subtitulo2_surf, subtitulo2_rect)

                # 2b. Texto Botón "Intentar de nuevo"
                boton_str = "TRY AGAIN" if idioma == "en" else "INTENTAR DE NUEVO"
                boton_surf = fuente_boton_gameover.render(boton_str, True, (0, 0, 0)) # Color negro
                boton_rect_texto = boton_surf.get_rect(center=rect_reintentar.center) 
                screen.blit(boton_surf, boton_rect_texto)
                # --- FIN MODIFICACIÓN DE ORDEN ---

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "salir" 
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "reintentar"
                        elif rect_menu.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main"

        # --- MODIFICADO: Pasa el idioma a la pantalla de victoria ---
        def mostrar_pantalla_victoria(idioma):
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "musica", "musica_victoria.mp3"))
            pygame.mixer.music.set_volume(volumen_actual) # <-- MODIFICADO
            pygame.mixer.music.play(-1)

            while True:
                screen.fill((0, 0, 0))
                screen.blit(win, (0, 0)) # 1. Fondo (vacío)
                mouse_pos = pygame.mouse.get_pos()

                # 2. Botones (vacíos/estáticos)
                if rect_reintentar_victoria.collidepoint(mouse_pos):
                    screen.blit(boton_win_intentar_hover, rect_reintentar_victoria)
                else:
                    screen.blit(boton_win_intentar, rect_reintentar_victoria)

                # Dibuja el botón de menú (con el texto ya en la imagen)
                if rect_menu_victoria.collidepoint(mouse_pos):
                    screen.blit(boton_win_menu_hover, rect_menu_victoria)
                else:
                    screen.blit(boton_win_menu, rect_menu_victoria)
                
                # 3. Textos (encima)
                # 3a. Título y subtítulos
                
                if idioma == "en":
                    titulo_str = "CONGRATULATIONS!"
                    sub1_str = "GREEN DOT FOR"
                    sub2_str = "YOU!"
                    coordenadas_titulo = (320, 260) # <-- Coordenadas para Inglés
                else:
                    titulo_str = "FELICIDADES"
                    sub1_str = "PUNTO VERDE PARA"
                    sub2_str = "TI"
                    coordenadas_titulo = (363, 213) # <-- Coordenadas para Español

                titulo_surf = fuente_victoria_titulo.render(titulo_str, True, (0, 0, 0)) # Color negro
                sub1_surf = fuente_victoria_subtitulo.render(sub1_str, True, (0, 0, 0)) # Color negro
                sub2_surf = fuente_victoria_subtitulo.render(sub2_str, True, (0, 0, 0)) # Color negro

                # Posición del título
                titulo_rect = titulo_surf.get_rect(topleft=coordenadas_titulo) # <-- MODIFICADO
                
                # Posición de subtítulos (centrados debajo del título)
                sub1_rect = sub1_surf.get_rect(centerx=titulo_rect.centerx, top=titulo_rect.bottom + 10)
                sub2_rect = sub2_surf.get_rect(centerx=titulo_rect.centerx, top=sub1_rect.bottom + 5)
                
                screen.blit(titulo_surf, titulo_rect)
                screen.blit(sub1_surf, sub1_rect)
                screen.blit(sub2_surf, sub2_rect)

                # 3b. Texto del botón Reintentar (centrado)
                if idioma == "en":
                    reintentar_str = "TRY AGAIN"
                else:
                    reintentar_str = "REINTENTAR"

                reintentar_surf = fuente_victoria_botones.render(reintentar_str, True, (0, 0, 0))
                reintentar_rect_texto = reintentar_surf.get_rect(center=rect_reintentar_victoria.center)
                screen.blit(reintentar_surf, reintentar_rect_texto)
                
                # --- Texto "MENU" ELIMINADO ---
                # --- FIN MODIFICACIONES VICTORIA ---

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return "salir"
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar_victoria.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "reintentar"
                        elif rect_menu_victoria.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main"
            
        #ganar
        if ganar(basura, objeto_en_mano):
            # --- MODIFICADO: Pasa el idioma ---
            resultado = mostrar_pantalla_victoria(idioma_actual)
            if resultado == "main":
                return "main"
            elif resultado == "reintentar":
                return "reintentar"
            elif resultado == "salir":
                return "salir"
                
        # -----------------------------
        # ANIMACIÓN DE MUERTE CORREGIDA
        # -----------------------------
        if vida_actual <= 0:
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

                    if frame_actual_muerte >= len(frames_muerte_derecha):
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = len(frames_muerte_derecha) - 1

                if ultima_direccion == "izquierda":
                    frames_muerte = frames_muerte_izquierda
                else:
                    frames_muerte = frames_muerte_derecha
                
                if frame_actual_muerte < len(frames_muerte): 
                    frame_muerte = frames_muerte[frame_actual_muerte]
                    rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                    screen.blit(frame_muerte, rect_muerte)

            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    resultado = mostrar_pantalla_perdida(idioma_actual)
                    if resultado == "main":
                        return "main"
                    elif resultado == "reintentar":
                        return "reintentar"
                    elif resultado == "salir":
                        return "salir"
        
                else:
                    if ultima_direccion == "izquierda":
                        frames_muerte = frames_muerte_izquierda
                    else:
                        frames_muerte = frames_muerte_derecha
                    frame_muerte = frames_muerte[-1]
                    rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                    screen.blit(frame_muerte, rect_muerte)
        
        muerte_por_tiempo = False
        if tiempo_restante <= 0 and not muerte_por_tiempo:
            muerte_por_tiempo = True
            vida_actual = 0

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys
        
    pygame.quit()
    if hasattr(sistema_pausa, 'return_value') and sistema_pausa.return_value:
        return sistema_pausa.return_value
    return return_value

if __name__ == "__main__":
    run_level1("es", 0.5)