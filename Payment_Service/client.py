from credit_card import Credit_card
from debit_card import Debit_Card
from payment_service import Payment_Service

obj1 = Credit_card('Praneeth', 123)
obj2 = Debit_Card('Rajesh', 856)

main_obj = Payment_Service()
main_obj.add_payment_method('Praneeth', obj1)
main_obj.add_payment_method('Rajesh', obj2)

main_obj.make_payment('Praneeth')
main_obj.make_payment('Rajesh')
