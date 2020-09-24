class GameStats:
    """used to track statistics like lives or score"""

    def __init__(self, ss_game):
        """Initialize stats"""
        self.settings = ss_game.settings
        self.reset_stats()
        
        #set game in an active state
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
