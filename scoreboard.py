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
        self.prep_high_score()

    def prep_score(self):
        """turn the score into a rendered image"""
        #TODO: round scores? i kinda like not rounding
        score_str = "{:,}".format(self.stats.score)

        self.score_image =self.font.render(score_str,True,
        self.text_color,self.settings.bg_color)

        #display the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20

    def prep_high_score(self):
        """turn the hi score into a rendered image"""
        high_score = round(self.stats.high_score, -1) #TODO: maybe remove? or at least add it up above too
        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True, 
        self.text_color, self.settings.bg_color)

        #center high score at top of screen

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """check to see if theres a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()