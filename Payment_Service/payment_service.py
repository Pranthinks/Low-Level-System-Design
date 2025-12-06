from interface import Payments
from card import Card


class Payment_Service:
    def __init__(self, dic : dict = None):
        self.dic = dic if dic else {}

    def add_payment_method(self, name, val: Payments):
        if name not in self.dic:
            self.dic[name] = val # store as list
        else:
            self.dic[name].append(val)
    def make_payment(self, name):
        payments = self.dic.get(name, [])
        print(payments)
        payments.pay()