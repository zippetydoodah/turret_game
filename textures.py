import pygame
from settings import *
from tile import Tile
from Turret import *
from wall import *
from mine import *
from generator import *
from power_plant import *
from healer import *

class Grass(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if Grass.tile_image is None:
            image = getImage("grass")
            Grass.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) 

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"grass",IMAGES["grass"],Grass.tile_image)

class Power_plant_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if Power_plant_tile.tile_image is None:
            image = getImage("power_plant")
            Power_plant_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) 

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"power_plant",IMAGES["power_plant"],Power_plant_tile.tile_image, plant = Basic_power_plant)

class Ore(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if Ore.tile_image is None:
            image = getImage("ore")
            Ore.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) 

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"ore",IMAGES["ore"],Ore.tile_image)

class Base_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if Base_tile.tile_image is None:
            image = getImage("base_tile")
            Base_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE)) 

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"base_tile",IMAGES["base_tile"],Base_tile.tile_image,turret = None,base = True)

class Machine_gun_turret(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if Machine_gun_turret.tile_image is None:
            image = getImage("machine_gun_turret")
            Machine_gun_turret.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"machine_gun_turret",IMAGES["machine_gun_turret"],Machine_gun_turret.tile_image,turret=Machine_gun)

class Flame_turret_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Flame_turret_tile.tile_image is None:
            image = getImage("flame_turret")
            Flame_turret_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"flame_turret",IMAGES["flame_turret"],Flame_turret_tile.tile_image,turret=Flame_turret)

class Laser_turret_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Laser_turret_tile.tile_image is None:
            image = getImage("laser_turret")
            Laser_turret_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"laser_turret",IMAGES["laser_turret"],Laser_turret_tile.tile_image,turret=Laser_turret)

class Mine_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Mine_tile.tile_image is None:
            image = getImage("mine")
            Mine_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"mine",IMAGES["mine"],Mine_tile.tile_image,mine = Basic_mine)

class Wall_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Wall_tile.tile_image is None:
            image = getImage("wall")
            Wall_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y,"wall",IMAGES["wall"],Wall_tile.tile_image,wall = Stone_wall)


class Generator_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Generator_tile.tile_image is None:
            image = getImage("generator")
            Generator_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y, "generator", IMAGES["generator"], Generator_tile.tile_image, generator= Basic_generator)

class Healer_tile(Tile):
    tile_image = None
    @staticmethod
    def load_image():
        if  Healer_tile.tile_image is None:
            image = getImage("healer")
            Healer_tile.tile_image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

    def __init__(self, x, y):
        self.load_image()
        super().__init__(x, y, "healer", IMAGES["healer"], Healer_tile.tile_image, healer = Basic_Healer)
