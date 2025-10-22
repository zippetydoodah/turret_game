from health_bar import *
from pygame import Vector2
from upgrades import Upgrades_UI
from structure import *
import time

class Healer(Structure):
    def __init__(self,pos,health,name,speed,reward,range,power):
        super().__init__(pos,health,power,name,[])
        self.speed = speed
        self.timer = None
        self.reward = reward
        self.base_range = range
        self.range = range
        self.font = pygame.font.SysFont('Arial', 25)
        self.start_time = None
        self.duration = 1.5

    def upgrade(self):
        pass

    def start_animation(self):
        self.start_time = time.time()

    def get_reward(self,power):
        if self.start_time and time.time() - self.start_time > self.duration:
            self.start_time = None

        if not self.timer:
            self.timer = time.time()

        if time.time() - self.timer > self.speed:
            self.timer = time.time()
            if power >= self.power_bar.total_power:
                self.power_bar.power = 10
                return self.reward
            
        return 0
    
    def render_animation(self,screen):
        if self.start_time:
            range_surf = pygame.Surface((self.range *2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(range_surf,(0,255,0,100),(self.range,self.range),self.range)
            screen.blit(range_surf,((self.pos[0] + TILE_SIZE/2) - self.range, (self.pos[1] + TILE_SIZE/2) - self.range))

    def render_extra(self,screen):
        font = self.font
        
        if self.power_bar.power == self.power_bar.total_power:   
            count_text = font.render("Timer:%s/%s"%(int(time.time() - self.timer),self.speed), 1, (0,0,0), None)
            count_text_rect = count_text.get_rect()
            count_text_rect.topleft = (WINDOW_WIDTH - 280,350)
            screen.blit(count_text,count_text_rect)

        count_text = font.render("Power:%s/%s"%(self.power_bar.power,self.power_bar.total_power), 1, (0,0,0), None)
        count_text_rect = count_text.get_rect()
        count_text_rect.topleft = (WINDOW_WIDTH - 280,300)
        screen.blit(count_text,count_text_rect)

class Basic_Healer(Healer):
     def __init__(self,pos):
        super().__init__(pos,10,"healer",speed= 5,reward = 2,range = 150,power = 10)