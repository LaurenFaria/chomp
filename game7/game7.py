import pygame
import sys
import random

#import all our necessary files
from fish import Fish,fishes
from background import draw_background
from game_parameters import *
from player import Player
from background import draw_background, add_fish, add_enemies
from enemy import enemies


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
add_fish(5)

#add enemy to the screen
add_enemies(3)

#draw player fish
player = Player(screen_width/2, screen_height/2)

#draw enemy fish
enemy = enemy(screen_width/2, screen_height/2)

#load new font to keep score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

#load new sound
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
pardon_me = pygame.mixer.Sound("../assets/sounds/Movie-08.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

#add alternate and game over
life_icon = pygame.image.load("..assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0,0,0))

#set the number of lives
lives = NUM_LIVES
#placeholder for orange fish

while lives > 0:
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
        pygame.mixer.Sound.play(chomp) #update to another sound
        #placeholder for losing lives
        score += len(result)
        #draw more green fish on the screen
        add_fish(len(result))

    fishes.update()

    #check is player collides with enemy fish
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        #play hurt sound
        pygame.mixer.Sound.play(hurt)
        lives -= len(result)
        #draw more enemy fish on the screen
        add_enemies(len(result))



    # check if fish have left the screen
    for fish in fishes:  # loop through fish in sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            add_fish(1)

    # check is any enemy is off the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width: #use the tile size
            enemies.remove(enemy)
            add_enemies(1)

    #draw the fish
    fishes.draw(screen)

    #draw the player fish
    player.draw(screen)
    enemy.draw(screen)

    #draw enemy fish
    enemies.update()

    #update score font
    text = score_font.render(f"{score}", True, (255,0,0))
    screen.blit(text, (screen_width - text.get_width()/2 - 30, 0))

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height-tile_size ))

#create a new background when the game is over
screen.blit(background, (0,0))

#show game over message
message = score_font.render('GAME OVER ', TRUE, (0,0,))
screen.blit(message, (screen_width/2 - message.get_width() /2, screen_height/2))

#show final score
score_text = score_font.render(f"SCORE: {score}", True, (0,0,0))
screen.blit(score_text, (screen_width/2 -score_text.get_width()/2, screen_height/2 +score_text.get_height()))

#update the display
pygame.display.flip()

#play gameover sound effect
pygame.mixer.Sound.play(bubbles)

#wait for user to exit the game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #limit the frame rate
    clock.tick(60)

pygame.quit()

