import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet fired form the ship"""

    def __init__(self, ss_game):
        """Create a bullet object at the ships current position"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)

        self.rect.midright = ss_game.ship.rect.midright

        #store the bullet's position as a decimal value

        self.x = float(self.rect.x)

    def update(self):
        """move the bullet right"""
        #update the decimal position
        self.x += self.settings.bullet_speed
        #update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)