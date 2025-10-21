from settings import *
from prices import *

class Slot:
    def __init__(self,pos,image_size = None):
        self.pos = pos 
        self.item = None
        self.image = pygame.transform.scale(getImage("slot"),(image_size,image_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos[0],self.pos[1])
        self.checking = False
        self.time_clicked = None
        self.cooldown_time = 0.1

    def change_position(self,new_pos):
        self.pos = new_pos
        self.rect.topleft = (self.pos)

    def render(self,screen):      

        screen.blit(self.image,self.rect)
        if self.item:
            item_image = getImage(self.item.type)
            item_image = pygame.transform.scale(item_image, (30,30))
            item_rect = item_image.get_rect()
            item_rect.center = self.rect.center 
            screen.blit(item_image, item_rect)

    def render_item_price(self,screen):

        if self.item:
            if not self.checking:
                font = pygame.font.SysFont('Arial', 25)
                text = font.render("--->   $%s"%(str(prices[self.item.type])), 1, (0,0,0), None)
                textRect = text.get_rect()
                textRect.topleft = (self.pos[0] + 50,self.pos[1] + 10)
                screen.blit(text,textRect)

            if self.checking:
                font = pygame.font.SysFont('Arial', 25)
                infotext = font.render("-> %s %s"%(str(self.item.type),(str(self.item.quantity))), 1, (0,0,0), None)
                infotextRect = infotext.get_rect()
                infotextRect.topleft = (self.pos[0] + 50,self.pos[1] + 10)
                screen.blit(infotext,infotextRect)

    def render_item_info(self,screen):

        if self.item:
            if not self.checking:
                font = pygame.font.SysFont('Arial', 25)
                text = font.render("%s"%(str(self.item.quantity)), 1, (0,0,0), None)
                textRect = text.get_rect()
                textRect.topleft = (self.pos[0] + 15,self.pos[1] + 15)

            elif self.checking:
                font = pygame.font.SysFont('Arial', 25)
                infotext = font.render("%s: %s"%(str(self.item.type),(str(self.item.quantity))), 1, (0,0,0), None)
                infotextRect = infotext.get_rect()
                infotextRect.topleft = (self.pos[0],self.pos[1] + 50)

            if not self.checking:
                screen.blit(text,textRect)
            
            else:
                screen.blit(infotext,infotextRect)