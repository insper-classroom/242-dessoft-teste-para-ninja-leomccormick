import pygame 
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from quit_screen import quit_screen

# Inicializa os módulos do pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Configura a janela do jogo com largura e altura especificadas
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo para ninja de Dessoft")

# Define o estado inicial do jogo
state = INIT    

# Loop principal do jogo
while True:
    if state == INIT:
        state = init_screen(WINDOW) # Mostra a tela inicial
    elif state == GAME: 
        state, score = game_screen(WINDOW) # Executa a tela do jogo
    elif state == QUIT: 
        state = quit_screen(WINDOW, score) # Mostra a tela de saída
    else:
        break # Sai do loop principal e encerra o jogo

pygame.quit()