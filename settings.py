class Settings():
    """Uma classe para armazenar todas as configurações da Invasão
    Alienígena."""
    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        #Configurações do huni
        self.huni_speed_factor = 1
        self.cheese_limit = 3


        self.cheese_points = 1

        self.scale_speed = 1.005

        self.time_cheese_lowest = 0.05

        self.initialize_dynamic_settings()




    def initialize_dynamic_settings(self):
        self.cheese_speed_factor = 0.5
        self.time_cheese = 1



    def increese_speed(self):
        if self.time_cheese <= 0.3:
            pass
        else:
            self.time_cheese -= self.time_cheese_lowest
        self.cheese_speed_factor *= self.scale_speed
