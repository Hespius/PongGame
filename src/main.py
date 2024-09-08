import pygame
from game_manager import GameManager
from settings import GameSettings

def main():
    pygame.init()
    settings = GameSettings()
    game_manager = GameManager(settings=settings)
    game_manager.run()

if __name__ == "__main__":
    main()
