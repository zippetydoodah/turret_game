import math
from settings import *
import pygame
from pygame import Vector2

class Base_ammunition:
    def __init__(self,pos,type,target,damage,speed):
        self.pos = Vector2(pos)
        self.type = type
        self.target_pos = target
        self.damage = damage
        self.base_damge = damage

        self.image = getImage(self.type)
        self.rect = self.image.get_rect()

        self.dx = self.target_pos[0]- self.pos.x
        self.dy = self.target_pos[1] - self.pos.y
        self.hyp = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))
        
        self.speed = speed

    def move(self, fast_forward):
        speed = self.speed
        if fast_forward.showing:
            speed = self.speed * 2

        self.pos.x += (self.dx / self.hyp * speed)
        self.pos.y += (self.dy / self.hyp * speed)

    def render(self,screen):
        self.rect.topleft = self.pos
        screen.blit(self.image,self.rect)

class Flame_ammo(Base_ammunition):
    def __init__(self, pos,target,speed = 5):
        super().__init__(pos, "flame",target,15,speed) # add other characteristics like speed direction and damage

class Laser_ammo(Base_ammunition):
    def __init__(self, pos,target,speed = 2):
        super().__init__(pos,"laser",target,2,speed)

class Machine_gun_ammo(Base_ammunition):
    def __init__(self, pos,target,speed = 5):
        super().__init__(pos,"bullet",target,2,speed) # add other characteristics like speed direction and damage
        