import numpy as np

from game import Game


class GameAnalyzer:
    def __init__(self):
        self.win_cnt_player1 = 0
        self.win_cnt_player2 = 0
        self.win_times = []

    def play_n_games(self, n, game_type):
        for i in range(n):
            game = Game(game_type=game_type, verbose="zero")
            winner, number_of_shots_to_win = game.play()
            self.win_times.append(number_of_shots_to_win)
            if winner == "player1":
                self.win_cnt_player1 += 1
            elif winner == "player2":
                self.win_cnt_player2 += 1
            elif winner == "player1player2":
                self.win_cnt_player1 += 0.5
                self.win_cnt_player2 += 0.5
            else:
                raise Exception("unexpected win result")
        self.print_tabulated_results()

    def print_tabulated_results(self):
        print("Player1 won {} games, Player2 won {} games".format(self.win_cnt_player1, self.win_cnt_player2))
        print("It took an average of {} shots to win, with best: {} and worst: {}".format(np.mean(self.win_times),
                                                                                          np.min(self.win_times),
                                                                                          np.max(self.win_times)))