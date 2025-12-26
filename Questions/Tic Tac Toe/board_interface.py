from abc import ABC, abstractmethod
from player_interface import PlayerInterface

class BoardInterface(ABC):
    @abstractmethod
    def place_symbol(self, player: PlayerInterface, pos: list) -> bool:
        """Places symbol; returns True if successful, False otherwise"""
        pass

    @abstractmethod
    def check_winner(self, player: PlayerInterface, pos: list) -> bool:
        pass

    
