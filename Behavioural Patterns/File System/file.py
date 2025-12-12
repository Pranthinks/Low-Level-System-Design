from abc import abstractmethod, ABC

class File(ABC):
    @abstractmethod
    def read(self):
        print('This is from file interface to read')
    
    
        