import pygame
from pygame import Vector2
from world import World
from selected_tile import *
from textures import *
from inventory import Inventory
from shop import Shop
from cash import Cash
from button import *
from defence import Defence
from effects import Effects
from options import Options
from game_settings import *
from settings import *
from chat import *
from power import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

def game_loop():
    cash = Cash()
    power = Power()

    world = World()

    inventory = Inventory()
    shop = Shop()
    defence = Defence()
    effects = Effects()
    options = Options()
    settings = Settings()
    chat = Chat()
    selected_tile = Selected_tile()
    selected_enemy = Selected_enemy()

    fast_forward = Button((WINDOW_WIDTH - 245,10),"unclicked_fast_forward","clicked_fast_forward",(75,75))
    pause_button = Button((WINDOW_WIDTH - 170,10),"pause","play",(75,75))
    skip_wave_button = Button((WINDOW_WIDTH - 320,10),"clicked_skip","unclicked_skip",(75,75))
    world.get_map()

    while True:

        clock.tick(60)
        screen.fill((0,0,0))
        
        selected_tile.set_tile(world.identify_turret(Vector2(world.coords_change(pygame.mouse.get_pos()))))
        selected_enemy.set_enemy(world.enemy_at_mouse())

        world.get_turrets()
        world.get_generators()
        world.get_walls()
        world.get_power_plants()
        world.get_healers()

        for event in pygame.event.get():

            world.place_turret(event,inventory)
            world.break_turret(event,inventory)
            world.get_clicked_structs(event)
            world.click_turrets(event,cash,chat)
            
            if skip_wave_button.pressed(event):
                world.skip_round()

            if shop.button.pressed(event):
                world.button_selection([defence.button,effects.button])
            shop.buy_item(event,inventory,cash)

            if defence.button.pressed(event):
                world.button_selection([shop.button,effects.button])
            defence.buy_item(event,inventory,cash)

            if effects.button.pressed(event):
                world.button_selection([shop.button,defence.button])
            effects.buy_item(event,inventory,cash)

            options.press(event,settings,None,chat)
            options.button.pressed(event)

            settings.update_buttons(event)

            inventory.drag(event)
            inventory.is_showing(event)

            pause_button.pressed_keep(event)
            fast_forward.pressed_keep(event)

            if event.type == pygame.QUIT:
                quit()
        
        if not world.is_alive():
            menu_loop()

        shop.restock()
        effects.restock()
        defence.restock()

        shop.update()
        chat.format_chat()
        chat.update_time()

        settings.update_time()
        skip_wave_button.update()
        options.update()
        defence.update()
        effects.update()

        shop.checking()
        inventory.checking()
        defence.checking()
        effects.checking()

        world.check_collisions()
        world.turret_collisions()
        world.check_settings(settings,pause_button)
        world.render(screen,selected_tile,settings)

        inventory.render(screen)
        shop.render(screen)
        options.render(screen)
        defence.render(screen)
        effects.render(screen)

        cash.render(screen)
        power.render(screen)

        world.render_effects(inventory,screen)
        world.render_enemies(screen,settings)
        world.render_bullets(screen)
        world.render_wave_number(screen,inventory)
        world.generate_money(cash,power)
        world.generate_power(power)

        selected_enemy.render(screen)
        selected_tile.render(screen)

        if options.exit:
            menu_loop()

        skip_wave_button.render(screen)
        pause_button.render_2(screen)
        fast_forward.render_2(screen)

        world.pause_time(pause_button)
        world.check_health()
        settings.render(screen)
        chat.render(screen)

        if not pause_button.showing:
            world.update_effects(False)
            world.shoot_check()
            world.collisions()
            world.move_bullets(fast_forward)
            world.get_enemies(cash,fast_forward,chat)
        
        if pause_button.showing:
            world.update_effects(True)
        world.reset_vars()
        
        pygame.display.flip()

def menu_loop():
    play_button = Button((WINDOW_WIDTH/2 - 100,300),"clicked_play","unclicked_play",(200,100))

    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            play_button.pressed(event)

            if event.type == pygame.QUIT:
                quit()

        if play_button.showing:
            game_loop()

        play_button.update()
        play_button.render(screen)

        pygame.display.flip()
    

menu_loop()

# make airborn enemies which are generally faster than land enemies apart from:
# make very fast very low health enemies that you need high bullet speed for.
# make turret that specialises in airborn enemies.
# make enemy stats be accessable from selected enemy shows in a box that appears above the enemy as long as you are hovering aboe the enemy: include effects
# make bombs highlight the enemies that will be killed or affected.