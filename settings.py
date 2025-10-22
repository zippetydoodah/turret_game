import os
import pygame 

IMAGE_FOLDER = "assets/"

TILE_SIZE = 25

HOTBAR_SLOTS = 5
STACK_SIZE = 1
WAIT_BETWEEN_WAVES = 15
HEALTH_SHOW_TIME = 2

SLOW_DOWN_TIME = 10
WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 800

IMAGES = {
    "zombie":"zombie.png",
    "troll":"troll.png",
    "dragon":"dragon.png",
    
    "grass":"grass.png",
    "ore":"ore.png",
    "base_tile":"base.png",

    "bullet":"bullet.png",
    "flame":"fire_ball.png",
    "laser":"laser.png",

    "flame_turret":"flame_turret_1.png",
    "machine_gun_turret":"turret_2.png",
    "laser_turret":"laser_turret.png",

    "generator":"generator.png",
    "power_plant":"power_plant.png",
    "healer":"healing_turret.png",

    "wall":"wall.png",
    "mine":"mine.png",

    "nuclear_bomb":"nuclear_bomb.png",
    "double_drops":"double_drops.png",
    "freeze_time":"effect_freeze.png",
    "slow_down":"slow_down.png",
    "bomb":"bomb.png",

    "faster_bullets":"faster_bullets.png",
    "fire_rate":"fire_rate.png",
    "increased_health":"increased_health.png",
    "range":"range.png",
    "increased_damage":"increase_damage.png",
    "increased_generation":"increased_generation.png",

    "bin":"bin.png",
    "wrench":"wrench.png",
    "tile_highlight":"turret_highlight.png",
    "notify":"notify.png",

    "slot":"inventory_slot.png",
    "effect_slot":"effect_slot.png",
    "shop_background":"shop_background.png",
    "cash_background":"cash_background.png",
    "defence_background":"defence_background.png",
    "inventory_background":"inventory_background_1.png",
    "effects_background":"effects_background.png",
    "settings_background":"settings_background.png",
    "turret_bg":"turret_bg.png",

    "clicked_shop":"clicked_shop.png",
    "unclicked_shop":"unclicked_shop.png",

    "play":"play.png",
    "pause":"pause.png",

    "clicked_options":"options_clicked.png",
    "unclicked_options":"options_unclicked.png",

    "clicked_play":"clicked_play.png",
    "unclicked_play":"unclicked_play.png",

    "unclicked_defence":"unclicked_defence.png",
    "clicked_defence":"clicked_defence.png",

    "clicked_effects":"clicked_effects.png",
    "unclicked_effects":"unclicked_effects.png",

    "clicked_settings":"clicked_settings.png",
    "unclicked_settings":"unclicked_settings.png",

    "clicked_exit":"clicked_exit.png",
    "unclicked_exit":"unclicked_exit.png",

    "unclicked_fast_forward":"unclicked_fast_forward.png",
    "clicked_fast_forward":"clicked_fast_forward.png",

    "unclicked_achievements":"unclicked_achievements.png",
    "clicked_achievements":"clicked_achievements.png",

    "clicked_skip":"clicked_skip.png",
    "unclicked_skip":"unclicked_skip.png",

    "clicked_chat":"clicked_chat.png",
    "unclicked_chat":"unclicked_chat.png",
}

IMAGE_CACHE = {}

def getImage(name):
    if name in IMAGE_CACHE:
        return IMAGE_CACHE[name]
    
    else:
        filename =IMAGES[name]
        path = os.path.join(IMAGE_FOLDER, filename)
        image = pygame.image.load(path).convert_alpha()

        IMAGE_CACHE[name] = image
        return image
    