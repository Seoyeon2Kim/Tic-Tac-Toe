# player.py
from abc import ABC, abstractmethod
import sys

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

            # Exit when the user inputs "exit" or "q"
            if raw.lower() in ("exit", "q"):
                print("Exiting the game...")
                sys.exit(0)

            try:
                r, c = map(int, raw.split())
                return r, c
            except Exception:
                print("Invalid input. Use two integers: row col from 0 to 2 (e.g. 1 2).")

