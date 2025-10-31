import pygame
from background import Background

class Power:
    def __init__(self):
        self.usage = 0
        self.power = 0
        self.background = Background("cash_background",(160,0),(160,90))
    
    def render(self,screen):
        col = (0,0,0)
        if self.usage > self.power:
            col = (255,0,0)
            
        self.background.render(screen)
        font = pygame.font.SysFont('Arial', 25)
        text = font.render("POWER:%s/%s"%(str(self.usage),str(self.power)), 1, col, None)
        textRect = text.get_rect()
        textRect.topleft = (175,20)
        screen.blit(text,textRect)