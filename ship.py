import pygame

class Ship:
    """A class to manaage the ship."""

    def __init__(self, ss_game):
        """Initialize the ship and set its starting position."""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images\spaceship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the left side of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_up:
            self.rect.y -= 1
        elif self.moving_down:
            self.rect.y += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

