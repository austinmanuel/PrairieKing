import pygame
from settings import *
import enemy
import random

def spawn_enemy_all_banks(enemy_group):
    #Upper Bank
    enemy_group.add(enemy.Enemy((TILE * 7 + (TILE * 2)), TILE * 2, enemy_type='orc'))
    enemy_group.add(enemy.Enemy((TILE * 8 + (TILE * 2)), TILE * 2, enemy_type='orc'))
    enemy_group.add(enemy.Enemy((TILE * 9 + (TILE * 2)), TILE * 2, enemy_type='orc'))
    #Lower Bank
    enemy_group.add(enemy.Enemy((TILE * 7 + (TILE * 2)), TILE * 17, enemy_type='orc'))
    enemy_group.add(enemy.Enemy((TILE * 8 + (TILE * 2)), TILE * 17, enemy_type='orc'))
    enemy_group.add(enemy.Enemy((TILE * 9 + (TILE * 2)), TILE * 17, enemy_type='orc'))
    #Left Bank
    enemy_group.add(enemy.Enemy(TILE * 2, TILE * 9, enemy_type='orc'))
    enemy_group.add(enemy.Enemy(TILE * 2, TILE * 10, enemy_type='orc'))
    enemy_group.add(enemy.Enemy(TILE * 2, TILE * 11, enemy_type='orc'))
    #Right Bank
    enemy_group.add(enemy.Enemy(TILE * 17, TILE * 9, enemy_type='orc'))
    enemy_group.add(enemy.Enemy(TILE * 17, TILE * 10, enemy_type='orc'))
    enemy_group.add(enemy.Enemy(TILE * 17, TILE * 11, enemy_type='orc'))
