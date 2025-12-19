from abc import ABC, abstractmethod

class Image(ABC):
    
    @abstractmethod
    def display_image(self):
        pass