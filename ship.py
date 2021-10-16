import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manaage the ship."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images\spaceship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the vertical position
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        # update the saved vert position
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # update the rect
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """recenter ship after death"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)