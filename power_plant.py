from health_bar import *
from pygame import Vector2
from upgrades import Upgrades_UI
from structure import *
import time

class Power_plant(Structure):
    def __init__(self,pos,health,name,power):
        super().__init__(pos,health,name,[])
        self.power = power
        
    def upgrade(self):
        pass
        
class Basic_power_plant(Power_plant):
     def __init__(self,pos):
        super().__init__(pos,10,"power_plant",power = 20)