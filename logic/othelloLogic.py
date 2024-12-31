from constant.board import Board
import pygame
import sys

pygame.init()
# ウィンドウサイズの設定
screen = pygame.display.set_mode((Board.SIZE, Board.SIZE + 60))
# ウィンドウタイトルの設定
pygame.display.set_caption("オセロ")


class Othello:
    def __init__(self):
        # 石配置用の配列設定
        self.board = [
            [None] * Board.BOARD_SIZE for _ in range(Board.BOARD_SIZE)
        ]

        # 初期石の設定
        mid = Board.BOARD_SIZE // 2
        self.board[mid - 1][mid - 1] = Board.WHITE
        self.board[mid - 1][mid] = Board.BLACK
        self.board[mid][mid - 1] = Board.BLACK
        self.board[mid][mid] = Board.WHITE

        # 黒の番から開始
        self.turn = Board.BLACK

    # ボードの描画

    def draw_board(self):
        screen.fill(Board.GREEN)
        for x in range(Board.BOARD_SIZE):
            for y in range(Board.BOARD_SIZE):
                rect = pygame.Rect(
                    x * Board.GRID_SIZE, y * Board.GRID_SIZE, Board.GRID_SIZE, Board.GRID_SIZE)
                pygame.draw.rect(screen, Board.BLACK, rect, Board.STROKE)
                if self.board[x][y] is not None:
                    self.draw_stone(x, y, self.board[x][y])

    # 石の描画
    def draw_stone(self, x, y, color):
        pygame.draw.circle(screen, color, (x * Board.GRID_SIZE + Board.GRID_SIZE //
                           2, y * Board.GRID_SIZE + Board.GRID_SIZE // 2), Board.GRID_SIZE // 2 - 4)
        self.draw_turn(Board.SIZE // 2, Board.SIZE + 30)

    # どっちの順番か表示
    def draw_turn(self, x, y):
        # フォントの作成
        font = pygame.font.Font(None, 48)  # フォントサイズの指定
        turn_msg = "Black turn"
        text_color = Board.BLACK
        if self.turn == Board.WHITE:
            turn_msg = "White turn"
            text_color = Board.WHITE
        text = font.render(turn_msg, True, text_color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    # 次の手の存在確認
    def has_valid_move(self):
        for x in range(Board.BOARD_SIZE):
            for y in range(Board.BOARD_SIZE):
                if self.is_valid_move(x, y):
                    return True
        return False

    # 有効な手かの確認
    def is_valid_move(self, x, y):
        try:
            if self.board[x][y] is not None:
                return False
            opponent = Board.WHITE if self.turn == Board.BLACK else Board.BLACK
            valid = False
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < Board.BOARD_SIZE and 0 <= ny < Board.BOARD_SIZE and self.board[nx][ny] == opponent:
                    while 0 <= nx < Board.BOARD_SIZE and 0 <= ny < Board.BOARD_SIZE:
                        nx += dx
                        ny += dy
                        if not (0 <= nx < Board.BOARD_SIZE and 0 <= ny < Board.BOARD_SIZE):
                            break
                        if self.board[nx][ny] is None:
                            break
                        if self.board[nx][ny] == self.turn:
                            valid = True
                            break
        except Exception as e:
            print("範囲外もしくは予期せぬエラーです")
            valid = False
        return valid

    # 石の配置と反転
    def next_move(self, x, y):
        if self.is_board_full():
            result = self.game_end()
            self.display_result(result)
        elif self.is_valid_move(x, y):
            self.board[x][y] = self.turn
            self.flip_stones(x, y)
            self.turn = Board.WHITE if self.turn == Board.BLACK else Board.BLACK
            if not self.has_valid_move() or self.is_board_full():
                self.turn = Board.WHITE if self.turn == Board.BLACK else Board.BLACK
                if not self.has_valid_move():
                    result = self.game_end()
                    self.display_result(result)

    # 石の反転
    def flip_stones(self, x, y):
        opponent = Board.WHITE if self.turn == Board.BLACK else Board.BLACK
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            pieces_to_flip = []
            nx, ny = x + dx, y + dy
            while 0 <= nx < Board.BOARD_SIZE and 0 <= ny < Board.BOARD_SIZE and self.board[nx][ny] == opponent:
                pieces_to_flip.append((nx, ny))
                nx += dx
                ny += dy
            if 0 <= nx < Board.BOARD_SIZE and 0 <= ny < Board.BOARD_SIZE and self.board[nx][ny] == self.turn:
                for px, py in pieces_to_flip:
                    self.board[px][py] = self.turn

    # 盤面がいっぱい（=ゲーム終了）のチェック
    def is_board_full(self):
        for row in self.board:
            if None in row:
                return False
        return True

    # 終了時のリザルト判定
    def game_end(self):
        black_count = sum(row.count(Board.BLACK) for row in self.board)
        white_count = sum(row.count(Board.WHITE) for row in self.board)
        if black_count > white_count:
            return "Winner black"
        elif white_count > black_count:
            return "Winner white"
        else:
            return "Draw"

    # リザルト表示
    def display_result(self, result):
        font = pygame.font.Font(None, 74)
        text = font.render(result, True, Board.YELLOW)
        text_rect = text.get_rect(center=(Board.SIZE // 2, Board.SIZE // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(10000)
        pygame.quit()
        sys.exit()
