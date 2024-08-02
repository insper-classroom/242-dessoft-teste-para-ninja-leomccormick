from config import QUIT, WIDTH, HEIGHT, FPS, GAME, WHITE, RED, GREEN, BLUE, GRAY, BLACK, barra_rect, sqr_1_rect, sqr_2_rect, sqr_3_rect, rect_certo, rect_errado, text_certo, text_errado, font_tempo
import pygame
from gerador import gera_numeros
from random import shuffle
import time


def game_screen(window):

    score = 0
    vidas = 3

    def verificar_e_gerar(n_atual: int, n_errado: int, sqr: pygame.Rect) -> tuple:
        nonlocal score, vidas
        pygame.draw.rect(window, WHITE, sqr)
        if n_atual == n_errado:
            print("Acertou")
            score += 1
            rect_certo.center = sqr.center
            window.blit(text_certo, rect_certo)
        else: 
            print("Errou")
            vidas -= 1
            rect_errado.center = sqr.center
            window.blit(text_errado, rect_errado)
        pygame.display.flip()
        time.sleep(1)
        n1, n2, n_errado, soma = gera_numeros()
        numeros = [n1, n2, n_errado]
        shuffle(numeros)
        print(score)
        return numeros, n_errado, soma
    
    state = GAME
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 50)

    n1, n2, n_errado, soma = gera_numeros()
    lista_sqrs = [n1, n2, n_errado]
    shuffle(lista_sqrs)
    n_sqr1, n_sqr2, n_sqr3 = lista_sqrs
    
    sqr_1 = True
    sqr_2 = True
    sqr_3 = True

    tempo_inicial = pygame.time.get_ticks()  # Guarda o tempo de início

    while (state != QUIT and state is not None):
        clock.tick(FPS)

        # Calcula o tempo decorrido
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) / 1000  # Tempo em segundos

        # Verifica se o tempo acabou
        print(f"{tempo_decorrido:.0f}")
        if tempo_decorrido >= 60:
            state = QUIT

        # Verifica se o jogador ainda tem vidas
        if vidas == 0:
            state = QUIT

        # Escrevendo os números 
        if sqr_1:
            text1 = font.render(str(n_sqr1), True,  BLACK)
            text1_rect = text1.get_rect()
            text1_rect.center = sqr_1_rect.center
        else:
            sqr_1 = True
            numeros, n_errado, soma = verificar_e_gerar(n_sqr1, n_errado, sqr_1_rect)
            n_sqr1, n_sqr2, n_sqr3 = numeros

        if sqr_2:
            text2 = font.render(str(n_sqr2), True, BLACK)
            text2_rect = text2.get_rect()
            text2_rect.center = sqr_2_rect.center
        else:
            sqr_2 = True
            numeros, n_errado, soma = verificar_e_gerar(n_sqr2, n_errado, sqr_2_rect)
            n_sqr1, n_sqr2, n_sqr3 = numeros

        if sqr_3:
            text3 = font.render(str(n_sqr3), True, BLACK)
            text3_rect = text3.get_rect()
            text3_rect.center = sqr_3_rect.center
        else:
            sqr_3 = True
            numeros, n_errado, soma = verificar_e_gerar(n_sqr3, n_errado, sqr_3_rect)
            n_sqr1, n_sqr2, n_sqr3 = numeros

        text_soma = font.render(str(soma), True, BLACK)
        text_soma_rect = text_soma.get_rect()
        text_soma_rect.center = (30, 30)

        text_tempo = font_tempo.render(f"Tempo restante: {60-tempo_decorrido:.0f}", True, BLACK)
        text_tempo_rect = text_tempo.get_rect()
        text_tempo_rect.topleft = (WIDTH-240, 20)

        # Processa eventos (fechar janela, teclas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sqr_1_rect.collidepoint(event.pos):
                    print(n_sqr1)
                    sqr_1 = False
                if sqr_2_rect.collidepoint(event.pos):
                    print(n_sqr2)
                    sqr_2 = False
                if sqr_3_rect.collidepoint(event.pos):
                    print(n_sqr3)
                    sqr_3 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = None

        window.fill(WHITE)  # Desenha o fundo
        pygame.draw.rect(window, GRAY, barra_rect)

        pygame.draw.rect(window, BLUE, sqr_1_rect)
        window.blit(text1, text1_rect)
        pygame.draw.rect(window, GREEN, sqr_2_rect)
        window.blit(text2, text2_rect)
        pygame.draw.rect(window, RED, sqr_3_rect)
        window.blit(text3, text3_rect)

        window.blit(text_soma, text_soma_rect)
        window.blit(text_tempo, text_tempo_rect)

        pygame.display.flip()  # Atualiza o display

    return state, score

