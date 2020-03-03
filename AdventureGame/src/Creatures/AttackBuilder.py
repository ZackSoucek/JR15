from random import choice

class Attack:
    def __init__(self, modifier, flatDamage, percentDamage, targetFunc, animation):
        self.modifier = modifier
        self.flatDamage = flatDamage
        self.percentDamage = percentDamage
        self.animation = animation
        self.targetFunc = targetFunc

    def runAttack(self, env, battle, animationHandler):
        targets = list(self.targetFunc(env))
        battle.lockdown(len(targets))
        for creature in targets:
            creature.takeDamage(self.modifier, self.flatDamage, self.percentDamage)
            animationHandler.addAnimation(
                self.animation, creature.position, creature.image.get_size(), 3, lambda: battle.unlock(1)
            )

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
