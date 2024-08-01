import pygame
from config import FPS, GAME, WHITE, font, BLUE, WIDTH, HEIGHT, BLACK

def init_screen(window):

    # Cria o texto do botão
    text = font.render("Jogar", True, WHITE)
    text_rect = text.get_rect()

    # Define as dimensões do botão
    button_width = 200
    button_height = 100
    button_x = (WIDTH - button_width) // 2
    button_y = (HEIGHT - button_height) // 2

    # Define o retângulo do botão e do texto
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    text_rect.center = button_rect.center

    clock = pygame.time.Clock()  # Ajusta a velocidade do jogo

    running = True
    while running:
        clock.tick(FPS)

        # Processa eventos (fechar janela, teclas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = None
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    state = GAME
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = None
                    running = False

        window.fill(WHITE)  # Desenha o fundo
        pygame.draw.rect(window, BLUE, button_rect) # Desenha o botão
        pygame.draw.rect(window, BLACK, button_rect, 5)  # Desenha a borda com 5 pixels de espessura
        window.blit(text, text_rect) # Desenha o texto no botão
        pygame.display.flip()  # Atualiza o display

    return state