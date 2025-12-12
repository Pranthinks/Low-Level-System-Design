from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def color(self):
        pass