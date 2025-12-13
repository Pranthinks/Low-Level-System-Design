from abc import ABC, abstractmethod


class Buttons(ABC):

    @abstractmethod
    def render(self):
        pass