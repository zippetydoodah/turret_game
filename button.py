from settings import *
import pygame
import time

class Button:
    def __init__(self,pos,name,name_2,expansion):
        self.pos = pos
        self.name = name
        self.name_2 = name_2
        self.expansion = expansion
        self.image_1 = pygame.transform.scale(getImage(self.name),self.expansion)
        self.image_2 = pygame.transform.scale(getImage(self.name_2),self.expansion)
        self.rect = self.image_1.get_rect()
        self.rect.topleft = self.pos
        self.cooldown = 0.2
        self.cooldown_time = None
        self.showing = False
        
    def pressed(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.Rect.collidepoint(self.rect,mouse_pos):
            self.cooldown_time = time.time()
            return True
        else:
            return False
    
    def pressed_keep(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.Rect.collidepoint(self.rect,mouse_pos):
            if self.showing:
                self.showing = False
            else:
                self.showing = True

    def update(self):
        if self.cooldown_time:
            if  time.time() - self.cooldown_time > self.cooldown:
                self.cooldown_time = None
                if self.showing:
                    self.showing = False
                else:
                    self.showing = True

    def render(self,screen):
        if self.cooldown_time == None:
            screen.blit(self.image_2,self.rect)

        elif self.cooldown_time != None:
            screen.blit(self.image_1,self.rect)

    def render_2(self,screen):
        if self.showing:
            screen.blit(self.image_2,self.rect)
        else:
            screen.blit(self.image_1,self.rect)
