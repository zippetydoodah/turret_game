from button import *
from background import *
from settings import *
from fader import *

class Settings:
    def __init__(self):
        self.turret_range_toggle = Button((200,300),"clicked_range_toggle","unclicked_range_toggle",(150,75))
        self.enemy_health = Button((200,400),"clicked_enemy_health","unclicked_enemy_health",(150,75))
        self.background = Background(("settings_background"),(150,150),(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.showing = False
        self.fader = Fader((WINDOW_WIDTH,WINDOW_HEIGHT),150,6,(0,0,0))

    def update_time(self):
        if self.showing and not self.fader.fading:
            self.fader.fade_in()

        if not self.showing and self.fader.fading:
            self.fader.fade_out()
        
        self.fader.update()

    def update_buttons(self,event):
        if self.showing:
            self.enemy_health.pressed_keep(event)
            self.turret_range_toggle.pressed_keep(event)

    def render(self,screen):
        self.fader.render(screen)
        if self.showing:
            self.background.render(screen)
            self.enemy_health.render_2(screen)
            self.turret_range_toggle.render_2(screen)
        