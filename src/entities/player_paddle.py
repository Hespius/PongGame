from entities import Paddle

class PlayerPaddle(Paddle):
    def __init__(self, game, position_x, position_y, width, height) -> None:
        super().__init__(game, position_x, position_y, width, height)

    def move(self, direction):
        if direction == "UP" and not self.at_the_top():
            self.rect.y -= self.speed
        elif direction == "DOWN" and not self.at_the_bottom():
            self.rect.y += self.speed
