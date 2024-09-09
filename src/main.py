import pygame
from game import Game
from settings import GameSettings

def main():
    pygame.init()
    settings = GameSettings()
    game_manager = Game(settings=settings)
    game_manager.run()

if __name__ == "__main__":
    main()
