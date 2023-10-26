import pygame
import sys
import random

#import all our necessary files
from fish import Fish,fishes
from background import draw_background
from game_parameters import *
from player import Player

#Initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("a school of moving fish")

#clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_height, screen_width*2), random.randint(tile_size, screen_height - tile_size)))

#draw player fish
player = Player(screen_width/2, screen_height/2)

#placeholder for orange fish

while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow keys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print ('you pressed the key up key')
                player.move_up()
            if event.key == pygame.K_DOWN:
                print('you pressed the key down key')
                player.move_down()
            if event.key == pygame.K_LEFT:
                print('you pressed the left arrow')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('you pressed the right key')
                player.move_right()



    #draw background
    screen.blit(background, (0,0))

    #update player fish
    player.update()
    #update
    fishes.update()

    # check if fish have left the screen
    for fish in fishes:  # loop through fish in sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - tile_size)))

    #draw the fish
    fishes.draw(screen)

    #draw the player fish
    player.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

pygame.quit()

