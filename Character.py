from Weapon import *

class Character:
    def __init__(self, mHealth,weaponA,weaponB,*weaponTypes):
        self.maxHealth = mHealth
        self.health = mHealth
        self.weaponTypes = weaponTypes
        self.primaryWeapon = weaponA
        self.secondaryWeapon = weaponB


    def take_damage(self, damage):
        self.health -= damage
