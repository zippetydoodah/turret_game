import pygame
from background import Background

class Cash:
    def __init__(self):
        self.money = 10
        self.background = Background("cash_background",(0,0),(160,90))

    def update(self,amount):
        self.money += amount

    def render(self,screen):

        self.background.render(screen)
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("CASH:$ %s"%(str(self.money)), 1, (0,0,0), None)
        textRect = text.get_rect()
        textRect.topleft = (5,20)
        screen.blit(text,textRect)