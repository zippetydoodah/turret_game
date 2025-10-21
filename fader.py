import pygame

class Fader:
    def __init__(self, screen_size, max_alpha=150, speed=10, color=(0,0,0)):
        self.width, self.height = screen_size
        self.max_alpha = max_alpha
        self.speed = speed
        self.color = color
        self.alpha = 0
        self.target_alpha = 0
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.fading = False

    def fade_in(self): 
        self.target_alpha = self.max_alpha
        self.fading = True

    def fade_out(self): 
        self.target_alpha = 0
        self.fading = True

    def update(self):

        if self.alpha < self.target_alpha:
            self.alpha = min(self.alpha + self.speed, self.target_alpha)
            self.fading = False
        elif self.alpha > self.target_alpha:
            self.fading = False
            self.alpha = max(self.alpha - self.speed, self.target_alpha)

    def render(self, screen):
        if self.alpha > 0:
            self.surface.fill((*self.color, self.alpha))
            screen.blit(self.surface, (0, 0))
