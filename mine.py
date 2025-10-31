from health_bar import *
from pygame import Vector2
from structure import *
class Mine:
    def __init__(self,pos,damage,name,range):
        self.pos = pos
        self.name = name
        self.damage = damage
        self.range = range

class Basic_mine(Mine):
     def __init__(self,pos):
        super().__init__(pos,damage = 100,name = "basic_mine",range = 50)