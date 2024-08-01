from config import QUIT, WIDTH, HEIGHT, FPS, GAME, WHITE, RED, GREEN, BLUE, GRAY, barra_rect
import pygame

def game_screen(window):
    clock = pygame.time.Clock()

    # Define as dimensões dos quadrados
    sqr_width = 100
    sqr_height = 100
    sqr_x = (WIDTH - sqr_width) // 2

    sqr_y_1 = HEIGHT - 150
    sqr_y_2 = HEIGHT - 250
    sqr_y_3 = HEIGHT - 350

    # Define os quadrados
    sqr_1_rect = pygame.Rect(sqr_x, sqr_y_1, sqr_width, sqr_height)
    sqr_2_rect = pygame.Rect(sqr_x, sqr_y_2, sqr_width, sqr_height)
    sqr_3_rect = pygame.Rect(sqr_x, sqr_y_3, sqr_width, sqr_height)

    sqr_1 = True
    sqr_2 = True
    sqr_3 = True

    running = True
    while running:
        clock.tick(FPS)

        # Processa eventos (fechar janela, teclas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = None
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sqr_1_rect.collidepoint(event.pos):
                    sqr_1 = False
                if sqr_2_rect.collidepoint(event.pos):
                    sqr_2 = False
                if sqr_3_rect.collidepoint(event.pos):
                    sqr_3 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False

        window.fill(WHITE)  # Desenha o fundo
        pygame.draw.rect(window, GRAY, barra_rect)

        if sqr_1:
            pygame.draw.rect(window, BLUE, sqr_1_rect)
        if sqr_2:
            pygame.draw.rect(window, GREEN, sqr_2_rect)
        if sqr_3:
            pygame.draw.rect(window, RED, sqr_3_rect)

#        window.blit(text, text_rect) # Desenha o texto no botão
        pygame.display.flip()  # Atualiza o display

    return state