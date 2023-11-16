# a pygame sprite class for a enemy fish

import pygame
import random
from game_parameters import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load('../assets/sprites/puffer_fish.png').convert()
        self.forward_image.set_colorkey((0,0,0))
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = MAX_SPEED

    def update(self):
        #update the x position
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self,screen):
        screen.blit(self.image, self.rect)

enemies = pygame.sprite.Group()