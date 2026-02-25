import pygame
import sys
from logger import log_state, log_event
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    print("Starting Asteroids!")
    
    # Title to the game windows
    pygame.display.set_caption("Asteroids!")

    # Set up font for score on screen
    fontObj = pygame.font.Font(None, 40)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidField = AsteroidField()

    dt: int = 0
    score: int = 0

    while True:

        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # set up the score screen and keep it updated
        score_screen = fontObj.render(f"Score: {score}", True, "white", None)
        textRectObj = score_screen.get_rect()
        textRectObj.topleft = (0,0)
    
        # write the score to the screen
        screen.blit(score_screen, textRectObj)

        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("GAME OVER! TRY AGAIN.")
                print(f"Your score was {score}")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 1

        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60)/1000
        
        

if __name__ == "__main__":
   main()
