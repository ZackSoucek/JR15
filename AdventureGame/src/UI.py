import pygame


class Button:
    def __init__(self, x, y, width, height, image, onClick, interruptQueue):
        self.onClick = onClick
        self.rect = pygame.Rect(x,y,width,height)
        self.image = pygame.transform.scale(image,(width,height))

        interruptQueue.addInterrupt(self.checkClicked, "mouse_pos", "mouse_clicked")
        self.clickFlag = False

    def checkClicked(self, mousePos, mouseClicked):
        if (not self.clickFlag) and mouseClicked[0] and self.rect.collidepoint(*mousePos):
            self.onClick()
        if self.clickFlag and not mouseClicked[0]:
            self.clickFlag = False
        if mouseClicked[0]:
            self.clickFlag = True

    def removeButton(self,interruptQueue):
        interruptQueue.removeInterrupt(self.checkClicked, "mouse_pos", "mouse_clicked")

    def drawButton(self, layers):
        layers[2].blit(self.image,self.rect)


