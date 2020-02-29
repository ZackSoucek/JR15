import sys, pygame
from src.InterruptQueue import *
from src.UI import *
from src.Battle import *

import ctypes
ctypes.windll.user32.SetProcessDPIAware()  # <== found it on stack overflow, it works

pygame.init()

size = width, height = 1920, 1080
speed = [20, 20]
black = 0, 0, 0



def revSpeed():
    speed[0] = -speed[0]
    speed[1] = -speed[1]
    print("changed speed")

screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

background = pygame.transform.scale(pygame.image.load("../art/UI example.png"), size)

battle = Battle(None,None,background,None)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    battle.getBattleInput()
    battle.drawBattle(screen)

    pygame.display.flip()