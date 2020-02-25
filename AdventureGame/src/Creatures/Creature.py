import pygame
from random import choice

class Creature:

    sizeHeight = 1000

    def __init__(self, position, size, health, speed, damageModifiers, image, attacks):
        self.size = size
        self.maxHealth = health
        self.currHealth = health
        self.damageModifiers = damageModifiers
        self.image = pygame.transform.smoothscale(image, (self.sizeHeight * size, self.sizeHeight * size))
        self.attacks = attacks
        self.position = position
        self.speed = speed

    def takeDamage(self, modifier, amount=0, percent=0): # can also be used for healing w/ - damage
        self.health -= amount * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])
        self.health -= (self.health * percent) * (1 if modifier not in self.damageModifiers else self.damageModifiers[modifier])

    def draw(self, x, y, screen):
        screen.blit(self.image, self.position)

    def movePosiotion(self, deltaX, deltaY):
        self.position = (self.position[0] + deltaX, self.position[1] + deltaY)

    def changePosition(self, x, y):
        self.position = (x, y)

    def getAttack(self, env):
        return choice(self.attacks)

    def attack(self, env):
        return self.getAttack(env)

