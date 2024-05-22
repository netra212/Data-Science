# Generators in Python.
# Python generators are a simple way of creating iterators.
import sys

def gen_demo():
    # In generator there is no return statement but there is yield statement. 
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)

# Difference between 'yield' Vs 'return'.
def square(num):
    for i in range(1, num+1):
        yield i**2

gen = square(10)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

# Range function using Generator.
def mero_range(start, end):
    for i in range(start, end):
        yield i
for i in mero_range(15,26):
    print(i, end=" ")


# Generator Expression
L = [i**2 for i in range(1,101)] # List expression. 

gen = (i**2 for i in range(1,101))
for i in gen:
    print(i, end=" ")

# Practical Example:
# import os
# import cv2 
# def image_data_reader(folder_path):
#     for file in os.listdir(folder_path):
#         f_array = cv2.imread(os.path.join(folder_path,file))
#         yield f_array
# gen = image_data_reader('folder_path')
# next(gen)
# next(gen)


# Representing infinite streams
def all_even():
    n = 0
    while True:
        yield n
        n+=2
even_num_gen = all_even()
next(even_num_gen)
next(even_num_gen)


# Chaining Generators
def fibonacci_numbers(nums):
    x,y = 0,1
    for _ in range(nums):
        x,y =y, x+y
        yield x
def square(nums):
    for num in nums:
       yield num**2

print(sum(square(fibonacci_numbers(10))))
 



