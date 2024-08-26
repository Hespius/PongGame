import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Set up the window
LENGTH = 640
WIDTH = 480
# X = LENGTH / 64
# Y = WIDTH * 3 / 8

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
        if self.rect.y >= WIDTH:
            self.rect.y = 0
        else:
            self.rect.y += direction

 
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

        player_paddle.draw(screen)
        player_paddle.move(1)

        pygame.display.update()
