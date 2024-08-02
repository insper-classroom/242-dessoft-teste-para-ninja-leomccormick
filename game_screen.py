from config import QUIT, WIDTH, HEIGHT, FPS, GAME, WHITE, RED, GREEN, BLUE, GRAY, BLACK, barra_rect
import pygame
from gerador import gera_numeros

def game_screen(window):
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)

    # Define os quadrados
    sqr_width = 100
    sqr_height = 100
    sqr_x = (WIDTH - sqr_width) // 2

    sqr_1_y = HEIGHT - 150
    sqr_2_y = HEIGHT - 250
    sqr_3_y = HEIGHT - 350

    sqr_1_rect = pygame.Rect(sqr_x, sqr_1_y, sqr_width, sqr_height)
    sqr_2_rect = pygame.Rect(sqr_x, sqr_2_y, sqr_width, sqr_height)
    sqr_3_rect = pygame.Rect(sqr_x, sqr_3_y, sqr_width, sqr_height)

    n1, n2, n_errado, soma = gera_numeros()
    n1, n2, n3, n4 = n1, n2, n_errado, soma
    
    sqr_1 = True
    sqr_2 = True
    sqr_3 = True

    running = True
    while running:
        clock.tick(FPS)



        # Escrevendo os números 
        if sqr_1:
            text1 = font.render(str(n1), True,  BLACK)
            text1_rect = text1.get_rect()
            text1_rect.center = sqr_1_rect.center
        else:
            sqr_1 = True
            if n1 == n_errado:
                print("Certo!")
            else: 
                print("Errado!")
            n1, n2, n_errado, soma = gera_numeros()

        if sqr_2:
            text2 = font.render(str(n2), True, BLACK)
            text2_rect = text2.get_rect()
            text2_rect.center = sqr_2_rect.center
        else:
            sqr_2 = True
            if n2 == n_errado:
                print("Certo!")
            else: 
                print("Errado!")
            n1, n2, n_errado, soma = gera_numeros()

        if sqr_3:
            text3 = font.render(str(n3), True, BLACK)
            text3_rect = text3.get_rect()
            text3_rect.center = sqr_3_rect.center
        else:
            sqr_3 = True
            if n3 == n_errado:
                print("Certo!")
            else: 
                print("Errado!")
            n1, n2, n_errado, soma = gera_numeros()

        text_soma = font.render(str(n4), True, BLACK)
        text_soma_rect = text_soma.get_rect()
        text_soma_rect.center = (50, 50)

        n1, n2, n3, n4 = n1, n2, n_errado, soma


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


    return state