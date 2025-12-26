from player_interface import PlayerInterface

class HumanPlayer(PlayerInterface):
    def __init__(self, symbol: str):
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.symbol

    def make_move(self, board) -> list:
        # Simple CLI input strategy
        row = int(input(f"Player {self.symbol}, enter row (0-2): "))
        col = int(input(f"Player {self.symbol}, enter col (0-2): "))
        return [row, col]
