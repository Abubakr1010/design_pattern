from enum import Enum
from abc import ABC, abstractmethod
import random


class Symbol(Enum):

    EMPTY = " "
    X = "X"
    O = "O"


class Board:

    def __init__(self, size: int = 3):
        self.size = size
        self.grid = [[None for _ in range(size)]for _ in range(size)]

    def display(self):
        for row in self.grid:
             print("|".join(cell.value if cell else " "for cell in row))
             print("-" * (self.size * 2))

    def is_valid_move(self, row: int, col:int) -> bool:
        return 0 <= row < self.size and 0 <= col <= self.size and self.grid[row][col]

    def place_peice(self, row:int, col:int, symbol: Symbol) -> bool:
        if self.is_valid_move(row, col):
            self.grid[row][col] = Symbol
            return True
        else:
            return False

    def is_full(self) -> bool:
        return all(cell is not None for row in self.grid for cell in row)


class Player(ABC):

    def __init__(self, name: str, symbol: Symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board:Board) -> tuple[int,int]:
        pass


class HumanPlayer(Player):

    def make_move(self, board:Board) -> tuple[int,int]:
        row = int(input(f"{self.name} {self.symbol.value}, enter row:"))
        col = int(input(f"{self.name} {self.symbol.value}, enter col:"))
        return row, col



class BotPlayer(Player):

    def make_move(self, board: Board):
            empty_list = [(r,c) for r in range(board.size) for c in range(board.size) if board.grid[r][c] is None]
            return random.choice(empty_list)


class Game:

    

board = Board()
bot = BotPlayer("Bot", Symbol.O)
bot.make_move(board)

print(board.display())
print(bot.make_move(board))