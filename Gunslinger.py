from Character import *
from Weapon import WeaponType

class Gunslinger(Character):

    def __init__(self):
        main_gun = Weapon(5,WeaponType.pistol)
        off_hand = Weapon(5,WeaponType.club)
        super().__init__(15, main_gun, off_hand,WeaponType.club,WeaponType.pistol)
