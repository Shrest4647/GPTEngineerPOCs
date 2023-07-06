Based on the requirements and assumptions, the core classes, functions, and methods that will be necessary are:

1. Game: Responsible for managing the game state, player moves, and AI moves.
   - `__init__(self, player_name, ai_name, ai_symbol)`: Initializes the game with player name, AI name, and AI symbol.
   - `start(self)`: Starts the game and manages the game loop.
   - `print_board(self)`: Prints the current state of the board.
   - `get_player_move(self)`: Gets the player's move from the command line.
   - `make_player_move(self, move)`: Makes the player's move on the board.
   - `make_ai_move(self)`: Makes the AI's move on the board.
   - `check_game_over(self)`: Checks if the game is over.
   - `print_winner(self)`: Prints the winner of the game.

2. AI: Represents the AI player and implements the minimax algorithm.
   - `__init__(self, name, symbol)`: Initializes the AI with a name and symbol.
   - `get_best_move(self, board_state)`: Implements the minimax algorithm to determine the best move for the AI.

3. main.py: The entry point of the application.

Now, let's proceed with the implementation of each file.

main.py
