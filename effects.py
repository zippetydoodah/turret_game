from button import Button
from background import *
from settings import *
from prices import *
from identify_item import *
from slots import Slot
import time

class Effects:
    def __init__(self):
        self.slots = {}
        self.button = Button((740 ,10),"clicked_effects","unclicked_effects",(150,75))
        self.background = Background("effects_background",(0,150),(210,420))
        self.showing = False
        
        x = 30
        y =  230
        for i in range(1, len(effects_slot_order) + 1):
            self.slots[i] = Slot((x,y),image_size=50)
            y += 55

    def buy_item(self,event,inventory,cash):
        mouse_pos = pygame.mouse.get_pos()
        inventory_check = False
        for islot in inventory.slots:
            if not inventory.slots[islot].item:
                inventory_check = True

        if inventory_check and self.showing:
            for key, slot in self.slots.items():
                
                if slot.rect.collidepoint(mouse_pos) and not slot.time_clicked and cash.money >= prices[slot.item.type]:
                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and slot.item:
                        inventory.add_item(slot.item.type,slot.item.quantity)
                        cash.update(-prices[slot.item.type])
                        slot.time_clicked = time.time()
                
                elif slot.time_clicked and time.time() - slot.time_clicked > slot.cooldown_time:
                    slot.time_clicked = None
    
    def checking(self):
        mouse_pos = pygame.mouse.get_pos()
        for key, slot in self.slots.items():
            if slot.rect.collidepoint(mouse_pos):
                slot.checking = True
            else:
                slot.checking = False
                
    def update(self):
        
        if self.button.showing:
            self.showing = True

        if not self.button.showing:
            self.showing = False  

    def restock(self):
        for slot in self.slots:
            if slot in effects_slot_order:
                if not self.slots[slot].item:
                    self.slots[slot].item = IDENTIFY_ITEM[effects_slot_order[slot]](1)

    def render(self,screen):
        self.button.update()
        self.button.render(screen)
        if self.showing:
            self.background.render(screen)
            for slot in self.slots:
                self.slots[slot].render(screen)
                self.slots[slot].render_item_price(screen)
    
class Effect_slot:
    def __init__(self,pos,image_size = 50,end_time = None):
        self.pos = pos 
        self.item = None
        self.image = pygame.transform.scale(getImage("effect_slot"),(image_size,image_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos[0],self.pos[1])
        self.end_time = end_time
        self.start_time = None
        self.pause_time = None
    
    def time_update(self, pause):
        if not self.item:
            return

        # Handle pausing/unpausing
        if pause:
            if not self.pause_time:
                # Just entered pause state
                self.pause_time = time.time()
        else:
            if self.pause_time:
                # Just unpaused, shift start_time forward
                paused_duration = time.time() - self.pause_time
                self.start_time += paused_duration
                self.pause_time = None

        # Only tick down if not paused
        if not self.pause_time:
            if time.time() - self.start_time > self.end_time:
                self.item = None
                self.start_time = None

    def render(self,screen):      
        
        screen.blit(self.image,self.rect)

        if self.item:
            item_image = getImage(self.item.type)
            item_image = pygame.transform.scale(item_image, (30,30))
            item_rect = item_image.get_rect()
            item_rect.center = self.rect.center 
            screen.blit(item_image, item_rect)

            
            if self.pause_time:
                time_left = int(self.end_time - (self.pause_time - self.start_time))
            else:
                time_left = int(self.end_time - (time.time() - self.start_time))

            font = pygame.font.SysFont('Arial', 25)
            text = font.render("%s"%(str(time_left)), 1, (0,0,0), None)
            textRect = text.get_rect()
            textRect.topleft = (self.pos[0] + 50,self.pos[1] +50)
            screen.blit(text,textRect)
