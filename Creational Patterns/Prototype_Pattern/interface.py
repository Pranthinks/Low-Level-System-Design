from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def add_piece(self, coins: str, pos: int):
        pass

    @abstractmethod
    def undo(self):
        pass

    