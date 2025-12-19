from decorator import Decorator

class Cheese(Decorator):

    def get_cost(self):
        return super().get_cost() + 20

    def get_description(self):
        return super().get_description() + ", Cheese"


class Olives(Decorator):

    def get_cost(self):
        return super().get_cost() + 15

    def get_description(self):
        return super().get_description() + ", Olives"
