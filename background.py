from settings import *

class Background:
    def __init__(self,name,pos,expansion):
        self.name = name
        self.pos = pos
        self.image = pygame.transform.scale(getImage(self.name),expansion)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def render(self,screen):
        screen.blit(self.image,self.rect)
        