import pygame
from utils.constants import LENGTH, WIDTH


class Field:

    @staticmethod
    def draw(screen):
        # draw a line in the middle of the screen
        color = (255, 255, 255)
        dash_length = 10
        for y in range(0, WIDTH, dash_length * 2):
            pygame.draw.line(screen, color, (LENGTH/2, y), (LENGTH/2, y + dash_length), 1)
