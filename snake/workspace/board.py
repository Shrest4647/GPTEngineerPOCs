import pygame

class Board:
    def __init__(self):
        self.board_size = 3
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.square_size = 200
        self.margin = 100

    def draw(self, window):
        window.fill((255, 255, 255))

        for row in range(self.board_size):
            for col in range(self.board_size):
                pygame.draw.rect(window, (0, 0, 0), (col * self.square_size + self.margin, row * self.square_size + self.margin, self.square_size, self.square_size), 2)
                symbol = self.board[row][col]
                if symbol != ' ':
                    font = pygame.font.Font(None, 150)
                    text = font.render(symbol, True, (0, 0, 0))
                    text_rect = text.get_rect(center=(col * self.square_size + self.margin + self.square_size // 2, row * self.square_size + self.margin + self.square_size // 2))
                    window.blit(text, text_rect)

    def get_clicked_position(self, pos):
        row = (pos[1] - self.margin) // self.square_size
        col = (pos[0] - self.margin) // self.square_size
        return int(row), int(col)

    def is_valid_move(self, row, col):
        return self.board[row][col] == ' '

    def make_move(self, row, col, symbol):
        self.board[row][col] = symbol

    def get_state(self):
        return [symbol for row in self.board for symbol in row]

    def check_win(self, symbol):
        # Check rows
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True

        # Check columns
        for col in range(self.board_size):
            if all(row[col] == symbol for row in self.board):
                return True

        # Check diagonals
        if all(self.board[i][i] == symbol for i in range(self.board_size)):
            return True
        if all(self.board[i][self.board_size - 1 - i] == symbol for i in range(self.board_size)):
            return True

        return False

    def check_draw(self):
        return all(symbol != ' ' for row in self.board for symbol in row) and not self.check_win('X') and not self.check_win('O')
