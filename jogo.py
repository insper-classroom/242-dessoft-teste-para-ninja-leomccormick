import pygame 
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from quit_screen import quit_screen

# Inicializa o pygame
pygame.init()

# Configura a janela do jogo
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo para ninja de Dessoft")

state = INIT    

# Loop principal do jogo
while True:
    if state == INIT:
        state = init_screen(WINDOW) # Tela inicial
    elif state == GAME: 
        state, score = game_screen(WINDOW) # Tela do jogo
    elif state == QUIT: 
        state = quit_screen(WINDOW, score) # Tela final
    else:
        break # Encerra o jogo

pygame.quit()