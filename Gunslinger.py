from Character import *


class Gunslinger(Character):

    def __init__(self):
        main_gun = Weapon(5)
        off_hand = Weapon(5)
        super().__init__(15, main_gun, off_hand)
