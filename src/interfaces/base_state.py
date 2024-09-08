from abc import ABC, abstractmethod


class BaseState(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def handle_input(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass
