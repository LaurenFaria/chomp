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
for _ in range(115):
    fishes.add(Fish(random.randint(screen_height, screen_width*2), random.randint(tile_size, screen_height - tile_size)))

#draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font to keep score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

#load new sound
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
pardon_me = pygame.mixer.Sound("../assets/sounds/Movie-08.wav")
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
                # play chomp sound
                pygame.mixer.Sound.play(pardon_me)
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()



    #draw background
    screen.blit(background, (0,0))

    #update player fish
    player.update()

    #check for collisions between the player and fish - use group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result:
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        #for x in result:
         #   score += 1
        #draw more green fish on the screen
        for _ in range(len(result)):
            fishes.add(Fish(random.randint(screen_width, screen_width *1.5), random.randint(tile_size, screen_height -2 * tile_size)))
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

    #update score font
    text = score_font.render(f"{score}", True, (255,0,0))
    screen.blit(text, (screen_width - text.get_width()/2 - 30, 0))


    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

pygame.quit()

