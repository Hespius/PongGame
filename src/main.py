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
            if not self.bottom_limit():
                self.rect.y += direction
        else:
            # Move the paddle up
            if not self.top_limit():
                self.rect.y += direction

    def top_limit(self):
        # Set up the top limit of the paddle
        if self.rect.y == 0:
            return True
        return False

    def bottom_limit(self):
        # Set up the bottom limit of the paddle
        if self.rect.y == WIDTH - self.rect.height:
            return True
        return False

    def at_the_limit(self):
        if self.top_limit() or self.bottom_limit():
            return True
        return False


# Set up the player paddle
player_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH/64, position_y=WIDTH/2, color=(255, 255, 255))
enemy_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH - LENGTH/32, position_y=WIDTH/2, color=(255, 255, 255))

# Set up the enemy paddle direction
enemy_paddle_direction = 1

while True:
    # Set up the frame rate
    clock.tick(120)

    # Set up the background
    screen.fill((0, 0, 0))

    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            exit()

    # Draw the player paddle
    player_paddle.draw(screen)

    if pygame.key.get_pressed()[K_UP]:
        player_paddle.move(-LENGTH/320)
    if pygame.key.get_pressed()[K_DOWN]:
        player_paddle.move(LENGTH/320)

    # Draw the enemy paddle
    enemy_paddle.draw(screen)

    if enemy_paddle.at_the_limit():
        enemy_paddle_direction *= -1

    enemy_paddle.move(enemy_paddle_direction  * LENGTH/320)

    pygame.display.update()
