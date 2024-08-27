import pygame
from utils.constants import WIDTH

class Paddle:
    def __init__(self, width, height, position_x, position_y, color) -> None:
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction):
        if direction > 0:
            # Move the paddle down
            if not self.is_at_bottom():
                self.rect.y += direction
        else:
            # Move the paddle up
            if not self.is_at_top():
                self.rect.y += direction

    def is_at_top(self):
        # Set up the top limit of the paddle
        if self.rect.y == 0:
            return True
        return False

    def is_at_bottom(self):
        # Set up the bottom limit of the paddle
        if self.rect.y == WIDTH - self.rect.height:
            return True
        return False

    def at_the_limit(self):
        if self.is_at_top() or self.is_at_bottom():
            return True
        return False
