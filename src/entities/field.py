import pygame
from utils.constants import LENGTH, WIDTH


class Field:

    @staticmethod
    def draw(screen):
        # Create a transparent surface
        transparent_surface = pygame.Surface((LENGTH, WIDTH), pygame.SRCALPHA)
        
        # Define the color with transparency (RGBA)
        color = (255, 255, 255, 36)  # 128 is the alpha value for 50% transparency
        
        dash_length = 10
        for y in range(0, WIDTH, dash_length * 2):
            pygame.draw.line(transparent_surface, color, (LENGTH / 2, y), (LENGTH / 2, y + dash_length), 1)

        # Blit the transparent surface onto the main screen
        screen.blit(transparent_surface, (0, 0))
