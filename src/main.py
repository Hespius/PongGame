import pygame
from sys import exit
from pygame.locals import *

from entities import Ball, Score, Paddle, EndGame, Field
from utils.constants import LENGTH, WIDTH, SCORE_TO_FINISH
from settings import GameSettings

pygame.init()

settings = GameSettings()

# Set up the window size
screen = pygame.display.set_mode((int(settings.get('Window', 'WINDOWS_LENGTH')), int(settings.get('Window', 'WINDOWS_WIDTH'))))

# Set up name of the window
pygame.display.set_caption(title="Pong")

# Set up the clock
clock = pygame.time.Clock()
fps = int(settings.get('Game', 'FPS'))

# Set up the player paddle
player_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH/64, position_y=WIDTH/2, color=(255, 255, 255), speed=LENGTH/320)
# Set up the enemy paddle
enemy_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH - LENGTH/32, position_y=WIDTH/2, color=(255, 255, 255), speed=LENGTH/320)
# Set up the ball
ball = Ball(radius=LENGTH/48, position_x=LENGTH/2 - LENGTH/64, position_y=WIDTH/2 - LENGTH/64, color=(255, 255, 255), speed=LENGTH/320)

# Set up the scores
player_score = Score(position_x=LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)
enemy_score = Score(position_x=LENGTH - LENGTH/2 + LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)

# Set up the enemy paddle direction
enemy_paddle_direction = 1

difficulty = settings.get('Game', 'DIFFICULTY')

while True:
    for events in pygame.event.get():
        if events.type == QUIT:
            pygame.quit()
            exit()

    # Set up the frame rate
    clock.tick(fps)

    # Set up the background
    screen.fill((0, 0, 0))

    # Draw the field
    Field.draw(screen)

    # Draw the scores
    player_score.draw(screen, "Player 1")
    enemy_score.draw(screen, "Player 2")

    # Player paddle movement
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_paddle.move("UP")
    if keys[K_DOWN]:
        player_paddle.move("DOWN")

    # Update the paddles
    enemy_paddle.update(ball, difficulty)

    # Draw the paddles
    player_paddle.draw(screen)
    enemy_paddle.draw(screen)

    # Draw the ball
    ball.draw(screen)
    ball.move()

    # Check if the ball collides with the paddles
    if ball.collision_with_paddle(player_paddle) or ball.collision_with_paddle(enemy_paddle):
        ball.speed_x *= -1

    # Enemy AI
    enemy_paddle.move(enemy_paddle_direction  * LENGTH/320)

    if ball.is_at_left():
        enemy_score.increase()
        ball.reset_position()
    if ball.is_at_right():
        player_score.increase()
        ball.reset_position()

    if EndGame.check_if_someone_win(player_score.score, enemy_score.score):
        EndGame.draw(screen, player_score.score, enemy_score.score)

    pygame.display.update()
