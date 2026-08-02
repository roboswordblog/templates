import pygame

class Background:
    def __init__(self, image, down):
        self.x = 0
        self.y = 0
        self.x2 = 800
        self.y2 = 0
        self.down = down
        self.image = pygame.transform.scale(pygame.image.load(image), (800, 600))
        self.image2 = pygame.transform.scale(pygame.image.load(image), (800, 600))
        self.direction = 0

    def update(self):
        self.x -= self.down * self.direction
        self.x2 -= self.down * self.direction

        if self.direction == 1:
            if self.x <= -800:
                self.x = self.x2 + 800
            if self.x2 <= -800:
                self.x2 = self.x + 800
        else:
            if self.x >= 800:
                self.x = self.x2 - 800
            if self.x2 >= 800:
                self.x2 = self.x - 800

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        window.blit(self.image2, (self.x2, self.y2))


class Backgrounds:
    def __init__(self):
        self.backgroundList = []

    def makeBackgroundList(self):
        self.backgroundList.append(Background("assets/background/0.png", 0.05))
        self.backgroundList.append(Background("assets/background/1.png", 0.1))
        self.backgroundList.append(Background("assets/background/2.png", 0.2))
        self.backgroundList.append(Background("assets/background/3.png", 0.4))
        self.backgroundList.append(Background("assets/background/4.png", 0.8))

    def update(self, window):
        for bg in self.backgroundList:
            bg.update()
            bg.draw(window)
