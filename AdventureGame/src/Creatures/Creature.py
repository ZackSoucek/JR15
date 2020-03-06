import pygame
from random import choice

class Creature:

    sizeHeight = 240
    nameFont = pygame.font.Font('../art/Example.ttf', 36)

    def __init__(self, size, health, speed, damageModifiers, image, attacks, name):
        self.size = size
        self.maxHealth = health
        self.currHealth = health
        self.damageModifiers = damageModifiers
        self.image = pygame.transform.scale(image, (int(self.sizeHeight * size), int(self.sizeHeight * size)))
        self.attacks = attacks
        self.position = (-1, -1)
        self.speed = speed
        self.name = self.nameFont.render(name, True, (100, 100, 100))  # center name below
        self.textPosition = (-1,-1)

    def takeDamage(self, modifier, amount=0, percent=0): # can also be used for healing w/ - damage
        self.health -= amount * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])
        self.health -= (self.health * percent) * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])

    def draw(self, layers):
        layers[1].blit(self.image, self.position)
        layers[2].blit(self.name,self.textPosition)

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

