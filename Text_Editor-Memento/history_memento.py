from collections import deque
from abc import ABC, abstractmethod

class History(ABC):
    def __init__(self):
        self.que = deque()
    
    def save(self, text):
        self.que.append(text)
    
    
    def undo(self):
        if self.que:
            self.que.pop()
        return self.que[-1] if self.que else ""
    
    def cur_print(self):
        return self.que[-1] if self.que else ""
    
    @abstractmethod
    def write(self, text):
        pass
