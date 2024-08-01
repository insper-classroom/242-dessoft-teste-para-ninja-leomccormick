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