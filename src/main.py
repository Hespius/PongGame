import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Set up the window
LENGTH = 640
WIDTH = 480

# Set up the window size
screen = pygame.display.set_mode(size=(LENGTH, WIDTH))

# Set up name of the window
pygame.display.set_caption(title="Pong")

# Set up the clock
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, width, height, position_x, position_y, color) -> None:
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, direction):
        if direction > 0:
            # Move the paddle down
            if not self.__bottom_limit():
                self.rect.y += direction
        else:
            # Move the paddle up
            if not self.__top_limit():
                self.rect.y += direction

    def __top_limit(self):
        # Set up the top limit of the paddle
        if self.rect.y == 0:
            return True
        return False

    def __bottom_limit(self):
        # Set up the bottom limit of the paddle
        if self.rect.y == WIDTH - self.rect.height:
            return True
        return False

# Set up the player paddle
player_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH/64, position_y=WIDTH/2, color=(255, 255, 255))


if __name__ == "__main__":
    while True:
        # Set up the frame rate
        clock.tick(120)

        # Set up the background
        screen.fill((0, 0, 0))

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                exit()

        if pygame.key.get_pressed()[K_UP]:
            player_paddle.move(-LENGTH/320)
        if pygame.key.get_pressed()[K_DOWN]:
            player_paddle.move(LENGTH/320)

        player_paddle.draw(screen)

        pygame.display.update()
