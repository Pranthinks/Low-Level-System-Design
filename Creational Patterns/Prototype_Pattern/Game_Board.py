from game_piece import GamePiece
from interface import Interface
import copy

class GameBoard(Interface):
    def __init__(self):
        self.obj = GamePiece()
        self.history = []      # Stack for undo
        

    def add_piece(self, coins: str, pos: int):
        # Save current state for undo
        self.history.append(self.obj.clone())
        self.obj.coins = coins
        self.obj.pos = pos
        print(f"Added piece: {self.obj.coins} at position {self.obj.pos}")

    def undo(self):
        if not self.history:
            print("Nothing to undo")
            return
        self.obj = self.history.pop()
        print(f"Undo: Piece is now {self.obj.coins} at position {self.obj.pos}")

    