import pygame
import os
import random
import prairieking
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, enemy_type):
        super().__init__()
        self.enemy_type = enemy_type
        self.x = pos_x
        self.y = pos_y
        self.rect = (self.x, self.y)
        self.images = []
        self.index = 0
        self.width = 56
        self.height = 56
        self.animation_frames = self.get_frames()
        self.image = self.animation_frames[self.index]
        self.oldtime = pygame.time.get_ticks()

    def update(self, king_pos):
        self.image = pygame.transform.scale(self.animation_frames[(self.index % 2)],(TILE, TILE))
        newtime = pygame.time.get_ticks()
        if newtime - self.oldtime > 450:
            self.index += 1
            self.oldtime = newtime
        #self.enemy_handle_movement(king_pos)

    def get_frames(self):
        animation_frames = []
        if self.enemy_type == 'orc':
            self.sheet = pygame.image.load(os.path.join('Assets','sprites','orc',
                'orc_sheet.png'))
            for i in range(2):
                frame = self.get_image(i, self.width - 1, self.height, 1)
                animation_frames.append(frame)
                i += 1

        return animation_frames

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    def enemy_handle_movement(self, king_pos):
        SPEED = SLOW_ENEMY_MOVEMENT
        if (self.x > king_pos[0]) and (self.x - SPEED >= king_pos[0]):
            self.x -= SPEED
        elif self.x > king_pos[0]:
            self.x = king_pos[0]
        elif (self.x < king_pos[0]) and (self.x + SPEED <= king_pos[0]):
            self.x += SPEED
        elif self.x < king_pos[0]:
            self.x = king_pos[0]

        if (self.y > king_pos[1]) and (self.y - SPEED >= king_pos[1]):
            self.y -= SPEED
        elif self.y > king_pos[1]:
            self.y = king_pos[1]
        elif (self.y < king_pos[1]) and (self.y + SPEED <= king_pos[1]):
            self.y += SPEED
        elif self.y < king_pos[1]:
            self.y = king_pos[1]
        self.rect = (self.x, self.y)
