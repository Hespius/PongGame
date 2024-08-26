import random
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


class Score:
    def __init__(self, position_x, position_y, color, font_size, font) -> None:
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.font = pygame.font.Font(font, int(font_size))
        self.score = 0

    def draw(self, surface, player):
        text = self.font.render(f"{str(player).upper()} : {str(self.score).upper()}", True, self.color)
        surface.blit(text, (self.position_x, self.position_y))

    def increase(self):
        self.score += 1

class Paddle:
    def __init__(self, width, height, position_x, position_y, color) -> None:
        self.rect = pygame.Rect(position_x, position_y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self, direction):
        if direction > 0:
            # Move the paddle down
            if not self.__is_at_bottom():
                self.rect.y += direction
        else:
            # Move the paddle up
            if not self.__is_at_top():
                self.rect.y += direction

    def __is_at_top(self):
        # Set up the top limit of the paddle
        if self.rect.y == 0:
            return True
        return False

    def __is_at_bottom(self):
        # Set up the bottom limit of the paddle
        if self.rect.y == WIDTH - self.rect.height:
            return True
        return False

    def at_the_limit(self):
        if self.__is_at_top() or self.__is_at_bottom():
            return True
        return False


class Ball:
    def __init__(self, radius, position_x, position_y, color, speed) -> None:
        self.color = color
        self.radius = radius
        self.position_x = position_x
        self.position_y = position_y
        self.speed_x = speed
        self.speed_y = speed

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.position_x, self.position_y), self.radius)


    def move(self):
        self.position_x += self.speed_x
        self.position_y += self.speed_y

        if self.__is_at_top() or self.__is_at_bottom():
            self.speed_y *= -1

    def __is_at_top(self):
        # Set up the top limit of the ball
        if self.position_y == 0:
            return True
        return False

    def __is_at_bottom(self):
        # Set up the bottom limit of the ball
        if self.position_y == WIDTH - self.radius:
            return True
        return False

    def at_the_limit(self):
        if self.__is_at_top() or self.__is_at_bottom():
            return True
        return False

    def collision_with_paddle(self, paddle):
        if (self.position_x - self.radius == paddle.rect.x and 
            self.position_y >= paddle.rect.y and 
            self.position_y <= paddle.rect.y + paddle.rect.height):
            return True
        return False

# Set up the player paddle
player_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH/64, position_y=WIDTH/2, color=(255, 255, 255))
# Set up the enemy paddle
enemy_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH - LENGTH/32, position_y=WIDTH/2, color=(255, 255, 255))
# Set up the ball
ball_direction = random.choice([1, -1])
ball = Ball(radius=LENGTH/64, position_x=LENGTH/2 - LENGTH/64, position_y=WIDTH/2 - LENGTH/64, color=(255, 255, 255), speed=ball_direction*LENGTH/320)

# Set up the scores
player_score = Score(position_x=LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)
enemy_score = Score(position_x=LENGTH - LENGTH/2 + LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)

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

    # Draw the scores
    player_score.draw(screen, "Player")
    enemy_score.draw(screen, "Enemy")

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

    # Draw the ball
    ball.draw(screen)
    ball.move()

    if ball.collision_with_paddle(player_paddle) or ball.collision_with_paddle(enemy_paddle):
        ball.speed_x *= -1

    enemy_paddle.move(enemy_paddle_direction  * LENGTH/320)



    pygame.display.update()
