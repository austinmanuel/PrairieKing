import pygame
import os

# Visual Settings
BASE_DIM = 700
TILE  = BASE_DIM / 18
DISPLAY_WIDTH = BASE_DIM - TILE * 2
DISPLAY_HEIGHT = BASE_DIM - TILE * 2
BULLET_WIDTH = 15
BULLET_HEIGHT = 15
BLACK = (0,0,0)
WHITE = (255,255,255)

# Game Settings
FPS = 30
BASE_VELOCITY = 5
VELOCITY = BASE_VELOCITY
SLOW_ENEMY_MOVEMENT = BASE_VELOCITY / 3
MED_ENEMY_MOVEMENT = BASE_VELOCITY / 2
FAST_ENEMY_MOVEMENT = BASE_VELOCITY
BULLET_VELOCITY = BASE_VELOCITY * 2
RATE_OF_FIRE = 300

# Pygame Settings
pygame.display.set_caption("Journey of the Prairie King")
WINDOW = pygame.display.set_mode((BASE_DIM, BASE_DIM))
MAP = pygame.transform.scale(pygame.image.load(os.path.join('Assets','maps',
    'JOPK_Level_1_1.png')), (DISPLAY_WIDTH, DISPLAY_HEIGHT))
SPLASH = pygame.image.load(os.path.join('Assets',
    'JOPK_logo.png')).convert_alpha()
SPLASH = pygame.transform.scale(SPLASH, (DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
CHARACTER_HIT = pygame.USEREVENT + 1
