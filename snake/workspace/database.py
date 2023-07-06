import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS game_history (id INTEGER PRIMARY KEY AUTOINCREMENT, board_state TEXT, player_name TEXT)")

    def save_game_state(self, board_state, player_name):
        self.cursor.execute("INSERT INTO game_history (board_state, player_name) VALUES (?, ?)", (','.join(board_state), player_name))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
