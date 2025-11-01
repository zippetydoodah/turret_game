from settings import *
from pygame import Vector2
from health_bar import Health_bar
import math
import time

class Enemy:
    def __init__(self,pos,target,name,speed,damage,health, drops):
        self.pos = Vector2(pos)
        self.target_pos = target
        self.name = name
        self.image = getImage(self.name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.damage = damage
        self.drops = drops

        self.health_bar = Health_bar(health,Vector2(self.pos.x,self.pos.y))
        self.dx = self.target_pos[0]- self.pos.x
        self.dy = self.target_pos[1] - self.pos.y
        self.hyp = math.sqrt((self.dx * self.dx) + (self.dy * self.dy))
        self.slow_down = None

    def move(self,fast_forward):
        speed = self.speed

        if fast_forward.showing:
            speed = self.speed * 2

        if self.slow_down and time.time() - self.slow_down < 10:
            speed = self.speed/3

        if self.slow_down and time.time() - self.slow_down > 10:
            self.slow_down = None

        self.pos.x += (self.dx / self.hyp * speed)
        self.pos.y += (self.dy / self.hyp * speed)
        self.health_bar.move(self.pos.x,self.pos.y)

    def render(self,screen,settings):
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos.x,self.pos.y)
        screen.blit(self.image,self.rect)
        if settings.enemy_health.showing:
            self.health_bar.render(screen,r = True)
        else:
            self.health_bar.render(screen)
        
class Zombie(Enemy):
    def __init__(self,pos,target):
        super().__init__(pos,target,"zombie",0.5,2,health= 100,drops = 5)

class Troll(Enemy):
    def __init__(self,pos,target):
        super().__init__(pos,target,"troll",0.4,10,health= 250,drops = 15)

class Dragon(Enemy):
    def __init__(self,pos,target):
        super().__init__(pos,target,"dragon",0.3,50,health = 1000,drops = 300)
    
