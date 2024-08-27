import pygame
from pygame.locals import K_KP_ENTER
from utils.constants import LENGTH, WIDTH, SCORE_TO_FINISH


class EndGame:

    @classmethod
    def check_if_someone_win(cls, player1_score, player2_score):
        if player1_score == SCORE_TO_FINISH or player2_score == SCORE_TO_FINISH:
            return True
        return False

    @classmethod
    def draw(cls, screen, player1_score, player2_score):
        if player1_score > player2_score:
            result = "You Wins"
        elif player1_score < player2_score:            
            result = "You Lose"
        else:
            result = "Draw"

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render(result, True, (255, 255, 255))
        text_rect = text.get_rect(center=(LENGTH / 2, WIDTH / 2))
        screen.blit(text, text_rect)
        pygame.display.update()

        wainting_for_enter = True
        while wainting_for_enter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_KP_ENTER):
                    pygame.quit()
                    exit()
