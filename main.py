import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.time.Clock()

    dt = 0

    clock = pygame.time.Clock()

    pygame.init()

    print("Starting Asteroids with pygame version:",pygame.version.ver)
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        log_state()

        for event in pygame.event.get():
            pass
        
        pygame.Surface.fill(screen, (0,0,0))

        clock.tick(60)

        dt = clock.tick(60)/1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
   main()
