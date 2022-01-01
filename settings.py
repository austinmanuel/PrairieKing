import pygame
import os

# Visual Settings
DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 900
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TILE_WIDTH = 53 
TILE_HEIGHT = 56
BULLET_WIDTH = 10
BULLET_HEIGHT = 10

# Game Settings
FPS = 30
VELOCITY = 3
BULLET_VELOCITY = 10
RATE_OF_FIRE = 300

# Pygame Settings
pygame.display.set_caption("Journey of the Prairie King")
WIN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets','JOPK_Level_1_1.png')), (DISPLAY_WIDTH, DISPLAY_HEIGHT))
#BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
#BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
CHARACTER_HIT = pygame.USEREVENT + 1

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets','prairie_king.png'))
CHARACTER_IMAGE.set_colorkey(MAGENTA)
CHARACTER_IMAGE = CHARACTER_IMAGE.convert()
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (TILE_WIDTH, TILE_HEIGHT))

BULLET_IMAGE = pygame.image.load(os.path.join('Assets','bullet.png'))
BULLET_IMAGE.set_colorkey(MAGENTA)
BULLET_IMAGE = BULLET_IMAGE.convert()
BULLET = pygame.transform.scale(BULLET_IMAGE,(BULLET_WIDTH, BULLET_HEIGHT))