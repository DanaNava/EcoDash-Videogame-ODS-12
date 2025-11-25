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
        self.return_value = "seleccion_nivel"
        nivel_instance.return_value = "seleccion_nivel"
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


def run_level2_retador(idioma_actual, volumen_actual, personaje=0):
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 2")
   
    sistema_pausa = SistemaPausa(screen)

    # -----------------------------
    # CARGA DE IMÁGENES (CON RUTAS CORREGIDAS)

    # -----------------------------

    fondo = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondo_nivel2retador.png")).convert_alpha()
    #arboles

    capa_arbol1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arbolesqiz1.png")).convert_alpha()
    capa_arbol2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arbolesqiz2.png")).convert_alpha()
    capa_arbol3 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb3.png")).convert_alpha()
    capa_arbol4 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb4.png")).convert_alpha()
    capa_arbol5 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb5.png")).convert_alpha()
    capa_arbol6 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb6.png")).convert_alpha()
    capa_arbol7 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb7.png")).convert_alpha()
    capa_arbol8 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb8.png")).convert_alpha()
    capa_arbol9 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb9.png")).convert_alpha()
    capa_arbol10 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb10.png")).convert_alpha()
    capa_arbol11 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb11.png")).convert_alpha()
    capa_arbol12 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb12.png")).convert_alpha()
    capa_arbol12_1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb12_1.png")).convert_alpha()
    capa_arbol13 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb13.png")).convert_alpha()
    capa_error1_arbol = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "err1.png")).convert_alpha()
    capa_error2_arbol = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "err2.png")).convert_alpha()
    capa_error3_arbol = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "err3.png")).convert_alpha()
    capa_arbol14 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb14.png")).convert_alpha()
    capa_arbol15 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb15.png")).convert_alpha()
    capa_arbol16 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb16.png")).convert_alpha()
    capa_arbol17 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb17.png")).convert_alpha()
    capa_arbol18 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb18.png")).convert_alpha()
    capa_arbol19 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb19.png")).convert_alpha()
    capa_arbol20 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb20.png")).convert_alpha()
    capa_arbol21 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb21.png")).convert_alpha()
    capa_arbol22 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb22.png")).convert_alpha()
    capa_arbol23 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb23.png")).convert_alpha()
    capa_arbol24 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb24.png")).convert_alpha()
    capa_arbol25 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb25.png")).convert_alpha()
    capa_arbol26 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb26.png")).convert_alpha()
    capa_arbol27 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb27.png")).convert_alpha()
    capa_arbol28 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb28.png")).convert_alpha()
    capa_arbol29 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb29.png")).convert_alpha()
    capa_arbol30 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb30.png")).convert_alpha()
    capa_arbol31 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb31.png")).convert_alpha()
    capa_arbol32 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb32.png")).convert_alpha()
    capa_arbol33 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb33.png")).convert_alpha()
    capa_arbol34 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb34.png")).convert_alpha()
    capa_arbol35 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb35.png")).convert_alpha()
    capa_arbol36 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb36.png")).convert_alpha()
    capa_arbol37 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb37.png")).convert_alpha()
    capa_arbol38 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb38.png")).convert_alpha()
    capa_arbol39 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb39.png")).convert_alpha()
    capa_arbol40 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb40.png")).convert_alpha()
    capa_arbol41 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb41.png")).convert_alpha()
    capa_arbol42 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb42.png")).convert_alpha()
    capa_arbol43 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb43.png")).convert_alpha()
    capa_arbol44 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb44.png")).convert_alpha()
    capa_arbol45 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb45.png")).convert_alpha()
    capa_arbol46 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb46.png")).convert_alpha()
    capa_arbol47 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb47.png")).convert_alpha()
    capa_arbol48 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb48.png")).convert_alpha()
    capa_arbol49 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb49.png")).convert_alpha()
    capa_arbol50 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb50.png")).convert_alpha()
    capa_arbol51 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb51.png")).convert_alpha()
    capa_arbol52 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb52.png")).convert_alpha()
    capa_arbol53 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb53.png")).convert_alpha()
    capa_arbol54 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb54.png")).convert_alpha()
    capa_arbol55 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb55.png")).convert_alpha()
    capa_arbol56 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb56.png")).convert_alpha()
    capa_arbol57 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb57.png")).convert_alpha()
    capa_arbol58 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb58.png")).convert_alpha()
    capa_arbol59 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb59.png")).convert_alpha()
    capa_arbol60 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb60.png")).convert_alpha()
    capa_arbol61 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb61.png")).convert_alpha()
    capa_arbol62 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb62.png")).convert_alpha()
    capa_arbol63 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb63.png")).convert_alpha()
    capa_arbol64 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb64.png")).convert_alpha()
    capa_arbol65 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb65.png")).convert_alpha()
    capa_arbol66 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb66.png")).convert_alpha()
    capa_arbol67 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "fondos", "arb67.png")).convert_alpha()
   

    #lampara

    capa_lampara1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara1.png")).convert_alpha()
    capa_lampara2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara2.png")).convert_alpha()
    capa_lampara3 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara3.png")).convert_alpha()
    capa_lampara4 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara4.png")).convert_alpha()
    capa_lampara5 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara5.png")).convert_alpha()
    capa_lampara6 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara6.png")).convert_alpha()
    capa_lampara7 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara7.png")).convert_alpha()
    capa_lampara8 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara8.png")).convert_alpha()
    capa_lampara9 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara9.png")).convert_alpha()
    capa_lampara10 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara10.png")).convert_alpha()
    capa_lampara11 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara11.png")).convert_alpha()
    capa_lampara12 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara12.png")).convert_alpha()
    capa_lampara13 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara13.png")).convert_alpha()
    capa_lampara14 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara14.png")).convert_alpha()
    capa_lampara15 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara15.png")).convert_alpha()
    capa_lampara16 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "lampara", "lampara16.png")).convert_alpha()

   

    #columpio
    capa_colum1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "columpio", "colu1.png")).convert_alpha()
    capa_colum2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "columpio", "colu2.png")).convert_alpha()
    capa_colum4 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "columpio", "colu4.png")).convert_alpha()
    capa_colum5 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "columpio", "colu5.png")).convert_alpha()
    capa_colum6 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "columpio", "colu6.png")).convert_alpha()

    #detalles menores
    cosa_1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa1.png")).convert_alpha()
    cosa_2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa2.png")).convert_alpha()
    cosa_3 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa3.png")).convert_alpha()
    cosa_4 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa4.png")).convert_alpha()
    cosa_5 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa5.png")).convert_alpha()
    cosa_6 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa6.png")).convert_alpha()
    cosa_7 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa7.png")).convert_alpha()
    cosa_8 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa8.png")).convert_alpha()
    cosa_9 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa9.png")).convert_alpha()
    cosa_10 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa10.png")).convert_alpha()
    cosa_11 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa11.png")).convert_alpha()
    cosa_12 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa12.png")).convert_alpha()
    cosa_13 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa13.png")).convert_alpha()
    cosa_14 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "detalles_menores", "cosa14.png")).convert_alpha()
   
    palomita_img = pygame.image.load("assets_PI/sprites/palomita.png").convert_alpha()
    x_img = pygame.image.load("assets_PI/sprites/x.png").convert_alpha()
    bienlarry_img = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/gracias_larry.png").convert_alpha()
    mallarry_img = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/tristesalarry.png").convert_alpha()
    # Pantalla de victoria y barras de vida
    w = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "Pantalla_victoria.jpeg"))
    bv = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_completa.png"))
    bv2 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_2co.png"))
    bv1 = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "barra_vida_1co.png"))
    cronometro = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "sprites", "Cronometro_PI.png")).convert_alpha()


    # Posturas estáticas para quieto (como respaldo)
    if personaje == 0:  # Hombre
        quieto_derecha = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_derecha.png")).convert_alpha()
        quieto_izquierda = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_izquierda.png")).convert_alpha()
        quieto_detras = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_detras.png")).convert_alpha()
        quieto_delante = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "posturas", "PI_personaje_m_ver_delante.png")).convert_alpha()
    else:  # Mujer
        quieto_derecha = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "posturas", "personaje_PI_femenino_derecha.png")).convert_alpha()
        quieto_izquierda = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "posturas", "personaje_PI_femenino_izquierda.png")).convert_alpha()
        quieto_detras = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "posturas", "personaje_PI_femenino_detras.png")).convert_alpha()
        quieto_delante = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "posturas", "personaje_PI_femenino.png")).convert_alpha()

    #Escalar imagenes

    win = pygame.transform.scale(w, (1024, 768))
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))

    #Cargar botones (Asumimos que las imágenes ya no tienen texto)

    boton_reintentar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_intenta_otra_vez.png")).convert_alpha()
    boton_reintentar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_intenta_otra_vez_hover.png")).convert_alpha()
    boton_menu = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_menu.png")).convert_alpha()
    boton_menu_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "perdida", "boton_menu_hover.png")).convert_alpha()

    boton_win_menu_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_menu_hover_pantalla_victoria.png"))
    boton_win_menu = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_menu_pantalla_victoria.png"))
    boton_win_intentar = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_intenta_otra_vez_victoria.png"))
    boton_win_intentar_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "boton_intenta_otra_vez_victoria_hover.png"))
    boton_ir_siguiente_nivel = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "ir_siguiente_nivel_normal.png"))
    boton_ir_siguiente_nivel_hover = pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "interfaces", "victoria", "ir_siguiente_nivel_normal_hover.png"))


    boton_ir_siguiente_nivel = pygame.transform.scale(boton_ir_siguiente_nivel, (240, 65))
    boton_ir_siguiente_nivel_hover = pygame.transform.scale(boton_ir_siguiente_nivel_hover, (240, 65))

    rect_reintentar_victoria = boton_win_intentar.get_rect(center=(515, 487))
    rect_menu_victoria = boton_win_menu.get_rect(center=(515, 570))

    rect_reintentar = boton_reintentar.get_rect(center=(515, 467))
    rect_menu = boton_menu.get_rect(center=(515, 550))

    rect_ir_siguiente_nivel =  boton_ir_siguiente_nivel.get_rect(center=(515, 404))

    # Personaje inicial

   # Personaje inicial - NO sobreescribir el parámetro 'personaje'
    personaje_actual = quieto_delante  # <--- Usar variable diferente
    personaje_draw_rect = personaje_actual.get_rect(center=(489, 420))
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
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella agua1.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella agua2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella agua3.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "basura", "inorganica", "botella_agua", "botella agua4.png")).convert_alpha()
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
   
    frames_surprice = [
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "surprice2.png")).convert_alpha(),
        pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "diseyo_nivel", "nivel 2", "surprice1.png")).convert_alpha()
    ]
   
    # -----------------------------

    # POSICIONES ALEATORIAS PARA BASURAS

    # -----------------------------

    # Lista de coordenadas posibles

    posiciones_basura = [
        (825, 621),  
        (552, 46),  
        (463, 681),  
        (973, 160),  
        (107, 193),  
        (287, 325),
        (197, 703),
        (29, 373),
        (962, 513)
    ]

    # Función para obtener posiciones aleatorias únicas

    def obtener_posiciones_aleatorias(cantidad):
        return random.sample(posiciones_basura, cantidad)
   

    # Obtener 6 posiciones aleatorias únicas (una para cada basura)

    posiciones_aleatorias = obtener_posiciones_aleatorias(9)

    # Definir basuras con animaciones y traducciones

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
        },
        {
            "frames": frames_cascara_huevo,
            "rect": frames_cascara_huevo[0].get_rect(topleft=posiciones_aleatorias[6]),
            "nombre": {"es": "Cáscaras de huevo", "en": "Egg Shells"},
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_jeringa,
            "rect": frames_jeringa[0].get_rect(topleft=posiciones_aleatorias[7]),
            "nombre": {"es": "Jeringa", "en": "Syringe"},
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_periodico,
            "rect": frames_periodico[0].get_rect(topleft=posiciones_aleatorias[8]),
            "nombre": {"es": "Periódico", "en": "Newspaper"},
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_surprice,
            "rect": frames_surprice[0].get_rect(topleft=(90, 572)),
            "nombre": {"es": "a Larry", "en": "Larry"},
            "tipo": "segura",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        }
    ]

    botes = [
        {"nombre": {"es": " al bote Inorgánico", "en": " in Inorganic bin"}, "tipo": "inorganica", "rect": pygame.Rect(394, 403, 40, 38)},
        {"nombre": {"es": " al bote Orgánico", "en": " in Organic bin"}, "tipo": "organica", "rect": pygame.Rect(302, 404, 40, 39)},
        {"nombre": {"es": " al bote Residuos peligrosos", "en": " in Hazardous bin"}, "tipo": "peligrosa", "rect": pygame.Rect(648, 696, 45, 58)},
        {"nombre": {"es": " al árbol", "en": " in the tree"}, "tipo": "segura", "rect": pygame.Rect(24, 164, 48, 20)}
    ]

    colisiones = [
        #izquierda

        pygame.Rect(0, 1, 10, 241), pygame.Rect(6, 250, 11, 102), pygame.Rect(0, 373, 14, 71), pygame.Rect(67, 448, 59, 20),
        pygame.Rect(0, 498, 4, 268),

        #abajo
        pygame.Rect(0, 762, 595, 6), pygame.Rect(609, 657, 22, 84), pygame.Rect(609, 760, 419, 6),

        #derecho
        pygame.Rect(1028, 460, 1, 308), pygame.Rect(1010, 418, 13, 23), pygame.Rect(1023, 0, 1, 407),

        #conjunto de bancas
        pygame.Rect(996, 77, 17, 40), pygame.Rect(897, 41, 75, 14), pygame.Rect(839, 72, 33, 71),

        #rejas
        pygame.Rect(837, 250, 11, 118), pygame.Rect(592, 382, 246, 3), pygame.Rect(208, 1, 630, 3), pygame.Rect(209, 30, 10, 332),
        pygame.Rect(248, 385, 202, 7),

        #bancas no puestas
        pygame.Rect(187, 234, 10, 87), pygame.Rect(603, 428, 25, 34),

        #mesa para comer?
        pygame.Rect(752, 456, 63, 81), pygame.Rect(709, 489, 17, 48), pygame.Rect(841, 488, 30, 48),

        #arboles y arbustos
        pygame.Rect(22, 83, 107, 60), pygame.Rect(88, 640, 45, 49), pygame.Rect(864, 236, 19, 125),

        #lampara
        pygame.Rect(415, 699, 7, 8),

        #juegos de los niños
        pygame.Rect(640, 252, 111, 34), pygame.Rect(271, 271, 154, 15), pygame.Rect(246, 137, 9, 19), pygame.Rect(489, 138, 11, 17), pygame.Rect(710, 36, 90, 47),

        #bote peligro
        pygame.Rect(648, 690, 30, 36),

        #bote inorganico
        pygame.Rect(404, 410, 21, 9),

        #bote organico
        pygame.Rect(309, 409, 22, 9),

        #detalles
        pygame.Rect(146, 47, 61, 8), pygame.Rect(974, 669, 48, 11)
    ]

    # -----------------------------
    # ANIMACIONES DEL PERSONAJE SEGÚN SELECCIÓN
    # -----------------------------
    def cargar_animaciones_personaje(personaje_elegido):
        def centrar_sprites(lista_frames):
            """Centra todos los sprites en un rectángulo de tamaño consistente"""
            frames_centrados = []
       
            # Encontrar el tamaño máximo entre todos los frames
            max_width = max(frame.get_width() for frame in lista_frames)
            max_height = max(frame.get_height() for frame in lista_frames)
       
            # Crear un tamaño objetivo ligeramente mayor para evitar recortes
            tamaño_objetivo = (max_width + 10, max_height + 10)
       
            for frame in lista_frames:
                # Crear una superficie transparente del tamaño objetivo
                superficie_centrada = pygame.Surface(tamaño_objetivo, pygame.SRCALPHA)
           
                # Calcular posición para centrar el sprite
                x = (tamaño_objetivo[0] - frame.get_width()) // 2
                y = (tamaño_objetivo[1] - frame.get_height()) // 2
           
                # Dibujar el frame centrado
                superficie_centrada.blit(frame, (x, y))
                frames_centrados.append(superficie_centrada)
       
            return frames_centrados
        if personaje_elegido == 0:  # Hombre
            return {
                "frames_dano": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_daño_derecha", "Pi_personaje_m_daño_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_daño_derecha", "Pi_personaje_m_daño_derecha2.png")).convert_alpha()
                ],
                "frames_muerte_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte", "Pi_personaje_m_muerte5.png")).convert_alpha()
                ],
                "frames_muerte_izquierda": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_muerte_izquierda", "Pi_personaje_m_muerte_izquierda5.png")).convert_alpha()
                ],
                "frames_caminar_delante": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_caminar_delante", "PI_personaje_m_caminar_delante6.png")).convert_alpha()
                ],
                "frames_caminar_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_derecha", "Pi_personaje_m_caminar_derecha6.png")).convert_alpha()
                ],
                "frames_caminar_detras": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_detras", "Pi_personaje_m_caminar_detras6.png")).convert_alpha()
                ],
                "frames_caminar_izquierda": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_m_caminar_izquierda", "Pi_personaje_m_caminar_izquierda6.png")).convert_alpha()
                ],
                "frames_quieto_detras": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras9.png")).convert_alpha()
                ],
                "frames_quieto_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "masculino", "animaciones", "Pi_personaje_animacion_quieto_derecha", "Pi_personaje_animacion_quieto_derecha9.png")).convert_alpha()
                ],
                "frames_quieto_izquierda": [
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
            }
        else:  # Mujer
            return {
                "frames_dano": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_recibir_daño_derecha", "Pi_personaje_m_animacion_recibir_daño_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_recibir_daño_derecha", "Pi_personaje_m_animacion_recibir_daño_derecha2.png")).convert_alpha()
                ],
                "frames_muerte_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_derecha", "Pi_personaje_m_animacion_muerte_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_derecha", "Pi_personaje_m_animacion_muerte_derecha2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_derecha", "Pi_personaje_m_animacion_muerte_derecha3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_derecha", "Pi_personaje_m_animacion_muerte_derecha4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_derecha", "Pi_personaje_m_animacion_muerte_derecha5.png")).convert_alpha()
                ],
                "frames_muerte_izquierda": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_izquierda", "Pi_personaje_m_animacion_muerte_izquierda1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_izquierda", "Pi_personaje_m_animacion_muerte_izquierda2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_izquierda", "Pi_personaje_m_animacion_muerte_izquierda3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_izquierda", "Pi_personaje_m_animacion_muerte_izquierda4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_muerte_izquierda", "Pi_personaje_m_animacion_muerte_izquierda5.png")).convert_alpha()
                ],
                "frames_caminar_delante": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_delante", "Pi_personaje_m_animacion_caminar_delante6.png")).convert_alpha()
                ],
                "frames_caminar_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_derecha", "Pi_personaje_m_animacion_caminar_derecha6.png")).convert_alpha()
                ],
                "frames_caminar_detras": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_detras", "Pi_personaje_m_animacion_caminar_detras6.png")).convert_alpha()
                ],
                "frames_caminar_izquierda": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_caminar_izquierda", "Pi_personaje_m_animacion_caminar_izquierda6.png")).convert_alpha()
                ],
                "frames_quieto_detras": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_detras", "Pi_personaje_m_animacion_quieto_detras1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "PI_personaje_m_animacion_quieto_detras", "PI_personaje_m_animacion_quieto_detras9.png")).convert_alpha()
                ],
                "frames_quieto_derecha": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_derecha", "Pi_personaje_m_animacion_quieto_derecha9.png")).convert_alpha()
                ],
                "frames_quieto_izquierda": [
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda1.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda2.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda3.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda4.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda5.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda6.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda7.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda8.png")).convert_alpha(),
                    pygame.image.load(os.path.join(BASE_DIR, "assets_PI", "personajes", "femenino", "animaciones", "Pi_personaje_m_animacion_quieto_izquierda", "Pi_personaje_m_animacion_quieto_izquierda9.png")).convert_alpha()
                ]
            }

    # Cargar animaciones según el personaje seleccionado
    animaciones = cargar_animaciones_personaje(personaje)
   
    # Asignar las animaciones a variables específicas
    frames_dano = animaciones["frames_dano"]
    frames_muerte_derecha = animaciones["frames_muerte_derecha"]
    frames_muerte_izquierda = animaciones["frames_muerte_izquierda"]
    frames_caminar_delante = animaciones["frames_caminar_delante"]
    frames_caminar_derecha = animaciones["frames_caminar_derecha"]
    frames_caminar_detras = animaciones["frames_caminar_detras"]
    frames_caminar_izquierda = animaciones["frames_caminar_izquierda"]
    frames_quieto_detras = animaciones["frames_quieto_detras"]
    frames_quieto_derecha = animaciones["frames_quieto_derecha"]
    frames_quieto_izquierda = animaciones["frames_quieto_izquierda"]


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

    # Establecer la duracion de cada frame
    tiempo_frame = 0
    duracion_frame = 100
    duracion_frame_movimiento = 80
    duracion_frame_quieto = 200  # Más lento para animaciones de quieto
    #tiempo en verde
    tiempo_color_cambio = 0
    color_tiempo_activo = False

    tiempo_color_error = 0
    color_error_activo = False

    duracion_color = 2000  # 2 segundos

    # -----------------------------
    # VARIABLES
    # -----------------------------

    #tiempo para las imahenes de la x y la palomita
    feedback_imagen = None
    feedback_tiempo = 0
    feedback_duracion_normal = 1000  # 1 segundo para palomita y X
    feedback_duracion_larry = 1590   # 1.5 segundos para imágenes de Larry
    feedback_pos = (0, 0)
   
    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 3000  # Aumentar a 3 segundos
   
    # velocidad del juego y personaje
    velocidad = 3.5
    velocidad_reducida = 1
    velocidad_normal = 3.5
    clock = pygame.time.Clock()
    #charco
    charco1_pos = (407,562)
    charco1_rect = pygame.Rect(charco1_pos[0], charco1_pos[1], 78,24)
    segundochar_pos = (781, 653)
    segundochar_rect = pygame.Rect(segundochar_pos[0], segundochar_pos[1],50,31)
    # Barra de vida
    vida_max = 3
    vida_actual = vida_max

    # Tiempo - SISTEMA MEJORADO CON PAUSA
    tiempo_total = 180
    inicio_tiempo = pygame.time.get_ticks()
    tiempo_pausa_acumulado = 0
    tiempo_ultima_pausa = 0
    tiempo_visual = tiempo_total
    fuente_tiempo = pygame.font.SysFont("dejavusansmono", 35)
    tiempo_color_cambio = 0
    duracion_color = 2000  # 2 segundos
    # --- ¡¡¡MODIFICADO AQUÍ!!! ---
    # --- Cargar las DOS fuentes ---

    try:
        # Fuente para Títulos (Game Over / Victoria)
        font_titulo_path = os.path.join(BASE_DIR, "assets_PI", "fuentes", "Stay Pixel DEMO.ttf")
        fuente_subtitulo_gameover = pygame.font.Font(font_titulo_path, 32)
        fuente_victoria_titulo = pygame.font.Font(font_titulo_path, 100)
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
        # 1. Crea una lista de la 'basura esencial' que debe ser recogida.
        #    Excluye explícitamente el objeto "a Larry" (la sorpresa).
        basura_esencial_restante = [
            obj for obj in basura if obj["nombre"][idioma_actual] != "Larry" and obj["nombre"][idioma_actual] != "a Larry"
        ]
       
        # 2. Verifica si el objeto en la mano NO es la basura esencial.
        #    El jugador PUEDE tener el objeto "Larry" en la mano al ganar.

        objeto_en_mano_esencial = (
            objeto_en_mano is not None and
            objeto_en_mano["nombre"][idioma_actual] != "Larry" and
            objeto_en_mano["nombre"][idioma_actual] != "a Larry"
        )
       

        # 3. La condición de victoria es:
        #    - La lista de basura esencial en el suelo debe estar vacía.
        #    - Y el jugador no debe tener otra basura esencial en la mano.
        return len(basura_esencial_restante) == 0 and not objeto_en_mano_esencial
   
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
            screen.blit(cronometro, (15, 60))

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

            # ¿Sigue activo el color verde?
            if pygame.time.get_ticks() - tiempo_color_cambio < duracion_color:
                color_tiempo = (40, 167, 69)  # verde
            else:
                color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)

            # Formato normal del tiempo (siempre se dibuja)
                minutos = tiempo_visual // 60
                segundos_restantes = tiempo_visual % 60
                texto_tiempo = fuente_tiempo.render(f"{minutos:02}:{segundos_restantes:02}", True, color_tiempo)
                screen.blit(texto_tiempo, (38, 85))

            # DIBUJAR SISTEMA DE PAUSA

            sistema_pausa.dibujar()

            pygame.display.flip()
            clock.tick(60)
            continue

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

    # CORRECCIÓN: Bloquear completamente el movimiento durante la muerte

        if not animando_muerte and not tiempo_fin_animacion:
            moving = False
            # Movimiento
            if not animando_dano:
                if keys[pygame.K_LEFT]:
                    hitbox.x -= velocidad
                    animacion_correr_izquierda = True
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "izquierda"
                    # Reiniciar frame de quieto cuando empieza a moverse

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

            # Edge detection (solo Enter)
            pressed_enter = keys[pygame.K_RETURN] and not prev_keys[pygame.K_RETURN]

            # ---------------------------------
            # PRIORIDAD: TIRAR SI YA TRAES ALGO EN LA MANO
            # ---------------------------------
            if pressed_enter and objeto_en_mano is not None:
                proximity = hitbox.inflate(24, 24)
                tiro_valido = False
                bote_correcto_encontrado = False
                bote_actual = None

                # Buscar bote cercano
                for bote in botes:
                    if proximity.colliderect(bote["rect"]):
                        tiro_valido = True
                        bote_actual = bote
                        break  # primer bote que encontramos

                if tiro_valido and bote_actual:
                    obj_nombre = objeto_en_mano['nombre'][idioma_actual]
                    bote_nombre = bote_actual['nombre'][idioma_actual]

                    # ---- CASO ESPECIAL: LARRY ----
                    es_larry = (
                        objeto_en_mano["nombre"][idioma_actual] == "Larry"
                        or objeto_en_mano["nombre"][idioma_actual] == "a Larry"
                    )

                    if es_larry:
                        # Solo el bote de tipo "segura" es correcto
                        if bote_actual["tipo"] == "segura":
                            # CORRECTO: Larry al árbol
                            bote_correcto_encontrado = True
                            mensaje = (
                                f"✓ llevaste {obj_nombre}{bote_nombre} muy bien!!!"
                                if idioma_actual == "es"
                                else f"✓ You took {obj_nombre}{bote_nombre} very well!!!"
                            )
                            objeto_en_mano = None
                            sonido_tirar_correcto.play()
                            feedback_imagen = bienlarry_img
                            feedback_tiempo = pygame.time.get_ticks()
                            feedback_pos = (screen.get_width() // 2, screen.get_height() // 2)
                        else:
                            # INCORRECTO especial para Larry (no quita vida ni errores)
                            bote_nombre_limpio = (
                                bote_nombre.replace(" al ", "")
                                        .replace(" bote ", "")
                                        .replace(" in ", "")
                                        .replace(" bin", "")
                            )
                            mensaje = (
                                f"Tiraste {obj_nombre} en {bote_nombre_limpio}, muy mal"
                                if idioma_actual == "es"
                                else f"You threw {obj_nombre} in {bote_nombre_limpio}, very bad"
                            )
                            sonido_tirar_incorrecto.play()
                            feedback_imagen = mallarry_img
                            feedback_tiempo = pygame.time.get_ticks()
                            feedback_pos = (screen.get_width() // 2, screen.get_height() // 2)
                            objeto_en_mano = None  # Larry se va igual
                        mensaje_tiempo = pygame.time.get_ticks()

                    else:
                        # ---- LÓGICA NORMAL PARA BASURA ----
                        if objeto_en_mano["tipo"] == bote_actual["tipo"]:
                            # Tiro CORRECTO
                            bote_correcto_encontrado = True
                            mensaje = (
                                f"✓ llevaste {obj_nombre} {bote_nombre}"
                                if idioma_actual == "es"
                                else f"✓ You took {obj_nombre}{bote_nombre}"
                            )
                            objeto_en_mano = None
                            sonido_tirar_correcto.play()
                            feedback_imagen = palomita_img
                            feedback_tiempo = pygame.time.get_ticks()
                            feedback_pos = (screen.get_width() // 2, screen.get_height() // 2)
                            tiempo_total += 1
                            tiempo_color_cambio = pygame.time.get_ticks()
                            color_tiempo_activo = True
                        else:
                            # Tiro INCORRECTO
                            errores += 1
                            mensaje = (
                                f"✗ No puedes tirar {obj_nombre} {bote_nombre}"
                                if idioma_actual == "es"
                                else f"✗ Cannot throw {obj_nombre} {bote_nombre}"
                            )
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            sonido_tirar_incorrecto.play()
                            feedback_imagen = x_img
                            feedback_tiempo = pygame.time.get_ticks()
                            feedback_pos = (screen.get_width() // 2, screen.get_height() // 2)
                            tiempo_total -= 10
                            velocidad -= 1
                            color_error_activo = True
                            tiempo_color_error = pygame.time.get_ticks()
                            vida_actual -= 1
                            if vida_actual < 0:
                                vida_actual = 0

                        mensaje_tiempo = pygame.time.get_ticks()

                else:
                    # No hay bote cercano: revisar si hay basura cerca para decidir el mensaje
                    basura_cercana = False
                    for obj in basura:
                        if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                            basura_cercana = True
                            break

                    if basura_cercana:
                        mensaje = (
                            "Ya tienes un objeto en la mano"
                            if idioma_actual == "es"
                            else "You are already holding an item"
                        )
                    else:
                        mensaje = (
                            "No hay un bote cerca"
                            if idioma_actual == "es"
                            else "No bin is nearby"
                        )
                    mensaje_tiempo = pygame.time.get_ticks()


            #---------------------------------
            # 2) RECOGER BASURA (si NO traes nada en la mano)
            # ---------------------------------
            if pressed_enter and objeto_en_mano is None:
                basura_cercana = False
                for obj in basura[:]:
                    if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                        basura_cercana = True
                        sonido_recoger.play()
                        obj["animando"] = False
                        objeto_en_mano = {
                            "imagen": obj["frames"][0],
                            "nombre": obj["nombre"],
                            "tipo": obj["tipo"]
                        }
                        basura.remove(obj)
                        obj_nombre = obj['nombre'][idioma_actual]
                        mensaje = (
                            f"Recogiste {obj_nombre}"
                            if idioma_actual == "es"
                            else f"You picked up {obj_nombre}"
                        )
                        mensaje_tiempo = pygame.time.get_ticks()
                        break

        # -----------------------------

        # ACTUALIZAR ANIMACIONES DE BASURA

        # -----------------------------

        tiempo_actual = pygame.time.get_ticks()
       
        for obj in basura:
            if obj["animando"]:
                tiempo_transcurrido = tiempo_actual - obj["tiempo_ultimo_frame"]
               
                # Lógica de timing para la animación
                if obj["frame_actual"] == 0:  # Primer frame - 500ms
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 1
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 1:  # Segundo frame - 100ms
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 2
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 2:  # Tercer frame - 100ms
                    if tiempo_transcurrido >= 100:
                        obj["frame_actual"] = 3
                        obj["tiempo_ultimo_frame"] = tiempo_actual
                elif obj["frame_actual"] == 3:  # Último frame - 500ms
                    if tiempo_transcurrido >= 500:
                        obj["frame_actual"] = 0  # Volver al primer frame
                        obj["tiempo_ultimo_frame"] = tiempo_actual

        # -----------------------------

        # DIBUJAR

        # -----------------------------

        screen.fill((0, 0, 0))
        screen.blit(fondo, (0, 0))
        screen.blit(cronometro, (15, 60))
        # BARRA DE VIDA
        if vida_actual == 3:
            screen.blit(barra_vida, (20, -20))
        elif vida_actual == 2:
            screen.blit(barra_vida2, (20, -20))
        elif vida_actual == 1:
            screen.blit(barra_vida1, (20, -20))

        for obj in basura:
        # Evitar que el índice se salga del rango
            if obj["frame_actual"] >= len(obj["frames"]):
                obj["frame_actual"] = 0
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
        #charco
        if hitbox.colliderect(charco1_rect) or hitbox.colliderect(segundochar_rect):
            velocidad = velocidad_reducida
        else:
            velocidad = velocidad_normal

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
       

        # --- CORRECCIÓN: NO dibujar personaje normal durante muerte ---
        elif not animando_muerte and not tiempo_fin_animacion:
            # Dibujar personaje normal solo si no está en animación de muerte
            screen.blit(frame, personaje_draw_rect)

        # DIBUJAR OBJETO EN LA MANO

        if objeto_en_mano is not None and not animando_muerte and not tiempo_fin_animacion:
            mano_x = personaje_draw_rect.centerx + 20
            mano_y = personaje_draw_rect.centery
            screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))

        #fondo arbol esquina izquierda

        screen.blit(capa_arbol1, (31, 576))
        screen.blit(capa_arbol2, (30, 579))
        screen.blit(capa_arbol3, (173, 564))
        screen.blit(capa_arbol4, (158, 558))
        screen.blit(capa_arbol5, (151, 546))
        screen.blit(capa_arbol6, (143, 540))
        screen.blit(capa_arbol7, (134, 535))
        screen.blit(capa_arbol8, (121, 537))
        screen.blit(capa_arbol9, (112, 535))
        screen.blit(capa_arbol10, (115, 532))
        screen.blit(capa_arbol11, (63, 546))
        screen.blit(capa_arbol12, (106, 535))
        screen.blit(capa_arbol12_1, (103, 537))
        screen.blit(capa_arbol13, (93, 537))
        screen.blit(capa_error1_arbol, (47, 560))
        screen.blit(capa_error2_arbol, (41, 566))
        screen.blit(capa_error3_arbol, (35, 569))
        screen.blit(capa_arbol14, (81, 537))
        screen.blit(capa_arbol15, (90, 535))
        screen.blit(capa_arbol16, (81, 540))
        screen.blit(capa_arbol17, (84, 537))
        screen.blit(capa_arbol18, (75, 543))
        screen.blit(capa_arbol19, (69, 543))
        screen.blit(capa_arbol20, (72, 540))
        screen.blit(capa_arbol21, (56, 549))
        screen.blit(capa_arbol22, (53, 552))
        screen.blit(capa_arbol23, (63, 546))
        screen.blit(capa_arbol24, (47, 558))
        screen.blit(capa_arbol25, (44, 563))
        screen.blit(capa_arbol26, (38, 569))
        screen.blit(capa_arbol27, (35, 572))
        screen.blit(capa_arbol28, (32, 575))
        screen.blit(capa_arbol29, (29, 578))
        screen.blit(capa_arbol30, (29, 583))
        screen.blit(capa_arbol31, (26, 595))
        screen.blit(capa_arbol32, (22, 607))
        screen.blit(capa_arbol33, (19, 612))
        screen.blit(capa_arbol34, (22, 627))
        screen.blit(capa_arbol35, (22, 635))
        screen.blit(capa_arbol36, (19, 637))
        screen.blit(capa_arbol37, (16, 641))
        screen.blit(capa_arbol38, (16, 647))
        screen.blit(capa_arbol39, (13, 653))
        screen.blit(capa_arbol40, (26, 673))
        screen.blit(capa_arbol41, (35, 675))
        screen.blit(capa_arbol42, (38, 681))
        screen.blit(capa_arbol43, (44, 684))
        screen.blit(capa_arbol44, (47, 687))
        screen.blit(capa_arbol45, (59, 684))
        screen.blit(capa_arbol46, (32, 675))
        screen.blit(capa_arbol47, (189, 581))
        screen.blit(capa_arbol48, (192, 583))
        screen.blit(capa_arbol49, (192, 598))
        screen.blit(capa_arbol50, (192, 638))
        screen.blit(capa_arbol51, (195, 586))
        screen.blit(capa_arbol52, (195, 604))
        screen.blit(capa_arbol53, (195, 618))
        screen.blit(capa_arbol54, (195, 624))
        screen.blit(capa_arbol55, (195, 641))
        screen.blit(capa_arbol56, (195, 647))
        screen.blit(capa_arbol57, (198, 650))
        screen.blit(capa_arbol58, (198, 658))
        screen.blit(capa_arbol59, (201, 655))
        screen.blit(capa_arbol60, (130, 665))
        screen.blit(capa_arbol61, (134, 674))
        screen.blit(capa_arbol62, (180, 675))
        screen.blit(capa_arbol63, (137, 690))
        screen.blit(capa_arbol64, (143, 688))
        screen.blit(capa_arbol65, (143, 693))
        screen.blit(capa_arbol66, (158, 693))
        screen.blit(capa_arbol67, (167, 693))
        screen.blit(capa_arbol66, (171, 696))
        screen.blit(capa_arbol66, (146, 696))
       
        #fondo lampara

        screen.blit(capa_lampara1, (412, 612))
        screen.blit(capa_lampara2, (415, 607))
        screen.blit(capa_lampara3, (422, 604))
        screen.blit(capa_lampara4, (432, 599))
        screen.blit(capa_lampara5, (425, 602))
        screen.blit(capa_lampara6, (455, 602))
        screen.blit(capa_lampara7, (462, 604))
        screen.blit(capa_lampara8, (466, 610))
        screen.blit(capa_lampara9, (469, 612))
        screen.blit(capa_lampara10, (466, 617))
        screen.blit(capa_lampara11, (462, 620))
        screen.blit(capa_lampara12, (459, 623))
        screen.blit(capa_lampara13, (455, 625))
        screen.blit(capa_lampara14, (459, 633))
        screen.blit(capa_lampara15, (408, 709))
        screen.blit(capa_lampara16, (405, 717))

        #columpio

        screen.blit(capa_colum1, (485, 54))
        screen.blit(capa_colum2, (486, 51))
        screen.blit(capa_colum4, (259, 60))
        screen.blit(capa_colum5, (242, 54))
        screen.blit(capa_colum6, (243, 51))
       
        #detalles menores
        screen.blit(cosa_1, (660, 215))
        screen.blit(cosa_2, (658, 217))
        screen.blit(cosa_3, (656, 222))
        screen.blit(cosa_4, (654, 225))
        screen.blit(cosa_5, (666, 225))
        screen.blit(cosa_6, (666, 231))
        screen.blit(cosa_7, (653, 232))
        screen.blit(cosa_8, (651, 234))
        screen.blit(cosa_9, (671, 234))
        screen.blit(cosa_10, (666, 240))
        screen.blit(cosa_11, (649, 242))
        screen.blit(cosa_12, (646, 243))
        screen.blit(cosa_13, (643, 252))
        screen.blit(cosa_14, (636, 253))    

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
            # [Nuevo] FEEDBACK VISUAL (palomita, X y Larry) - CENTRO DE PANTALLA
        if feedback_imagen:
            tiempo_actual_feedback = pygame.time.get_ticks()
           
            # Determinar qué duración usar según el tipo de imagen
            if feedback_imagen in [bienlarry_img, mallarry_img]:
                duracion_actual = feedback_duracion_larry
            else:
                duracion_actual = feedback_duracion_normal
           
            # Dibujar si aún está en tiempo
            if tiempo_actual_feedback - feedback_tiempo < duracion_actual:
                centro_pantalla = (screen.get_width() // 2, screen.get_height() // 2)
                feedback_rect = feedback_imagen.get_rect(center=centro_pantalla)
                screen.blit(feedback_imagen, feedback_rect)
            else:
                feedback_imagen = None



         # MOSTRAR TIEMPO
        if tiempo_restante <= 30 and not musica_cambiada:
            # Cambiar a música apresurada
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "musica", "musica_apresurada.ogg"))
            pygame.mixer.music.set_volume(volumen_actual)
            pygame.mixer.music.play(-1)
            musica_cambiada = True
        elif tiempo_restante > 30 and musica_cambiada:
            # Volver a música normal si el tiempo se recupera
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "musica", "musica_nivel.wav"))
            pygame.mixer.music.set_volume(volumen_actual)
            pygame.mixer.music.play(-1)
            musica_cambiada = False

        # --- CONTROL DE COLORES TEMPORALES DEL CRONÓMETRO ---

        if color_error_activo:
            # Prioridad: el rojo del error manda primero
            if pygame.time.get_ticks() - tiempo_color_error < duracion_color:
                color_tiempo = (220, 20, 60)  # rojo fuerte
            else:
             color_error_activo = False
             color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)

        elif color_tiempo_activo:
            # Verde solo si no hay error activo
            if pygame.time.get_ticks() - tiempo_color_cambio < duracion_color:
                color_tiempo = (40, 167, 69)  # verde
            else:
                color_tiempo_activo = False
                color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)
        else:
            # Color normal
            color_tiempo = (255, 0, 0) if tiempo_visual <= 30 else (255, 255, 255)

        # -------------------------
        minutos = tiempo_visual // 60
        segundos_restantes = tiempo_visual % 60
        tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"

        texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
        cronometro = pygame.transform.scale(cronometro, (150, 90))
        screen.blit(texto_tiempo, (17, 85))
        # DIBUJAR BOTÓN DE PAUSA
        sistema_pausa.dibujar()

        # --- MODIFICADO: Pasa el idioma a la pantalla de pérdida ---
        def mostrar_pantalla_perdida(idioma):
            pygame.mixer.music.load(os.path.join(BASE_DIR, "assets_PI", "sonidos", "musica de perdida.mp3"))
            pygame.mixer.music.set_volume(volumen_actual)
            pygame.mixer.music.play(-1)
            sonido_morir.play()

            while True:
                screen.fill((0, 0, 0))
                screen.blit(pantalla_perdida, (0, 0)) # Fondo (con "GAME OVER")
                mouse_pos = pygame.mouse.get_pos()

                # --- ¡MODIFICACIÓN DE ORDEN DE DIBUJADO! -
               
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
            pygame.mixer.music.set_volume(volumen_actual)
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

                if rect_ir_siguiente_nivel.collidepoint(mouse_pos):
                    screen.blit(boton_ir_siguiente_nivel_hover, rect_ir_siguiente_nivel)
                else:
                    screen.blit(boton_ir_siguiente_nivel, rect_ir_siguiente_nivel)
               
                # 3. Textos (encima)
                # 3a. Título y subtítulos

           
                if idioma == "en":
                    titulo_str = "WELL DONE!"
                    sub1_str = "CHANGE BEGINS"
                    sub2_str = "WITH YOU!"
                    coordenadas_titulo = (300, 180) # <-- Coordenadas para Inglés
                else:
                    titulo_str = "¡BIEN HECHO!"
                    sub1_str = "¡EL CAMBIO EMPIEZA"
                    sub2_str = "CONTIGO!"
                    coordenadas_titulo = (275, 150) # <-- Coordenadas para Español

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
                if idioma == "en":
                    siguiente_nivel_str = "NEXT LEVEL"
                else:
                    siguiente_nivel_str = "SIGUIENTE NIVEL"

                siguiente_nivel_surf = fuente_victoria_botones.render(siguiente_nivel_str, True, (0, 0, 0))
                siguiente_nivel_rect_texto = siguiente_nivel_surf.get_rect(center=rect_ir_siguiente_nivel.center)
                screen.blit(siguiente_nivel_surf, siguiente_nivel_rect_texto)

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
                        elif rect_ir_siguiente_nivel.collidepoint(mouse_pos):
                            print("Botón siguiente nivel presionado")
                            print("Retornando 'nivel3' desde mostrar_pantalla_victoria")
                            pygame.mixer.music.stop()
                            return "nivel3"
           
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
            elif resultado == "nivel3":
                print("Retornando 'nivel3' desde run_level1")
                return "nivel3"
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

                # CORRECCIÓN: Limpiar pantalla y dibujar solo la animación de muerte
                if ultima_direccion == "izquierda":
                    frames_muerte = frames_muerte_izquierda
                else:
                    frames_muerte = frames_muerte_derecha
               
                if frame_actual_muerte < len(frames_muerte):
                    frame_muerte = frames_muerte[frame_actual_muerte]
                    rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                    # DIBUJAR SOLO LA ANIMACIÓN DE MUERTE, no el personaje normal
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
                    # DIBUJAR SOLO LA ANIMACIÓN DE MUERTE, no el personaje normal
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
    run_level2_retador("es", 0.5)