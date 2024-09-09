import random
import pygame


class Ball:
    def __init__(self, game) -> None:
        self.game = game
        self.__set_properties()
        self.set_innitial_position()
        self.rect = pygame.Rect(self.position_x, self.position_y, self.radius, self.radius)

    def __set_properties(self):
        self.color = (255, 255, 255)
        self.radius = self.game.screen.get_width() / 48

    def set_innitial_position(self):
        self.position_x = (self.game.screen.get_width() - self.radius) / 2
        self.position_y = (self.game.screen.get_height() - self.radius) / 2
        self.speed_x = random.choice([1, -1]) * (self.game.screen.get_width() / 320)
        self.speed_y = random.choice([1, -1]) * (self.game.screen.get_height() / 320)

    def update(self):
        if self.__is_at_top() or self.__is_at_bottom():
            self.speed_y *= -1

        if self.__is_at_left() or self.__is_at_right():
            self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y        

    def render(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

    def __is_at_top(self):
        return self.rect.top <= 0

    def __is_at_bottom(self):
        return self.rect.bottom >= self.game.screen.get_height()

    def __is_at_left(self):
        return self.rect.left <= 0

    def __is_at_right(self):
        return self.rect.right >= self.game.screen.get_width()

    def collision_with_paddle(self, paddle):
        return self.rect.colliderect(paddle.rect)
