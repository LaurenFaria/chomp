import pygame
import sys

from game_parameters import *
from background import draw_background  #import draw background function

#initialize game
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("learning to get event types")

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print ('you pressed the key up key')
            if event.key == pygame.K_DOWN:
                print ('you pressed te key down key')
            if event.key == pygame.K_LEFT:
                print('you pressed the left arrow')
            if event.key == pygame.K_RIGHT:
                print('you pressed the right key')


    # draw the background
    screen.blit(background, (0,0))

    # update the display
    pygame.display.flip()

pygame.quit()
sys.exit()