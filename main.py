import pygame
import player as p
import score
import asteroid as a
import asteroidfield as af
import shot as s
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state,log_event
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable= pygame.sprite.Group()
    drawable =pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    p.Player.containers = (updatable,drawable)
    a.Asteroid.containers = (asteroids,updatable,drawable)
    af.AsteroidField.containers = (updatable)
    s.Shot.containers = (shots,updatable,drawable)
    score.Score.containers = (drawable)
    dt = 0
    player1 = p.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid1 = af.AsteroidField()
    player_score = score.Score()
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
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    player_score.update()

        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) /1000
        


if __name__ == "__main__":
    main()
