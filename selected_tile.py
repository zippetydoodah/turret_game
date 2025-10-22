import pygame
import os
from settings import *

class HighlightedTile:
    def __init__(self, tile):
        self.tile = tile
        self.image = getImage("tile_highlight")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.tile_highlight_rect = self.image.get_rect()
    
    def render(self, screen):
        
        if self.tile.type and self.tile.turret or self.tile.wall or self.tile.mine or self.tile.generator or self.tile.plant or self.tile.healer:

            if self.tile.turret:
                range_surf = pygame.Surface((self.tile.turret.range *2, self.tile.turret.range*2), pygame.SRCALPHA)
                pygame.draw.circle(range_surf,(123,123,123,100),(self.tile.turret.range,self.tile.turret.range),self.tile.turret.range)
                screen.blit(range_surf,((self.tile.pos.x + TILE_SIZE/2) - self.tile.turret.range, (self.tile.pos.y + TILE_SIZE/2) - self.tile.turret.range))
                self.tile.turret.health_bar.render(screen,True)
                if self.tile.turret.power_bar:
                    self.tile.turret.power_bar.render(screen,True)

            if self.tile.mine:
                range_surf = pygame.Surface((self.tile.mine.range *2, self.tile.mine.range*2), pygame.SRCALPHA)
                pygame.draw.circle(range_surf,(123,123,123,100),(self.tile.mine.range,self.tile.mine.range),self.tile.mine.range)
                screen.blit(range_surf,((self.tile.pos.x + TILE_SIZE/2) - self.tile.mine.range, (self.tile.pos.y + TILE_SIZE/2) - self.tile.mine.range))

            if self.tile.healer:
                range_surf = pygame.Surface((self.tile.healer.range *2, self.tile.healer.range*2), pygame.SRCALPHA)
                pygame.draw.circle(range_surf,(123,123,123,100),(self.tile.healer.range,self.tile.healer.range),self.tile.healer.range)
                screen.blit(range_surf,((self.tile.pos.x + TILE_SIZE/2) - self.tile.healer.range, (self.tile.pos.y + TILE_SIZE/2) - self.tile.healer.range))

                self.tile.healer.health_bar.render(screen,True)
                self.tile.generator.power_bar.render(screen,True)

            if self.tile.wall:
                self.tile.wall.health_bar.render(screen,True)

            if self.tile.generator:
                self.tile.generator.health_bar.render(screen,True)
                self.tile.generator.power_bar.render(screen,True)

            if self.tile.plant:
                self.tile.plant.health_bar.render(screen,True)            

            self.tile_highlight_rect.topleft = self.tile.pos
            screen.blit(self.image, self.tile_highlight_rect)
