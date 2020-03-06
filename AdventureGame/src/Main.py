import sys, pygame

import ctypes
ctypes.windll.user32.SetProcessDPIAware()  # <== found it on stack overflow, it works

pygame.init()

from src.InterruptQueue import *
from src.UI import *
from src.Battle import *
from src.Creatures.Creature import *
from src.Creatures.Hero import *

size = width, height = 1920, 1080
empty = pygame.Color(0, 0, 0, 0)

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

backdrop = pygame.surface.Surface((width, height),pygame.SRCALPHA)
ui = pygame.surface.Surface((width, height),pygame.SRCALPHA)
characters = pygame.surface.Surface((width, height),pygame.SRCALPHA)
attacks = pygame.surface.Surface((width, height),pygame.SRCALPHA)
layers = [backdrop, characters, ui, attacks]

background = pygame.transform.scale(pygame.image.load("../art/Fortress.png"), size)
enemyImage = pygame.transform.scale(pygame.image.load(r"..\art\Slime\Slime.png"), (32, 32))

enemies = [
    Creature(1, 100, 50, dict(), enemyImage, None, "Samuel"),
    Creature(2, 100, 50, dict(), enemyImage, None, "Timothy"),
    Creature(1, 100, 50, dict(), enemyImage, None, "Christopher")
]

heroes = [
    Hero(100, 50, dict(), enemyImage, "Cat"),
    Hero(100, 50, dict(), enemyImage, "Bus"),
    Hero(100, 50, dict(), enemyImage, "Carpenter"),
    Hero(100, 50, dict(), enemyImage, "Destroyer of Worlds")
]

battle = Battle(enemies, heroes, background, None)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    battle.getBattleInput()
    battle.drawBattle(layers)

    for layer in layers:
        screen.blit(layer, (0, 0))
        layer.fill(empty)

    pygame.display.flip()