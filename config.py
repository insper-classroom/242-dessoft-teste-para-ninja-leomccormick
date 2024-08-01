import pygame

pygame.font.init() 

WIDTH = 3 * 250  # Largura da tela
HEIGHT = 3 * 250  # Altura da tela
FPS = 60  # Frames por segundo

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Define algumas cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define a cor do botão e do texto
BUTTON_COLOR = BLUE
BUTTON_TEXT_COLOR = WHITE

# Define a fonte e o tamanho do texto
font = pygame.font.Font(None, 74)