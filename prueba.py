import pygame
from nivel_1 import run_level1

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Menú principal")
font = pygame.font.Font(None, 40)

boton_rect = pygame.Rect(300, 250, 200, 60)

running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(event.pos):
                run_level1()  # << Aquí se abre el nivel 1

    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (0, 150, 0), boton_rect)
    texto = font.render("Nivel 1", True, (255, 255, 255))
    screen.blit(texto, (boton_rect.x + 40, boton_rect.y + 15))
    
    pygame.display.flip()

pygame.quit()
