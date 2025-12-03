# cli.py
from .player import HumanPlayer
from .game import Game

def run_cli() -> None:
    p1 = HumanPlayer("X")
    p2 = HumanPlayer("Y")  # or "O"
    game = Game(p1, p2)
    game.run()

