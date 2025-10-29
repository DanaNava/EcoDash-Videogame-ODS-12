import pygame
import sys
import random



def run_level2():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Nivel 2")

    # -----------------------------
    # CARGA DE IMÁGENES
    #nombre = pygame.image.load("").convert_alpha()
    # -----------------------------
    fondo = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondo_nivel2.png").convert_alpha()
    #arboles
    capa_arbol1 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arbolesqiz1.png").convert_alpha()
    capa_arbol2 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arbolesqiz2.png").convert_alpha()
    capa_arbol3 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb3.png").convert_alpha()
    capa_arbol4 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb4.png").convert_alpha()
    capa_arbol5 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb5.png").convert_alpha()
    capa_arbol6 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb6.png").convert_alpha()
    capa_arbol7 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb7.png").convert_alpha()
    capa_arbol8 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb8.png").convert_alpha()
    capa_arbol9 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb9.png").convert_alpha()
    capa_arbol10 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb10.png").convert_alpha()
    capa_arbol11 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb11.png").convert_alpha()
    capa_arbol12 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb12.png").convert_alpha()
    capa_arbol12_1 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb12_1.png").convert_alpha()
    capa_arbol13 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb13.png").convert_alpha()
    capa_error1_arbol = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/err1.png").convert_alpha()
    capa_error2_arbol = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/err2.png").convert_alpha()
    capa_error3_arbol = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/err3.png").convert_alpha()
    capa_arbol14 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb14.png").convert_alpha()
    capa_arbol15 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb15.png").convert_alpha()
    capa_arbol16 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb16.png").convert_alpha()
    capa_arbol17 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb17.png").convert_alpha()
    capa_arbol18 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb18.png").convert_alpha()
    capa_arbol19 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb19.png").convert_alpha()
    capa_arbol20 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb20.png").convert_alpha()
    capa_arbol21 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb21.png").convert_alpha()
    capa_arbol22 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb22.png").convert_alpha()
    capa_arbol23 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb23.png").convert_alpha()
    capa_arbol24 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb24.png").convert_alpha()
    capa_arbol25 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb25.png").convert_alpha()
    capa_arbol26 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb26.png").convert_alpha()
    capa_arbol27 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb27.png").convert_alpha()
    capa_arbol28 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb28.png").convert_alpha()
    capa_arbol29 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb29.png").convert_alpha()
    capa_arbol30 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb30.png").convert_alpha()
    capa_arbol31 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb31.png").convert_alpha()
    capa_arbol32 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb32.png").convert_alpha()
    capa_arbol33 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb33.png").convert_alpha()
    capa_arbol34 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb34.png").convert_alpha()
    capa_arbol35 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb35.png").convert_alpha()
    capa_arbol36 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb36.png").convert_alpha()
    capa_arbol37 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb37.png").convert_alpha()
    capa_arbol38 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb38.png").convert_alpha()
    capa_arbol39 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb39.png").convert_alpha()
    capa_arbol40 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb40.png").convert_alpha()
    capa_arbol41 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb41.png").convert_alpha()
    capa_arbol42 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb42.png").convert_alpha()
    capa_arbol43 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb43.png").convert_alpha()
    capa_arbol44 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb44.png").convert_alpha()
    capa_arbol45 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb45.png").convert_alpha()
    capa_arbol46 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb46.png").convert_alpha()
    capa_arbol47 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb47.png").convert_alpha()
    capa_arbol48 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb48.png").convert_alpha()
    capa_arbol49 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb49.png").convert_alpha()
    capa_arbol50 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb50.png").convert_alpha()
    capa_arbol51 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb51.png").convert_alpha()
    capa_arbol52 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb52.png").convert_alpha()
    capa_arbol53 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb53.png").convert_alpha()
    capa_arbol54 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb54.png").convert_alpha()
    capa_arbol55 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb55.png").convert_alpha()
    capa_arbol56 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb56.png").convert_alpha()
    capa_arbol57 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb57.png").convert_alpha()
    capa_arbol58 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb58.png").convert_alpha()
    capa_arbol59 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb59.png").convert_alpha()
    capa_arbol60 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb60.png").convert_alpha()
    capa_arbol61 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb61.png").convert_alpha()
    capa_arbol62 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb62.png").convert_alpha()
    capa_arbol63 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb63.png").convert_alpha()
    capa_arbol64 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb64.png").convert_alpha()
    capa_arbol65 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb65.png").convert_alpha()
    capa_arbol66 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb66.png").convert_alpha()
    capa_arbol67 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/fondos/arb67.png").convert_alpha()
   

        



    #lampara
    capa_lampara1 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara1.png").convert_alpha()
    capa_lampara2 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara2.png").convert_alpha()
    capa_lampara3 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara3.png").convert_alpha()
    capa_lampara4 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara4.png").convert_alpha()
    capa_lampara5 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara5.png").convert_alpha()
    capa_lampara6 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara6.png").convert_alpha()
    capa_lampara7 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara7.png").convert_alpha()
    capa_lampara8 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara8.png").convert_alpha()
    capa_lampara9 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara9.png").convert_alpha()
    capa_lampara10 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara10.png").convert_alpha()
    capa_lampara11 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara11.png").convert_alpha()
    capa_lampara12 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara12.png").convert_alpha()
    capa_lampara13 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara13.png").convert_alpha()
    capa_lampara14 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara14.png").convert_alpha()
    capa_lampara15 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara15.png").convert_alpha()
    capa_lampara16 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/lampara/lampara16.png").convert_alpha()

    #columpio
    capa_colum1 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/columpio/colu1.png").convert_alpha()
    capa_colum2 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/columpio/colu2.png").convert_alpha()
    capa_colum4 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/columpio/colu4.png").convert_alpha()
    capa_colum5 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/columpio/colu5.png").convert_alpha()
    capa_colum6 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/columpio/colu6.png").convert_alpha()

    #detalles menores
    cosa_1 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa1.png").convert_alpha()
    cosa_2 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa2.png").convert_alpha()
    cosa_3 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa3.png").convert_alpha()
    cosa_4 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa4.png").convert_alpha()
    cosa_5 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa5.png").convert_alpha()
    cosa_6 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa6.png").convert_alpha()
    cosa_7 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa7.png").convert_alpha()
    cosa_8 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa8.png").convert_alpha()
    cosa_9 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa9.png").convert_alpha()
    cosa_10 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa10.png").convert_alpha()
    cosa_11 = pygame.image.load("assets_PI/diseyo_nivel/nivel 2/detalles_menores/cosa11.png").convert_alpha()

   
    # Pantalla de victoria y barras de vida
    w = pygame.image.load("assets_PI/interfaces/victoria/Pantalla_victoria.jpeg")
    bv = pygame.image.load("assets_PI/sprites/barra_vida_completa.png")
    bv2 = pygame.image.load("assets_PI/sprites/barra_vida_2co.png")
    bv1 = pygame.image.load("assets_PI/sprites/barra_vida_1co.png")

    # Posturas estáticas para quieto (como respaldo)
    quieto_derecha = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_derecha.png").convert_alpha()
    quieto_izquierda = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_izquierda.png").convert_alpha()
    quieto_detras = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_detras.png").convert_alpha()
    quieto_delante = pygame.image.load("assets_PI/personajes/masculino/posturas/PI_personaje_m_ver_delante.png").convert_alpha()

    #Escalar imagenes
    win = pygame.transform.scale(w, (1024, 768))
    barra_vida = pygame.transform.scale(bv, (150, 118))
    barra_vida2 = pygame.transform.scale(bv2, (150, 118))
    barra_vida1 = pygame.transform.scale(bv1, (150, 118))

    #Cargar botones
    boton_reintentar = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez.png").convert_alpha()
    boton_reintentar_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_intenta_otra_vez_hover.png").convert_alpha()
    boton_menu = pygame.image.load("assets_PI/interfaces/perdida/boton_menu.png").convert_alpha()
    boton_menu_hover = pygame.image.load("assets_PI/interfaces/perdida/boton_menu_hover.png").convert_alpha()

    boton_win_menu_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_hover_pantalla_victoria.png")
    boton_win_menu = pygame.image.load("assets_PI/interfaces/victoria/boton_menu_pantalla_victoria.png")
    boton_win_intentar = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria.png")
    boton_win_intentar_hover = pygame.image.load("assets_PI/interfaces/victoria/boton_intenta_otra_vez_victoria_hover.png")

    rect_reintentar_victoria = boton_win_menu.get_rect(center=(515, 487))
    rect_menu_victoria = boton_win_intentar.get_rect(center=(515, 570))

    rect_reintentar = boton_reintentar.get_rect(center=(515, 467))
    rect_menu = boton_menu.get_rect(center=(515, 550))

    # Personaje inicial
    personaje = quieto_delante
    personaje_draw_rect = personaje.get_rect(center=(489, 420))
    hitbox = pygame.Rect(0, 0, 70, 70)
    hitbox.center = personaje_draw_rect.center

    # -----------------------------
    # CARGA musica de fondo
    # -----------------------------
    pygame.mixer.music.load("assets_PI/musica/musica_nivel.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # -----------------------------
    # CARGA efectos de sonido
    # -----------------------------
    sonido_caminar = pygame.mixer.Sound("assets_PI/sonidos/pasos_madera.wav")
    sonido_dano = pygame.mixer.Sound("assets_PI/sonidos/recibir_daño.wav")
    sonido_morir = pygame.mixer.Sound("assets_PI/sonidos/morir.wav")
    sonido_recoger = pygame.mixer.Sound("assets_PI/sonidos/recoger_basura.wav")
    sonido_tirar_correcto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_bien.wav")
    sonido_tirar_incorrecto = pygame.mixer.Sound("assets_PI/sonidos/tirar_basura_sonido_error.wav")

    # Volúmenes
    sonido_caminar.set_volume(1)
    sonido_dano.set_volume(0.5)
    sonido_morir.set_volume(1)
    sonido_recoger.set_volume(0.4)
    sonido_tirar_correcto.set_volume(0.5)
    sonido_tirar_incorrecto.set_volume(1)

     # -----------------------------
    # BASURA CON ANIMACIONES
    # -----------------------------
    # Cargar frames de animación para cada basura
    # Botella de agua
    frames_botella_agua = [
        pygame.image.load("assets_PI/basura/inorganica/botella_agua/botella agua1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/botella_agua/botella agua2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/botella_agua/botella agua3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/botella_agua/botella agua4.png").convert_alpha()
    ]
    
    # Lata
    frames_lata = [
        pygame.image.load("assets_PI/basura/inorganica/lata/lata1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/lata/lata2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/lata/lata3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/lata/lata4.png").convert_alpha()
    ]
    
    # Periódico
    frames_periodico = [
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/inorganica/periodico/periodico_mas_grande4.png").convert_alpha()
    ]
    
    # Banana
    frames_banana = [
        pygame.image.load("assets_PI/basura/organica/Banana/banano1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Banana/banano2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Banana/banano3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Banana/banano4.png").convert_alpha()
    ]
    
    # Cascara de huevo
    frames_cascara_huevo = [
        pygame.image.load("assets_PI/basura/organica/Cascara_huevo/cascara_huevo_2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Cascara_huevo/cascara_huevo_3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Cascara_huevo/cascara_huevo_4.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Cascara_huevo/cascara_huevo_5.png").convert_alpha()
    ]
    
    # Manzana
    frames_manzana = [
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/organica/Manzana/manzene4.png").convert_alpha()
    ]
    
    # Batería
    frames_bateria = [
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Bateria/batería item -9c3f1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Bateria/batería item -9c3f2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Bateria/batería item -9c3f3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Bateria/batería item -9c3f4.png").convert_alpha()
    ]
    
    # Foco
    frames_foco = [
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a975.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a976.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a977.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Foco/Foquito item-a978.png").convert_alpha()
    ]
    
    # Jeringa
    frames_jeringa = [
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Jeringa/Jeringa1.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Jeringa/Jeringa2.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Jeringa/Jeringa3.png").convert_alpha(),
        pygame.image.load("assets_PI/basura/residuos_peligrosos/Jeringa/Jeringa4.png").convert_alpha()
    ]
    frames_surprice = [
        pygame.image.load("assets_PI/diseyo_nivel/nivel 2/surprice2.png").convert_alpha(),
        pygame.image.load("assets_PI/diseyo_nivel/nivel 2/surprice1.png").convert_alpha() 
    ]
    
    # -----------------------------
    # POSICIONES ALEATORIAS PARA BASURAS
    # -----------------------------
    # Lista de coordenadas posibles
    posiciones_basura = [
        (825, 621),  
        (552, 46),  
        (463, 681),  
        (961, 83),  
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

    # Definir basuras con animaciones
    basura = [
        {
            "frames": frames_banana, 
            "rect": frames_banana[0].get_rect(topleft=posiciones_aleatorias[0]), 
            "nombre": "un Plátano", 
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_botella_agua, 
            "rect": frames_botella_agua[0].get_rect(topleft=posiciones_aleatorias[1]), 
            "nombre": "una Botella de agua", 
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_foco, 
            "rect": frames_foco[0].get_rect(topleft=posiciones_aleatorias[2]), 
            "nombre": "un Foco", 
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_lata, 
            "rect": frames_lata[0].get_rect(topleft=posiciones_aleatorias[3]), 
            "nombre": "una Lata", 
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_manzana, 
            "rect": frames_manzana[0].get_rect(topleft=posiciones_aleatorias[4]), 
            "nombre": "una Manzana", 
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_bateria, 
            "rect": frames_bateria[0].get_rect(topleft=posiciones_aleatorias[5]), 
            "nombre": "una Batería", 
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_cascara_huevo, 
            "rect": frames_cascara_huevo[0].get_rect(topleft=posiciones_aleatorias[6]), 
            "nombre": "Cascaras de huevo", 
            "tipo": "organica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_jeringa, 
            "rect": frames_jeringa[0].get_rect(topleft=posiciones_aleatorias[7]), 
            "nombre": "una Jeringa", 
            "tipo": "peligrosa",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_periodico, 
            "rect": frames_periodico[0].get_rect(topleft=posiciones_aleatorias[8]), 
            "nombre": "un Periodico", 
            "tipo": "inorganica",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        },
        {
            "frames": frames_surprice, 
            "rect": frames_surprice[0].get_rect(topleft=(90, 572)),
            "nombre": "a Larry", 
            "tipo": "segura",
            "frame_actual": 0,
            "tiempo_ultimo_frame": 0,
            "animando": True
        }

        
        ]

    botes = [
        {"nombre": "al bote Inorganico", "tipo": "inorganica", "rect": pygame.Rect(386, 403, 53, 28)},
        {"nombre": "al bote Organico", "tipo": "organica", "rect": pygame.Rect(305, 411, 31, 8)},
        {"nombre": "al bote Residuos peligrosos", "tipo": "peligrosa", "rect": pygame.Rect(648, 710, 30, 36)},
        {"nombre": " al arbol", "tipo": "segura", "rect": pygame.Rect(24, 164, 48, 20)}

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
        pygame.Rect(837, 250, 11, 118), pygame.Rect(598, 376, 237, 4), pygame.Rect(208, 1, 630, 3), pygame.Rect(209, 30, 10, 332), 
        pygame.Rect(248, 385, 202, 7),
        #bancas no puestas 
        pygame.Rect(187, 234, 10, 87), pygame.Rect(615, 438, 11, 52), 
        #mesa para comer?
        pygame.Rect(702, 494, 18, 83), pygame.Rect(737, 529, 86, 10), pygame.Rect(850, 495, 12, 93), pygame.Rect(758, 456, 50, 25),
        #arboles y arbustos
        pygame.Rect(22, 83, 107, 60), pygame.Rect(88, 640, 45, 49), pygame.Rect(864, 236, 19, 125),
        #lampara
        pygame.Rect(415, 699, 7, 8),
        #juegos de los niños
        pygame.Rect(604, 268, 151, 26), pygame.Rect(271, 271, 154, 15), pygame.Rect(246, 137, 9, 19), pygame.Rect(489, 138, 11, 17), pygame.Rect(710, 36, 90, 47),
        #bote peligro
        pygame.Rect(648, 710, 30, 36),
        #bote inorganico
        pygame.Rect(404, 410, 21, 9),
        #bote organico
        pygame.Rect(309, 409, 22, 9),
        #detalles
        pygame.Rect(146, 47, 61, 8), pygame.Rect(974, 669, 48, 11)

    ]

    # -----------------------------
    # ANIMACIONES
    # -----------------------------
    frames_dano = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_daño_derecha/Pi_personaje_m_daño_derecha2.png").convert_alpha()
    ]

    # ANIMACIONES DE MUERTE POR DIRECCIÓN
    frames_muerte_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte/Pi_personaje_m_muerte5.png").convert_alpha()
    ]

    frames_muerte_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_muerte_izquierda/Pi_personaje_m_muerte_izquierda5.png").convert_alpha()
    ]

    # Para delante y detrás, usar las mismas que derecha
    frames_muerte_delante = frames_muerte_derecha
    frames_muerte_detras = frames_muerte_derecha

    frames_caminar_delante = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_caminar_delante/PI_personaje_m_caminar_delante6.png").convert_alpha()
    ]

    frames_caminar_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_derecha/Pi_personaje_m_caminar_derecha6.png").convert_alpha()
    ]

    frames_caminar_detras = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_detras/Pi_personaje_m_caminar_detras6.png").convert_alpha()
    ]

    frames_caminar_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_m_caminar_izquierda/Pi_personaje_m_caminar_izquierda6.png").convert_alpha()
    ]

    # ANIMACIONES DE QUIETO
    frames_quieto_detras = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/PI_personaje_m_animacion_quieto_detras/PI_personaje_m_animacion_quieto_detras9.png").convert_alpha()
    ]

    frames_quieto_derecha = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_derecha/Pi_personaje_animacion_quieto_derecha9.png").convert_alpha()
    ]

    frames_quieto_izquierda = [
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda1.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda2.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda3.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda4.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda5.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda6.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda7.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda8.png").convert_alpha(),
        pygame.image.load("assets_PI/personajes/masculino/animaciones/Pi_personaje_animacion_quieto_izquierda/Pi_personaje_animacion_quieto_izquierda9.png").convert_alpha()
    ]

    # Para delante postura estática
    frames_quieto_delante = [quieto_delante]

    pantalla_perdida = pygame.image.load("assets_PI/interfaces/perdida/game over 2.0.png").convert_alpha()

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

    # -----------------------------
    # VARIABLES
    # -----------------------------
    
    # Mostrar mensajes
    objeto_en_mano = None
    mensaje = ""
    mensaje_tiempo = 0
    duracion_mensaje = 3000  # Aumentar a 3 segundos
    fuente = pygame.font.Font(None, 32)  # Fuente más pequeña
    
    # velocidad del juego y personaje
    velocidad = 5
    clock = pygame.time.Clock()
    
    # Barra de vida 
    vida_max = 3
    vida_actual = vida_max

    # Tiempo
    tiempo = 180
    inicio_tiempo = pygame.time.get_ticks()
    fuente_tiempo = pygame.font.Font(None, 48)

    # Variable indicadora para cambiar la musica
    musica_cambiada = False

   # Verificar si gano
    def ganar(basura, objeto_en_mano):
        
        # 1. Crea una lista de la 'basura esencial' que debe ser recogida.
        #    Excluye explícitamente el objeto "a Larry" (la sorpresa).
        basura_esencial_restante = [
            obj for obj in basura if obj["nombre"] != "a Larry"
        ]
        
        # 2. Verifica si el objeto en la mano NO es la basura esencial.
        #    El jugador PUEDE tener el objeto "a Larry" en la mano al ganar.
        objeto_en_mano_esencial = (
            objeto_en_mano is not None and 
            objeto_en_mano["nombre"] != "a Larry"
        )
        
        # 3. La condición de victoria es:
        #    - La lista de basura esencial en el suelo debe estar vacía.
        #    - Y el jugador no debe tener otra basura esencial en la mano.
        return len(basura_esencial_restante) == 0 and not objeto_en_mano_esencial

    # Variable para el while infinito, para las teclas pulsadas y un contador de errores
    running = True
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

        keys = pygame.key.get_pressed()
        old_hitbox = hitbox.copy()

       # CORRECCIÓN: Bloquear completamente el movimiento durante la muerte
        if not animando_muerte and not tiempo_fin_animacion:
            moving = False
            # Movimiento
            if not animando_dano:
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    hitbox.x -= velocidad
                    animacion_correr_izquierda = True
                    animacion_correr_derecha = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "izquierda"
                    # Reiniciar frame de quieto cuando empieza a moverse
                    frame_actual_quieto_izquierda = 0
                elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    hitbox.x += velocidad
                    animacion_correr_derecha = True
                    animacion_correr_izquierda = False
                    animacion_correr_delante = False
                    animacion_correr_detras = False
                    moving = True
                    ultima_direccion = "derecha"
                    frame_actual_quieto_derecha = 0
                elif keys[pygame.K_UP] or keys[pygame.K_w]:
                    hitbox.y -= velocidad
                    animacion_correr_detras = True
                    animacion_correr_delante = False
                    animacion_correr_izquierda = False
                    animacion_correr_derecha = False
                    moving = True
                    ultima_direccion = "detras"
                    frame_actual_quieto_detras = 0
                elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
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

            # Edge detection
            pressed_o = keys[pygame.K_o] and not prev_keys[pygame.K_o]
            pressed_p = keys[pygame.K_p] and not prev_keys[pygame.K_p]
            pressed_z = keys[pygame.K_z] and not prev_keys[pygame.K_z]
            pressed_x = keys[pygame.K_x] and not prev_keys[pygame.K_x]

            # Recoger objetos
            if pressed_o or pressed_z:
                for obj in basura[:]:
                    if hitbox.inflate(12, 12).colliderect(obj["rect"]):
                        if objeto_en_mano is None:
                            sonido_recoger.play()
                            # Detener animación y usar solo el primer frame
                            obj["animando"] = False
                            objeto_en_mano = {
                                "imagen": obj["frames"][0],  # Usar solo el primer frame
                                "nombre": obj["nombre"],
                                "tipo": obj["tipo"]
                            }
                            basura.remove(obj)
                            mensaje = f"Recogiste {obj['nombre']}"
                        else:
                            mensaje = "Ya tienes un objeto en la mano"
                        mensaje_tiempo = pygame.time.get_ticks()
                        break

            # Tirar basura - VERSIÓN CORREGIDA
            if pressed_p or pressed_x:
                if objeto_en_mano is None:
                    mensaje = "No tienes ningún objeto en la mano"
                    mensaje_tiempo = pygame.time.get_ticks()
                else:
                    proximity = hitbox.inflate(24, 24)
                    tiro_valido = False
                    bote_correcto_encontrado = False
                    bote_actual = None

                    # PRIMERO: Encontrar qué bote está cerca
                    for bote in botes:
                        if proximity.colliderect(bote["rect"]):
                            tiro_valido = True
                            bote_actual = bote  # Guardar referencia al bote cercano
                            break  # Solo nos interesa el bote más cercano

                    # SEGUNDO: Procesar el tiro solo si hay un bote cercano
                    if tiro_valido and bote_actual:
                        # Verificar si es el bote CORRECTO para este objeto
                        if objeto_en_mano["tipo"] == bote_actual["tipo"]:
                            # Tiro CORRECTO
                            bote_correcto_encontrado = True
                            mensaje = f"✓ llevaste {objeto_en_mano['nombre']}{bote_actual['nombre']}"
                            objeto_en_mano = None
                            sonido_tirar_correcto.play()
                        else:
                            # Tiro INCORRECTO - NO tirar pero recibir daño
                            errores += 1
                            mensaje = f"✗ No puedes tirar {objeto_en_mano['nombre']} en {bote_actual['nombre']}"
                            animando_dano = True
                            frame_actual_dano = 0
                            tiempo_frame = pygame.time.get_ticks()
                            # IMPORTANTE: NO liberar el objeto - el jugador lo mantiene en la mano
                            sonido_tirar_incorrecto.play()
                
                            # BARRA DE VIDA
                            vida_actual -= 1
                            if vida_actual < 0:
                                vida_actual = 0

                        mensaje_tiempo = pygame.time.get_ticks()
                    else:
                        # No hay bote cercano
                        mensaje = "No hay un bote cerca"
                        mensaje_tiempo = pygame.time.get_ticks()

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
        else:
            # Dibujar personaje normal
            screen.blit(frame, personaje_draw_rect)

        # DIBUJAR OBJETO EN LA MANO
        if objeto_en_mano is not None and not animando_muerte:
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
        screen.blit(cosa_1, (615, 232))
        screen.blit(cosa_2, (613, 239))
        screen.blit(cosa_3, (611, 242))
        screen.blit(cosa_4, (614, 247))
        screen.blit(cosa_5, (614, 248))
        screen.blit(cosa_6, (610, 249))
        screen.blit(cosa_7, (608, 251))
        screen.blit(cosa_8, (610, 257))
        screen.blit(cosa_9, (610, 257))
        screen.blit(cosa_10, (632, 260))
        screen.blit(cosa_11, (603, 260))


   
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

        # [Nuevo] TIEMPO
        tiempo_actual = pygame.time.get_ticks()
        segundos = (tiempo_actual - inicio_tiempo) // 1000
        tiempo_restante = max(0, tiempo - segundos)

        if tiempo_restante <= 30 and not musica_cambiada:
            pygame.mixer.music.load("assets_PI/musica/musica_apresurada.ogg")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            musica_cambiada = True

        color_tiempo = (255, 0, 0) if tiempo_restante <= 30 else (255, 255, 255)

        # Convertir a minutos y segundos
        minutos = tiempo_restante // 60
        segundos_restantes = tiempo_restante % 60

        # Formato mm:ss con ceros (01:05)
        tiempo_formateado = f"{minutos:02}:{segundos_restantes:02}"

        pygame.draw.rect(screen, (0, 0, 0), (20, 90, 100, 50))
        texto_tiempo = fuente_tiempo.render(f" {tiempo_formateado}", True, color_tiempo)
        screen.blit(texto_tiempo, (20, 90))

        def mostrar_pantalla_perdida():
            pygame.mixer.music.load("assets_PI/sonidos/musica de perdida.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
            sonido_morir.play()

            while True:
                screen.fill((0, 0, 0))
                screen.blit(pantalla_perdida, (0, 0))

                mouse_pos = pygame.mouse.get_pos()

                # Botones
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_reintentar_hover, rect_reintentar)
                else:
                    screen.blit(boton_reintentar, rect_reintentar)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_menu_hover, rect_menu)
                else:
                    screen.blit(boton_menu, rect_menu)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "reintentar"  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main"  # volver al menú

        def mostrar_pantalla_victoria():
            pygame.mixer.music.load("assets_PI\musica\musica_victoria.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

            while True:
                screen.fill((0, 0, 0))
                screen.blit(win, (0, 0))

                mouse_pos = pygame.mouse.get_pos()

                # Botones
                if rect_reintentar.collidepoint(mouse_pos):
                    screen.blit(boton_win_intentar, rect_reintentar_victoria)
                else:
                    screen.blit( boton_win_intentar_hover, rect_reintentar_victoria)

                if rect_menu.collidepoint(mouse_pos):
                    screen.blit(boton_win_menu, rect_menu_victoria)
                else:
                    screen.blit(boton_win_menu_hover, rect_menu_victoria)

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if rect_reintentar.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "reintentar"  # reiniciar nivel
                        elif rect_menu.collidepoint(mouse_pos):
                            pygame.mixer.music.stop()
                            return "main" # volver al menú
            
        #ganar
        if ganar(basura, objeto_en_mano):
            resultado = mostrar_pantalla_victoria()
            if resultado == "main":
                return "main"  # Volver al menú principal
            elif resultado == "reintentar":
                return "reintentar" # Reiniciar nivel
                

         
        # -----------------------------
        # ANIMACIÓN DE MUERTE CORREGIDA
        # -----------------------------
        if errores >= 3:
            if not animando_muerte and not tiempo_fin_animacion:
                animando_muerte = True
                frame_actual_muerte = 0
                tiempo_frame_muerte = pygame.time.get_ticks()
                tiempo_fin_animacion = None
                sonido_morir.play()
                # CORRECCIÓN: Detener sonido de caminar y otros sonidos
                sonido_caminar.stop()

            if animando_muerte:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_frame_muerte >= duracion_frame:
                    frame_actual_muerte += 1
                    tiempo_frame_muerte = ahora

                    if frame_actual_muerte >= 5:  # 5 frames de animación de muerte
                        animando_muerte = False
                        tiempo_fin_animacion = pygame.time.get_ticks()
                        frame_actual_muerte = 4  # Último frame

                # CORRECCIÓN: Seleccionar animación de muerte según la dirección
                if ultima_direccion == "izquierda":
                    frames_muerte = frames_muerte_izquierda
                else:
                    frames_muerte = frames_muerte_derecha  # Para derecha, delante y detrás

                screen.fill((0, 0, 0))
                screen.blit(fondo, (0, 0))
                frame_muerte = frames_muerte[frame_actual_muerte]
                rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                screen.blit(frame_muerte, rect_muerte)
                pygame.display.flip()
                clock.tick(60)

            elif tiempo_fin_animacion:
                ahora = pygame.time.get_ticks()
                if ahora - tiempo_fin_animacion >= 1500:
                    resultado = mostrar_pantalla_perdida()
                    if resultado == "main":
                        return "main"  # Volver al menú principal
                    elif resultado == "reintentar":
                        return "reintentar"  # Reiniciar nivel
        
                else:
                    # CORRECCIÓN: Mantener la última animación de muerte según dirección
                    if ultima_direccion == "izquierda":
                        frames_muerte = frames_muerte_izquierda
                    else:
                        frames_muerte = frames_muerte_derecha

                    screen.fill((0, 0, 0))
                    screen.blit(fondo, (0, 0))
                    frame_muerte = frames_muerte[-1]
                    rect_muerte = frame_muerte.get_rect(center=hitbox.center)
                    screen.blit(frame_muerte, rect_muerte)
                    pygame.display.flip()
                    clock.tick(60)
        
        muerte_por_tiempo = False
        # Perder si se acaba el tiempo
        if tiempo_restante <= 0 and not muerte_por_tiempo:
            muerte_por_tiempo = True
            errores = 3

        pygame.display.flip()
        clock.tick(60)
        prev_keys = keys
        
    pygame.quit()

if __name__ == "__main__":
    run_level2()