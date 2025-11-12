import pygame
import player as p
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable= pygame.sprite.Group()
    drawable =pygame.sprite.Group()
    
    p.Player.containers = (updatable,drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
       
        updatable.update(dt)
        
        for player in drawable:
            player.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) /1000
        


if __name__ == "__main__":
    main()
