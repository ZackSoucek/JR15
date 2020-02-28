
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

def targetEnemies(func):
    return lambda env: func(env.enemies)

def targetHeros(func):
    return lambda env: func(env.heroes)

def targetAll(group):
    pass


def targetRandom(group):
    pass


def targetMinFeature(group, feature):
    def targetMinX(group):
        pass
    return targetMinX
