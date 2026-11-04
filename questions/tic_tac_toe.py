from enum import Enum
from abc import ABC, abstractmethod


class Symbol(Enum):

    EMPTY = " "
    X = "X"
    O = "O"


class Board:

    def __init__(self, size: int = 3):
        self._size = size
        self.grid = [[None for _ in range(size)]for _ in range(size)]

    def display(self):
        for row in self.grid:
             print("|".join(cell.value if cell else " "for cell in row))
             print("-" * (self._size * 2))


class Player(ABC):

    def __init__(self, name: str):
        self._size = name
        self.symbol = Symbol

    @abstractmethod
    def make_move(self):
        pass


class HumanPlayer(Player):

    def make_move(self):
            pass



class BotPlayer(Player):

    def make_move(self):
            pass

    


board = Board()
print (board.display())