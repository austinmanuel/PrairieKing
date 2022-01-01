import pygame
from pygame import key

pygame.init()

from settings import *
from utils import *
import prairieking as pk

def draw_window(pk_group, king_bullets):
    WIN.blit(BG, (0,0))
    pk_group.draw(WIN)
    for bullet in king_bullets:
        WIN.blit(pk.BULLET, (bullet[1].x, bullet[1].y))

    pygame.display.update()

def main():
    king = pk.PrairieKing()
    pk_group = pygame.sprite.Group()
    pk_group.add(king)
    king_bullets = []

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
                king.pk_fire(keys_pressed, king, king_bullets)
                oldtime = newtime

            pk_group.update(keys_pressed)
        king.pk_handle_movement(keys_pressed)
        king.pk_handle_bullets(king_bullets)
        draw_window(pk_group, king_bullets)


    main()

if __name__ == "__main__":
    main()
