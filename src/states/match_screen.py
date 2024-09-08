import pygame
from src.interfaces.base_state import BaseState
from entities import Ball, Paddle, Score
from utils.constants import LENGTH, WIDTH

class MatchScreen(BaseState):
    def __init__(self, game):
        super().__init__(game)
        self.clock = pygame.time.Clock()
        self.player_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH/64, position_y=WIDTH/2, color=(255, 255, 255), speed=LENGTH/320)
        self.enemy_paddle = Paddle(width=LENGTH/64, height=WIDTH/4, position_x=LENGTH - LENGTH/32, position_y=WIDTH/2, color=(255, 255, 255), speed=LENGTH/320)
        self.ball = Ball(radius=LENGTH/48, position_x=LENGTH/2 - LENGTH/64, position_y=WIDTH/2 - LENGTH/64, color=(255, 255, 255), speed=LENGTH/320)
        self.player_score = Score(position_x=LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)
        self.enemy_score = Score(position_x=LENGTH - LENGTH/2 + LENGTH/8, position_y=WIDTH/32, color=(255, 255, 255), font_size=LENGTH/16, font=None)

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player_paddle.move("UP")
        if keys[pygame.K_DOWN]:
            self.player_paddle.move("DOWN")

        self.enemy_paddle.update(self.ball, "hard")
        self.ball.move()

        if self.ball.is_at_left():
            self.enemy_score.increase()
            self.ball.reset_position()
        if self.ball.is_at_right():
            self.player_score.increase()
            self.ball.reset_position()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.player_paddle.draw(screen)
        self.enemy_paddle.draw(screen)
        self.ball.draw(screen)
        self.player_score.draw(screen, "Player 1")
        self.enemy_score.draw(screen, "Player 2")
