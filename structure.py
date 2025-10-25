from health_bar import *
from power_bar import *
from pygame import Vector2
from upgrades import *

class Structure:
    def __init__(self,pos,health,power,name,upgrades):
        self.pos = pos
        self.name = name
        self.health = health
        self.upgrades = upgrades
        self.health_bar = Health_bar(health,Vector2(self.pos[0],self.pos[1]))
        if power:
            self.power_bar = Power_bar(power,Vector2(self.pos[0],self.pos[1] - 5))
        else:
            self.power_bar = None

        self.UI = Upgrades_UI(self.name,self.upgrades,self.health_bar,self.power_bar)

        self.showing = False
        self.slot = Slot((WINDOW_WIDTH - 170,460),image_size=50)
        self.slot.item = Wrench(1)

    def update_power(self,power):
        if power >= self.power_bar.total_power:
            self.power_bar.power = self.power_bar.total_power
        else:
            self.power_bar.power = 0
        
    def inputs(self,event,mouse_pos,cash,chat):
        if self.showing:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if self.slot.rect.collidepoint(mouse_pos):
                    difference = self.health_bar.total_health - self.health_bar.health

                    if cash.money >= int(difference/2):
                        cash.update( -int(difference/2))
                        self.health_bar.health = self.health_bar.total_health 
       
            self.UI.buy_item(event,cash,chat)

    def render_ui(self,screen,selected_tile):
        
        self.upgrade()
        if self.name == "healer":
            self.render_animation(screen)

        if self.showing and selected_tile.tile.type and selected_tile.tile.turret != self and selected_tile.tile.healer != self and (self.name == "flame_turret" or self.name == "machine_gun_turret" or self.name == "healer"):
            range_surf = pygame.Surface((self.range *2, self.range*2), pygame.SRCALPHA)
            pygame.draw.circle(range_surf,(123,123,123,100),(self.range,self.range),self.range)
            screen.blit(range_surf,((self.pos[0] + TILE_SIZE/2) - self.range, (self.pos[1] + TILE_SIZE/2) - self.range))
        
        if self.showing:
            self.health_bar.render(screen,r = True)
            if self.power_bar:
                self.power_bar.render(screen,r = True)
            self.UI.render(screen)
            self.slot.render(screen)

        if self.showing and (self.name == "generator" or self.name == "healer"):
            self.render_extra(screen)

    def render(self,screen):
        self.health_bar.render(screen)
        self.power_bar.render(screen)