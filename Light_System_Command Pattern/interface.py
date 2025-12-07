from abc import ABC, abstractmethod


class Interface(ABC):

    @abstractmethod
    def execute(self):
        pass
    