import pygame
from settings import Settings
import game_function as gf
from huni import Huni
from pygame.sprite import Group
from time import time
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init() #Inicia as configurações do pygame

    #screen = pygame.display.set_mode((1200, 700)) #Cria um display que ira aparecer o jogo de dimensoes 1200x700
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Pegar queijo")

    huni = Huni(ai_settings, screen)
    cheeses = Group()

    start_time = time()

    stats = GameStats(ai_settings)

    sb = Scoreboard(ai_settings, screen, stats)

    play_button = Button(ai_settings, screen, "Play")

    pygame.mixer.music.load('music/WM - Fuleragem- cortado.wav')
    pygame.mixer.music.play(-1)


    # Inicia o laço principal do jogo
    while True:
        gf.check_events(stats, sb, play_button, huni, cheeses)

        if stats.game_active:
            gf.update_huni(huni)
            gf.update_cheeses(ai_settings, stats, screen, sb, huni, cheeses)
            #Criando cheeses
            current_time = time()
            elapsed_time = current_time - start_time
            if elapsed_time > ai_settings.time_cheese:
                gf.create_cheese(ai_settings, screen, cheeses)
                start_time = time()

        gf.update_screen(ai_settings, screen, stats, sb, huni, cheeses, play_button)




if __name__ == '__main__':
    run_game()