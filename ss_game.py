import sys,pygame

from settings import Settings

class SideScroller:
    """Overall class to manage the game assets and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Side Scroller")

        #Background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass of the loop
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    ss = SideScroller()
    ss.run_game()