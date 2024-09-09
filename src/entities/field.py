import pygame


class Field:

    def __init__(self, game):
        self.game = game
        self.height = game.screen.get_height()
        self.width = game.screen.get_width()

    def render(self, screen):
        transparent_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        color = (255, 255, 255, 36)

        dash_length = 10

        for y in range(0, self.height, dash_length * 2):
            pygame.draw.line(transparent_surface, color, (self.width / 2, y), (self.width / 2, y + dash_length), 1)

        screen.blit(transparent_surface, (0, 0))
