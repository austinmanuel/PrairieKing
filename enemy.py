import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        super().__init__()
        if enemy_type == 'orc':
            self.image = 
        if enemy_type == 'ogre':
        if enemy_type == 'spike':
        self.image = CHARACTER
        self.image.set_colorkey(MAGENTA)
        self.image.convert()
        self.rect = (self.x, self.y)
        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT
