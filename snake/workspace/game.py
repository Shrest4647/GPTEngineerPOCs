import pygame
from board import Board
from player import Player
from ai import AI
from database import Database
from scoreboard import Scoreboard

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the game objects
board = Board()
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
ai = AI("AI", "O")
database = Database()
scoreboard = Scoreboard()

# Game loop
def game_loop():
    running = True
    current_player = player1
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if current_player == player1:
                    pos = pygame.mouse.get_pos()
                    row, col = board.get_clicked_position(pos)
                    if board.is_valid_move(row, col):
                        board.make_move(row, col, current_player.symbol)
                        database.save_game_state(board.get_state(), current_player.name)
                        game_over = board.check_win(current_player.symbol) or board.check_draw()
                        if game_over:
                            scoreboard.update_score(current_player.name)
                else:
                    row, col = ai.get_best_move(board.get_state())
                    board.make_move(row, col, current_player.symbol)
                    database.save_game_state(board.get_state(), current_player.name)
                    game_over = board.check_win(current_player.symbol) or board.check_draw()
                    if game_over:
                        scoreboard.update_score(current_player.name)

                current_player = player2 if current_player == player1 else player1

        # Draw the game board
        board.draw(window)

        # Update the display
        pygame.display.update()

    pygame.quit()

# Start the game
game_loop()
