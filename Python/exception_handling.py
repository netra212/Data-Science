# stages where Errors may happens in the Program. 
# During Compilation -> Syntax Error:  something in the program in not written according to the program grammar.

# During Exceution -> Exceptions. 

"""
Types of Error
1. Syntax Error:
2. Index Error:
3. ModuleNotFoundError:
4. KeyError: Especially in the dictionary. 
5. TypeError:
6. ValueError: function argument in an in appropriate type. 
7. NameError:
8. AttributeError:
"""

# Exceptions: raised by python runtime. 
# Example: Memory Overflow, Divide by 0 -> Logical Error, Database error. 

try:
    with open('sample1235.txt','r') as f:
        print(f.read())
except:
    print("sorry, file not found.")

# catching specific exception.
try: 
    f = open('sample1234.txt','r')
    print(f.read())
    # print(m)
    print(5/0)
except FileNotFoundError:
    print("file not found")
except NameError:
    print("Variable not defined.")
except ZeroDivisionError:
    print("can't divide by zero.")
except Exception as e:
    print(e.with_traceback)

# else
try:
    f = open('sample1.txt','r')
except FileNotFoundError:
    print(" File not found brother...")
except Exception:
    print("There is some issues.")
else: # else if tyo time ma use garcham, if we are so sure than there is no wrong in the try block.
    print(f.read())

# finally. 
try:
    f = open('sample1.txt','r')
except FileNotFoundError:
    print(" File not found brother...")
except Exception:
    print("There is some issues.")
else: # else if tyo time ma use garcham, if we are so sure than there is no wrong in the try block.
    print(f.read())
finally:
    print("This must print.")

# raise Exception

# raise NameError("Just trying ....... !")
# Java 
# try -> try
# except -> catch.
# raise -> throw.
class MyException(Exception):
    def __init__(self,message):
        print(message)

class Bank:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self,amount):
        if amount < 0:
            raise MyException("amount cannot be -ve")
        if self.balance < amount:
            raise MyException("paisa chaina tww sanga...")
        self.balance = self.balance - amount

obj = Bank(10000)
try:
    obj.withdraw(5000)
except MyException as e:
    print(e)
else:
    print(obj.balance)

# why do we need the custom class for the exception ?
# Because if we want to fully control of the applications. 
class SecurityError(Exception):
    def __init__(self,message):
        print(message)
    
    def logout(self):
        print('logout')

class Google:
    def __init__(self,name, email, password, device):
        self.name = name 
        self.email = email 
        self.password = password 
        self.device = device
    
    def login(self, email, password, device):
        if device != self.device:
            raise SecurityError("Bhaii tero tww wattt lagyo...")
        if email == self.email and password == self.password:
            print("welcome")

google = Google('Netra','netra200021kcbdr@gmail.com', 'netra123', 'android')

try:
    google.login('netra200021kcbdr@gmail.com', 'netra123','macbook')
except SecurityError as e:
    e.logout()
else:
    print(google.name)
finally:
    print("Database connection closed.")


# Application ko Logic ko basis ma Error throw garnu cha vane tyo condition ma custom exception class use garincha....



