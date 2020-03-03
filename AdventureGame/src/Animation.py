import pygame


class Animation:
    def __init__(self, folderPath, numFrames, frameTime):
        self.frames = [pygame.image.load(folderPath + f"/{i}.png") for i in range(numFrames)]
        self.position = (-1,-1)
        self.frameTime = frameTime
        self.time = -1
        self.running = False

    def start(self, size, position):
        self.frames = [pygame.transform.scale(frame,size) for frame in self.frames]
        self.position = position
        self.time = pygame.time.get_ticks()
        self.running = True

    def drawFrame(self, layers, layer):
        frame = (pygame.time.get_ticks() - self.time)%self.frameTime
        if frame > len(self.frames) - 1:
            self.running = False
            frame = len(self.frames) - 1
        layers[layer].blit(self.frames[frame], self.position)

        return self.running

    def getFrame(self, layers):
        frame = (pygame.time.get_ticks() - self.time)%self.frameTime
        if frame > len(self.frames) - 1:
            self.running = False
            frame = len(self.frames) - 1

        return self.running, self.frames[frame]


class AnimationHandler:
    def __init__(self):
        self.animations = []

    def addAnimation(self, animation, position, size, layer, onFinish):
        self.animations.start(size, position)
        self.animations.append((animation, onFinish, layer))

    def runAnimations(self, layers):
        nextAnimations = []
        for animation, onFinish, layer in self.animations:
            if animation.drawFrame(layers, layer):
                nextAnimations.append((animation, onFinish, layer))
            else:
                onFinish()
        self.animations = nextAnimations


