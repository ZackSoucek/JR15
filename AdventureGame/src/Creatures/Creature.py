import pygame
from random import choice
from math import ceil

class Creature:

    sizeHeight = 240
    nameFont = pygame.font.Font('../art/Example.ttf', 36)
    namePlate = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateMiddle.png'), (50, 50)).convert_alpha()
    namePlateLeft = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateLeft.png'), (13, 50)).convert_alpha()
    namePlateRight = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateRight.png'), (13, 50)).convert_alpha()

    def __init__(self, size, health, speed, damageModifiers, image, attacks, name, nameFont = None):
        self.size = size
        self.maxHealth = health
        self.currHealth = health
        self.damageModifiers = damageModifiers
        self.image = pygame.transform.scale(image, (int(self.sizeHeight * size), int(self.sizeHeight * size)))
        self.attacks = attacks
        self.position = (-1, -1)
        self.speed = speed
        self.name = (nameFont if nameFont != None else self.nameFont).render(name, True, (0, 0, 0))  # center name below
        self.textPosition = (-1,-1)

    def takeDamage(self, modifier, amount=0, percent=0): # can also be used for healing w/ - damage
        self.health -= amount * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])
        self.health -= (self.health * percent) * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])

    def draw(self, layers):
        layers[1].blit(self.image, self.position)

        self.drawNamePlate(layers)
        layers[2].blit(self.name,self.textPosition)  # add in text box

    def drawNamePlate(self, layers):
        fragments = ceil(self.name.get_width() / self.namePlate.get_width())
        deltaX = -(self.namePlate.get_width() * fragments - self.name.get_width()) // 2
        deltaY = -(self.namePlate.get_height() - self.name.get_height()) // 2
        for i in range(fragments):
            layers[2].blit(self.namePlate, (self.textPosition[0] + deltaX + i * self.namePlate.get_width(), self.textPosition[1] + deltaY))

        layers[2].blit(self.namePlateLeft, (self.textPosition[0] + deltaX - self.namePlateLeft.get_width(), self.textPosition[1] + deltaY))
        layers[2].blit(self.namePlateRight, (self.textPosition[0] + deltaX + self.namePlate.get_width() * fragments, self.textPosition[1] + deltaY))


    def movePosiotion(self, deltaX, deltaY):
        self.position = (self.position[0] + deltaX, self.position[1] + deltaY)
        self.textPosition = (self.textPosition[0] + deltaX, self.textPosition[1] + deltaY)

    def changePosition(self, x, y):
        self.position = (x, y)
        self.textPosition = (x + (self.size*self.sizeHeight - self.name.get_width()) // 2, y + self.size*self.sizeHeight + 5)

    def getAttack(self, env):
        return choice(self.attacks)

    def attack(self, env):
        return self.getAttack(env)

    def getFeature(self, feature):
        if feature == "health":
            return self.currHealth
        elif feature == "maxhealth":
            return self.maxHealth
        elif feature == "speed":
            return self.speed
        return "notImplemented"

