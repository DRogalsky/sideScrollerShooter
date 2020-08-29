import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ss_game):
        """Initialize the alien and set the starting position"""

        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # loading alien image and set the rect attribute

        self.image = pygame.image.load('images/alienship.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact x and y position
        #TODO: check if needed later

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)