from random import choice

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

# decorators for targeting group
def targetEnemies(func):
    return lambda env: func(env.enemies)

def targetHeros(func):
    return lambda env: func(env.heroes)

def targetAll(func):
    return lambda env: func(env.heroes + env.enemies)

# functions for specific targeting within the group
def targetAll(group):
    for person in group:
        yield person

def targetRandom(group):
    yield group.choice()


def targetMinFeature(feature):
    def targetMinX(group):
        yield min(group, lambda x: x.getFeature(feature))
    return targetMinX

def targetMaxFeature(feature):
    def targetMaxX(group):
        yield max(group, lambda x: x.getFeature(feature))
    return targetMaxX
