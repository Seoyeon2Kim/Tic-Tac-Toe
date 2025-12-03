# board.py
from typing import List, Optional

class Board:
    def __init__(self) -> None:
        self.grid: List[List[str]] = [[" "]*3 for _ in range(3)]

    def place(self, row: int, col: int, mark: str) -> bool:
        if 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == " ":
            self.grid[row][col] = mark
            return True
        return False

    def winner(self) -> Optional[str]:
        lines = []
        # rows and cols
        lines.extend(self.grid)
        lines.extend([[self.grid[r][c] for r in range(3)] for c in range(3)])
        # diagonals
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])
        for line in lines:
            if line[0] != " " and line.count(line[0]) == 3:
                return line[0]
        return None

    def full(self) -> bool:
        return all(cell != " " for row in self.grid for cell in row)

    def __str__(self) -> str:
        rows = [" | ".join(r) for r in self.grid]
        return "\n---------\n".join(rows)

