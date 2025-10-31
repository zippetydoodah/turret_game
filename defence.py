from button import Button
from background import *
from identify_item import *
from settings import *
from slots import Slot
from prices import *
import time

class Defence:
    def __init__(self):
        self.button = Button((530 ,10),"clicked_defence","unclicked_defence",(150,75))
        self.background = Background("defence_background",(0,150),(210,420))
        self.slots = {}
        self.showing = False
        
        x = 30
        y =  230
        for i in range(1, len(defence_slot_order) + 1):
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
            if slot in defence_slot_order:
                if not self.slots[slot].item:
                    self.slots[slot].item = IDENTIFY_ITEM[defence_slot_order[slot]](1)

    def render(self,screen):
        self.button.update()
        self.button.render(screen)

        if self.showing:
            self.background.render(screen)

            for slot in self.slots:
                self.slots[slot].render(screen)
                self.slots[slot].render_item_price(screen)
    