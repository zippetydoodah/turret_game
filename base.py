from settings import *
from structure import *

class Base(Structure):
    def __init__(self,pos):
        super().__init__(pos,100,None,"base",[])
        
    def upgrade(self):
        pass

    def check_death(self):
        if self.health_bar.health <= 0:
            return False
        else:
            return True # fix this in world so that it just checks structs not if each individual struct
        
    def render(self,screen):
        self.health_bar.render(screen)