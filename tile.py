from pygame import Vector2
from Turret import Basic_Turret
from settings import *
from base import Base
from ores import *

class None_tile:
    def __init__(self,x,y):
        self.pos = Vector2(x,y)
        self.type = None

    def render(self,screen):
        pass

class Tile:
    def __init__(self,x,y,type, name, image,turret = None,base = None,wall = None,mine = None,generator = None,plant = None,healer = None,ore = None):
        self.pos = Vector2(x,y)
        self.type = type
        self.name = name   
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.notify_image = getImage("notify")
        
        #self.structure = struct()
        # have only one struct variable rather than seperate so easier to access.
        
        if ore:
            self.ore = ore()
        else:
            self.ore = None

        if base:
            self.base = Base(self.pos)
        else:
            self.base = None
            
        if mine:
            self.mine = mine((self.pos.x,self.pos.y))
        else:
            self.mine = None

        if turret:
            self.turret = turret((self.rect.center[0],self.rect.center[1]),self.pos)
        else:
            self.turret = None
        
        if wall:
            self.wall = wall((self.pos.x,self.pos.y))
        else:
            self.wall = None

        if generator:
            self.generator = generator((self.pos.x,self.pos.y))
        else:
            self.generator = None 
            
        if plant:
            self.plant = plant((self.pos.x,self.pos.y))
        else:
            self.plant = None 

        if healer:
            self.healer = healer((self.pos.x,self.pos.y))
        else:
            self.healer = None

    def render(self,screen):
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        screen.blit(self.image,self.rect)

        if self.turret:
            if self.turret.health_bar.health < self.turret.health_bar.total_health:
                rect = self.notify_image.get_rect()
                rect.center = self.pos
                screen.blit(self.notify_image,rect)
