class Scoreboard:
    def __init__(self):
        self.scores = {'Player 1': 0, 'Player 2': 0, 'AI': 0}

    def update_score(self, player_name):
        self.scores[player_name] += 1
