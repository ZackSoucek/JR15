import pygame
from random import choice

class Creature:

    sizeHeight = 240

    def __init__(self, size, health, speed, damageModifiers, image, attacks):
        self.size = size
        self.maxHealth = health
        self.currHealth = health
        self.damageModifiers = damageModifiers
        self.image = pygame.transform.scale(image, (self.sizeHeight * size, self.sizeHeight * size))
        self.attacks = attacks
        self.position = (-1,-1)
        self.speed = speed

    def takeDamage(self, modifier, amount=0, percent=0): # can also be used for healing w/ - damage
        self.health -= amount * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])
        self.health -= (self.health * percent) * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])

    def draw(self, layers):
        layers[1].blit(self.image, self.position)

    def movePosiotion(self, deltaX, deltaY):
        self.position = (self.position[0] + deltaX, self.position[1] + deltaY)

    def changePosition(self, x, y):
        self.position = (x, y)

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

