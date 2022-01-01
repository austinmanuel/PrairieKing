import pygame
from pygame import key

pygame.init()

from settings import *

class PrairieKing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = CHARACTER
        self.image.set_colorkey(MAGENTA)
        self.image.convert()
        self.x = 450
        self.y = 450
        self.rect = (self.x, self.y)

    def pk_handle_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a]:
            self.x -= VELOCITY
        if keys_pressed[pygame.K_d]:
            self.x += VELOCITY
        if keys_pressed[pygame.K_w]:
            self.y -= VELOCITY
        if keys_pressed[pygame.K_s]:
            self.y += VELOCITY
    
    def update(self, keys_pressed):
        self.pk_handle_movement(keys_pressed)

def pk_fire(keys_pressed, pk, pk_bullets):
    if keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_LEFT]:
        bullet = pygame.Rect(pk.x, pk.y, 10, 5)
        pk_bullets.append(['ul', bullet])
    elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_RIGHT]:
        bullet = pygame.Rect(pk.x + pk.width, pk.y, 10, 5)
        pk_bullets.append(['ur', bullet])
    elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_LEFT]:
        bullet = pygame.Rect(pk.x, pk.y + pk.height, 10, 5)
        pk_bullets.append(['dl', bullet])
    elif keys_pressed[pygame.K_DOWN] and keys_pressed[pygame.K_RIGHT]:
        bullet = pygame.Rect(pk.x + pk.width, pk.y + pk.height, 10, 5)
        pk_bullets.append(['dr', bullet])
    elif keys_pressed[pygame.K_LEFT]:
        bullet = pygame.Rect(pk.x - 5, pk.y + pk.height//2, 10, 5)
        pk_bullets.append(['l', bullet])
    elif keys_pressed[pygame.K_RIGHT]:
        bullet = pygame.Rect(pk.x + pk.width, pk.y + pk.height//2, 10, 5)
        pk_bullets.append(['r', bullet])
    elif keys_pressed[pygame.K_UP]:
        bullet = pygame.Rect(pk.x + pk.width//2, pk.y - 5, 10, 5)
        pk_bullets.append(['u', bullet])
    elif keys_pressed[pygame.K_DOWN]:
        bullet = pygame.Rect(pk.x + pk.width//2, pk.y + pk.height, 10, 5)
        pk_bullets.append(['d', bullet])

def pk_handle_bullets(pk_bullets):
    for bullet in pk_bullets:
        if bullet[0] == 'r':
            bullet[1].x += BULLET_VELOCITY
        if bullet[0] == 'l':
            bullet[1].x -= BULLET_VELOCITY
        if bullet[0] == 'u':
            bullet[1].y -= BULLET_VELOCITY
        if bullet[0] == 'd':
            bullet[1].y += BULLET_VELOCITY
        if bullet[0] == 'ul':
            bullet[1].x -= BULLET_VELOCITY
            bullet[1].y -= BULLET_VELOCITY
        if bullet[0] == 'ur':
            bullet[1].x += BULLET_VELOCITY
            bullet[1].y -= BULLET_VELOCITY
        if bullet[0] == 'dl':
            bullet[1].x -= BULLET_VELOCITY
            bullet[1].y += BULLET_VELOCITY
        if bullet[0] == 'dr':
            bullet[1].x += BULLET_VELOCITY
            bullet[1].y += BULLET_VELOCITY

def draw_window(pk_group, pk_bullets):
    WIN.blit(BG, (0,0))
    pk_group.draw(WIN)
    for bullet in pk_bullets:
        WIN.blit(BULLET, (bullet[1].x, bullet[1].y))

    pygame.display.update()

def main():
    pk = PrairieKing()
    pk_group = pygame.sprite.Group()
    pk_group.add(pk)
    pk_bullets = []

    clock = pygame.time.Clock()
    oldtime = pygame.time.get_ticks()
    run = True
    pygame.event.clear()
    pk_group.draw(WIN)

    while run:
        clock.tick(FPS)
        newtime = pygame.time.get_ticks()
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if keys_pressed:
            if newtime - oldtime > RATE_OF_FIRE:
                pk_fire(keys_pressed, pk, pk_bullets)
                oldtime = newtime
        
        pk_group.update(keys_pressed)
        #pk_handle_movement(keys_pressed, pk)
        pk_handle_bullets(pk_bullets)
        draw_window(pk_group, pk_bullets)
         

    main()

if __name__ == "__main__":
    main()