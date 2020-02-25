import pygame


class InterruptQueue:
    def __init__(self):
        self.queue = []

    def addInterrupt(self, func, *args):
        self.queue.append((func, args))

    def removeInterrupt(self, func, *args):
        self.queue.remove((func, args))

    def runInterrupts(self):
        argDict = {
            "mouse_pos": pygame.mouse.get_pos(),
            "mouse_clicked": pygame.mouse.get_pressed()
        }

        for func, args in self.queue:
            func(*(argDict[arg] for arg in args))

