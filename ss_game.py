import sys,pygame

from settings import Settings
from ship import Ship

class SideScroller:
    """Overall class to manage the game assets and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        pygame.display.set_caption("Side Scroller")

        self.ship = Ship(self)

        #Background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #Watch for keyboard events in game
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #check which button the player pressed
        if event.key == pygame.K_q:
            #press q to quit
            sys.exit()
        elif event.key == pygame.K_UP:
            #move ship up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            #move ship down
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        #Check when the player releases a key
        if event.key == pygame.K_UP:
            #move ship up
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            #move ship down
            self.ship.moving_down = False


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass of the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ss = SideScroller()
    ss.run_game()