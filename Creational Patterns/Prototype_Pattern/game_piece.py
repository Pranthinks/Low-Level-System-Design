import copy

class GamePiece:
    def __init__(self, coins=None, pos=None):
        self.coins = coins
        self.pos = pos

    # Prototype method to clone the object
    def clone(self):
        return copy.deepcopy(self)
