import pygame


class Huni():

    def __init__(self, ai_settings, screen):
        """Inicializa o huni e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings


        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('img/huni.bmp') #Carrega a imagem
        self.rect = self.image.get_rect() #Acessa o atributo rect da superficie, trata elementos do jogo como
                                          # retangulos
        self.screen_rect = screen.get_rect() #Amazenando o retangulo da tela em self.screen_rect


        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centery = self.screen_rect.centery #Faz com que o eixo y central da espaço-nave seja igual ao
                                                     # eixo y da tela
        self.rect.left = self.screen_rect.left #Faz com que a barte da esquerda da espaço-nave seja igual a
                                                   # parte da esquerda da tela



        # Não pode ser self.rect.centerx pois rect armazena apenas parte inteira do valor
        # Então transformamos em float o slf.rect.centerx
        self.center = float(self.rect.centery)



        # Flag de movimento
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.huni_speed_factor

        if self.moving_up and self.rect.top > (self.rect.height/3):
            self.center -= self.ai_settings.huni_speed_factor

        # Atualiza o objeto rect de acordo com self.center
        self.rect.centery = self.center



    def blitme(self):
        """Desenha o huni em sua posição atual."""
        self.screen.blit(self.image, self.rect) #Desenhará a imagem na tela na posição especificada por self.rect



    def center_huni(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.screen_rect.centery