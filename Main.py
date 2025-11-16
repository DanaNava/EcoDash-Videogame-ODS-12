import pygame

# Importamos todas las pantallas necesarias para la navegación del juego
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

def main():
    pygame.init()   # Inicializa todos los módulos de pygame
    pygame.mixer.init()   # Inicializa el sistema de sonido de pygame

    # Variables de estado para el volumen e idioma
    volumen_juego = 0.5
    idioma_juego = "es"
    
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

        elif resultado in ["facil"]:   # Si se elige la dificultad fácil
            pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)   # Pasar a la selección de nivel

        elif resultado == "tutorial":
            # Manejar el tutorial con posibilidad de reintento
            reiniciar_tutorial = True
            while reiniciar_tutorial and running:
                # Pasar idioma y volumen al tutorial
                resultado_tutorial = run_tutorial()

                if resultado_tutorial == "main":
                    # Volver al menú principal
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

        elif resultado == "nivel1":
            # Manejar el nivel 1 con posibilidad de reintento y progresión
            nivel_actual = "nivel1"
            reiniciar_nivel = True
            while reiniciar_nivel and running:
                if nivel_actual == "nivel1":
                    resultado_nivel = run_level1(idioma_juego, volumen_juego)
                elif nivel_actual == "nivel2":
                    resultado_nivel = run_level2(idioma_juego, volumen_juego)
                elif nivel_actual == "nivel3":
                    resultado_nivel = run_level3(idioma_juego, volumen_juego)

                if resultado_nivel == "main":
                    # Volver al menú principal
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
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
                    # Por defecto, regresa al menú
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False
            
            if not running:
                break

        elif resultado == "nivel2":
            # Manejar el nivel 2 con posibilidad de reintento y progresión
            nivel_actual = "nivel2"
            reiniciar_nivel = True
            while reiniciar_nivel and running:
                if nivel_actual == "nivel2":
                    resultado_nivel = run_level2(idioma_juego, volumen_juego)
                elif nivel_actual == "nivel3":
                    resultado_nivel = run_level3(idioma_juego, volumen_juego)

                if resultado_nivel == "main":
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True
                    
                elif resultado_nivel == "nivel3":
                    # Avanzar al nivel 3
                    nivel_actual = "nivel3"
                    reiniciar_nivel = True
                    print(f"Avanzando a {nivel_actual}")

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
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False
            
            if not running:
                break

        elif resultado == "nivel3":
            # Manejar el nivel 3 con posibilidad de reintento
            reiniciar_nivel = True
            while reiniciar_nivel and running:
                # Pasar el idioma y el volumen al nivel 3
                resultado_nivel = run_level3(idioma_juego, volumen_juego)

                if resultado_nivel == "main":
                    if not pygame.mixer.get_init():
                        pygame.mixer.init()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
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
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False
            
            if not running:
                break

        elif resultado == "salir" or resultado is None:
            running = False
            break

    pygame.quit()   # Cierra pygame y finaliza el programa


if __name__ == "__main__":
    main()