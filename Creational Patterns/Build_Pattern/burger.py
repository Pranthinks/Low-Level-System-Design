
class Burger:

    def __init__(self):
        self.bun = None
        self.cheese = None
        self.chilli = None
    
    def __str__(self):
        return f"Burger(bun={self.bun}, patty={self.cheese}, chilli={self.chilli})"
