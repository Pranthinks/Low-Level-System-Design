from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def display(self, temp):
        pass