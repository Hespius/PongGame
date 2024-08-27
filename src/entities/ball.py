import random
import pygame
from utils.constants import LENGTH, WIDTH


class Ball:
    def __init__(self, radius, position_x, position_y, color, speed) -> None:
        self.rect = pygame.Rect(position_x, position_y, radius, radius)
        self.color = color
        self.radius = radius
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed
        self.speed_y = speed

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.is_at_top() or self.is_at_bottom():
            self.speed_y *= -1

    def is_at_top(self):
        # Set up the top limit of the ball
        if self.rect.top <= 0:
            return True
        return False

    def is_at_bottom(self):
        # Set up the bottom limit of the ball
        if self.rect.bottom >= WIDTH:
            return True
        return False

    def is_at_left(self):
        # Set up the left limit of the ball
        if self.rect.left <= 0:
            return True
        return False

    def is_at_right(self):
        # Set up the right limit of the ball
        if self.rect.right >= LENGTH:
            return True
        return False

    def at_the_limit(self):
        if (self.is_at_top() or 
            self.is_at_bottom() or 
            self.is_at_left() or 
            self.is_at_right()):
            return True
        return False

    def collision_with_paddle(self, paddle):
        return self.rect.colliderect(paddle.rect)

    def reset_position(self):
        self.rect.x = LENGTH // 2 - self.rect.width // 2
        self.rect.y = WIDTH // 2 - self.rect.height // 2
        self.speed_x = random.choice([1, -1]) * abs(self.speed_x)
        self.speed_y = random.choice([1, -1]) * abs(self.speed_y)
