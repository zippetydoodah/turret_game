import pygame
from slots import Slot
from settings import *
from identify_item import *
from background import Background
import math

class Inventory:
    def __init__(self):

        self.slots = {}
        self.dragging = None
        self.selected_slot = 1
        self.dragging = None
        self.background = Background("inventory_background",(0, WINDOW_HEIGHT - 150),(WINDOW_WIDTH,200))
        self.bin_slot = Slot((50,WINDOW_HEIGHT - 100),image_size=50)
        self.bin_slot.item = IDENTIFY_ITEM["bin"](1)
        self.showing = True

        x = WINDOW_WIDTH/4  
        y =  WINDOW_HEIGHT - 100
        for i in range(1, HOTBAR_SLOTS + 1):
            self.slots[i] = Slot((x,y),image_size=50)
            x += 60

    # def resize(self, new_width,new_height):
    #     self.background = Background("inventory_background",(0, new_height - 150),(new_width,200))

    def checking(self):
        mouse_pos = pygame.mouse.get_pos()

        for key, slot in self.slots.items():
            if slot.rect.collidepoint(mouse_pos):
                slot.checking = True
            else:
                slot.checking = False

    def add_item(self,type,quantity):
        for key, slot in self.slots.items():
            if slot.item == None:
                slot.item = IDENTIFY_ITEM[type](quantity)
                break

            if slot.item and slot.item.type == type and slot.item.quantity < STACK_SIZE and slot.item.quantity  + quantity < STACK_SIZE:
                slot.item.quantity += quantity
                break

    def is_showing(self,event):
        if event.type == pygame.KEYDOWN and event.key ==pygame.K_i:
            if self.showing:
                self.showing = False
            else:
                self.showing = True

    def drag(self,event):
        mouse_pos = pygame.mouse.get_pos()

        for key, slot in self.slots.items():
            if slot.rect.collidepoint(mouse_pos):
                slot.checking = True
            else:
                slot.checking = False

        if not self.dragging:
            for key, slot in self.slots.items():
                if slot.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and slot.item:
                        self.dragging = slot.item
                        slot.item = None

        elif self.dragging:

            if self.bin_slot.rect.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.dragging = None

            for key, slot in self.slots.items():
                if slot.rect.collidepoint(mouse_pos):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not slot.item:
                        slot.item = self.dragging
                        self.dragging = None

                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and slot.item.type == self.dragging.type:
                        if slot.item.quantity + self.dragging.quantity <= STACK_SIZE:
                            slot.item.quantity += self.dragging.quantity
                            self.dragging = None

                        elif slot.item.quantity + self.dragging.quantity > STACK_SIZE:
                            diff = STACK_SIZE - slot.item.quantity
                            slot.item.quantity += diff
                            self.dragging.quantity -= diff
                            
    def remove_item(self):

        if self.slots[self.selected_slot].item:
            self.slots[self.selected_slot].item.quantity -= 1

            if self.slots[self.selected_slot].item.quantity == 0:
                self.slots[self.selected_slot].item = None
            
    def render(self,screen):
        mouse_pos = pygame.mouse.get_pos()
        x = math.floor(mouse_pos[0]/TILE_SIZE) *TILE_SIZE
        y = math.floor(mouse_pos[1]/TILE_SIZE) * TILE_SIZE
        pos = (x,y)
        
        if self.showing:
            self.background.render(screen)
            
            for slot in self.slots:
                self.slots[slot].render(screen)

            for slot in self.slots:
                self.slots[slot].render_item_info(screen)
            
            self.bin_slot.render(screen)
                
        if self.dragging:

            drag_image = getImage(self.dragging.type)
            drag_image = pygame.transform.scale(drag_image, (25,25))
            drag_rect = drag_image.get_rect()
            drag_rect.center = (pygame.mouse.get_pos())
            screen.blit(drag_image,drag_rect)

            if self.dragging.range:
                range_surf = pygame.Surface((self.dragging.range*2, self.dragging.range*2), pygame.SRCALPHA)
                pygame.draw.circle(range_surf,(123,123,123,100),(self.dragging.range,self.dragging.range),self.dragging.range)
                screen.blit(range_surf,((pos[0] + TILE_SIZE/2) - self.dragging.range, (pos[1] + TILE_SIZE/2) - self.dragging.range))