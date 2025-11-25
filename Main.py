import pygame

# Importamos todas las pantallas necesarias para la navegación del juego---------------
from proyecto import Main
from configuracion import Configuracion
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel
from nivel_1 import run_level1
from nivel_2 import run_level2
from Nivel_3 import run_level3 
from tutorial import run_tutorial
from creditos import Creditos
from nivel1_retador import run_level1retador
from nivel2_retador import run_level2_retador
from nivel3_retador import run_level3_retador
#Aun no funcional la intro
from intro import run_intro

def main():
    pygame.init()   # Inicializa todos los módulos de pygame---------------------------
    pygame.mixer.init()   # Inicializa el sistema de sonido de pygame------------------

    # Variables de estado para el volumen, idioma, personaje y dificultad
    volumen_juego = 0.5
    idioma_juego = "es"
    personaje_juego = 0  # 0 = hombre, 1 = mujer (valor por defecto)
    dificultad = None

    screen = pygame.display.set_mode((1024, 768))   # Crea la ventana del juego con resolución 1024x768
    pygame.display.set_caption("Eco Dash")   # Título de la ventana

    # Cargar música de fondo del menú principal UNA SOLA VEZ al inicio
    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
    pygame.mixer.music.set_volume(volumen_juego)
    pygame.mixer.music.play(-1)

    # Cargar efecto de sonido para los clics
    click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    click_sound.set_volume(0.5)   # volumen del clic

    # Pasar el idioma y volumen a la pantalla inicial
    pantalla_actual = Main(screen, idioma_juego, volumen_juego)   # comienza en la pantalla main, la inicial
    
    # Variable para controlar el bucle principal
    running = True

    while running:
        # La pantalla actual (que ya tiene el idioma) se ejecuta
        resultado = pantalla_actual.run()
        
        # Lógica de navegación entre pantallas
        if resultado == "select_character":
            pantalla_actual = Select_character(screen, idioma_juego, volumen_juego)   # Ir a la pantalla de selección de personaje

        elif resultado == "configuracion":
            # Ir al menú de configuración - NO PAUSAR LA MÚSICA
            pantalla_actual = Configuracion(screen, idioma_juego, volumen_juego)
            
            # Recibir TRES valores de vuelta
            resultado_config, nuevo_idioma, nuevo_volumen = pantalla_actual.run()   # Ejecutar pantalla de configuración
            
            # Actualizar las variables globales
            idioma_juego = nuevo_idioma
            volumen_juego = nuevo_volumen
            
            # Actualiza el volumen de la música principal por si cambió
            pygame.mixer.music.set_volume(volumen_juego)
            
            if resultado_config == "main":
                pantalla_actual = Main(screen, idioma_juego, volumen_juego)
            elif resultado_config == "salir":
                running = False
                break

        elif resultado == "creditos":
            pantalla_actual = Creditos(screen, idioma_juego, volumen_juego)

        elif resultado == "main":
            # Asegurar que la música esté sonando al volver al main
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
            pantalla_actual = Main(screen, idioma_juego, volumen_juego)   # Volver al menú principal

        elif resultado == "seleccion_dificultad":
            pantalla_actual = Seleccion_dificultad(screen, idioma_juego, volumen_juego)   # Ir a la pantalla de selección de dificultad
        
        # MODIFICACIÓN: Capturar la selección de personaje desde Select_character
        elif isinstance(resultado, dict) and "accion" in resultado:
            # Esto viene de Select_character con información del personaje
            accion = resultado["accion"]
            personaje_juego = resultado["personaje"]  # 0 = hombre, 1 = mujer
            
            print(f"Personaje seleccionado: {'Hombre' if personaje_juego == 0 else 'Mujer'}")
            
            if accion == "seleccion_dificultad":
                pantalla_actual = Seleccion_dificultad(screen, idioma_juego, volumen_juego)
            elif accion == "main":
                pantalla_actual = Main(screen, idioma_juego, volumen_juego)
            elif accion == "seleccion_personaje":
                # Ir directamente a selección de nivel si se presionó "Select"
                pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)

        elif resultado == "facil":
            dificultad = "facil"
            pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)

        elif resultado == "medio":
            dificultad = "medio"
            pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
        
        elif resultado == "tutorial":
        # Manejar el tutorial con posibilidad de reintento
            reiniciar_tutorial = True
            while reiniciar_tutorial and running:
                # Pasar idioma, volumen y personaje al tutorial (CORREGIDO)
                resultado_tutorial = run_tutorial(idioma_juego, volumen_juego)

                if resultado_tutorial == "main":
                    # Volver al menú principal (TUTORIAL MANTIENE "main")
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_tutorial = False

                elif resultado_tutorial == "tutorial":
                    reiniciar_tutorial = True

                elif resultado_tutorial == "salir":
                    running = False
                    reiniciar_tutorial = False

                else:
                    # Por defecto, volver al menú principal
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_tutorial = False
        
            if not running:
                break
        
        #nivel 1----------------------------------------------------------------------------------
        elif resultado == "nivel1":

        #------intro-----------------------------------
            intro_resultado = run_intro(idioma_juego, volumen_juego)
            if intro_resultado == "main":
                pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                continue  # Volver al menú sin iniciar nivel
            elif intro_resultado == "salir":
                running = False
                break
        #------------------------------------------
            # Manejar el nivel 1 con posibilidad de reintento y progresión
            nivel_actual = "nivel1"
            reiniciar_nivel = True
            while reiniciar_nivel and running:
                if nivel_actual == "nivel1":
                    if dificultad == "medio":
                        # Pasar personaje al nivel retador
                        resultado_nivel = run_level1retador(idioma_juego, volumen_juego, personaje_juego)
                    else:
                        # Pasar personaje al nivel normal
                        resultado_nivel = run_level1(idioma_juego, volumen_juego, personaje_juego)
                
                elif nivel_actual == "nivel2":
                    if dificultad == "medio":
                        resultado_nivel = run_level2_retador(idioma_juego, volumen_juego, personaje_juego)
                    else:
                        resultado_nivel = run_level2(idioma_juego, volumen_juego, personaje_juego)
                
                elif nivel_actual == "nivel3":
                    if dificultad == "medio":
                        resultado_nivel = run_level3_retador(idioma_juego, volumen_juego, personaje_juego)
                    else:
                        resultado_nivel = run_level3(idioma_juego, volumen_juego, personaje_juego)

                if resultado_nivel == "main":
                        # Volver a selección de nivel en lugar de menú principal
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                            pygame.mixer.music.set_volume(volumen_juego)
                            pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
                        
                elif resultado_nivel == "seleccion_nivel":
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
                        reiniciar_nivel = False

                elif resultado_nivel == "reintentar":
                        # Reintentar el nivel actual
                        reiniciar_nivel = True
                    
                elif resultado_nivel == "salir":
                        running = False
                        reiniciar_nivel = False
                        
                elif resultado_nivel == "nivel2":
                        # Avanzar al nivel 2
                        nivel_actual = "nivel2"
                        reiniciar_nivel = True
                        print(f"Avanzando a {nivel_actual}")

                elif resultado_nivel == "nivel3":
                        # Avanzar al nivel 3
                        nivel_actual = "nivel3"
                        reiniciar_nivel = True
                        print(f"Avanzando a {nivel_actual}")

                else:
                        # Por defecto, regresa a selección de nivel
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
            
                if not running:
                        break
        #fin del nivel 1-----------------------------------------------------------------
        
        #nivel 2 ------------------------------------------------------------------------
        elif resultado == "nivel2":
            if dificultad == "medio":
                reiniciar_nivel = True
                while reiniciar_nivel and running:
                    # Pasar el idioma, volumen y personaje al nivel 2 retador
                    resultado_nivel = run_level2_retador(idioma_juego, volumen_juego, personaje_juego)

                    if resultado_nivel == "main":
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                            pygame.mixer.music.set_volume(volumen_juego)
                            pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False

                    elif resultado_nivel == "seleccion_nivel":
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
                        reiniciar_nivel = False

                    elif resultado_nivel == "reintentar":
                        reiniciar_nivel = True

                    elif resultado_nivel == "salir":
                        running = False
                        reiniciar_nivel = False
                else:
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                    reiniciar_nivel = False
            elif dificultad == "facil":
                reiniciar_nivel = True
                while reiniciar_nivel and running:
                    # Pasar el idioma, volumen y personaje al nivel 2 fácil (CORREGIDO)
                    resultado_nivel = run_level2(idioma_juego, volumen_juego, personaje_juego)
                    if resultado_nivel == "main":
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
                        
                    elif resultado_nivel == "seleccion_nivel":
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
                        reiniciar_nivel = False    
                        
                    elif resultado_nivel == "reintentar":
                        reiniciar_nivel = True

                    elif resultado_nivel == "salir":
                        running = False
                        reiniciar_nivel = False

                    else:
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
            
            if not running:
                break
        #fin del nivel 2----------------------------------------------------------------------
        
        #nivel 3------------------------------------------------------------------------------
        elif resultado == "nivel3":
            # Manejar el nivel 3 con posibilidad de reintento
            if dificultad == "medio":
                reiniciar_nivel = True
                while reiniciar_nivel and running:
                    # Pasar el idioma, volumen y personaje al nivel 3 retador
                    resultado_nivel = run_level3_retador(idioma_juego, volumen_juego, personaje_juego)

                    if resultado_nivel == "main":
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False

                    elif resultado_nivel == "seleccion_nivel":
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
                        reiniciar_nivel = False

                    elif resultado_nivel == "reintentar":
                        reiniciar_nivel = True

                    elif resultado_nivel == "salir":
                        running = False
                        reiniciar_nivel = False
                else:
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                    reiniciar_nivel = False
            elif dificultad == "facil":
                reiniciar_nivel = True
                while reiniciar_nivel and running:
                    # Pasar el idioma, volumen y personaje al nivel 3 fácil (CORREGIDO)
                    resultado_nivel = run_level3(idioma_juego, volumen_juego, personaje_juego)
                    if resultado_nivel == "main":
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
                    
                    elif resultado_nivel == "seleccion_nivel":
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)
                        reiniciar_nivel = False
                        
                    elif resultado_nivel == "reintentar":
                        reiniciar_nivel = True

                    elif resultado_nivel == "salir":
                        running = False
                        reiniciar_nivel = False

                    else:
                        if not pygame.mixer.get_init():
                            pygame.mixer.init()
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                        pygame.mixer.music.set_volume(volumen_juego)
                        pygame.mixer.music.play(-1)
                        pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)  # CAMBIADO
                        reiniciar_nivel = False
            
            if not running:
                break
        #fin del nivel 3-------------------------------------------------------------------------------

        elif resultado == "salir" or resultado is None:
            running = False
            break
    
    pygame.quit()   # Cierra pygame y finaliza el programa


if __name__ == "__main__":
    main()