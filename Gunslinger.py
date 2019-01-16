from Character import *
from Weapon import WeaponType

class Gunslinger(Character):

    def __init__(self, defaultMainGun = Weapon(lambda x,y: 5,WeaponType.knife, "Bent Knife", "Despite how it looks it used to be a knife", None),
                 defaultOffHand = Weapon(lambda x,y: 5,WeaponType.knife, "Bent Knife", "Despite how it looks it used to be a knife", None)):
        main_gun = defaultMainGun
        off_hand = defaultOffHand
        super().__init__(15, main_gun, off_hand,WeaponType.club,WeaponType.pistol)
