# Tic-Tac-Toe
This Tic-Tac-Toe Game is written in Python language

## Design overview
- **Board:** Manages a 3x3 grid, validates moves, and checks win/draw.
- **Player:** Abstract base for different input strategies.
  - **HumanPlayer** uses CLI prompts.
- **Game:** Orchestrates turns, applies rules, and ends when win/draw.
- **CLI:** Thin UI layer to keep logic testable.
- **Entry point:** `src/main.py`



## Getting started

### Prerequisites
- Python 3.11+

### Setup and run
- **Windows:**

