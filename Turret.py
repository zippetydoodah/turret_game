from ammunition import *
import time
from health_bar import Health_bar
from button import *
from upgrades import *
from items import *
from structure import *

class Basic_Turret(Structure):
    def __init__(self,centre_pos,pos,speed, ammo, name, range,health,power = None,upgrades = []):
        super().__init__(pos,health,power,name,upgrades)
        
        self.target_enemy = None
        self.centre_pos = centre_pos
        self.base_speed = speed
        self.speed = speed
        self.ammo = ammo
        self.base_range = range
        self.range = range

        self.base_bullet_speed = self.ammo((0,0),(0,0)).speed

        self.elapsed_cooldown_time = None   
        self.elapsed_fire_time = None 
        self.speed_timer = None

        self.bullets_fired = []

    def upgrade(self):
        self.health_bar.total_health =  self.health_bar.initial_health + 5 * (self.UI.slots[1].level - 1 )
        self.speed = self.base_speed - (0.05 * self.UI.slots[2].level)

        if Increased_range_upgrade in self.upgrades:    
            self.range = self.base_range + (self.UI.slots[3].level * 10)
            
        if Increased_damage in self.upgrades:
            self.ammo.damage = self.ammo.base_damage + self.UI.slots[4].level * 2

        if self.power_bar:
            added_power = 0
            for slot in self.UI.slots:
                if slot.level > 1:
                    added_power += slot.level - 1
            self.power_bar.total_power = self.power_bar.initial_power + added_power

    def shoot(self):
        bullet_speed = self.base_bullet_speed + self.UI.slots[0].level

        if not self.speed_timer and not self.elapsed_fire_time:
            if self.power_bar and self.power_bar.power == self.power_bar.total_power:
                self.bullets_fired.append(self.ammo(self.centre_pos,self.target_enemy.pos,bullet_speed))
                self.speed_timer = time.time()
                
            elif not self.power_bar:
                self.bullets_fired.append(self.ammo(self.centre_pos,self.target_enemy.pos,bullet_speed))
                self.speed_timer = time.time()

        if self.speed_timer and time.time() - self.speed_timer > self.speed:
            self.speed_timer = None
    
    def render(self,screen):
        
        to_remove = []
        for ammunition in self.bullets_fired:
            if ammunition.pos.x > WINDOW_WIDTH or ammunition.pos.x < 0 or ammunition.pos.y > WINDOW_HEIGHT or ammunition.pos.y <0:
                to_remove.append(ammunition)
            else:
                ammunition.render(screen)

        for a in to_remove:
            self.bullets_fired.remove(a)
        
class Flame_turret(Basic_Turret):
    def __init__(self,centre_pos,pos):
        super().__init__(centre_pos,pos,speed = 0.5, ammo = Flame_ammo,name ="flame_turret", range = 100,health = 40,upgrades = [Faster_bullets_upgrade,Increased_health_upgrade,Fire_rate_upgrade,Increased_range_upgrade])
# every 0.5 seconds it fires a bullet
# fires for 6 seconds in total and then has 2 second cooldown time before firing again.
class Machine_gun(Basic_Turret):
    def __init__(self,centre_pos,pos):
        super().__init__(centre_pos,pos,speed = 0.3, ammo = Machine_gun_ammo,name ="machine_gun_turret",range = 300,health = 20,upgrades = [Faster_bullets_upgrade,Increased_health_upgrade,Fire_rate_upgrade,Increased_damage_upgrade])

class Laser_turret(Basic_Turret):
    def __init__(self,centre_pos,pos):
        super().__init__(centre_pos,pos,speed = 0.15, ammo = Laser_ammo,name ="laser_turret",range = 150,health = 50,power = 5,upgrades = [Faster_bullets_upgrade,Increased_health_upgrade,Fire_rate_upgrade,Increased_damage_upgrade])
