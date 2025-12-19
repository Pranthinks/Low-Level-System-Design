from service import Email_Service
from adapter import Adapter_Email
from Third_party import Custom_Email


obj = Email_Service()
obj.Sending()

obj1 = Custom_Email()

ada = Adapter_Email(obj1)
ada.Sending()