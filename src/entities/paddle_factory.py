from entities import Paddle, AIPaddle, PlayerPaddle

class PaddleFactory:
    def __init__(self, game):
        self.game = game

    def create_left_paddle(self):
        width = self.game.screen.get_width() / 64
        height = self.game.screen.get_height() / 4
        position_x = self.game.screen.get_width() / 64
        position_y = self.game.screen.get_height() / 2
        return PlayerPaddle(self.game, position_x, position_y, width, height)

    def create_right_paddle(self):
        width = self.game.screen.get_width() / 64
        height = self.game.screen.get_height() / 4
        position_x = self.game.screen.get_width() - self.game.screen.get_width() / 32
        position_y = self.game.screen.get_height() / 2
        return AIPaddle(self.game, position_x, position_y, width, height)
