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























