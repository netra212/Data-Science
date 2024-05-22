"""
# Class Relationships:
1. Aggregation. 
2. Inheritance. 
"""

"""
# 1. Aggregation:
# => Has-A relationships. 
# one class owns the other class. 
# one class is owner and other class is the property. 
Example:-
class 1: Customer. 
class 2: Address.
Customer has a Address. 
Customers owns a Address. 

Another example:-
class 1: Restaurant.
class 2: Menu.
Restaurant has A Menu. 
"""

class Customer:

    def __init__(self,name,gender, address):
        self.name = name
        self.gender = gender
        self.address = address # address is the complex entity because there are so many thing on the address like post code, name of the address, road name and so on. 

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name 
        self.address.edit_address(new_city, new_pin, new_state)

class Address:

    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin 
        self.state = state 
    
    def get_city(self):
        return self.__city
    
    def edit_address(self, new_city, new_pin, new_state):
        self.new_city = new_city
        self.new_pin = new_pin 
        self.new_state = new_state
        
address = Address("Banke", 123124, "Nepal")
customer = Customer("Netra kc", "Male", address)

customer.print_address()

# Q1. Does above Customer class can fetch the city of the Address class. ?
# No, we cannot access the private attribute while we are performing the aggrations. 
# so, how can we print the value of the city ?
# ans: use the getter method.

customer.edit_profile('Yagya', 'mumbai', 1231,'Kathmandu')
customer.print_address()

