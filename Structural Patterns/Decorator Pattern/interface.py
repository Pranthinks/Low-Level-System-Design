from abc import ABC, abstractmethod


class pizza(ABC):

    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass
