import pygame

# Importamos todas las pantallas
from proyecto import Main        
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel

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
            pantalla_actual = main()

        elif resultado == "seleccion_dificultad":
            pantalla_actual = Seleccion_dificultad(screen)

        elif resultado in ["facil", "medio", "dificil"]:  # Ajusta según lo que devuelva
            pantalla_actual = Seleccion_nivel(screen)

        elif resultado in ["nivel1", "nivel2", "nivel3"]:
            print(f"✅ ¡Iniciar lógica del {resultado} aquí!")
            # Aquí puedes iniciar tu juego real o cargar el nivel

        elif resultado == "salir" or resultado is None:
            break  # Salimos del juego

    pygame.quit()


if __name__ == "__main__":
    main()
