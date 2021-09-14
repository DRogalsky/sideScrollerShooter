class Settings:
    """A class to store all settings"""

    def __init__(self):
        """Initialize the games settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 3.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed = 0.75

        # Speed and score increase per 10 enemies shot
        self.speedup_scale = 1.3
        self.score_scale = 1.5

        #Scoring
        self.alien_points = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the changinging values"""

        #speeds
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.75

    def increase_speed(self):
        """increases the speed of all sprites and point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #TODO: maybe change scoring a bit feels a bit high