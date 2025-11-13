import pygame

# Importamos todas las pantallas necesarias para la navegación del juego
from proyecto import Main
from configuracion import Configuracion        
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel
from nivel_1 import run_level1 
from tutorial import run_tutorial  # ¡IMPORTANTE! Agregar esta línea

def main():
    pygame.init()
    pygame.mixer.init()

    # Cargar música de fondo del menú principal
    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Eco Dash")

    # Cargar efecto de sonido para los clics
    click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    click_sound.set_volume(0.5)

    pantalla_actual = Main(screen)

    while True:
        resultado = pantalla_actual.run()

        # Lógica de navegación entre pantallas (AGREGAR TUTORIAL)
        if resultado == "select_character":
            pantalla_actual = Select_character(screen)

        elif resultado == "configuracion":
            pantalla_actual = Configuracion(screen)

        elif resultado == "main":
            pantalla_actual = Main(screen)

        elif resultado == "seleccion_dificultad":
            pantalla_actual = Seleccion_dificultad(screen)

        elif resultado in ["facil"]:
            pantalla_actual = Seleccion_nivel(screen)

        elif resultado == "tutorial":  # ¡NUEVA OPCIÓN!
            # Manejar el tutorial con posibilidad de reintento
            reiniciar_tutorial = True
            while reiniciar_tutorial:
                resultado_tutorial = run_tutorial()  # Ejecuta el tutorial

                if resultado_tutorial == "main":
                    # Volver al menú principal
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_tutorial = False

                elif resultado_tutorial == "tutorial":
                    # Reiniciar el tutorial
                    reiniciar_tutorial = True

                else:
                    # Por defecto, volver al menú principal
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_tutorial = False

        elif resultado in ["nivel1"]:
            # Manejar el nivel 1 con posibilidad de reintento
            reiniciar_nivel = True
            while reiniciar_nivel:
                resultado_nivel = run_level1()

                if resultado_nivel == "main":
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True

                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False
                    
        elif resultado == "salir" or resultado is None:
            break

    pygame.quit()

if __name__ == "__main__":
    main()