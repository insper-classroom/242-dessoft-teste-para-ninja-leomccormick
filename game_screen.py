from config import QUIT, WIDTH, HEIGHT, FPS, GAME, WHITE, RED, GREEN, BLUE, GRAY, BLACK, barra_rect
import pygame
from gerador import gera_numeros

def game_screen(window):
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 40)

    # Define os quadrados
    sqr_width = 100
    sqr_height = 100
    sqr_x = (WIDTH - sqr_width) // 2

    sqr_y_1 = HEIGHT - 150
    sqr_y_2 = HEIGHT - 250
    sqr_y_3 = HEIGHT - 350

    sqr_1_rect = pygame.Rect(sqr_x, sqr_y_1, sqr_width, sqr_height)
    sqr_2_rect = pygame.Rect(sqr_x, sqr_y_2, sqr_width, sqr_height)
    sqr_3_rect = pygame.Rect(sqr_x, sqr_y_3, sqr_width, sqr_height)

    sqr_1 = True
    sqr_2 = True
    sqr_3 = True

    running = True
    while running:
        clock.tick(FPS)

        n1, n2, n_errado, soma = gera_numeros()

        n1, n2, n3, n4 = n1, n2, n_errado, soma

        # Escrevendo os números 
        text1 = font.render(str(n1), True,  BLACK)
        text1_rect = text1.get_rect()
        text1_rect.center = sqr_1_rect.center

        text2 = font.render(str(n2), True, BLACK)
        text2_rect = text2.get_rect()
        text2_rect.center = sqr_2_rect.center

        text3 = font.render(str(n3), True, BLACK)
        text3_rect = text3.get_rect()
        text3_rect.center = sqr_3_rect.center

        text_soma = font.render(str(n4), True, BLACK)
        text_soma_rect = text_soma.get_rect()
        text_soma_rect.center = (50, 50)

        window.fill(WHITE)  # Desenha o fundo
        pygame.draw.rect(window, GRAY, barra_rect)


        pygame.draw.rect(window, BLUE, sqr_1_rect)
        window.blit(text1, text1_rect)
        pygame.draw.rect(window, GREEN, sqr_2_rect)
        window.blit(text2, text2_rect)
        pygame.draw.rect(window, RED, sqr_3_rect)
        window.blit(text3, text3_rect)

        window.blit(text_soma, text_soma_rect)
        pygame.display.flip()  # Atualiza o display

        botoes = True
        while botoes:
            # Processa eventos (fechar janela, teclas)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = None
                    running = False
                    botoes = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if sqr_1_rect.collidepoint(event.pos):
                        print(n1)
                        sqr_1 = False
                        botoes = False
                    if sqr_2_rect.collidepoint(event.pos):
                        print(n2)
                        sqr_2 = False
                        botoes = False
                    if sqr_3_rect.collidepoint(event.pos):
                        print(n3)
                        sqr_3 = False
                        botoes = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        state = None
                        running = False
                        botoes = False

    return state