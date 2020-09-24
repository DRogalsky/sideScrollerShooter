import sys,pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class SideScroller:
    """Overall class to manage the game assets and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #grab the screen width and height for later calculations
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()

        pygame.display.set_caption("Side Scroller")

        #create instance to store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # counter for time based stuff TODO: see if there is a better way to do this
        self.counter = 0

        # flag to control amount of bullets you can fire
        self.recently_fired = False

        #Background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.state.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_screen()
                self._update_aliens()
                if self.counter % 100 == 0:
                    self.recently_fired = False

    #event handlers

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
        elif event.key == pygame.K_SPACE:
            #shoot a bullet if not recently fired
            if self.recently_fired == False:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        #Check when the player releases a key
        if event.key == pygame.K_UP:
            #move ship up
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            #move ship down
            self.ship.moving_down = False

    #misc helper functions

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        self.recently_fired = True
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _spawn_enemy(self):
        """Spawns enemies randomly from the right side of the screen"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = self.screen_width
        self.aliens.add(alien)

    def _ship_hit(self):
        """respond to ship being hit by alien"""

        if self.stats.ships_left > 0:
            #Decrement ships
            self.stats.ships_left -= 1

            #Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Recenter the ship
            self.ship.center_ship

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    # update functions

    def _update_bullet(self):
        """Update position of bullets and get rid of old bullets"""

        # update position of old bullets
        self.bullets.update()

        # Get rid of bullets that are off screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)

        # see if it hit an alien
        # get rid of both if so
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

    def _update_aliens(self):
        """make the aliens move slowly to the left"""

        #update position of aliens
        self.aliens.update()

        #increase counter
        self.counter += 1

        #delete offscreen aliens
        for alien in self.aliens.copy():
            if alien.rect.right < 0:
                self.aliens.remove(alien)

        #spawn new enemies if counter is 10
        if self.counter == 500:
            self._spawn_enemy()
            self.counter = 0

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass of the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ss = SideScroller()
    ss.run_game()