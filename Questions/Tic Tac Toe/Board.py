from board_interface import BoardInterface
from player_interface import PlayerInterface

class GameBoard(BoardInterface):
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def place_symbol(self, player: PlayerInterface, pos: list) -> bool:
        row, col = pos
        if 0 <= row < 3 and 0 <= col < 3:
            if self.board[row][col] is None:
                self.board[row][col] = player.get_symbol()
                return True
        return False

    def check_winner(self, player: PlayerInterface, pos: list) -> bool:
        val = player.get_symbol()
        row, col = pos

        # Check row and column
        if all(self.board[row][i] == val for i in range(3)) or \
           all(self.board[i][col] == val for i in range(3)):
            return True

        # Check diagonals
        if row == col and all(self.board[i][i] == val for i in range(3)):
            return True

        if row + col == 2 and all(self.board[i][2-i] == val for i in range(3)):
            return True

        return False

    def print_board(self):
        for row in self.board:
            print([cell if cell is not None else "-" for cell in row])
        print()
