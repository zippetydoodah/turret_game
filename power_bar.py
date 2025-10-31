import pygame
import time
from settings import *

class Power_bar:
    def __init__(self,total_power,pos):
        self.pos = pos
        self.total_power = total_power
        self.power = total_power
        self.initial_power = total_power
        self.rect_height = 5
        self.multiplier = 100 / total_power
        self.hit_time = None

    def update_health(self,power):
        if power > self.total_power:
            self.power = self.total_power
        else:
            self.power = 0

        self.hit_time = time.time()

    def move(self,x,y):
        self.pos.x = x
        self.pos.y = y - 10
    
    def render(self,screen,r = False):
        self.multiplier = 100 / self.total_power 
        if self.hit_time and time.time() - self.hit_time < HEALTH_SHOW_TIME or r:
            self.hitrect1 = pygame.Rect(self.pos.x, self.pos.y, 100/2, self.rect_height)
            self.hitrect = pygame.Rect(self.pos.x, self.pos.y, (self.power * self.multiplier)/2, self.rect_height)
            pygame.draw.rect(screen, (255, 0, 0), self.hitrect1)
            pygame.draw.rect(screen, (255, 255, 0), self.hitrect)
        else:
            self.hit_time = None