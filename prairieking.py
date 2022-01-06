import pygame
from settings import *

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets','sprites',
    'prairie_king','prairie_king.png')).convert_alpha()
CHARACTER = pygame.transform.scale(CHARACTER_IMAGE, (TILE, TILE))

BULLET_IMAGE = pygame.image.load(os.path.join('Assets','bullet.png')).convert_alpha()
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
        self.width = TILE
        self.height = TILE
        self.oldtime = pygame.time.get_ticks()
        self.bullets = []

    def pk_handle_movement(self, keys_pressed):
        # Up Left
        if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_w]:
            if self.x > TILE:
                self.x -= VELOCITY * 0.7
            if self.y > TILE:
                self.y -= VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Down Left
        elif keys_pressed[pygame.K_a] and keys_pressed[pygame.K_s]:
            if self.x > TILE:
                self.x -= VELOCITY * 0.7
            if self.y < DISPLAY_HEIGHT - TILE * 2:
                self.y += VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Up Right
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_w]:
            if self.x < DISPLAY_WIDTH - TILE * 2:
                self.x += VELOCITY * 0.7
            if self.y > TILE:
                self.y -= VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Down Right
        elif keys_pressed[pygame.K_d] and keys_pressed[pygame.K_s]:
            if self.x < DISPLAY_WIDTH - TILE * 2:
                self.x += VELOCITY * 0.7
            if self.y < DISPLAY_HEIGHT - TILE * 2:
                self.y += VELOCITY * 0.7
            self.rect = (self.x, self.y)
        # Left
        elif keys_pressed[pygame.K_a] and self.x > TILE:
            self.x -= VELOCITY
            self.rect = (self.x, self.y)
        # Right
        elif keys_pressed[pygame.K_d] and self.x < DISPLAY_WIDTH - TILE * 2:
            self.x += VELOCITY
            self.rect = (self.x, self.y)
        # Up
        elif keys_pressed[pygame.K_w] and self.y > TILE:
            self.y -= VELOCITY
            self.rect = (self.x, self.y)
        # Down
        elif keys_pressed[pygame.K_s] and self.y < DISPLAY_HEIGHT - TILE * 2:
            self.y += VELOCITY
            self.rect = (self.x, self.y)

    def update(self, keys_pressed):
        self.pk_handle_movement(keys_pressed)
        self.pk_handle_bullets()
        self.pk_check_fire(keys_pressed)

    def pk_check_fire(self, keys_pressed):
        if pygame.time.get_ticks() - self.oldtime > RATE_OF_FIRE:
            self.oldtime = pygame.time.get_ticks()
            self.pk_fire(keys_pressed)

    def pk_fire(self, keys_pressed):
        if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(self.x, self.y, 10, 5)
            self.bullets.append(['ul', bullet])
        elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(self.x + self.width, self.y, 10, 5)
            self.bullets.append(['ur', bullet])
        elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(self.x, self.y + self.height, 10, 5)
            self.bullets.append(['dl', bullet])
        elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(self.x + self.width, self.y +
                self.height, 10, 5)
            self.bullets.append(['dr', bullet])
        elif keys_pressed[pygame.K_LEFT]:
            bullet = pygame.Rect(self.x - 5, self.y + self.height//2, 10, 5)
            self.bullets.append(['l', bullet])
        elif keys_pressed[pygame.K_RIGHT]:
            bullet = pygame.Rect(self.x + self.width, self.y +
                self.height//2, 10, 5)
            self.bullets.append(['r', bullet])
        elif keys_pressed[pygame.K_UP]:
            bullet = pygame.Rect(self.x + self.width//2, self.y - 5, 10, 5)
            self.bullets.append(['u', bullet])
        elif keys_pressed[pygame.K_DOWN]:
            bullet = pygame.Rect(self.x + self.width//2, self.y +
                self.height, 10, 5)
            self.bullets.append(['d', bullet])

    def pk_handle_bullets(self):
        for bullet in self.bullets:
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
