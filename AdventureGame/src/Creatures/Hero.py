import pygame
from src.Creatures.Creature import Creature

class Hero(Creature):

    def __init__(self, health, speed, damageModifiers, image, name):
        super().__init__((310-60)/Creature.sizeHeight, health, speed, damageModifiers, image, None, name)

    def draw(self, layers):
        super().draw(layers)

