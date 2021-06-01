import pygame.font
from pygame.sprite import Group
from cheese import Cheese

class Scoreboard():
    """Uma classe para mostrar informações sobre pontuação."""
    def __init__(self, ai_settings, screen, stats):
        """Inicializa os atributos da pontuação."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.prep_score()

        #Maior pontuação
        self.prep_high_score()

        #Vidas
        self.prep_cheeses()



    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        #round arredendo para o multiplo mais próximo de 10
        rounded_score = self.stats.score
        score_str = "{}".format(rounded_score) #Apresentar o valro sendo 1,000,000 em vez de 1000000

        #Criar imagem
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Transforma a pontuação máxima em uma imagem renderizada."""
        high_score = self.stats.high_score
        high_score_str = "{}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



    def prep_level(self):
        """Transforma o nível em uma imagem renderizada."""
        self.level_image = self.font.render(str(self.stats.level),True, self.text_color, self.ai_settings.bg_color)
        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10



    def prep_cheeses(self):
        """Mostra quantas espaçonaves restam."""
        self.cheeses = Group()
        for cheese_number in range(self.stats.cheese_left):
            cheese = Cheese(self.ai_settings, self.screen)
            cheese.image = pygame.transform.scale(cheese.image, [50, 50])
            cheese.rect.x = 10 + cheese_number * cheese.rect.width
            cheese.rect.y = 10
            self.cheeses.add(cheese)


    def show_score(self):
        """Desenha a pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Desenha as espaçonaves
        self.cheeses.draw(self.screen)