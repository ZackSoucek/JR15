
class Attack:
    def __init__(self, modifier, flatDamage, percentDamage, targetFunc, animation):
        self.modifier = modifier
        self.flatDamage = flatDamage
        self.percentDamage = percentDamage
        self.animation = animation
        self.targetFunc = targetFunc

    def runAttack(self, env):
        for creature in self.targetFunc(env):
            creature.takeDamage(self.modifier, self.flatDamage, self.percentDamage)


def targetAll(env):
    pass


def targetRandom(env):
    pass


def targetMinFeature(env, feature):
    def targetMinX(env):
        pass
    return targetMinX
