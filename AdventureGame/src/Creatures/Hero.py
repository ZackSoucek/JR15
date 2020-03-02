import pygame
from src.Creatures.Creature import Creature


class Hero(Creature):

    def __init__(self, health, speed, damageModifiers, image):
        super().__init__(310/Creature.sizeHeight, health, speed, damageModifiers, image, None)


