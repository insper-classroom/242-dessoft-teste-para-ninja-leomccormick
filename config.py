import pygame

pygame.font.init() 

WIDTH = 800 # Largura da tela
HEIGHT = 600  # Altura da tela
FPS = 60  # Frames por segundo

# Barra cinza inferior da tela de jogo
barra_rect = pygame.Rect(0, 550, 800, 50)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Define algumas cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)

# Define a cor do botão e do texto
BUTTON_COLOR = BLUE
BUTTON_TEXT_COLOR = WHITE

font_tempo = pygame.font.Font(None, 35)
font_pont_final = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 36)

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

# Define a fonte do "feedback"
font_feedback = pygame.font.Font(None, 50)

text_certo = font_feedback.render("Certo!", True, GREEN)
text_errado = font_feedback.render("Errado!", True, RED)

rect_certo = text_certo.get_rect()
rect_errado = text_errado.get_rect()