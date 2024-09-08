import pygame
from pygame.surface import Surface
from interfaces import BaseState

class StartScreen(BaseState):

    def __init__(self, game):
        super().__init__(game)
        self.__alpha = 255
        self.__fade_out = True
        self.__fade_speed = 5

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    from states.match_screen import MatchScreen
                    self.game.set_state(MatchScreen(self.game))

    def update(self):
        if self.__fade_out:
            self.__alpha -= self.__fade_speed
            if self.__alpha <= 0:
                self.__alpha = 0
                self.__fade_out = False
        else:
            self.__alpha += self.__fade_speed
            if self.__alpha >= 255:
                self.__alpha = 255
                self.__fade_out = True

    def render(self, screen: Surface):
        screen.fill((0, 0, 0))
        self.__render_start_text(screen)
        self.__render_game_title(screen)


    def __render_game_title(self, screen):
        font = pygame.font.Font(None, screen.get_width() // 4)
        text = font.render(self.game.title, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 3)
        screen.blit(text, text_rect)

    def __render_start_text(self, screen):
        font = pygame.font.Font(None, screen.get_width() // 10)
        text = font.render("Press Enter to Start", True, (255, 255, 255))
        text = text.convert_alpha()
        text.set_alpha(self.__alpha)
        text_rect = text.get_rect()
        text_rect.center = (screen.get_width() // 2, screen.get_height() // 1.5)
        screen.blit(text, text_rect)