from button import *
from background import *
from settings import *
from fader import *

class Chat:
    def __init__(self):
        self.chat = []
        self.background = Background(("settings_background"),(0,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
        self.showing = False
        self.fader = Fader((WINDOW_WIDTH,WINDOW_HEIGHT),150,6,(0,0,0))
    
    def add_text(self,text):
        self.chat.append(Text(text,(10,500),30))

    def format_chat(self):
        start_y = WINDOW_HEIGHT - 500  
        spacing = 5
    
        for i, box in enumerate(reversed(self.chat)):
            new_y = start_y - i * (30 + spacing)
            box.update_pos((box.pos[0], new_y))
        
    def update_time(self):
        if self.showing and not self.fader.fading:
            self.fader.fade_in()

        if not self.showing and self.fader.fading:
            self.fader.fade_out()
        self.fader.update()

    def render(self,screen):
        self.fader.render(screen)
        if self.showing:
            self.background.render(screen)
            for text in self.chat:
                text.render(screen)

class Text:
    def __init__(self,text,pos,size):
        self.text = text
        self.pos = pos
        self.speed = 1
        self.font = pygame.font.SysFont('Arial', size)
        self.texts = self.font.render("%s"%(self.text), True, (0,0,0), None)
        self.textRect = self.texts.get_rect()
        self.textRect.topleft = pos

    def update_pos(self,newpos):
        self.pos = newpos

    def render(self,screen):
        self.textRect.topleft = self.pos
        screen.blit(self.texts,self.textRect)
