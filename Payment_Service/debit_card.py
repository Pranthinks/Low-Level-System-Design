from card import Card

class Debit_Card(Card):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
    
    def pay(self):
        print(f"Paying with Debit Card {self.get_name()} ({self.get_number()})")
