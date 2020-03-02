import sys, pygame
from src.InterruptQueue import *
from src.UI import *
from src.Battle import *
from src.Creatures.Creature import *

import ctypes
ctypes.windll.user32.SetProcessDPIAware()  # <== found it on stack overflow, it works

pygame.init()

size = width, height = 1920, 1080
empty = pygame.Color(0,0,0,0)

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

backdrop = pygame.surface.Surface((width, height),pygame.SRCALPHA)
ui = pygame.surface.Surface((width, height),pygame.SRCALPHA)
characters = pygame.surface.Surface((width, height),pygame.SRCALPHA)
attacks = pygame.surface.Surface((width, height),pygame.SRCALPHA)
layers = [backdrop, characters, ui, attacks]

background = pygame.transform.scale(pygame.image.load("../art/UI example.png"), size)
enemyImage = pygame.transform.scale(pygame.image.load(r"..\art\Miner\Full Body Sprite\Miner Sprite 16x16.png"), (16,16))

enemies = [
    Creature(1, 100, 50, dict(), enemyImage, None),
    Creature(2, 100, 50, dict(), enemyImage, None),
    Creature(1, 100, 50, dict(), enemyImage, None)
]

battle = Battle(enemies, None, background, None)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    battle.getBattleInput()
    battle.drawBattle(layers)

    for layer in layers:
        screen.blit(layer, (0, 0))
        layer.fill(empty)

    pygame.display.flip()