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
            self.grid[row][col] = symbol
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

    def __init__(self, player1: Player, player2: Player, size: int = 3):
        self.board = Board(size)
        self.player = [player1, player2]
        self.current_player_index = 0

    def start(self):
        print("🚀 Game Started!")

        while True:
            self.board.display()
            current_player =  self.player[self.current_player_index]

            try:
                row, col = current_player.make_move(self.board)
                if not self.board.place_peice(row, col, current_player.symbol):
                    print("Invalid move try again")
            except (ValueError, IndexError):
                print ('Invalid input format try again')
                continue

    def check_game_over(self, row:int, col, int, symbol:Symbol) -> bool:

        size = self.board.size
        grid = self.board.grid 

        row_win = all(grid[row][i] == symbol for i in range(size))
        col_win = all(grid[i][col] == symbol for i in range(size))
        dig_win = all(grid[i][i] == symbol for i in range(size))
        anti_dig_win = all(grid[i][size - 1 - i] for i  in range(size))

        return row_win or col_win or dig_win or anti_dig_win



board = Board()
bot = BotPlayer("Bot", Symbol.O)
bot.make_move(board)

print(board.display())
print(bot.make_move(board))