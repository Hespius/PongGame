import pygame
from src.interfaces.base_state import BaseState

class GameOverScreen(BaseState):
    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from states.start_screen import StartScreen
                    self.game.set_state(StartScreen(self.game))

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 255, 255))
        screen.blit(text, (200, 250))
        text = font.render("Press Enter to Restart", True, (255, 255, 255))
        screen.blit(text, (100, 350))
