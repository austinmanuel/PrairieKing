import pygame
import os

# Visual Settings
DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 900
BLACK = (0,0,0)
WHITE = (255,255,255)
TILE  = 56
BULLET_WIDTH = 15
BULLET_HEIGHT = 15

# Game Settings
FPS = 30
VELOCITY = 5
BULLET_VELOCITY = 10
RATE_OF_FIRE = 300

# Pygame Settings
pygame.display.set_caption("Journey of the Prairie King")
WINDOW = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
MAP = pygame.transform.scale(pygame.image.load(os.path.join('Assets','maps',
    'JOPK_Level_1_1.png')), (DISPLAY_WIDTH, DISPLAY_HEIGHT))
SPLASH = pygame.image.load(os.path.join('Assets',
    'JOPK_logo.png')).convert_alpha()
SPLASH = pygame.transform.scale(SPLASH, (DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
CHARACTER_HIT = pygame.USEREVENT + 1
