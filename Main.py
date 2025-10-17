import pygame

# Importamos todas las pantallas necesarias para la navegación del juego
from proyecto import Main
from configuracion import Configuracion        
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel
from nivel_1 import run_level1
from nivel_2 import run_level2

def main():
    pygame.init()  # Inicializa todos los módulos de pygame
    pygame.mixer.init()  # Inicializa el sistema de sonido de pygame

    # Cargar música de fondo del menú principal
    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen de la música (0.0 a 1.0)
    pygame.mixer.music.play(-1)  # Reproduce la música en loop infinito (-1)

    screen = pygame.display.set_mode((1024, 768))  # Crea la ventana del juego con resolución 1024x768
    pygame.display.set_caption("Eco Dash")  # Título de la ventana

    # Cargar efecto de sonido para los clics
    click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    click_sound.set_volume(0.5)  # volumen del clic

    pantalla_actual = Main(screen)  # comienza en la pantalla main, la inicial

    while True:
        resultado = pantalla_actual.run()  # Se ejecuta la pantalla actual

        # Lógica de navegación entre pantallas
        if resultado == "select_character":
            pantalla_actual = Select_character(screen)  # Ir a la pantalla de selección de personaje

        elif resultado == "configuracion":
            pantalla_actual = Configuracion(screen)

        elif resultado == "main":
            pantalla_actual = Main(screen)  # Volver al menú principal

        elif resultado == "seleccion_dificultad":
            pantalla_actual = Seleccion_dificultad(screen)  # Ir a la pantalla de selección de dificultad

        elif resultado in ["facil"]:  # Si se elige la dificultad fácil, por ahora la unica disponible
            pantalla_actual = Seleccion_nivel(screen)  # Pasar a la selección de nivel

        elif resultado  == "nivel1":
            # Manejar el nivel 1 con posibilidad de reintento
            reiniciar_nivel = True
            while reiniciar_nivel:
                resultado_nivel = run_level1()  # Ejecuta el nivel y espera un resultado

                if resultado_nivel == "main":
                    # Si el se quiere volver al menú principal
                    pygame.mixer.music.stop()  # Se detiene la música del nivel
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")  # Se carga la música del menú
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False  # Sale del bucle del nivel

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True  # Se reinicia el nivel

                else:
                    # Si no se especifica nada, regresa al menú por defecto
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False

        elif resultado  == "nivel2":
            # Manejar el nivel 1 con posibilidad de reintento
            reiniciar_nivel = True
            while reiniciar_nivel:
                resultado_nivel = run_level2()  # Ejecuta el nivel y espera un resultado

                if resultado_nivel == "main":
                    # Si el se quiere volver al menú principal
                    pygame.mixer.music.stop()  # Se detiene la música del nivel
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")  # Se carga la música del menú
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False  # Sale del bucle del nivel

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True  # Se reinicia el nivel
        elif resultado == "salir" or resultado is None:
            break  # Sale del juego si se elige "salir" o si no hay respuesta válida

    pygame.quit()  # Cierra pygame y finaliza el programa


if __name__ == "__main__":
    main()  # Ejecuta la función principal si este archivo es el que se está ejecutando directamente
