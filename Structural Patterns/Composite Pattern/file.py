from abc import ABC, abstractmethod

class FileSystemItem(ABC):

    @abstractmethod
    def Show_details(self):
        pass
