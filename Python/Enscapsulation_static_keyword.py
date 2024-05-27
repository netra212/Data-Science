# Enscapsulation and static keyword.

class Person:

    def __init__(self,name_input, country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'Nepal':
            print("Namaste -> ", self.name)
        else:
            print("Hello ", self.name)

# How to access attributes.
p = Person("Netra", "Nepal")
print(p.name)
p.greet()

# Attribute creation from outside of the class. 
p.gender = 'male'
print(p.gender)

# Reference variable: # Object without a reference. 
# -> Reference variables holds the Object. 
# -> We can create objects without reference variables as well. 
# -> An object can have multiple reference variables. 
# -> Assigning a new reference variable to an existing object does not create a new object. 

class Person:

    def __init__(self):
        self.name = "Netra"
        self.gender = 'male'

p = Person() 
q = p
# p <- reference variable. 
# Reference variable holds the object.

# Multiple Reference.
print(id(p))
print(id(q))

# change attribute value with the help of 2nd Object. 
print(p.name)
print(q.name)
q.name = "yagya"
print(q.name)
print(p.name)

# Pass by reference. 
class Person:

    def __init__(self,name, gender):
        self.name = name 
        self.gender = gender 

# outside the class -> hence it is function. 
# Passing a class ko Object to the function. 
# since we are passing the object as input, but we are actually passed the reference of the object here as person so that the address of the person and p is same because technically both of them are same. 
def greet(person):
    print(id(person))
    print("Hii my name is ", person.name, " I am a ", person.gender)
    person.name = "Radhika kc"
    print(person.name)

p = Person("Netra kc", 'male')
print(id(p))
greet(p)
print(p.name)
# x = greet(p)
# print(x.name)
# print(x.gender)

# Note:- Objects in the python are mutable for the user-defined classes Just like lists/sets/dictionary.


"""
#. Enscapsulation.
"""

# Instance var -> Python tutor.
# Value of the instance variables depend on the Objects. 
# For Object, value of the instance variable are differents.
class Person: 

    def __init__(self, name_input, country_input):
        self.name = name_input
        self.country = country_input

p1 = Person("Netra", "Nepal")
p2 = Person("Steve", "Australia")

print(p1.name)

# ATM Machine:
class ATM:

    # constructor : Function inside the class. 
    # constructor(special function) -> superpower -> 
    def __init__(self):

        print(id(self)) # <-- Print the id of the address. 
        # self is object. 

        self.pin = ''
        self.__balance = 0
        # _ATM__balance = 'heheheh'
        # calling the menu() function
        self.__menu()

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Brother you will be Punish if you passed an incorrect data type value here...")

    def __menu(self):
        user_input = input("""
        Hi How can i help you ?
        1. Press 1 to create pin. 
        2. Press 2 to change pin. 
        3. Press 3 to check balance. 
        4. Press 4 to withrdrawl balance. 
        5. Anything else to exit. 
                           """)
        
        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw_balance()
        else:
            # exit the program. 
            exit()
    
    def create_pin(self):
        user_pin = input("Enter a pin.")
        self.pin = user_pin

        user_balance = int(input("Enter a balance."))
        self.__balance = user_balance

        print("Pin create succesfully.")
        self.__menu()

    def change_pin(self):
        old_pin = input("Enter your old Pin")
        if old_pin == self.pin:
            new_pin = input("Enter a new pin")
            self.pin = new_pin
            print("Pin changed succesfully.")
            self.__menu()
        else:
            print("Not allowed to change the pin. ")
            self.__menu()

    def check_balance(self):
        check_pin = input("Enter your pin.")
        if self.pin == check_pin:
            print("your balance is : ", self.__balance)
        else:
            print("Pin Incorrect can't check balance.")

    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if self.pin == user_pin:
            amount_to_be_withdrawl = int(input("Enter balance to withdraw"))
            if amount_to_be_withdrawl <= self.__balance:
                self.__balance = self.__balance - amount_to_be_withdrawl
                print("Withdrawl successfull.")
                print("Remaining balance: ", self.__balance)
            else:
                print("Not sufficient balance.")
        else:
            print("Incorrect pin, balance can't be withdrawl.")
        self.__menu()

# atm = ATM()
# # atm.__balance = 'hehehe'
# # atm._ATM__balance = 'hello world brother'
# atm.set_balance(1000)
# atm.get_balance(1000)



"""
#. Collection of Objects:
"""
class Person:

    def __init__(self,name, gender):
        self.name = name 
        self.gender = gender 

p1 = Person("netra", "male")
p2 = Person("radhika", "female")
p3 = Person("yagya", "male")

L = [p1,p2,p3]
for i in L:
    print(i)

for i in L:
    print(i.name, i.gender)


# dict of Objects:
dct = {'p1':p1,'p2':p2,'p3':p3}
for i in dct:
    print(dct[i].gender)


"""
#. static variable (Vs Instance variable)
"""

# ATM Machine:
class ATM:
    """
    Instance variables defined here...
    """
    __counter = 1

    # constructor : Function inside the class. 
    # constructor(special function) -> superpower -> 
    def __init__(self):

        print(id(self)) # <-- Print the id of the address. 
        # self is object. 

        self.pin = ''
        self.__balance = 0
        self.cid = ATM.__counter # self -> current object. for static variable, class ko name use garcham. 
        # If variable ko agadii self lageko cha vane chaii, tyo instance variable.
        # If variable ko agadii Class ko name lageko cha vane chaii tyo static variable.
        ATM.__counter = ATM.__counter + 1
        # _ATM__balance = 'heheheh'
        # calling the menu() function
        self.__menu()

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Brother you will be Punish if you passed an incorrect data type value here...")

    # utility function: function which does not needs an object to access. 
    @staticmethod
    def get_counter():
        return ATM.__counter

    def __menu(self):
        user_input = input("""
        Hi How can i help you ?
        1. Press 1 to create pin. 
        2. Press 2 to change pin. 
        3. Press 3 to check balance. 
        4. Press 4 to withrdrawl balance. 
        5. Anything else to exit. 
                           """)
        
        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw_balance()
        else:
            # exit the program. 
            exit()
    
    def create_pin(self):
        user_pin = input("Enter a pin.")
        self.pin = user_pin

        user_balance = int(input("Enter a balance."))
        self.__balance = user_balance

        print("Pin create succesfully.")
        self.__menu()

    def change_pin(self):
        old_pin = input("Enter your old Pin")
        if old_pin == self.pin:
            new_pin = input("Enter a new pin")
            self.pin = new_pin
            print("Pin changed succesfully.")
            self.__menu()
        else:
            print("Not allowed to change the pin. ")
            self.__menu()

    def check_balance(self):
        check_pin = input("Enter your pin.")
        if self.pin == check_pin:
            print("your balance is : ", self.__balance)
        else:
            print("Pin Incorrect can't check balance.")

    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if self.pin == user_pin:
            amount_to_be_withdrawl = int(input("Enter balance to withdraw"))
            if amount_to_be_withdrawl <= self.__balance:
                self.__balance = self.__balance - amount_to_be_withdrawl
                print("Withdrawl successfull.")
                print("Remaining balance: ", self.__balance)
            else:
                print("Not sufficient balance.")
        else:
            print("Incorrect pin, balance can't be withdrawl.")
        self.__menu()

c1 = ATM()
c2 = ATM()
c3 = ATM()
print(c1.cid)

# Instance variable is a object variable. value of instance variable is different for all the object. 
# static variable is a class variable. value of static variable is same for all the object. 
# eg: name of the customer is instance variable, balance of the customer is also instance variable, swift code for the bank is static variable, cgpa is instance variable, name of the university is static variable. 
# 




