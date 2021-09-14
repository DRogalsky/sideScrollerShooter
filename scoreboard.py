import pygame.font

class Scoreboard:
    """Keeps and displays scoring information"""
    def __init__(self, ss_game):
        """initialize scorekeeping attributes"""
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        #font settings for the scoreboard
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial scorboard image
        self.prep_score()

    def prep_score(self):
        """turn the score into a rendered image"""
        score_str = str(self.stats.score)

        self.score_image =self.font.render(score_str,True,
        self.text_color,self.settings.bg_color)

        #display the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)