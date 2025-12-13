from abc import ABC, abstractmethod

class UIfactory(ABC):
    
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_scrollbar(self):
        pass

