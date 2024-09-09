import pygame
from pygame import Surface


class Paddle:
    def __init__(self, game, position_x, position_y, width, height) -> None:
        self.game = game
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = (255, 255, 255)
        self.speed = self.game.screen.get_height() * 0.005

    def at_the_top(self):
        return self.rect.y <= 0

    def at_the_bottom(self):
        return self.rect.y >= self.game.screen.get_height() - self.rect.height

    def render(self, screen: Surface):
        pygame.draw.rect(screen, self.color, self.rect)
