from card import Card

class Credit_card(Card):
    def __init__(self, name, number):
        super().__init__(name, number)
    
    def pay(self):
        print(f"Paying with Credit Card {self.get_name()} ({self.get_number()})")
    
