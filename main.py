import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Set up the window
LENGTH = 640
WIDTH = 480

screen = pygame.display.set_mode((LENGTH, WIDTH))

# Set up name of the window
pygame.display.set_caption("Pong")

while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            exit()
        pygame.display.update()
