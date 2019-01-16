class Weapon:

    def __init__(self, damageFunc,weaponType):
        self.damageFunc = damageFunc
        self.type = weaponType

    def getDamage(self,str,spd):
        return self.damageFunc(str,spd)


def damageFuncGenerator(basedamage,strScale,spdScale):
    def damageFunc(str,spd):
        return basedamage + (str * strScale) + (spd * spdScale)
    return damageFunc


from enum import Enum
class WeaponType(Enum):
    pistol = 1
    club = 2