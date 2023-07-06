import random

class AI:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_best_move(self, board_state):
        # Implement minimax algorithm to determine the best move
        return self.get_random_move(board_state)

    def get_random_move(self, board_state):
        empty_positions = [i for i, char in enumerate(board_state) if char == "E"]
        return random.choice(empty_positions)
