"""
#. Abstraction:
"""
from abc import ABC, abstractmethod

# In order to be class as abstract, class have to be inherited from the ABC module.
class BankApp(ABC):

    def __init__(self):
        pass

    def database(self):
        print("Connected to Database.")
    
    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print("Login into mobile..")
    
    def security(self):
        print("Mobile security..")
    
    def display(self):
        print("Display..")



    






