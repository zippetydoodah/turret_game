from health_bar import *
from pygame import Vector2
from upgrades import Upgrades_UI
from structure import *
import time

class Generator(Structure):
    def __init__(self,pos,health,name,speed,reward,power):
        super().__init__(pos,health,power,name,[Increased_generation_upgrade])
        self.speed = speed
        self.timer = None
        self.base_reward = reward
        self.reward = reward

    def upgrade(self):
        if Increased_generation_upgrade in self.upgrades:
            self.reward = self.base_reward * self.UI.slots[0].level

    def get_reward(self,power):

        if not self.timer:
            self.timer = time.time()

        if time.time() - self.timer > self.speed:
            self.timer = time.time()
            if power >= self.power_bar.total_power:
                self.power_bar.power = self.power_bar.total_power
                return self.reward
            
        return 0
    
    def render_extra(self,screen):
        if self.power_bar.power == self.power_bar.total_power:   
            font = self.font
            
            count_text = font.render("Timer:%s/%s"%(int(time.time() - self.timer),self.speed), 1, (0,0,0), None)
            count_text_rect = count_text.get_rect()
            count_text_rect.topleft = (WINDOW_WIDTH - 280,350)
            screen.blit(count_text,count_text_rect)

    
class Basic_generator(Generator):
     def __init__(self,pos):
        super().__init__(pos, 10, "generator", speed= 5, reward = 4, power = 10)