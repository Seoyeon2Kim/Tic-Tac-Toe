# Tic-Tac-Toe
This Tic-Tac-Toe Game is written in Python language

The game would work like the below :


https://github.com/user-attachments/assets/0e066f7e-2510-4854-9a02-c0c04c8211ca




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

