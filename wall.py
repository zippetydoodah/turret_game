from health_bar import *
from pygame import Vector2
from structure import *
from upgrades import *

class Wall(Structure):
    def __init__(self,pos,health,name):
        super().__init__(pos,health,name,[Increased_health_upgrade])

    def upgrade(self):
        self.health_bar.total_health =  self.health_bar.initial_health + 5 * (self.UI.slots[0].level - 1)
        
class Stone_wall(Wall):
     def __init__(self,pos):
        super().__init__(pos,50,"stone_wall")