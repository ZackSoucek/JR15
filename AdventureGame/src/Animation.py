import pygame


class Animation:
    def __init__(self, folderPath, size, position, numFrames, frameTime):
        self.frames = [pygame.transform.scale(pygame.image.load(folderPath + f"\\{i}.png"),size) for i in range(numFrames)]
        self.position = position
        self.frameTime = frameTime
        self.time = -1
        self.running = False

    def start(self):
        self.time = pygame.time.get_ticks()
        self.running = True

    def drawFrame(self, layers):
        frame = (pygame.time.get_ticks() - self.time)%self.frameTime
        if frame > len(self.frames) - 1:
            self.running = False
            frame = len(self.frames) - 1
        layers[3].blit(self.frames[(pygame.time.get_ticks() - self.time)%self.frameTime], self.position)

        return self.running






