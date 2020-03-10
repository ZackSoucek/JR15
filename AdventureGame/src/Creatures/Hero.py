import pygame
from src.Creatures.Creature import Creature
from src.UI import drawBar

class Hero(Creature):

    nameFont = pygame.font.Font('../art/Example.ttf', 26)
    numberFont = pygame.font.Font('../art/Example.ttf', 17)
    healthbar = pygame.transform.scale(pygame.image.load("../art/Basic UI/healthbar.png"), (310 - 100, 25)).convert_alpha()
    healthbarBar = pygame.transform.scale(pygame.image.load("../art/Basic UI/healthbarBar.png"), (310 - 100, 25)).convert_alpha()

    namePlate = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateMiddle.png'),
                                       (50 * 26 // 36, 50* 26 // 36)).convert_alpha()
    namePlateLeft = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateLeft.png'),
                                           (13* 26 // 36, 50* 26 // 36)).convert_alpha()
    namePlateRight = pygame.transform.scale(pygame.image.load('../art/Basic UI/NameplateRight.png'),
                                            (13* 26 // 36, 50* 26 // 36)).convert_alpha()

    def __init__(self, health, speed, damageModifiers, image, name):
        image.fill((0,0,0))
        super().__init__((310-100)/Creature.sizeHeight, health, speed, damageModifiers, image, None, name, self.nameFont)

    def draw(self, layers, selected):
        super().draw(layers, selected)
        drawBar(self.healthbar, self.healthbarBar, self.currHealth / self.maxHealth, 54,202, (self.position[0], self.position[1] + self.size * self.sizeHeight + 5), layers)
        damage = self.numberFont.render(str(self.currHealth), False, (0, 0, 0))
        layers[2].blit(damage, (self.position[0] + 20 - damage.get_width()//2, self.position[1] + self.size * self.sizeHeight + 5 + (self.healthbar.get_height() - self.numberFont.get_height()) // 2 + 1))

    def changePosition(self, x, y):
        self.position = (x, y)
        self.textPosition = (x + (self.size*self.sizeHeight - self.name.get_width()) // 2, y - self.name.get_height())

    def basicAttack(self, env):
        print("basic attack")

    def uniqueAttack(self, env):
        print("unique attack")

    def specialAttack(self, env):
        print("special attack")
