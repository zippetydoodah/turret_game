
class Item:
    def __init__(self,type,quantity,placeable,range = None):
        self.type = type
        self.quantity = quantity
        self.placeable = placeable
        self.range = range

class Flame_turret_item(Item):
    def __init__(self,quantity):
        super().__init__(type = "flame_turret",quantity = quantity,placeable= True, range = 100)

class Healer_item(Item):
    def __init__(self,quantity):
        super().__init__(type = "healer",quantity = quantity,placeable= True, range = 150)

class Machine_gun_turret_item(Item):
    def __init__(self,quantity):
        super().__init__(type = "machine_gun_turret",quantity = quantity,placeable = True, range = 300)

class Generator_turret(Item):
    def __init__(self,quantity):
        super().__init__(type = "generator",quantity = quantity,placeable = True)

class Power_plant_item(Item):
    def __init__(self,quantity):
        super().__init__(type = "power_plant",quantity = quantity,placeable = True)
    
class Effect_nuclear(Item):
    def __init__(self,quantity):
        super().__init__(type = "nuclear_bomb",quantity = quantity,placeable = False)

class Effect_x2_drops(Item):
    def __init__(self,quantity):
        super().__init__(type = "double_drops",quantity = quantity,placeable = False)

class Effect_freeze_time(Item):
    def __init__(self,quantity):
        super().__init__(type = "freeze_time",quantity = quantity,placeable = False)

class Effect_slow_down(Item):
    def __init__(self,quantity):
        super().__init__(type = "slow_down",quantity = quantity,placeable = False,range = 150)

class Effect_bomb(Item):
    def __init__(self,quantity):
        super().__init__(type = "bomb",quantity = quantity,placeable = False,range = 150)

class Wall(Item):
    def __init__(self,quantity):
        super().__init__(type = "wall",quantity = quantity,placeable = True)

class Mine(Item):
    def __init__(self,quantity):
        super().__init__(type = "mine",quantity = quantity,placeable = True, range = 50)

class Bin(Item):
    def __init__(self,quantity):
        super().__init__(type = "bin",quantity = quantity,placeable= False)

class Wrench(Item):
    def __init__(self,quantity):
        super().__init__(type = "wrench",quantity = quantity,placeable= False)

class Fire_rate(Item):
    def __init__(self,quantity):
        super().__init__(type = "fire_rate",quantity = quantity,placeable= False)

class Faster_bullets(Item):
    def __init__(self,quantity):
        super().__init__(type = "faster_bullets",quantity = quantity,placeable= False)

class Increased_health(Item):
    def __init__(self,quantity):
        super().__init__(type = "increased_health",quantity = quantity,placeable= False)

class Range(Item):
    def __init__(self,quantity):
        super().__init__(type = "range",quantity = quantity,placeable= False)

class Increased_damage(Item):
    def __init__(self,quantity):
        super().__init__(type = "increased_damage",quantity = quantity,placeable= False)

class Increased_generation(Item):
    def __init__(self,quantity):
        super().__init__(type = "increased_generation",quantity = quantity,placeable= False)