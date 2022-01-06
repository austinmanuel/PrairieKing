import pygame
from settings import *
import utils
import prairieking as pk
import enemy
import random

pygame.init()

def spawn_enemy(enemy_type):
    rand = random.randint(7,9)
    spawn_bank = random.choice(['u','d','l','r'])
    if spawn_bank == 'u':
        x = TILE * rand + (TILE * 2)
        y = TILE * 2
    elif spawn_bank == 'r':
        x = TILE * 17
        y = TILE * (rand + 2)
    elif spawn_bank == 'd':
        x = TILE * rand + (TILE * 2)
        y = TILE * 17
    elif spawn_bank == 'l':
        x = TILE * 2
        y = TILE * (rand + 2)
    spawned_enemy = enemy.Enemy(x, y, enemy_type=enemy_type)
    return spawned_enemy

def draw_window(pk_group, king, enemy_group):
    WINDOW.blit(MAP, (TILE * 2, TILE * 2))
    pk_group.draw(WINDOW)
    enemy_group.draw(WINDOW)
    for bullet in king.bullets:
        WINDOW.blit(pk.BULLET, (bullet[1].x, bullet[1].y))

    pygame.display.update()

def game_intro():
    intro = True

    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render('Press any key to continue', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - (DISPLAY_HEIGHT // 2)
        + (DISPLAY_HEIGHT // 4))

    WINDOW.fill(BLACK)
    WINDOW.blit(SPLASH, (DISPLAY_WIDTH / 2 - (DISPLAY_WIDTH / 4),
        DISPLAY_HEIGHT / 2 - (DISPLAY_HEIGHT / 4)))
    WINDOW.blit(text, textRect)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                intro = False


        pygame.display.update()

def main():
    game_intro()

    king = pk.PrairieKing()
    pk_group = pygame.sprite.GroupSingle()
    pk_group.add(king)

    enemy_group = pygame.sprite.Group()
    enemy_group.add(spawn_enemy('orc'))
    #utils.spawn_enemy_all_banks(enemy_group)

    clock = pygame.time.Clock()
    run = True
    pygame.event.clear()

    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys_pressed[pygame.K_ESCAPE]:
                run = False
                pygame.quit()
                quit()

        pk_group.update(keys_pressed, enemy_group)
        enemy_group.update((king.x, king.y))

        draw_window(pk_group, king, enemy_group)

if __name__ == "__main__":
    main()
