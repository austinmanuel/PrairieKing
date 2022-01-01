import pygame
import os
from settings import *

class Enemy(pygame.sprite.Sprite, enemy_type):
    def __init__(self, enemy_type):
        super().__init__()
        self.images = []
        self.index = 0
        self.x = 0
        self.y = 0
        if enemy_type == 'orc':
            self.images.append(os.path.join('Assets','sprites','orc','frame0.png'))
            self.images.append(os.path.join('Assets','sprites','orc','frame1.png'))
        if enemy_type == 'ogre':
            pass
        if enemy_type == 'spike':
            pass
        self.image = self.image[self.index]
        self.image.convertalpha()
        self.rect = (self.x, self.y)
        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT
