import sys
import pygame
from constant.board import Board
from logic.othelloLogic import Othello


def main():
    game = Othello()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= Board.GRID_SIZE
                y //= Board.GRID_SIZE
                game.next_move(x, y)
        game.draw_board()
        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
