from abc import ABC, abstractmethod


class Interface(ABC):
    def open_file(self):
        print("Opening the File!!!")

    def close_file(self):
        print("Closing the File!!!")

    @abstractmethod
    def parse_file(self):
        pass

    # Template method: defines the skeleton of the algorithm
    def process_file(self):
        self.open_file()
        self.parse_file()
        self.close_file()