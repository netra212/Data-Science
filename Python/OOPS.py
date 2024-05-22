# Type of classes in Python : built-in classes and user defined classes. 

# ATM Machine:
class ATM:

    # constructor : Function inside the class. 
    def __init__(self):

        print(id(self)) # <-- Print the id of the address. 
        # self is object. 

        self.pin = ''
        self.balance = 0
        # calling the menu() function
        self.menu()

    def menu(self):
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
        self.balance = user_balance

        print("Pin create succesfully.")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old Pin")
        if old_pin == self.pin:
            new_pin = input("Enter a new pin")
            self.pin = new_pin
            print("Pin changed succesfully.")
            self.menu()
        else:
            print("Not allowed to change the pin. ")
            self.menu()

    def check_balance(self):
        check_pin = input("Enter your pin.")
        if self.pin == check_pin:
            print("your balance is : ", self.balance)
        else:
            print("Pin Incorrect can't check balance.")

    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if self.pin == user_pin:
            amount_to_be_withdrawl = int(input("Enter balance to withdraw"))
            if amount_to_be_withdrawl <= self.balance:
                self.balance = self.balance - amount_to_be_withdrawl
                print("Withdrawl successfull.")
                print("Remaining balance: ", self.balance)
            else:
                print("Not sufficient balance.")
        else:
            print("Incorrect pin, balance can't be withdrawl.")
        self.menu()

atm = ATM()

# Different between Methods Vs Function:
# If the function is created inside the class then this is called method. 
# If the function is created outside of the class then this is called function. 


# Magic Method:
# __name__
# __init__ : constructor which is magic method. 


"""
# Constructor:
Q. What are the true benefits of the constructor:
-> when we do not want to give control to the user, 
# -> constructor is used to write an configuration related code. 
# internet connect sanga connect hune code.
# user laii nasoderww garne kam haru naii, constructor ko under ma rakcham. 
# Example:-
# God -> Programmer, Earth -> Class, Object -> Human being.

Note:- We cannot change the name of the constructor. 
"""

"""
Golden Rules of OOPS:
class: Rules made here....!
       Only the object of the class can have right to access the member of the class. 
      

Object:
self keywords:
# self is current object. 
# self helps to call the one method to another method inside the class. 
# For the intra class communication, we need to use the self as current object. 
"""

class Fraction:

    # parameterized constructor : required inputs. 
    def __init__(self,x,y):
        self.num = x
        self.deno = y

    def __str__(self):
        return '{}/{}'.format(self.num, self.deno)

    def __add__(self,other):
        new_num = self.num*other.deno + other.num*self.deno
        new_deno = self.deno*other.deno

        return '{}/{}'.format(new_num, new_deno)

    def __sub__(self, other):
        new_num = self.num*other.deno - other.num*self.deno
        new_deno = self.deno*other.deno

        return '{}/{}'.format(new_num, new_deno)

    def __mul__(self, other):
        new_num = self.num*other.num
        new_deno = self.deno*other.deno

        return '{}/{}'.format(new_num, new_deno)
    
    def __truediv__(self, other):
        new_num = self.num*other.deno
        new_deno = self.deno*other.num

        return '{}/{}'.format(new_num, new_deno)

fr1 = Fraction(4,5)
print(fr1)





