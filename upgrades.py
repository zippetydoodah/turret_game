from slots import Slot
from identify_item import *
from background import *
import time

class Upgrades_UI:
    def __init__(self,upgrades_list,turret_health):
        self.slots = []
        self.upgrade_list = upgrades_list
        self.background = Background("turret_bg",(WINDOW_WIDTH - 300,150),(210,420))

        x = WINDOW_WIDTH - 280
        y =  210
        for upgrade in self.upgrade_list:
            upgrade_instance = upgrade((x,y))
            self.slots.append(upgrade_instance)
            y += 55

        self.turret_health = turret_health

    def buy_item(self,event,cash,chat):
        mouse_pos = pygame.mouse.get_pos()
        for slot in self.slots:
        
            if slot.slot.rect.collidepoint(mouse_pos) and not slot.slot.time_clicked and cash.money >= slot.current_price:
                
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and slot.slot.item and slot.level != slot.max_level:
                    if cash.money >= slot.current_price:
                        chat.add_text(("Upgraded: " + slot.name + ", Level: " + str(slot.level)))
                        cash.update(-slot.current_price)
                        slot.level += 1
                        slot.slot.time_clicked = time.time()
            
            elif slot.slot.time_clicked and time.time() - slot.slot.time_clicked > slot.slot.cooldown_time:
                slot.slot.time_clicked = None

    def checking(self):
        mouse_pos = pygame.mouse.get_pos()
        for slot in self.slots:
            if slot.slot.rect.collidepoint(mouse_pos):
                slot.slot.checking = True
            else:
                slot.slot.checking = False
                
            slot.update_price()

    def render(self,screen):
        self.background.render(screen)
        for slot in self.slots:
            slot.render(screen)
        font = pygame.font.SysFont('Arial', 25)

        if not self.upgrade_list == []:
            Title_text = font.render("Upgrades:", 1, (0,0,0), None)
            Title_text_rect = Title_text.get_rect()
            Title_text_rect.topleft = (WINDOW_WIDTH - 280,170)
            screen.blit(Title_text,Title_text_rect)

        health_text = font.render("Health:%s/%s"%(self.turret_health.health,self.turret_health.total_health), 1, (0,0,0), None)
        health_text_rect = health_text.get_rect()
        health_text_rect.topleft = (WINDOW_WIDTH - 280,440)
        screen.blit(health_text,health_text_rect)
        hitrect1 = pygame.Rect(WINDOW_WIDTH - 280,465,100, 25)

        hitrect = pygame.Rect(WINDOW_WIDTH - 280,465, (self.turret_health.health * self.turret_health.multiplier), 25)
        pygame.draw.rect(screen, (255, 0, 0),hitrect1)
        pygame.draw.rect(screen, (0, 255, 0), hitrect)

class Upgrade_slot:
    def __init__(self,pos,name,price_multiplier,start_price,max_level):
        self.level = 1
        self.max_level = max_level
        self.multiplier = price_multiplier
        self.start_price = start_price
        self.current_price = start_price
        self.name = name
        self.pos = pos
        self.slot = Slot(self.pos,image_size=50)
        self.slot.item = IDENTIFY_ITEM[self.name](1)
        self.font = pygame.font.SysFont('Arial', 25)

    def update_price(self):
        self.current_price = (self.level*self.start_price)

    def render(self,screen):
        self.slot.render(screen)
        
        if not self.slot.checking:
            t = "$" + str(self.current_price)
            if self.level == self.max_level:
                t = "MAX"
            text = self.font.render("--->   %s"%(t), 1, (0,0,0), None)
            textRect = text.get_rect()
            textRect.topleft = (self.pos[0] + 50,self.pos[1] + 10)
            screen.blit(text,textRect)

        if self.slot.checking:
            infotext = self.font.render("-> %s"%(str(self.slot.item.type)), 1, (0,0,0), None)
            infotextRect = infotext.get_rect()
            infotextRect.topleft = (self.pos[0] + 50,self.pos[1] + 10)
            screen.blit(infotext,infotextRect)

        infotext = self.font.render("Level:%s"%(str(self.level)), 1, (0,0,0), None)
        infotextRect = infotext.get_rect()
        infotextRect.topleft = (self.pos[0] + 50,self.pos[1] + 35)
        screen.blit(infotext,infotextRect)

class Faster_bullets_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"faster_bullets",2.5,5,5)
    
class Fire_rate_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"fire_rate",2,10,5)
    
class Increased_health_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"increased_health",1.5,30,5)

class Increased_range_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"range",3,40,3)

class Increased_damage_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"increased_damage",1.5,20,8)

class Increased_generation_upgrade(Upgrade_slot):
    def __init__(self,pos):
        super().__init__(pos,"increased_generation",1.5,20,8)