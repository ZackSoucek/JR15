from src.UI import *
from src.InterruptQueue import *
from src.Creatures.Environment import *
from src.Creatures.Creature import *
import pygame


class ButtonLayout:
    def __init__(self, interruptQueue, *buttons):
        self.buttons = list(buttons)
        self.interruptQueue = interruptQueue
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def checkButtons(self):
        if self.active:
            self.interruptQueue.runInterrupts()

    def drawButtons(self, layers):
        if self.active:
            for button in self.buttons:
                button.drawButton(layers)


class Battle:

    frame = None

    def __init__(self, enemies, heroes, background, characteristics):
        self.environment = Environment(enemies,heroes,characteristics)
        self.setEnemyPositions()

        self.background = background

        self.basicButtonInterrupt = InterruptQueue()  # x, y, width, height, image, onClick, interruptQueue
        self.basicButtonLayout = ButtonLayout(
            self.basicButtonInterrupt,
            Button(
                1470, 720, 200, 100,
                pygame.image.load("../art/buttons/BasicAttack.png"),
                lambda: print("Basic Attack"),
                self.basicButtonInterrupt
            ),
            Button(
                1680, 720, 200, 100,
                pygame.image.load("../art/buttons/UniqueAttack.png"),
                lambda: print("Unique Attack"),
                self.basicButtonInterrupt
            ),
            Button(
                1470, 830, 200, 100,
                pygame.image.load("../art/buttons/SpecialAttack.png"),
                lambda: print("Special Attack"),
                self.basicButtonInterrupt
            ),
            Button(
                1680, 830, 200, 100,
                pygame.image.load("../art/buttons/Defense.png"),
                lambda: print("Defense"),
                self.basicButtonInterrupt
            ),
            Button(
                1470, 940, 200, 100,
                pygame.image.load("../art/buttons/Items.png"),
                lambda: print("Items"),
                self.basicButtonInterrupt
            ),
            Button(
                1680, 940, 200, 100,
                pygame.image.load("../art/buttons/Run.png"),
                lambda: print("Run"),
                self.basicButtonInterrupt
            )
        )
        self.basicButtonLayout.activate()


    def drawBattle(self,layers):
        layers[0].blit(self.background, (0, 0))
        self.basicButtonLayout.drawButtons(layers)
        for enemy in self.environment.enemies:
            enemy.draw(layers)

    def getBattleInput(self):
        self.basicButtonLayout.checkButtons()

    def setEnemyPositions(self):
        totSize = sum(enemy.size for enemy in self.environment.enemies)
        distBetween = 50
        sizeToSpace = Creature.sizeHeight
        space = 1580 - (len(self.environment.enemies)-1) * distBetween - totSize * sizeToSpace
        x = 160 + space / 2
        y = 560
        for enemy in self.environment.enemies:
            enemy.changePosition(x, y - enemy.size * sizeToSpace)
            x += distBetween + enemy.size * sizeToSpace




