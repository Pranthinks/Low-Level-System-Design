from abc import ABC, abstractmethod

class Interface_Vehicle(ABC):
    
    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def space_needed(self):
        pass