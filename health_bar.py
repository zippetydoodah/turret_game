import pygame
import time
from settings import *

class Health_bar:
    def __init__(self,total_health,pos):
        self.pos = pos
        self.total_health = total_health
        self.health = total_health
        self.initial_health = total_health
        self.rect_height = 10
        self.multiplier = 100 / total_health 
        self.hit_time = None

    def update_health(self,amount):
        self.health -= amount
        if self.health > self.total_health:
            self.health = self.total_health
        self.hit_time = time.time()

    def move(self,x,y):
        self.pos.x = x
        self.pos.y = y - 10
    
    def render(self,screen,r = False):
        self.multiplier = 100 / self.total_health 
        if self.hit_time and time.time() - self.hit_time < HEALTH_SHOW_TIME or r:
            self.hitrect1 = pygame.Rect(self.pos.x, self.pos.y, 100/2, self.rect_height)
            self.hitrect = pygame.Rect(self.pos.x, self.pos.y, (self.health * self.multiplier)/2, self.rect_height)
            pygame.draw.rect(screen, (255, 0, 0), self.hitrect1)
            pygame.draw.rect(screen, (0, 255, 0), self.hitrect)
        else:
            self.hit_time = None