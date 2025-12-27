from abc import ABC, abstractmethod

class Interface_Products(ABC):

    @abstractmethod
    def SKN(self):
        pass
    @abstractmethod
    def Quantity(self):
        pass
    @abstractmethod
    def price(self):
        pass