import pygame


LENGTH = 640
WIDTH = 480

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

        transparent_surface = pygame.Surface((LENGTH, WIDTH), pygame.SRCALPHA)
        transparent_surface.set_alpha(16)
        color = (255, 255, 255)
        giant_font = pygame.font.Font(None, int(WIDTH / 2))
        giant_text = giant_font.render(f"{str(self.score)}", True, color)
        giant_text_rect = giant_text.get_rect(center=(self.position_x + LENGTH/8, self.position_y + WIDTH/2))
        transparent_surface.blit(giant_text, giant_text_rect)
        screen.blit(transparent_surface, (0, 0))

    def increase(self):
        self.score += 1
