from settings import *
from textures import *
from identify_tile import IDENTIFY_TILE
from identify_item import *
from enemy import *
from effects import Effect_slot
from items import *
import math
import random
from tile import * 

class World:
    def __init__(self):
        self.MAP = []
        self.STRUCT_MAP = []

        self.enemies = []
        self.wave = 0
        self.wave_time = None

        self.double_drops_slot = Effect_slot((WINDOW_WIDTH - 100,WINDOW_HEIGHT - 100), image_size=50, end_time = 30)
        self.freeze_time_slot = Effect_slot((WINDOW_WIDTH - 180,WINDOW_HEIGHT - 100), image_size=50, end_time = 10)

        self.since_paused = None
        self.base_tile = None

        self.turrets = []
        self.walls = []
        self.generators = []
        self.healers = []
        self.plants = []
        self.structs = []
        self.font = pygame.font.SysFont('Arial', 25)

    def reset_vars(self):
        self.turrets = []
        self.walls = []
        self.generators = []
        self.structs = []
        self.healers = []
        self.plants = []

    def get_enemies(self,cash,fast_forward,chat):
        if not self.wave_time:
            self.wave_time = time.time()

        if self.wave_time and time.time() - self.wave_time > WAIT_BETWEEN_WAVES:
            self.wave_time = None
            self.wave += 1
            enemy = None
            if self.wave >= 15:
                m = 1
                enemy = "Troll"

            if self.wave >= 50:
                m = 0.5
                enemy = "Dragon"

            elif self.wave < 15 :
                m = 2
                enemy = "Zombie"

            chat.add_text("Round" + str(self.wave) + ":" + enemy + "x" + str(round(self.wave * m)) )

            for i in range(round(self.wave * m)):
                x = random.choice([0,WINDOW_WIDTH])
                y = random.randint(0,WINDOW_HEIGHT)

                if self.wave >= 50:
                    self.enemies.append(Dragon((x,y),self.base_tile.pos))

                elif self.wave >= 15:
                    self.enemies.append(Troll((x,y),self.base_tile.pos))

                else:
                    self.enemies.append(Zombie((x,y),self.base_tile.pos))

        to_remove = []
        for enemy in self.enemies:
            if enemy.pos.x < 0 or enemy.pos.x > WINDOW_WIDTH or enemy.pos.y < 0 or enemy.pos.y > WINDOW_HEIGHT:
                self.enemies.remove(enemy)

            if not self.freeze_time_slot.start_time:
                enemy.move(fast_forward)
            
            if enemy.health_bar.health <= 0:
                to_remove.append(enemy)
                if not self.double_drops_slot.start_time:
                    cash.update(enemy.drops)
                else:
                    cash.update(enemy.drops*2)

        for enemy in to_remove:
            self.enemies.remove(enemy)

    def render_enemies(self,screen):
        for enemy in self.enemies:
            enemy.render(screen)
    
    def button_selection(self,buttons):
        for button in buttons:
            button.showing = False

    def check_collisions(self): 
        to_remove = []
        for enemy in self.enemies:
            if enemy.rect.colliderect(self.base_tile.rect):
                self.base_tile.base.health_bar.update_health(enemy.damage)
                to_remove.append(enemy)

        for e in to_remove:
            self.enemies.remove(e)
        
    def is_alive(self):
        return self.base_tile.base.check_death()

    def skip_round(self):
        self.wave_time = WAIT_BETWEEN_WAVES

    def get_map(self):
        self.MAP = self.generate_tiles()
        self.STRUCT_MAP = self.generate_structs()

        coords = self.coords_change((WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

        self.STRUCT_MAP[coords[0]][coords[1]] = Base_tile(coords[0]*TILE_SIZE,coords[1]*TILE_SIZE)
        self.base_tile = self.STRUCT_MAP[coords[0]][coords[1]]

    def generate_structs(self):
        struct_map = []
        for x in range(0,int(WINDOW_WIDTH/TILE_SIZE)):
            struct_map.append([])
            for y in range(0,int(WINDOW_HEIGHT/TILE_SIZE)):
                struct_map[x].append(None_tile(x * TILE_SIZE,y*TILE_SIZE))

        return struct_map
    
    def generate_tiles(self):
        width = int(WINDOW_WIDTH/TILE_SIZE)
        height = int(WINDOW_HEIGHT/TILE_SIZE)

        TERRAIN_TYPES = ["grass", "grass","grass","grass","azurite"]
        
        grid = [[random.choice(TERRAIN_TYPES) for _ in range(height + 1)] for _ in range(width + 1)]

        for x in range(0, width):
            for y in range(0, height):
                neighbors = [
                    grid[x-1][y],
                    grid[x][y-1],
                    grid[x-1][y-1],

                ]
                if random.random() < 0.99:
                    grid[x][y] = random.choice(neighbors)
        tiles = []
        count = 0

        for tile in grid:
            count2 = 0
            tiles.append([])
            for t in tile:
                if t == "grass":
                    tiles[count].append(Grass(count * TILE_SIZE,count2 * TILE_SIZE))
                if t == "azurite":
                    tiles[count].append(Azurite_tile(count * TILE_SIZE,count2 * TILE_SIZE))

                count2 += 1
            count += 1

        return tiles

    def coords_change(self,coords):
        x = math.floor(coords[0]/TILE_SIZE)
        y = math.floor(coords[1]/TILE_SIZE)
        return (x,y)
    
    def remove_bg_tile(self,tile):
        (x,y) = self.coords_change((tile.pos.x,tile.pos.y))
        self.MAP[x][y] = Grass(tile.pos.x,tile.pos.y)

    def remove_struct_tile(self,tile):
        (x,y) = self.coords_change((tile.pos.x,tile.pos.y))
        self.STRUCT_MAP[x][y] = None_tile(tile.pos.x,tile.pos.y)
    
    def collisions(self):
        for bullet in self.get_bullets():
            for enemy in self.enemies:

                if enemy.rect.colliderect(bullet.rect):
                    enemy.health_bar.update_health(bullet.damage)
                    
                    for turret in self.turrets:
                        for b in turret.turret.bullets_fired:

                            if bullet == b:
                                turret.turret.bullets_fired.remove(b)

    def turret_collisions(self):
        to_remove = set()

        for enemy in self.enemies:
            for turret in self.turrets:
                if enemy.rect.colliderect(turret.rect):
                    turret.turret.health_bar.update_health(enemy.damage)
                    to_remove.add(enemy)

        for enemy in self.enemies:
            for generator in self.generators:
                if enemy.rect.colliderect(generator.rect):
                    generator.generator.health_bar.update_health(enemy.damage)
                    to_remove.add(enemy)

        for enemy in self.enemies:
            for wall in self.walls:
                if enemy.rect.colliderect(wall.rect):
                    wall.wall.health_bar.update_health(enemy.damage)
                    to_remove.add(enemy)

        for enemy in self.enemies:
            for healer in self.healers:
                if enemy.rect.colliderect(healer.rect):
                    healer.healer.health_bar.update_health(enemy.damage)
                    to_remove.add(enemy)

        mine_kill = None
        for enemy in self.enemies:
            for mine in self.get_mines():
                if enemy.rect.colliderect(mine.rect):
                    self.remove_struct_tile(mine)
                    mine_kill = mine

        if mine_kill:
            for enemy in self.enemies:
                if mine_kill.pos.distance_to(enemy.pos) < mine_kill.mine.range:
                    enemy.health_bar.update_health(mine_kill.mine.damage)

        for enemy in to_remove:
            self.enemies.remove(enemy)
    
    def place_turret(self,event,inventory):
        pos = self.coords_change(pygame.mouse.get_pos())
        tile = self.STRUCT_MAP[pos[0]][pos[1]]
        to_remove = []

        if inventory.dragging and inventory.dragging.placeable:
            to_place = IDENTIFY_TILE[inventory.dragging.type]
        else:
            to_place = None

        if tile != self.base_tile and tile not in self.structs and to_place:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                self.STRUCT_MAP[pos[0]][pos[1]] = to_place(pos[0]*TILE_SIZE,pos[1]*TILE_SIZE)
                inventory.dragging = None

        if inventory.dragging and not inventory.dragging.placeable:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:

                if inventory.dragging.type == "nuclear_bomb":
                    self.enemies = []
                    inventory.dragging = None
                
                elif inventory.dragging.type == "double_drops":
                    self.double_drops_slot.item = Effect_x2_drops(1)
                    self.double_drops_slot.start_time = time.time()
                    inventory.dragging = None

                elif inventory.dragging.type == "freeze_time":
                    self.freeze_time_slot.item = Effect_freeze_time(1)
                    self.freeze_time_slot.start_time = time.time()
                    inventory.dragging = None

                elif inventory.dragging.type == "slow_down":
                    pos = pygame.mouse.get_pos()
                    vpos = Vector2(pos[0],pos[1])

                    for enemy in self.enemies:
                        if vpos.distance_to(enemy.pos) < inventory.dragging.range:
                            enemy.slow_down = time.time()
                    inventory.dragging = None

                elif inventory.dragging.type == "bomb":
                    pos = pygame.mouse.get_pos()
                    vpos = Vector2(pos[0],pos[1])

                    for enemy in self.enemies:
                        if vpos.distance_to(enemy.pos) < inventory.dragging.range:
                            to_remove.append(enemy)

                    inventory.dragging = None
                    for e in to_remove:
                        self.enemies.remove(e)
                
    def break_turret(self,event,inventory):
        pos = self.coords_change(pygame.mouse.get_pos())
        tile = self.STRUCT_MAP[pos[0]][pos[1]]

        if tile.type:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                inventory.add_item(tile.type,1)
                self.STRUCT_MAP[pos[0]][pos[1]] = None_tile(tile.pos.x,tile.pos.y)

    def identify_turret(self,pos):
        x_idx, y_idx = int(pos.x), int(pos.y)
        max_x = len(self.STRUCT_MAP)
        max_y = len(self.STRUCT_MAP[0]) if max_x > 0 else 0

        # Clamp x and y to be within bounds
        x_idx = max(0, min(x_idx, max_x - 1))
        y_idx = max(0, min(y_idx, max_y - 1))

        return self.STRUCT_MAP[x_idx][y_idx]
    
    def add_tile(self,pos,type):
        self.MAP[pos.x/TILE_SIZE][pos.y/TILE_SIZE] = IDENTIFY_TILE[type](pos.x,pos.y)

    def shoot_check(self):

        for enemy in self.enemies:
            for turret in self.turrets:  
                dx = enemy.pos.x - (turret.pos.x + TILE_SIZE/2)
                dy = enemy.pos.y - (turret.pos.y + TILE_SIZE/2)
                distance = (dx**2 + dy**2)**0.5

                if distance <= turret.turret.range:
                    turret.turret.shoot(enemy.pos)

    def heal_turret(self,amount,tile):
        for struct in self.structs:
            if struct != tile:

                dx = struct.pos.x - (tile.pos.x + TILE_SIZE/2)
                dy = struct.pos.y - (tile.pos.y + TILE_SIZE/2)
                distance = (dx**2 + dy**2)**0.5
                
                if distance <= tile.healer.range:
                    
                    if struct.generator:
                        if struct.generator.health_bar.health < struct.generator.health_bar.total_health:
                            struct.generator.health_bar.update_health(-amount)
                            tile.healer.start_animation()

                    if struct.wall:
                        if struct.wall.health_bar.health < struct.wall.health_bar.total_health:
                            struct.wall.health_bar.update_health(-amount)
                            tile.healer.start_animation()

                    if struct.turret:   
                        if struct.turret.health_bar.health < struct.turret.health_bar.total_health:
                            struct.turret.health_bar.update_health(-amount)
                            tile.healer.start_animation()

                    if struct.plant:
                       if struct.plant.health_bar.health < struct.plant.health_bar.total_health:
                            struct.plant.health_bar.update_health(-amount)
                            tile.healer.start_animation()
                            
                    if struct.healer:
                        if struct.healer.health_bar.health < struct.healer.health_bar.total_health:
                            struct.healer.health_bar.update_health(-amount)
                            tile.healer.start_animation()

    def generate_money(self,cash,power):
        total_power = power.power
        used_power = 0

        for g in self.generators:
            used_power += g.generator.power_bar.total_power
            g.generator.update_power(total_power)
            cash.money += g.generator.get_reward(total_power)
            total_power -= g.generator.power_bar.total_power

        for h in self.healers:
            used_power += h.healer.power_bar.total_power
            h.healer.update_power(total_power)
            to_add = h.healer.get_reward(total_power)

            if to_add:
                self.heal_turret(h.healer.reward,h)

            total_power -= h.healer.power_bar.total_power
        
        for t in self.turrets:
            if t.turret.power_bar:
                used_power += t.turret.power_bar.total_power
                t.turret.update_power(total_power)
                total_power -= t.turret.power_bar.total_power

        power.usage = used_power

    def generate_power(self,power):
        total_power = 0

        for p in self.plants:
            coords = self.coords_change(p.pos)
            source_tile = self.MAP[coords[0]][coords[1]]

            if source_tile.type and source_tile.ore:
                if source_tile.ore.amount > 0:
                    p.plant.power_bar.power = p.plant.power_bar.total_power
                    if p.plant.get_reward(source_tile):
                        source_tile.ore.amount -= 1
                    total_power += p.plant.power_bar.power
                else:
                    self.MAP[coords[0]][coords[1]] = Grass(coords[0]*TILE_SIZE,coords[1]*TILE_SIZE)
            else:
                p.plant.power_bar.power = 0


        power.power = total_power

    def check_health(self):
        turrets = self.turrets
        walls = self.walls
        generators = self.generators
        healers = self.healers
        plants = self.plants

        to_remove = []
        for wall in walls:
            if wall.wall.health_bar.health <= 0:
                to_remove.append(wall)

        for turret in turrets:
            if turret.turret.health_bar.health <= 0:
                to_remove.append(turret)

        for generator in generators:
            if generator.generator.health_bar.health <= 0:
                to_remove.append(generator)

        for healer in healers:
            if healer.healer.health_bar.health <= 0:
                to_remove.append(healer)

        for plant in plants:
            if plant.plant.health_bar.health <= 0:
                to_remove.append(plant)

        for tile in to_remove:
            self.remove_struct_tile(tile)
    
    def get_bullets(self):
        
        bullets = []
        turrets = self.turrets
        for turret in turrets:
            if turret.turret.bullets_fired:
                bullets += turret.turret.bullets_fired
        return bullets
    
    def get_power_plants(self):
        plants = []
        for column in self.STRUCT_MAP:
            for w in column:
                if w.type and w.plant:
                    plants.append(w)

        self.plants = plants
        self.structs.extend(plants)

    def get_healers(self):       
        healers = []
        for column in self.STRUCT_MAP:
            for h in column:
                if h.type and h.healer:
                    healers.append(h)

        self.healers = healers
        self.structs.extend(healers)

    def get_walls(self):        
        walls = []
        for column in self.STRUCT_MAP:
            for w in column:
                if w.type and w.wall:
                    walls.append(w)
        self.walls = walls
        self.structs.extend(walls)

    def get_generators(self):
        generators = []
        for column in self.STRUCT_MAP:
            for g in column:
                if g.type and g.generator:
                    generators.append(g)
        self.generators = generators
        self.structs.extend(generators)

    def get_turrets(self):
        
        turrets = []
        for column in self.STRUCT_MAP:
            for t in column:
                if t.type and t.turret:
                    turrets.append(t)
        self.turrets = turrets
        self.structs.extend(turrets)
    
    def get_mines(self):
        mines = []
        for column in self.STRUCT_MAP:
            for t in column:
                if t.type and t.mine:
                    mines.append(t)
        return mines
    
    def get_clicked_structs(self,event):
        structs = self.structs
        pos = self.coords_change(pygame.mouse.get_pos())
        pos = (pos[0]*TILE_SIZE,pos[1]*TILE_SIZE)
        showing_struct = None

        for t in structs:
            if t.pos == pos:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if t.turret:
                        t.turret.showing = not t.turret.showing
                        showing_struct = t
                        
                    if t.generator:
                        t.generator.showing = not t.generator.showing
                        showing_struct = t

                    if t.wall:
                        t.wall.showing = not t.wall.showing
                        showing_struct = t

                    if t.plant:
                        t.plant.showing = not t.plant.showing
                        showing_struct = t

                    if t.healer:
                        t.healer.showing = not t.healer.showing
                        showing_struct = t

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if t.turret and t.turret.showing:
                    t.turret.showing = False

                if t.wall and t.wall.showing:
                    t.wall.showing = False

                if t.generator and t.generator.showing:
                    t.generator.showing = False

                if t.plant and t.plant.showing:
                    t.plant.showing = False

                if t.healer and t.healer.showing:
                    t.healer.showing = False

        if showing_struct:
            for t in structs:
                if t != showing_struct:

                    if t.generator:
                        t.generator.showing = False

                    if t.wall:
                        t.wall.showing = False

                    if t.turret:
                        t.turret.showing = False

                    if t.plant:
                        t.plant.showing = False

                    if t.healer:
                        t.healer.showing = False

    def move_bullets(self,fast_forward):
        bullets = self.get_bullets()
        for bullet in bullets:
            bullet.move(fast_forward)
            
    def render_bullets(self,screen):
        bullets = self.get_bullets()
        for bullet in bullets:
            bullet.render(screen)
    
    def update_effects(self,pause):
        self.double_drops_slot.time_update(pause)
        self.freeze_time_slot.time_update(pause)

    def check_settings(self,settings,pause_button):
        if settings.showing and pause_button.showing == False:
            pause_button.showing = True
            
    def pause_time(self,pause_button):
        if not pause_button.showing:
            if not self.since_paused:
                self.since_paused = time.time()
                
        else:
            if self.since_paused:
                print(time.time() - self.since_paused)
                self.since_paused = None
    
    def render_effects(self,inventory,screen):
        if inventory.showing:
            self.double_drops_slot.render(screen)
            self.freeze_time_slot.render(screen)

    def render_wave_number(self,screen,inventory):
        if inventory.showing:
            self.base_tile.base.render(screen)
            font = self.font
            text = font.render("Round:%s"%(str(self.wave)), 1, (0,0,0), None)
            textRect = text.get_rect()
            textRect.topleft = (WINDOW_WIDTH - 400,WINDOW_HEIGHT-90)
            screen.blit(text,textRect)

            if self.wave_time:
                text = font.render("Time to wave:%s"%(str(int(WAIT_BETWEEN_WAVES - (time.time() - self.wave_time)))), 1, (0,0,0), None)
                textRect = text.get_rect()
                textRect.topleft = (WINDOW_WIDTH - 400,WINDOW_HEIGHT-60)
                screen.blit(text,textRect)
    
    def click_turrets(self,event,cash,chat):
        for struct in self.structs:
            if struct.turret:
                struct.turret.inputs(event,pygame.mouse.get_pos(),cash,chat)
            if struct.wall:
                struct.wall.inputs(event,pygame.mouse.get_pos(),cash,chat)
            if struct.generator:
                struct.generator.inputs(event,pygame.mouse.get_pos(),cash,chat)
            if struct.plant:
                struct.plant.inputs(event,pygame.mouse.get_pos(),cash,chat)
            if struct.healer:
                struct.healer.inputs(event,pygame.mouse.get_pos(),cash,chat)
        
    def render_turret(self,screen,selected_tile):
        for struct in self.structs:
            
            if struct.turret:
                struct.turret.UI.checking()
                struct.turret.render_ui(screen,selected_tile)

            if struct.wall:
                struct.wall.UI.checking()
                struct.wall.render_ui(screen,selected_tile)

            if struct.generator:
                struct.generator.UI.checking()
                struct.generator.render_ui(screen,selected_tile)

            if struct.plant:
                struct.plant.UI.checking()
                struct.plant.render_ui(screen,selected_tile)

            if struct.healer:
                struct.healer.UI.checking()
                struct.healer.render_ui(screen,selected_tile)

    def render(self,screen,selected_tile):
        to_render = []
        for column in self.MAP:
            for t in column:
                t.render(screen)

        for column in self.STRUCT_MAP:
            for t in column:

                t.render(screen)
                if t.type:
                    if t.turret:
                        to_render.append(t)
                    if t.wall:
                        to_render.append(t)

        for t in to_render:
            if t.turret:
                t.turret.health_bar.render(screen)
            if t.wall:
                t.wall.health_bar.render(screen)

        self.base_tile.base.render(screen)
    
        self.render_turret(screen,selected_tile)
    