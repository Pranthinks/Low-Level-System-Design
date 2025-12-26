from abc import ABC, abstractmethod

class PlayerInterface(ABC):
    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def make_move(self, board) -> list:
        """Return position [row, col] where the player wants to move."""
        pass
