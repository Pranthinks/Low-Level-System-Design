from abc import ABC, abstractmethod


class Scroll(ABC):

    @abstractmethod
    def render(self):
        pass