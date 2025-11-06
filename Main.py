import pygame

# Importamos todas las pantallas necesarias para la navegación del juego
from proyecto import Main
from configuracion import Configuracion
from select_character import Select_character
from seleccion_dificultad import Seleccion_dificultad
from seleccion_nivel import Seleccion_nivel
from nivel_1 import run_level1
from creditos import Creditos  # <-- 1. IMPORTACIÓN AÑADIDA

def main():
    pygame.init()   # Inicializa todos los módulos de pygame
    pygame.mixer.init()   # Inicializa el sistema de sonido de pygame

    # Cargar música de fondo del menú principal
    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
    
    # --- AÑADIDO: Variable de estado para el volumen ---
    volumen_juego = 0.5
    
    pygame.mixer.music.set_volume(volumen_juego)   # Ajusta el volumen de la música (0.0 a 1.0)
    pygame.mixer.music.play(-1)   # Reproduce la música en loop infinito (-1)

    screen = pygame.display.set_mode((1024, 768))   # Crea la ventana del juego con resolución 1024x768
    pygame.display.set_caption("Eco Dash")   # Título de la ventana

    # --- AÑADIDO: Variable de estado para el idioma ---
    idioma_juego = "es"

    # Cargar efecto de sonido para los clics
    click_sound = pygame.mixer.Sound("assets_PI/sonidos/sonido_click.wav")
    click_sound.set_volume(0.5)   # volumen del clic

    # --- MODIFICADO: Pasar el idioma y volumen a la pantalla inicial ---
    pantalla_actual = Main(screen, idioma_juego, volumen_juego)   # comienza en la pantalla main, la inicial
    
    # --- AÑADIDO: Variable 'running' para controlar el bucle principal ---
    running = True

    while running: # <-- MODIFICADO
        # La pantalla actual (que ya tiene el idioma) se ejecuta
        resultado = pantalla_actual.run()

        # Lógica de navegación entre pantallas
        if resultado == "select_character":
            # --- MODIFICADO: Pasar el idioma y volumen ---
            pantalla_actual = Select_character(screen, idioma_juego, volumen_juego)   # Ir a la pantalla de selección de personaje

        elif resultado == "configuracion":
            # --- Ir al menú de configuración ---
            pygame.mixer.music.pause()   # Pausa la música del menú principal
            
            # --- MODIFICADO: Pasar el idioma y volumen actual ---
            pantalla_actual = Configuracion(screen, idioma_juego, volumen_juego)
            
            # --- MODIFICADO: Recibir TRES valores de vuelta ---
            resultado_config, nuevo_idioma, nuevo_volumen = pantalla_actual.run()   # Ejecutar pantalla de configuración
            
            # --- AÑADIDO: Actualizar las variables globales ---
            idioma_juego = nuevo_idioma
            volumen_juego = nuevo_volumen # <-- ACTUALIZA EL VOLUMEN
            
            # Actualiza el volumen de la música principal por si cambió
            pygame.mixer.music.set_volume(volumen_juego) 
            
            pygame.mixer.music.unpause()   # Reanuda la música al volver
            
            if resultado_config == "main":
                # --- MODIFICADO: Pasar el idioma y volumen actualizado ---
                pantalla_actual = Main(screen, idioma_juego, volumen_juego)
            elif resultado_config == "salir":
                running = False # <-- MODIFICADO: Termina el bucle principal
                break   # Si se elige salir desde configuración
        
        # --- 2. BLOQUE ELIF AÑADIDO ---
        elif resultado == "creditos":
            pantalla_actual = Creditos(screen, idioma_juego, volumen_juego)
        # --- FIN DE LA MODIFICACIÓN ---

        elif resultado == "main":
            # --- MODIFICADO: Pasar el idioma y volumen ---
            pantalla_actual = Main(screen, idioma_juego, volumen_juego)   # Volver al menú principal

        elif resultado == "seleccion_dificultad":
            # --- MODIFICADO: Pasar el idioma y volumen ---
            pantalla_actual = Seleccion_dificultad(screen, idioma_juego, volumen_juego)   # Ir a la pantalla de selección de dificultad

        elif resultado in ["facil"]:   # Si se elige la dificultad fácil, por ahora la unica disponible
            # --- MODIFICADO: Pasar el idioma y volumen ---
            pantalla_actual = Seleccion_nivel(screen, idioma_juego, volumen_juego)   # Pasar a la selección de nivel

        elif resultado in ["nivel1"]:
            # Manejar el nivel 1 con posibilidad de reintento
            reiniciar_nivel = True
            while reiniciar_nivel:
                
                # --- ¡MODIFICADO AQUÍ! ---
                # Ahora pasamos el idioma y el volumen al nivel
                resultado_nivel = run_level1(idioma_juego, volumen_juego)   # Ejecuta el nivel y espera un resultado
                # --- FIN DE LA MODIFICACIÓN ---

                if resultado_nivel == "main":
                    # Si el se quiere volver al menú principal
                    pygame.mixer.music.stop()   # Se detiene la música del nivel
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")   # Se carga la música del menú
                    pygame.mixer.music.set_volume(volumen_juego) # <-- Usa el volumen guardado
                    pygame.mixer.music.play(-1)
                    # --- MODIFICADO: Pasar el idioma y volumen ---
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False   # Sale del bucle del nivel

                elif resultado_nivel == "reintentar":
                    reiniciar_nivel = True   # Se reinicia el nivel
                
                # --- AÑADIDO: Manejar el "salir" del nivel 1 ---
                elif resultado_nivel == "salir":
                    running = False # Le dice al bucle principal que se pare
                    reiniciar_nivel = False # Le dice al bucle del nivel que se pare
                # --- FIN AÑADIDO ---

                else:
                    # Si no se especifica nada, regresa al menú por defecto
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets_PI/musica/musica_main.wav")
                    pygame.mixer.music.set_volume(volumen_juego) # <-- Usa el volumen guardado
                    pygame.mixer.music.play(-1)
                    # --- MODIFICADO: Pasar el idioma y volumen ---
                    pantalla_actual = Main(screen, idioma_juego, volumen_juego)
                    reiniciar_nivel = False
            
            # --- AÑADIDO: Si el bucle de nivel se rompió por "salir", rompemos el principal ---
            if not running:
                break

        elif resultado == "salir" or resultado is None:
            running = False # <-- MODIFICADO
            break   # Sale del juego si se elige "salir" o si no hay respuesta válida

    pygame.quit()   # Cierra pygame y finaliza el programa


if __name__ == "__main__":
    main()   # Ejecuta la función principal si este archivo es el que se está ejecutando directamente