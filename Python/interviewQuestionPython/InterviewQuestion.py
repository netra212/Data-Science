# Multi-threading.
# Descriptors. 

"""
#. What is a Module ?
-> Any file with an extension of .py is called a module in python. 
-> whenever we execute a program it's module name is __main__ and this is stored in __name__ variable.
"""
def display():
    print("Hello..")

display()
print(__name__)

def hi():
    print('Hi...')

hi()
print(__name__)

def square(num):
    print(num**2)

for i in range(1,11):
    square(i)

# Question1. What do you mean by __name__ == '__main__'

"""
Importing a Module
-> But what is the need to import a module ?
-> How to import a module.
"""
print("\n")
import test  # importing the test module.
test.hello('khatri')

# Import multiple module -> user defined + builtin.

print("\nImport multiple module -> user defined + builtin.")
import math
import test 
print(test.hello('Bahadur khatri'))
print(math.floor(4.3))
print("\n")


"""
#. Variations of Import statements.
"""
import math, random, test

"""
# importing specific names from module.
"""
from math import factorial, floor
from test import hello

print(factorial(5))


"""
#. Renaming module. 
"""
import math as m 
m.factorial(5)

from math import factorial as fact
"""
#. Order of Execution of a module.
"""
import sys
for p in sys.path:
    print(p)


"""
#. What are Packages in Python...?
-> directory containing similar sub packages and modules. 
-> The __init__.py file may be empty or contain some initialization code related to the package. 
"""


"""
#. PyPl -> Python Package Index. 
pip --> Python Manager Utility.
"""





