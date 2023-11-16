import pygame
from game_parameters import *
import random
from fish import Fish, fishes
from enemy import Enemy

def draw_background(surf):
    #Load our tiles from the assets folder
    sand = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    water = pygame.image.load("../assets/sprites/water.png").convert()
    #Make PNGs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    # fill the screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x, y))

    # draw a sandy bottom
    for x in range(0, screen_width, tile_size):
        surf.blit(sand, (x, screen_height - tile_size))

    # place seagrass randomly across the bottom
    for _ in range(4):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height - tile_size * 2))

def add_fish(numb_fish):
    for _ in range(numb_fish):
        fishes.add(Fish(random.randint(screen_height, screen_width * 2), random.randint(tile_size, screen_height - tile_size)))

def add_enemies(numb_enemies):
    for _ in range(numb_enemies):
        enemies.add(Enemy(random.randint(screen_height, screen_width * 2), random.randint(tile_size, screen_height - tile_size)))
