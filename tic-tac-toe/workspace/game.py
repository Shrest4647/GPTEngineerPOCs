from ai import AI

class Game:
    def __init__(self, player_name, ai_name, ai_symbol):
        self.player_name = player_name
        self.ai_name = ai_name
        self.ai_symbol = ai_symbol
        self.board = ["E"] * 9
        self.ai = AI(ai_name, ai_symbol)

    def start(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()
        while not self.check_game_over():
            self.get_player_move()
            if not self.check_game_over():
                self.make_ai_move()
                self.print_board()
        self.print_winner()

    def print_board(self):
        print("Current Board State:")
        for i in range(0, 9, 3):
            print(self.board[i], self.board[i + 1], self.board[i + 2])

    def get_player_move(self):
        valid_moves = [str(i) for i in range(1, 10)]
        while True:
            move = input("Enter your move (1-9): ")
            if move in valid_moves and self.board[int(move) - 1] == "E":
                self.make_player_move(int(move))
                break
            else:
                print("Invalid move. Please try again.")

    def make_player_move(self, move):
        self.board[move - 1] = "X"

    def make_ai_move(self):
        board_state = "".join(self.board)
        best_move = self.ai.get_best_move(board_state)
        self.board[best_move] = self.ai_symbol

    def check_game_over(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != "E":
                return True
        if "E" not in self.board:
            return True
        return False

    def print_winner(self):
        if "X" in self.board:
            print(f"{self.player_name} wins!")
        elif self.ai_symbol in self.board:
            print(f"{self.ai_name} wins!")
        else:
            print("It's a tie!")
