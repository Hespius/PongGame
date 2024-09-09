from enum import Enum
import pygame
from pygame.locals import K_KP_ENTER

LENGTH = 640
WIDTH = 480
SCORE_TO_FINISH = 5

class Result(Enum):
    WIN = "You Wins"
    LOSE = "You Lose"
    DRAW = "Draw"

class EndGame:

    @staticmethod
    def check_if_someone_win(player1_score, player2_score):
        if player1_score == SCORE_TO_FINISH or player2_score == SCORE_TO_FINISH:
            return True
        return False

    @staticmethod
    def draw(screen, player1_score, player2_score):
        if player1_score > player2_score:
            result = Result.WIN
        elif player1_score < player2_score:
            result = Result.LOSE
        else:
            result = Result.DRAW

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, WIDTH // 4)
        text = font.render(result.value, True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2, WIDTH / 2 - WIDTH / 4))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, WIDTH // 8)

        text = font.render(f"Player 1", True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2 - LENGTH / 4, WIDTH / 2 - WIDTH / 16))
        screen.blit(text, text_rect)

        text = font.render(f"{player1_score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2 - LENGTH / 4, WIDTH / 2 + WIDTH / 16))
        screen.blit(text, text_rect)

        text = font.render(f"Player 2", True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2 + LENGTH / 4, WIDTH / 2 - WIDTH / 16))
        screen.blit(text, text_rect)

        text = font.render(f"{player2_score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2 + LENGTH / 4, WIDTH / 2 + WIDTH / 16))
        screen.blit(text, text_rect)

        font = pygame.font.Font(None, WIDTH // 16)
        text = font.render("Press Enter to exit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2, WIDTH / 2 + WIDTH / 4))
        screen.blit(text, text_rect)

        pygame.display.update()

        wainting_for_enter = True
        while wainting_for_enter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_KP_ENTER):
                    pygame.quit()
                    exit()
