import pygame

# Importamos todas las pantallas
from prueba import Main        
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Mi Juego")

    pantalla_actual = Main(screen)  # Primera pantalla

    while True:
        resultado = pantalla_actual.run()  # Esperamos respuesta

        # 🔁 Lógica de navegación según la respuesta
        if resultado == "select_character":
            pantalla_actual = Select_character(screen)

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
