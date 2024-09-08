import pygame
from pygame.locals import QUIT
from states.start_screen import StartScreen
from interfaces import BaseState

class GameManager:
    title = "Pong!"

    def __init__(self, settings):
        self.__state = None
        self.__settings = settings
        self.__set_screen()
        self.__set_title()
        self.__set_fps()

    def __set_screen(self):
        self.screen = pygame.display.set_mode(
            (int(self.__settings.get("Window", "WINDOWS_LENGTH")),
             int(self.__settings.get("Window", "WINDOWS_WIDTH")))
        )

    def __set_title(self):
        pygame.display.set_caption(GameManager.title)

    def __set_fps(self):
        self.clock = pygame.time.Clock()
        self.fps = int(self.__settings.get("Game", "FPS"))

    def change_to(self, state: BaseState):
        self.__state = state

    def handle_input(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                exit()

        self.__state.handle_input(events)

    def update(self):
        self.__state.update()

    def render(self):
        self.__state.render(self.screen)

    def run(self):

        self.change_to(StartScreen(self))

        while True:
            events = pygame.event.get()
            self.handle_input(events)
            self.update()
            self.render()
            pygame.display.update()
            self.clock.tick(self.fps)
