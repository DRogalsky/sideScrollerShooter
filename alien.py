import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ss_game):
        """Initialize the alien and set the starting position"""

        super().__init__()
        self.screen = ss_game.screen

        # need to make an alien image.... brb