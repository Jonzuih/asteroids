import pygame
import constants
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print(f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    # spawn point
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    
    player_ship = Player(x, y)


    # FPS and game-timing
    clock = pygame.time.Clock()
    dt = 0

    # infinite WHILE loop for game
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        screen.fill("black")
        player_ship.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
