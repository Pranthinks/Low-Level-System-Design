from abc import ABC, abstractmethod
from interface import Payments

class Card(Payments):
    def __init__(self, name: str , number: int):
        super().__init__()
        self.__name = name
        self.__number = number
    
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number

    
    