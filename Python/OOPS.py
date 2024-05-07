# Type of classes in Python : built-in classes and user defined classes. 

# ATM Machine:
class ATM:

    # constructor : Function inside the class. 
    def __init__(self):
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
# 
# 

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

"""
