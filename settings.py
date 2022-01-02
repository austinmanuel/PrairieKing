import pygame
import os

# Visual Settings
DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 900
MAGENTA = (255,0,255)
TILE_WIDTH = 53
TILE_HEIGHT = 56
BULLET_WIDTH = 10
BULLET_HEIGHT = 10

# Game Settings
FPS = 30
VELOCITY = 5
BULLET_VELOCITY = 10
RATE_OF_FIRE = 300

# Pygame Settings
pygame.display.set_caption("Journey of the Prairie King")
WIN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets','maps','JOPK_Level_1_1.png')), (DISPLAY_WIDTH, DISPLAY_HEIGHT))
CHARACTER_HIT = pygame.USEREVENT + 1
