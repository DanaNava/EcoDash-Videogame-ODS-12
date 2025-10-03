# Importar pygame
import pygame
import sys

def run_level1():
     
    pygame.init()

    # Crear pantalla
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Trash Hunters')
    
    #Imagenes
    background = pygame.image.load("assets_PI/diseyo_nivel/nivel1/fondo_2.png")
    personaje = pygame.image.load("assets_PI\personajes\masculino\posturas\PI_personaje_m_ver_delante.png")
    capa_delante = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_fondo_2.png")
    capa_delante_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel1/puerta_izquierda_fondo.png")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")
    win = pygame.transform.scale(w, (1024, 768))

    platano = pygame.image.load("assets_PI/basura/organica/banano.png")
    agua = pygame.image.load("assets_PI/basura/inorganica/botella agua.png")
    foco = pygame.image.load("assets_PI/basura/residuos_peligrosos/Foquito item-a975.png")
    lata = pygame.image.load("assets_PI/basura/inorganica/lata.png")
    manzana = pygame.image.load("assets_PI/basura/organica/manzene.png")
    bateria = pygame.image.load("assets_PI/basura/residuos_peligrosos/batería item -9c3f.png")
    
    # Inventario del personaje 
    inventario = []
    
    # Coordenadas de cada objeto
    basura = [
         {"nombre": "Plátano", "tipo": "organica", "imagen": platano, "rect": platano.get_rect(topleft=(200, 350))},
         {"nombre": "Agua", "tipo": "inorganica", "imagen": agua, "rect": agua.get_rect(topleft=(620, 400))},
         {"nombre": "Foco", "tipo": "peligrosa", "imagen": foco, "rect": foco.get_rect(topleft=(420, 640))},
         {"nombre": "Lata", "tipo": "inorganica", "imagen": lata, "rect": lata.get_rect(topleft=(920, 280))},
         {"nombre": "Manzana", "tipo": "organica", "imagen": manzana, "rect": manzana.get_rect(topleft=(360, 250))},
         {"nombre": "Batería", "tipo": "peligrosa", "imagen": bateria, "rect": bateria.get_rect(topleft=(50, 600))}
      ]
    
    # Velocidad del personaje
    velocidad = 5
    
    # Variable de la velocidad del juego
    clock = pygame.time.Clock()

    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo
    tiempo = 120
    inicio_tiempo = pygame.time.get_ticks()
    fuente_tiempo =pygame.font.Font(None, 48)

    # Verificar si gano
    def ganar(basura, objeto_en_mano):
        return len(basura) == 0 and objeto_en_mano is None
    
    # Hitbox del personajito
    personaje_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 50, 50)
    hitbox.center = personaje_rect.center
    
    # Objetos con los que el personaje hara colision
    colisiones = [
            pygame.Rect(9, 150, 14, 601), #pared izquierda
            pygame.Rect(10, 737, 1005, 17), #pared abajo
            pygame.Rect(1003, 11, 10, 734), #pared derecha
            pygame.Rect(690,17, 21, 450), #pared bodega izquierda
            pygame.Rect(261,15, 9, 250), #pared esquina izquierda
            pygame.Rect(26,146, 239, 140), #pared esquina arriba
            pygame.Rect(719,184, 66, 5), #cajas
            pygame.Rect(872,82, 122, 85), #estanteria
            pygame.Rect(708,336, 134, 120), #pared abajo bodega_1
            pygame.Rect(767,500, 43, 1), #perchero
            pygame.Rect(924,336, 79, 120), #pared abajo bodega_2
            pygame.Rect(400,58, 289, 73), #pared arriba sala
            pygame.Rect(421,219, 70, 71), #sofa rojo
            pygame.Rect(645,220, 43, 52), #mesa con tele
            pygame.Rect(950,577, 20, 26), #sofa zul
            pygame.Rect(178,530, 120, 20), #mesa redonda_arriba
            pygame.Rect(176,572, 120, 20), #mesa redonda_abajo
            pygame.Rect(217,451, 42, 60), #silla arriba
            pygame.Rect(127,545, 35, 1), #silla IZQUIERDA
            pygame.Rect(311,544, 35, 1), #silla derecha
            pygame.Rect(215,600, 42, 9), #silla abajo
            pygame.Rect(284,155, 20, 35), #bote azul
            pygame.Rect(341,156, 20, 35), #bote VERDE
            pygame.Rect(793,179, 20, 20), #bote rojo 
    ]
    
#declaramos los botes dentro de una lista
    botes = [
    {"nombre": "Azul", "tipo": "inorganica", "rect": pygame.Rect(284, 155, 20, 35)},
    {"nombre": "Verde", "tipo": "organica", "rect": pygame.Rect(341, 156, 20, 35)},
    {"nombre": "Rojo", "tipo": "peligrosa", "rect": pygame.Rect(793, 179, 20, 20)}
    ]
    
 # Animacion para daño
    frames_dano = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha2.png").convert_alpha()
    ]

    animando_dano = False
    frame_actual_dano = 0
    tiempo_frame_dano = 0
    duracion_frame = 100  # ms por frame (ajustable)

 # Variable que detecta nuevas pulsaciones
    prev_keys = pygame.key.get_pressed()

 # mensaje y variable bandera
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 2000
    fuente = pygame.font.Font(None, 36)

    # Bucle del juego
    while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    # Variable que guarda la ultima posicion del personaje
          old_hitbox = hitbox.copy()
          # Variable para detectar las teclas que se presionan
          teclas = pygame.key.get_pressed()
    
    # Movimiento del personajito con las teclas
          if teclas[pygame.K_LEFT]:
                hitbox.x -= velocidad
            
          if teclas[pygame.K_RIGHT]:
                hitbox.x += velocidad
    
          if teclas[pygame.K_UP]:
                hitbox.y -= velocidad
    
          if teclas[pygame.K_DOWN]:
                hitbox.y += velocidad
    
    # For que detecta colisiones
          for rect in colisiones:
               if hitbox.colliderect(rect):
                  hitbox.x = old_hitbox.x 
                  hitbox.y = old_hitbox.y                           
                  break
               
    # Hitbox centrado con el personaje
          personaje_rect.center = hitbox.center    

   # 3) Detectar pulsaciones nuevas (edge detection)
          pressed_e = teclas[pygame.K_e] and not prev_keys[pygame.K_e]
          pressed_q = teclas[pygame.K_q] and not prev_keys[pygame.K_q]
  
          # Recoger: solo si se pulsa E (una vez) y está cerca (inflate para comodidad)
          if pressed_e:
              for obj in basura[:]:
                  # usar un área un poco mayor para facilitar recogida
                  if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                      if objeto_en_mano is None:
                          objeto_en_mano = obj
                          basura.remove(obj)
                          mensaje = f"Recogiste: {obj['nombre']}"
                      else:
                          mensaje = "Ya tienes un objeto en la mano"
                      mensaje_tiempo = pygame.time.get_ticks()
                      print(mensaje)
                      break  # sólo 1 objeto por pulsación
  
          # Tirar: pulsa Q (una vez) y estar cerca de un bote (inflate para proximidad)
          # Tirar basura (tecla Q)
          if pressed_q:
              if objeto_en_mano is None:
                  mensaje = "No tienes ningún objeto en la mano"
                  mensaje_tiempo = pygame.time.get_ticks()
              else:
                  proximity = hitbox.inflate(24, 24)
                  tiro_valido = False  # Para saber si se detectó un bote cerca
  
                  for bote in botes:
                      if proximity.colliderect(bote["rect"]):
                          tiro_valido = True
                          if objeto_en_mano["tipo"] == bote["tipo"]:
                              mensaje = f"Tiraste {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                              objeto_en_mano = None
                          else:
                              mensaje = f"No puedes tirar {objeto_en_mano['nombre']} en bote {bote['nombre']}"
                              animando_dano = True
                              frame_actual_dano = 0
                              tiempo_frame_dano = pygame.time.get_ticks()
                              mensaje_tiempo = pygame.time.get_ticks()

                        # BARRA DE VIDA
                              vida_actual -= 1
                              if vida_actual < 0:
                                  vida_actual = 0
                              elif vida_actual == 2:
                                    vida_actual = 2
                              elif vida_actual == 1:
                                    vida_actual = 1
                          break
  
                  if not tiro_valido:
                      mensaje = "No hay un bote cerca"
                      mensaje_tiempo = pygame.time.get_ticks()       
                                             
    # Imagen de fondo a la pantalla
          screen.blit(background, (0, 0))

    # [Nuevo] BARRA DE VIDA ---------    
          if vida_actual == 3:
              screen.blit(barra_vida, (20, -20))
          elif vida_actual == 2:
              screen.blit(barra_vida2, (20, -20))
          elif vida_actual == 1:
              screen.blit(barra_vida1, (20, -20))         
    
    # Dibujar la basura en el mapa
          for obj in basura:
               screen.blit(obj["imagen"], obj["rect"].topleft)
            
    # Dibujar personaje
          screen.blit(personaje, personaje_rect)

    # [Nuevo] DIBUJAR OBJETO EN LA MANO -------------------
          if objeto_en_mano is not None:
             mano_x = personaje_rect.centerx + 20
             mano_y = personaje_rect.centery 
             screen.blit(objeto_en_mano["imagen"], (mano_x, mano_y))

    
    # Dibujar basura
          screen.blit(capa_delante, (709, 334))
          screen.blit(capa_delante_2, (814, 418))

    # Mensaje con fondo sólido para que no deje "sombra"
          if mensaje and pygame.time.get_ticks() - mensaje_tiempo < duracion_mensaje:
              mensaje_rect = pygame.Rect(12, 12, 500, 36)
              pygame.draw.rect(screen, (0, 0, 0), mensaje_rect)
              texto = fuente.render(mensaje, True, (255, 255, 255))
              screen.blit(texto, (20, 20))
          else:
              mensaje = ""
  
  
          if animando_dano:
              ahora = pygame.time.get_ticks()
              if ahora - tiempo_frame_dano >= duracion_frame:
                  frame_actual_dano += 1
                  tiempo_frame_dano = ahora
  
                  if frame_actual_dano >= len(frames_dano):
                      animando_dano = False
                      frame_actual_dano = 0
  
          if animando_dano:  # se sigue mostrando
               frame = frames_dano[frame_actual_dano]
               rect_dano = frame.get_rect(center=personaje_rect.center)
               screen.blit(frame, rect_dano)  
      
          for rect in colisiones:
              pygame.draw.rect(screen, (255, 0, 0), rect, 2)

      # Actualizar las teclas presionadas
          prev_keys = teclas

# [Nuevo] TIEMPO-----------
          tiempo_actual = pygame.time.get_ticks()
          segundos = (tiempo_actual - inicio_tiempo)  // 1000
          tiempo_restante = max(0, tiempo - segundos)

          pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
          texto_tiempo = fuente_tiempo.render(f" {tiempo_restante}", True, (255, 255, 255))
          screen.blit(texto_tiempo, (20, 90))

# Perder si se acaba el tiempo
          if tiempo_restante <= 0:
              mensaje = "Fondo de perder"
              screen.fill((0, 0, 0), (20, 90, 100, 50))
              texto = fuente_tiempo(f"{tiempo_restante}", True, (255, 255, 255))
              screen.blit(texto_tiempo, (20, 90))
            
          if ganar(basura, objeto_en_mano):
              screen.blit(win, (0,0))   

# Actualizar pantalla
          pygame.display.flip()

# Velocidad a la que va a correr el juego
          clock.tick(60) 
if __name__ == "__main__":
    run_level1()