# game.py
from .board import Board
from .player import Player

class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.board = Board()
        self.players = [p1, p2]
        self.turn = 0

    def step(self) -> bool:
        current = self.players[self.turn]
        print(self.board)
        r, c = current.choose_move(self.board)
        if not self.board.place(r, c, current.mark):
            print("Invalid move. Try again.")
            return False
        winner = self.board.winner()
        if winner:
            print(self.board)
            print(f"Winner: {winner}")
            return True
        if self.board.full():
            print(self.board)
            print("Draw.")
            return True
        self.turn = 1 - self.turn
        return False

    def run(self) -> None:
        finished = False
        while not finished:
            finished = self.step()

