import pygame
from ui import *
from particles import *
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("")

class States:
  def __init__(self):
    self.function = self.run

  def run(self):
    for particle in particleList:
      particle.draw(window)
      particle.update()

  def homePage(self):
    pass

  def connect(self, function):
    self.function = function

states = States()
clock = pygame.time.Clock()

while True:
    states.function()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(60)
    pygame.display.update()
  
