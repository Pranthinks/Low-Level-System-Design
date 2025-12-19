from interface import pizza


class Base_pizza(pizza):

    def get_cost(self):
        return 100

    def get_description(self):
        return "Basic Pizza"