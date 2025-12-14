from interface import Interface
from Game_Board import GameBoard

obj = GameBoard()

obj.add_piece('Red', 4)
obj.add_piece('Green', 9)
obj.undo()
obj.undo()