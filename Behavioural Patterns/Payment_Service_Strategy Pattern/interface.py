from abc import ABC, abstractmethod

class Payments(ABC):
    @abstractmethod
    def pay(self):
        print('This is the payment method of interface')
