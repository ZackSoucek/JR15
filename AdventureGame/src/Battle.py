from src.UI import *
from src.InterruptQueue import *
from src.Creatures.Environment import *
from src.Creatures.Creature import *
from src.Animation import *
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

    frame = pygame.image.load("../art/Frame.png")

    def __init__(self, enemies, heroes, background, characteristics):
        self.environment = Environment(enemies,heroes,characteristics)
        self.setEnemyPositions()
        self.setHeroPositions()

        self.background = background

        self.basicButtonInterrupt = InterruptQueue()  # x, y, width, height, image, onClick, interruptQueue
        self.basicButtonLayout = ButtonLayout(
            self.basicButtonInterrupt,
            Button(
                1470, 721, 205, 106,
                pygame.image.load("../art/buttons/BasicAttack.png"),
                lambda: print("Basic Attack") if self.locked != 0 else None,
                self.basicButtonInterrupt
            ),
            Button(
                1675, 721, 205, 106,
                pygame.image.load("../art/buttons/UniqueAttack.png"),
                lambda: print("Unique Attack") if self.locked != 0 else None,
                self.basicButtonInterrupt
            ),
            Button(
                1470, 827, 205, 106,
                pygame.image.load("../art/buttons/SpecialAttack.png"),
                lambda: print("Special Attack") if self.locked != 0 else None,
                self.basicButtonInterrupt
            ),
            Button(
                1675, 827, 205, 106,
                pygame.image.load("../art/buttons/Defense.png"),
                lambda: print("Defense") if self.locked != 0 else None,
                self.basicButtonInterrupt
            ),
            Button(
                1470, 933, 205, 106,
                pygame.image.load("../art/buttons/Items.png"),
                lambda: print("Items") if self.locked != 0 else None,
                self.basicButtonInterrupt
            ),
            Button(
                1675, 933, 205, 106,
                pygame.image.load("../art/buttons/Run.png"),
                lambda: print("Run") if self.locked != 0 else None,
                self.basicButtonInterrupt
            )
        )
        self.basicButtonLayout.activate()

        self.animationHandler = AnimationHandler()
        self.locked = 0


    def drawBattle(self,layers):
        layers[0].blit(self.background, (0, 0))
        layers[2].blit(self.frame, (0, 0))
        self.basicButtonLayout.drawButtons(layers)
        for enemy in self.environment.enemies:
            enemy.draw(layers)

        for hero in self.environment.heroes:
            hero.draw(layers)

        self.animationHandler.runAnimations(layers)

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

    def setHeroPositions(self):
        distBetween = 30
        sizeToSpace = 310
        x = 70
        y = 1010
        for hero in self.environment.heroes:
            hero.changePosition(x, y - sizeToSpace)
            x += distBetween + sizeToSpace

    def lockdown(self, amt):
        self.locked = amt

    def unlock(self, amt):
        self.locked -= amt
        if self.locked < 0:
            self.locked = 0




