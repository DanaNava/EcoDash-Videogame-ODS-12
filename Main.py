import pygame

# Importamos todas las pantallas
from proyecto import Main        
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel
from nivel_1 import run_level1

def main():
    pygame.init()
    pygame.mixer.init()

    # Cargar música de fondo
    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
    pygame.mixer.music.set_volume(0.5)  # 0.0 a 1.0
    pygame.mixer.music.play(-1)  # -1 = loop infinito

    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Mi Juego")

    # Cargar sonidos
    click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    click_sound.set_volume(0.5)  # Ajusta el volumen (0.0 a 1.0)

    pantalla_actual = Main(screen)  # Primera pantalla

    while True:
        resultado = pantalla_actual.run()  # Esperamos respuesta

        # 🔁 Lógica de navegación según la respuesta
        if resultado == "select_character":
            pantalla_actual = Select_character(screen)

        elif resultado == "main":
            pantalla_actual = Main(screen)

        elif resultado == "seleccion_dificultad":
            pantalla_actual = Seleccion_dificultad(screen)

        elif resultado in ["facil"]:  # Ajusta según lo que devuelva
            pantalla_actual = Seleccion_nivel(screen)

        elif resultado in ["nivel1"]:
           # Manejar el nivel 1 con reintentos
            reiniciar_nivel = True
            while reiniciar_nivel:
                resultado_nivel = run_level1()
                if resultado_nivel == "main":
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False  # Salir del bucle, volver al menú

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True  # Continuar en el bucle (reiniciar nivel)
                else:
                    # Por defecto volver al menú con su música
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(0.5)
                    pygame.mixer.music.play(-1)
                    pantalla_actual = Main(screen)
                    reiniciar_nivel = False  # Por defecto volver al menú

        elif resultado == "salir" or resultado is None:
            break  # Salimos del juego

    pygame.quit()


if __name__ == "__main__":
    main()
