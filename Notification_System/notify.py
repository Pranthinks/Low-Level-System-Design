from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def notify(self):
        print('This is NOtification from Interface')
