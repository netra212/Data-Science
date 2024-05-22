import module1

"""
importing a module1 is like whole code shift here... like this...
def square(num):
    print(num**2)

for i in range(1,11):
    square(i)
"""

print(__name__)
print(module1.__name__) # print the name of the python. 
user_input = int(input("Enter a number: "))
module1.square(user_input)
module1.main()






