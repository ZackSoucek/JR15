import pygame
from src.Creatures.Creature import Creature


class Hero(Creature):

    def __init__(self, position, size, health, speed, damageModifiers, image):
        super().__init__(position, size, health, speed, damageModifiers, image, None)