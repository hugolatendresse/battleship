import numpy as np

from src.game_analyzer import GameAnalyzer


def main():
    # np.random.seed(0)
    game_analyzer = GameAnalyzer()
    game_analyzer.play_n_games(n=100, game_type="machine_vs_machine")


if __name__ == "__main__":
    main()
