class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""
    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        filename = 'highScore.txt'
        with open(filename) as file_object:
            self.high_score = int(file_object.read())



    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.cheese_left = self.ai_settings.cheese_limit
        self.score = 0
        self.level = 1



