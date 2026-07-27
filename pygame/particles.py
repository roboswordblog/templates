import pygame
import random

particleList = []

class Particle:
    def __init__(self, x, y, color, timer, dir, speed=0.1):
        self.x = x
        self.y = y
        self.color = color
        self.size = timer
        self.dir = dir
        self.speed = speed
        particleList.append(self)

    def update(self):
        if self.dir:
            self.x += self.dir[0]
            self.y += self.dir[1]
        else:
            self.x += random.randint(-5, 5)
            self.y += random.randint(-5, 5)
        self.size -= self.speed
        if self.size <= 0:
            particleList.remove(self)

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)
