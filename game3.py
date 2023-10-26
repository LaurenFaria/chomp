import pygame
import sys
import random
from fish import Fish, fishes #importing a sprite class and sprite group

#Initialize oygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit ot draw tiles")

#load game font
#custom_font = pygame.font.Font("assets/fonts/Gretoon.ttf" , 70)

def draw_background(surf):
    #Load our tiles from the assets folder
    sand = pygame.image.load("C:assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    water = pygame.image.load("assets/sprites/water.png").convert()
    #Make PNGs transparent
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen with water
    for x in range(0,screen_width,tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,y))

    #draw a sandy bottom
    for x in range (0, screen_width, tile_size):
        surf.blit(sand,(x,screen_height - tile_size))

    #place seagrass randomly across the bottom
    for _ in range(4):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x,screen_height-tile_size*2))

    #draw the text
    #text = custom_font.render("Chomp", True, (255,29,0))
    #text = custom_font.render('Chomp', True, (255,29,0))
    #surf.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))

# Main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(0, screen_width-tile_size), random.randint(0,tile_size, screen_height - tile_size)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background
    screen.blit(background, (0, 0))

    # update the display
    pygame.display.flip()


pygame.quit()