import pygame
import random
from utils.constants import WIDTH

class Paddle:
    def __init__(self, width, height, position_x, position_y, color, speed) -> None:
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, direction):
        if direction == "UP":
            # Move the paddle down
            self.rect.y -= self.speed
        elif direction == "DOWN":
            # Move the paddle up
            self.rect.y += self.speed

        # Limit the paddle's movement inside the screen
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()

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

    def update(self, ball, difficulty):
        if difficulty == "easy":
            target_y = ball.rect.centery + 50  # Add a little offset
            speed = self.speed * 0.5  # Slow speed
        elif difficulty == "medium":
            target_y = ball.rect.centery + random.randint(-20, 20)
            speed = self.speed * 0.65  # Moderate speed
        elif difficulty == "hard":
            target_y = ball.rect.centery + random.randint(-10, 10)
            speed = self.speed  * 0.80  # High speed

        # Player paddle movement
        if self.rect.centery < target_y:
            self.rect.y += speed
        elif self.rect.centery > target_y:
            self.rect.y -= speed

        # Limit the paddle's movement inside the screen
        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()
