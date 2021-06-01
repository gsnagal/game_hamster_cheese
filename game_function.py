import sys
import pygame
from cheese import Cheese
from time import sleep
from random import randint


def check_keyup_events(event, huni):
    if event.key == pygame.K_UP:  # Se for solto a seta para cima
        huni.moving_up = False

    elif event.key == pygame.K_DOWN:  # Se for solto a seta para baixo
        huni.moving_down = False



def check_keydown_events(event, huni):
    if event.key == pygame.K_UP:  # Se a tecla for a seta para cima
        # Move o huni para cima
        huni.moving_up = True

    elif event.key == pygame.K_DOWN:  # Se a tecla for a seta para a baixo
        # Move o huni para a baixo
        huni.moving_down = True



def exit_game(stats):
    filename = 'highScore.txt'
    with open(filename, 'w') as file_object:
        file_object.write('{}'.format(stats.high_score))
    sys.exit()  # Sai do jogo qndo o usuario desistir



def check_events(stats, sb, play_button, huni, cheeses):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    # Observa eventos de teclado e de mouse
    for event in pygame.event.get():  # Retorna os eventos detectados pelo pygame, qualquer evento do teclado
        # ou mouse fará o for executar

        if event.type == pygame.QUIT:
            exit_game(stats)

        elif event.type == pygame.KEYDOWN: #Verifica se uma tecla foi precionada
            check_keydown_events(event, huni)

        elif event.type == pygame.KEYUP: #Quando soltar a tecla
           check_keyup_events(event, huni)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() #Devolve uma tupla contendo as coordenadas x e y do cursor quando é clicado
            check_play_button(stats, sb, play_button, huni, cheeses, mouse_x, mouse_y)



def check_play_button(stats, sb, play_button, huni, cheeses, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) #Veirifica se as cordenadas x e y corresponde a área rect
    if button_clicked and not stats.game_active: #O game_active tem que ser false
        pygame.mouse.set_visible(False) #Oculta o mouse

        # Reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True

        # Reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_cheeses()

        # Esvazia a lista de alienígenas e de projéteis
        cheeses.empty()

        # Cria uma nova frota e centraliza a espaçonave
        huni.center_huni()



def update_screen(ai_settings, screen, stats, sb, huni, cheeses, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela."""
    # Redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)  # Para mudar o background da cor do bg_color

    huni.blitme()
    cheeses.draw(screen)

    # Desenha a informação sobre pontuação
    sb.show_score()
    sb.prep_level()

    if not stats.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível
    pygame.display.flip()




def update_huni(huni):
    huni.update()




def create_cheese(ai_settings, screen, cheeses):
    # Cria um alienígena e o posiciona na linha
    cheese = Cheese(ai_settings, screen)
    min_spawn = cheese.rect.height
    max_spawn = ai_settings.screen_height - cheese.rect.height
    random_number = randint(min_spawn, max_spawn)
    cheese.rect.y = random_number
    cheeses.add(cheese)



def update_cheeses(ai_settings, stats, screen, sb, huni, cheeses):
    """Verifica se a frota está em uma das bordas e então atualiza as posições de todos os alienígenas da frota."""
    cheeses.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    check_huni_cheese_collisions(ai_settings, stats, screen, sb, huni, cheeses)



def check_huni_cheese_collisions(ai_settings, stats, screen, sb, huni, cheeses):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido
    for cheese in cheeses.copy():
        if cheese.rect.colliderect(huni):
            cheeses.remove(cheese)
            stats.score += ai_settings.cheese_points
            sb.prep_score()
            ai_settings.increese_speed()


    check_cheese_left(stats, screen, sb, huni, cheeses)


def check_cheese_left(stats, screen, sb, huni, cheeses):
    """Verifica se algum alienígena alcançou a parte inferior da tela."""
    screen_rect = screen.get_rect()
    for cheese in cheeses.sprites():
        if cheese.rect.left <= screen_rect.left:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            if stats.cheese_left > 1:
                # Decrementa ships_left
                stats.cheese_left -= 1

                sb.prep_cheeses()

                cheeses.remove(cheese)

                # # Esvazia a lista de alienígenas e de projéteis
                # cheeses.empty()
                # # Cria uma nova frota e centraliza a espaçonave
                # huni.center_huni()
                # # Faz uma pausa
                # sleep(1)

            else:
                check_high_score(stats, sb)
                stats.game_active = False
                pygame.mouse.set_visible(True)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()