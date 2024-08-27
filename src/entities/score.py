import pygame


class Score:
    def __init__(self, position_x, position_y, color, font_size, font) -> None:
        self.font = pygame.font.Font(font, int(font_size))
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.score = 0

    def draw(self, screen, player):
        text = self.font.render(f"{str(player).upper()} : {str(self.score).upper()}", True, self.color)
        screen.blit(text, (self.position_x, self.position_y))

    def increase(self):
        self.score += 1
