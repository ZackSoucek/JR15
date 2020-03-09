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

def drawBar(OuterBar, InnerBar, percent, innerStart, innerEnd, position, layers):
    layers[2].blit(OuterBar, position)
    layers[2].blit(InnerBar.subsurface(pygame.Rect((innerStart + (innerEnd - innerStart) * (1 - percent), 0), (percent * (innerEnd - innerStart), InnerBar.get_height()))), (position[0] + innerStart + (innerEnd - innerStart) * (1 - percent), position[1]))
