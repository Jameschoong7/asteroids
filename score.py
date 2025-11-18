import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)
        self.score =0
        pygame.font.init()
        self.font=pygame.font.Font(None, 32)
    
    def draw(self,screen):
        score_text = self.font.render(f"Score:{self.score}",True,(255,255,255))
        screen.blit(score_text,(0,0))

    def update(self):
        self.score +=1
        print(self.score)