class Weapon:

    def __init__(self, damagegiven,weaponType):
        self.damage = damagegiven
        self.type = weaponType

from enum import Enum
class WeaponType(Enum):
    pistol = 1
    club = 2