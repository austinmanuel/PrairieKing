import pygame
from settings import *

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets','sprites','prairie_king','prairie_king.png'))
CHARACTER_IMAGE.set_colorkey(MAGENTA)
CHARACTER_IMAGE = CHARACTER_IMAGE.convert()
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (TILE_WIDTH, TILE_HEIGHT))

BULLET_IMAGE = pygame.image.load(os.path.join('Assets','bullet.png'))
BULLET_IMAGE.set_colorkey(MAGENTA)
BULLET_IMAGE = BULLET_IMAGE.convert()
BULLET = pygame.transform.scale(BULLET_IMAGE,(BULLET_WIDTH, BULLET_HEIGHT))
#BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
#BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))

class PrairieKing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = CHARACTER
        self.x = 450
        self.y = 450
        self.rect = (self.x, self.y)
        self.width = TILE_WIDTH
        self.height = TILE_HEIGHT

    def pk_handle_movement(self, keys_pressed):
        # Up Left
        if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w]:
            if self.x > TILE_WIDTH:
                self.x -= VELOCITY * 0.7
            if self.y > TILE_HEIGHT:
                self.y -= VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Down Left
        elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s]:
            if self.x > TILE_WIDTH:
                self.x -= VELOCITY * 0.7
            if self.y < DISPLAY_HEIGHT - TILE_HEIGHT * 2:
                self.y += VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Up Right
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w]:
            if self.x < DISPLAY_WIDTH - TILE_WIDTH * 2:
                self.x += VELOCITY * 0.7
            if self.y > TILE_HEIGHT:
                self.y -= VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Down Right
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s]:
            if self.x < DISPLAY_WIDTH - TILE_WIDTH * 2:
                self.x += VELOCITY * 0.7
            if self.y < DISPLAY_HEIGHT - TILE_HEIGHT * 2:
                self.y += VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Left
        elif keys_pressed[pygame.K_a] and self.x > TILE_WIDTH:
            self.x -= VELOCITY
            self.rect = (self.x, self.y)
        # Right
        elif keys_pressed[pygame.K_d] and self.x < DISPLAY_WIDTH - TILE_WIDTH * 2:
            self.x += VELOCITY
            self.rect = (self.x, self.y)
        # Up
        elif keys_pressed[pygame.K_w] and self.y > TILE_HEIGHT:
            self.y -= VELOCITY
            self.rect = (self.x, self.y)
        # Down
        elif keys_pressed[pygame.K_s] and self.y < DISPLAY_HEIGHT - TILE_HEIGHT * 2:
            self.y += VELOCITY
            self.rect = (self.x, self.y)

    def update(self, keys_pressed, king_bullets):
        self.pk_handle_movement(keys_pressed)
        self.pk_handle_bullets(king_bullets)

    def pk_fire(self, keys_pressed, pk, king_bullets):
        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(pk.x, pk.y, 10, 5)
            king_bullets.append(['ul', bullet])
        elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(pk.x + pk.width, pk.y, 10, 5)
            king_bullets.append(['ur', bullet])
        elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(pk.x, pk.y + pk.height, 10, 5)
            king_bullets.append(['dl', bullet])
        elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(pk.x + pk.width, pk.y + pk.height, 10, 5)
            king_bullets.append(['dr', bullet])
        elif keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(pk.x - 5, pk.y + pk.height//2, 10, 5)
            king_bullets.append(['l', bullet])
        elif keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(pk.x + pk.width, pk.y + pk.height//2, 10, 5)
            king_bullets.append(['r', bullet])
        elif keys_pressed[pygame.K_UP]:
            bullet = pygame.Rect(pk.x + pk.width//2, pk.y - 5, 10, 5)
            king_bullets.append(['u', bullet])
        elif keys_pressed[pygame.K_DOWN]:
            bullet = pygame.Rect(pk.x + pk.width//2, pk.y + pk.height, 10, 5)
            king_bullets.append(['d', bullet])

    def pk_handle_bullets(self, king_bullets):
        for bullet in king_bullets:
            if bullet[0] == 'r':
                bullet[1].x += BULLET_VELOCITY
            if bullet[0] == 'l':
                bullet[1].x -= BULLET_VELOCITY
            if bullet[0] == 'u':
                bullet[1].y -= BULLET_VELOCITY
            if bullet[0] == 'd':
                bullet[1].y += BULLET_VELOCITY
            if bullet[0] == 'ul':
                bullet[1].x -= int(BULLET_VELOCITY * .7)
                bullet[1].y -= int(BULLET_VELOCITY * .7)
            if bullet[0] == 'ur':
                bullet[1].x += int(BULLET_VELOCITY * .7)
                bullet[1].y -= int(BULLET_VELOCITY * .7)
            if bullet[0] == 'dl':
                bullet[1].x -= int(BULLET_VELOCITY * .7)
                bullet[1].y += int(BULLET_VELOCITY * .7)
            if bullet[0] == 'dr':
                bullet[1].x += int(BULLET_VELOCITY * .7)
                bullet[1].y += int(BULLET_VELOCITY * .7)
