# player.py
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, mark: str) -> None:
        self.mark = mark

    @abstractmethod
    def choose_move(self, board) -> tuple[int, int]:
        pass

class HumanPlayer(Player):
    def choose_move(self, board) -> tuple[int, int]:
        while True:
            raw = input(f"Player {self.mark}, enter move (row col): ").strip()
            try:
                r, c = map(int, raw.split())
                return r, c
            except Exception:
                print("Invalid input. Use two integers: row col (0-2).")

