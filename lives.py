import pygame
import constants


class Lives(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.lives = constants.PLAYER_LIFE
        pygame.font.init()
        self.font=pygame.font.Font(None, 32)
    
    def draw(self,screen):
        lives_text = self.font.render(f"Lives:{self.lives}",True,(255,255,255))
        screen.blit(lives_text,(1,20))

    def update(self):
        self.lives -=1
        print(self.lives)