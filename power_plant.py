from health_bar import *
from pygame import Vector2
from upgrades import Upgrades_UI
from structure import *
import time

class Power_plant(Structure):
    def __init__(self,pos,health,name,power,speed):
        super().__init__(pos,health,power,name,[])

        self.pos = pos
        self.power = power
        self.total_power = power
        self.timer = None
        self.speed = speed
        self.source_tile = None

    def upgrade(self):
        pass
    
    def get_reward(self,source_tile):
        self.source_tile = source_tile
        
        if not self.timer:
            self.timer = time.time()
        
        if self.timer and time.time() - self.timer > self.speed:
            self.timer = None
            return True
        
        else:
            return False
        
    def render_extra(self,screen):
        if self.source_tile:
            font = self.font

            count_text = font.render("Resources:%s"%(self.source_tile.ore.amount), 1, (0,0,0), None)
            count_text_rect = count_text.get_rect()
            count_text_rect.topleft = (WINDOW_WIDTH - 280,400)
            screen.blit(count_text,count_text_rect)

        
class Basic_power_plant(Power_plant):
     def __init__(self,pos):
        super().__init__(pos,10,"power_plant",power = 20,speed = 5)