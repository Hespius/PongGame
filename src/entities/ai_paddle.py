from entities import Paddle


class AIPaddle(Paddle):
    def __init__(self, game, position_x, position_y, width, height) -> None:
        super().__init__(game, position_x, position_y, width, height)
        self.difficulty = self.game.settings.get("Game", "difficulty")

    def update(self, ball):
        if self.difficulty == "easy":
            self.easy_mode(ball)
        elif self.difficulty == "medium":
            self.medium_mode(ball)
        elif self.difficulty == "hard":
            self.hard_mode(ball)

    def easy_mode(self, ball):
        if ball.rect.centery < self.rect.centery and not self.at_the_top():
            self.rect.y -= self.speed * 0.5
        elif ball.rect.centery > self.rect.centery and not self.at_the_bottom():
            self.rect.y += self.speed * 0.5

    def medium_mode(self, ball):
        if ball.rect.centery < self.rect.centery and not self.at_the_top():
            self.rect.y -= self.speed * 0.75
        elif ball.rect.centery > self.rect.centery and not self.at_the_bottom():
            self.rect.y += self.speed * 0.75

    def hard_mode(self, ball):
        if ball.rect.centery < self.rect.centery and not self.at_the_top():
            self.rect.y -= self.speed
        elif ball.rect.centery > self.rect.centery and not self.at_the_bottom():
            self.rect.y += self.speed
