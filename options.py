from button import Button
from settings import *


class Options:
    def __init__(self):
        self.button = Button((WINDOW_WIDTH - 75 ,10),"clicked_options","unclicked_options",(70,70))
        self.exit_button = Button((WINDOW_WIDTH - 75 ,80),"clicked_exit","unclicked_exit",(70,70))
        self.achievements_button = Button((WINDOW_WIDTH - 75 ,150),"clicked_achievements","unclicked_achievements",(70,70))
        self.settings_button = Button((WINDOW_WIDTH - 75 ,290),"clicked_settings","unclicked_settings",(70,70))
        self.chat_button = Button((WINDOW_WIDTH - 75 ,220),"clicked_chat","unclicked_chat",(70,70))
        self.showing = False
        self.exit = False

    def update(self):
        
        if self.button.showing:
            self.showing = True

        if not self.button.showing:
            self.showing = False   

        if self.showing:
            self.exit_button.update()
            self.settings_button.update()
            self.achievements_button.update()
            self.chat_button.update()

    def press(self,event,settings,achievements,chat):

        if self.showing:
            self.exit_button.pressed(event)
            if self.settings_button.pressed(event):
                settings.showing = not settings.showing
            if settings.showing and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                settings.showing = False

            if self.achievements_button.pressed(event):
                pass

            if self.chat_button.pressed(event):
            
                chat.showing = not chat.showing
            if chat.showing and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    chat.showing = False
        if self.exit_button.cooldown_time:
            self.exit = True

    def render(self,screen):
        self.button.update()
        self.button.render(screen)

        if self.showing:
            self.settings_button.render(screen)
            self.achievements_button.render(screen)
            self.exit_button.render(screen)
            self.chat_button.render(screen)