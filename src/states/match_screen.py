import pygame
from interfaces import BaseState
from entities import Ball, Field
from entities.paddle_factory import PaddleFactory


class MatchScreen(BaseState):
    def __init__(self, game) -> None:
        super().__init__(game)
        paddle_factory = PaddleFactory(game)
        self.player_paddle = paddle_factory.create_left_paddle()
        self.enemy_paddle = paddle_factory.create_right_paddle()
        self.ball = Ball(game)
        self.field = Field(game)
        # self.player_score = Score(game)
        # self.enemy_score = Score(game)

    def handle_input(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player_paddle.move("UP")
        if keys[pygame.K_DOWN]:
            self.player_paddle.move("DOWN")

    def update(self):
        # Atualizar a posição do paddle do inimigo
        # Atualizar os placares
        self.enemy_paddle.update(self.ball)

        if (self.ball.collision_with_paddle(self.player_paddle) or 
            self.ball.collision_with_paddle(self.enemy_paddle)):
            self.ball.speed_x *= -1

        self.ball.update()

        # if self.ball.is_at_left():
        #     self.enemy_score.increase()
        #     self.ball.reset_position()
        # if self.ball.is_at_right():
        #     self.player_score.increase()
        #     self.ball.reset_position()

    def render(self, screen):
        screen.fill((0, 0, 0))
        self.player_paddle.render(screen)
        self.enemy_paddle.render(screen)
        self.ball.render(screen)
        self.field.render(screen)
        # self.player_score.draw(screen, "Player 1")
        # self.enemy_score.draw(screen, "Player 2")
