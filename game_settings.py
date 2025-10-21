from button import *
from background import *
from settings import *
from fader import *

class Settings:
    def __init__(self):
        #self.turret_range_toggle = Button((100,WINDOW_HEIGHT - 200),"unclicked_range_toggle","clicked_range_toggle",(75,75))
        self.background = Background(("settings_background"),(0,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.showing = False
        self.fader = Fader((WINDOW_WIDTH,WINDOW_HEIGHT),150,6,(0,0,0))

    def update_time(self):
        if self.showing and not self.fader.fading:
            self.fader.fade_in()

        if not self.showing and self.fader.fading:
            self.fader.fade_out()
        
        self.fader.update()

    def render(self,screen):
        self.fader.render(screen)
        if self.showing:
            #self.turret_range_toggle.render(screen)
            self.background.render(screen)
        