from abc import ABC, abstractmethod

class Interface_Payments(ABC):

    @abstractmethod
    def pay(self, vehicle_name: str):
        pass
    