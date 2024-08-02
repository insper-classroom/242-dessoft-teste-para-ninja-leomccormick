import pygame
from config import FPS, BLACK, WHITE, WIDTH, HEIGHT, font_pont_final, font_small

def quit_screen(window, score: int):
    clock = pygame.time.Clock()
        
    running = True
    while running:
        clock.tick(FPS)

        # Processa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None

        # Cria os textos
        text_score = font_pont_final.render(f"Pontuação Final: {score}", True, BLACK)
        text_score_rect = text_score.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        text_sair = font_small.render("Pressione ESC para sair", True, BLACK)
        text_sair_rect = text_sair.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        window.fill(WHITE)
        window.blit(text_score, text_score_rect)
        window.blit(text_sair, text_sair_rect)
        pygame.display.flip()
    return None