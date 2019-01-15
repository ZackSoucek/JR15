from Weapon import *

class Character:
    def __init__(self, mHealth, weaponA, weaponB):
        self.maxHealth = mHealth
        self.health = mHealth
        self.primaryWeapon = weaponA
        self.secondaryWeapon = weaponB


    def take_damage(self, damage):
        self.health -= damage
