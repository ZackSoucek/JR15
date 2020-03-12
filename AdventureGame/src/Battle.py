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

    frame = pygame.image.load("../art/UI.png")

    def runIfUp(self, func):
        return lambda: func() if not self.pauseAnimations and self.currentCreature in self.environment.heroesSet else None

    def __init__(self, enemies, heroes, background, characteristics):
        self.environment = Environment(enemies, heroes, characteristics)
        self.setEnemyPositions()
        self.setHeroPositions()

        self.moveQueue = []
        self.currentCreature = None
        self.getNextCharacter()

        self.background = background

        self.pauseAnimations = AnimationHandler()

        self.globalInterrupt = InterruptQueue()

        self.basicButtonInterrupt = InterruptQueue()  # x, y, width, height, image, onClick, interruptQueue
        self.basicButtonLayout = ButtonLayout(
            self.basicButtonInterrupt,
            Button(
                1470 + 2, 720, 200, 100,
                pygame.image.load("../art/buttons/BasicAttack.png").convert(),
                self.runIfUp(lambda: (self.currentCreature.basicAttack(self.environment, self.getNextCharacter))),
                self.basicButtonInterrupt
            ),
            Button(
                1675 + 2, 720, 200, 100,
                pygame.image.load("../art/buttons/UniqueAttack.png").convert(),
                self.runIfUp(lambda: (self.currentCreature.uniqueAttack(self.environment, self.getNextCharacter))),
                self.basicButtonInterrupt
            ),
            Button(
                1470 + 2, 830, 200, 100,
                pygame.image.load("../art/buttons/SpecialAttack.png").convert(),
                self.runIfUp(lambda: (self.currentCreature.specialAttack(self.environment, self.getNextCharacter))),
                self.basicButtonInterrupt
            ),
            Button(
                1675 + 2, 830, 200, 100,
                pygame.image.load("../art/buttons/Defense.png").convert(),
                lambda: print("Defense") if not self.pauseAnimations and self.currentCreature in self.environment.heroesSet else None,
                self.basicButtonInterrupt
            ),
            Button(
                1470 + 2, 940, 200, 100,
                pygame.image.load("../art/buttons/Items.png").convert(),
                lambda: print("Items") if not self.pauseAnimations and self.currentCreature in self.environment.heroesSet else None,
                self.basicButtonInterrupt
            ),
            Button(
                1675 + 2, 940, 200, 100,
                pygame.image.load("../art/buttons/Run.png").convert(),
                lambda: print("Run") if not self.pauseAnimations and self.currentCreature in self.environment.heroesSet else None,
                self.basicButtonInterrupt
            )
        )
        self.basicButtonLayout.activate()


    def drawBattle(self,layers):
        layers[0].blit(self.background, (0, 0))
        layers[2].blit(self.frame, (0, 0))
        self.basicButtonLayout.drawButtons(layers)
        for enemy in self.environment.enemies:
            enemy.draw(layers, enemy == self.currentCreature)

        for hero in self.environment.heroes:
            hero.draw(layers, hero == self.currentCreature)

        self.pauseAnimations.runAnimations(layers)

    def getBattleInput(self):
        self.basicButtonLayout.checkButtons()
        self.globalInterrupt.runInterrupts()

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
            hero.changePosition(x + 50, y - sizeToSpace + 65)
            x += distBetween + sizeToSpace

    def fillMoveQueue(self):
        self.moveQueue = sorted(self.environment.enemies + self.environment.heroes, key=lambda c: c.speed)

    def getNextCharacter(self):
        if not self.moveQueue:
            self.fillMoveQueue()
        self.currentCreature = self.moveQueue.pop()
        if self.currentCreature not in self.environment.heroesSet:
            self.currentCreature.getAttack(self.environment).runAttack(self.environment, self.getNextCharacter, self.pauseAnimations)





