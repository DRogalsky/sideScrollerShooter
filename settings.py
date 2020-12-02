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
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 5

        # Alien settings
        self.alien_speed = 0.75