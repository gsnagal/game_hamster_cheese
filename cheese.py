import pygame
from pygame.sprite import Sprite

class Cheese(Sprite):
    """Uma classe que representa um único queijo."""

    def __init__(self, ai_settings, screen):
        """Inicializa o queijo e define sua posição inicial."""
        super(Cheese, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do queijo e define seu atributo rect
        self.image = pygame.image.load('img/cheese.bmp')
        self.rect = self.image.get_rect()

        # self.rect_screen = self.screen.get_rect

        # Inicia cada novo queijo na direita aleatorio
        self.rect.x = ai_settings.screen_width - self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do queijo
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)



    def blitme(self):
        """Desenha o queijo em sua posição atual."""
        self.screen.blit(self.image, self.rect)



    def update(self):
        """Move o alienígena para a direita."""
        self.x -= self.ai_settings.cheese_speed_factor
        self.rect.x = self.x