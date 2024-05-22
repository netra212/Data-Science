# Namespaces.
# Decorators.
# Generators.
# Iterators.

# Namespaces : space that holds names(identifiers). namespaces are dictionary of identifiers(keys) and their objects(values).
# 4 Types of the namespaces:
# 1. Builtin Namespaces. 
# 2. Global Namespaces. 
# 3. Enclosing Namespaces. 
# 4. Local Namespaces. 

# scope : textual region where the particular variable can be accessible. 

# LEGB Rul: Local Enclosing Global Builtin. 

# Local and Global:
# Global scope.
a = 2 # so global variable.
def temp():
    # local scope. 
    b = 3 # local variable.
    print(b) 
temp()
print(a)

# Again.
a = 2 # so global variable.
def temp():
    # local scope. 
    b = 3 # local variable.
    print(b) 
temp()
print(a)

# Local and global -> local does not have but global has. 

a = 2
def temp():
    # local var
    print(a)
    # If local ma variable chaina vane, python intepreter le global ma gayarww khojna jancha, then if global ma payena vane built in ma khojcha..
temp()
print(a)

# local and global --> editing global. 
a = 2
def temp():
    global a
    a += 1 # we cannot make any changes into the global variables. but we can change only with keyword 'global'.
    print(a)
temp()
print(a)

# local and global -> global created inside local. 

def temp():
    # local var. 
    global a # possible to create a global variable from local. 
    a = 1
    print(a)
temp()
print(a)

# local and global -> function parameter is local 
def temp(z): # function paramter is always a lcoal scope. 
    print(z)
a = 5
temp(5)
print(5)


# Built-in scope. 
import builtins
print(dir(builtins)) # how to see all the builtins. 

# Renaming the built-ins.
L = [1,2,3]

def max():
    print('hello world')
# max(L) raise an error, because according to the LEGB Rule, Python Intepreter first search at the global scope, then check, since the function max() is not taking an any arguments from the users so it will throws an errors. 


# Enclosing scope. 
def outer(): # outer scope.
    a = 3 # Enclosing scope.
    def inner(): # local scope. 
        a = 4
        print(a)
        print('inner function')
    inner() 
    print('outer function')
a = 1
outer()
print('Main Program Ends here.')


# non-local keyword.
def outer(): # outer scope.
    a = 3 # Enclosing scope.
    def inner(): # local scope. 
        nonlocal a # we are telling the python interpreter that we want to change the enclosing's scope variable but this is not a good programing practice. 
        a += 4
        print(a)
        print('inner function')
    inner() 
    print('outer function')
a = 1
outer()
print('Main Program Ends here.')


# summary.

print("************************************")
print("Decorators")

"""
Decorators: a function that receives another function as input and adds some functionality(decoration) to and it and returns it.

-> This can happens only because python function are 1st class citizens. 

There are 2 types of decorators available in Python:
1. Built in decorators like @staticmethod, @classmethod, @abstractmethod and @property etc. 

2. User defined decorators that we programmes can create according to our needs. 

"""
# Python  are 1st class citizens. 
def modify(func, num): # this acts as decorators. 
    return func(num)

def square(num): # this acts as input. 
    return num*2

modify(square,2)

# simple Example:-
# clojure: Inner function can access even the outer function is finished executed.
# Basically, even the parents died, child can still access the property of the parents that is decorators in simple terms.  
def my_decorator(func):
    def wrapper():
        print('*****')
        func()
        print('*****')
    return wrapper

def hello():
    print('hello, i am a hello function...')

def display():
    print("Hello, netra brother...")

a = my_decorator(hello)
print(a())

b = my_decorator(display)
print(b())

# more functions. 
def my_decorator(func):
    def wrapper():
        print('*****')
        func()
        print('*****')
    return wrapper

@my_decorator
def hello():
    print('hello, i am a hello function...')

hello()

# Anything meaningful ?
import time 

# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         print("time taken by : ", func.__name__, time.time()-start, " secs")
#     return wrapper

# @timer
# def hello():
#     print("Hello world...")
#     time.sleep(2)

# @timer  
# def display():
#     print("Displaying something..")
#     time.sleep(4)

# @timer
# def square(num):
#     time.sleep(1)
#     return num*2

# hello()
# # display()
# square(2)

# A big Problem:
# check the data types with the help of the decorators. 
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("Not a valida data type.")
        return inner_wrapper
    return outer_wrapper

@sanity_check(int) 
def square(num):
    print(num**2)

@sanity_check(str)
def greet(name):
    print('Hello: ', name)

square(2)
greet('netra')

# One Last decorators with arguments 

# Iterators: Iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory.

# L = [x for x in range(1,1000)]
# L -> Iterable. 
# range() -> Iterable. 
# for i in L:
#     print(i*2, end='')

# Iterable : iterable is an object, which can iterate over.
# Iterable generates an iterator which passed to iter() method.

L = [1,2,3,4,5]
type(L)

print(type(iter(L)))

# Note:- Points to remember.
# Every Iterator is also an Iterable. 
# Not all Iterables are Iterators. 

# Tricks:
# 1. Every Iterable has an iter function. 
# 2. Every Iterators has both iter function as well as next function. 

a = 2
print(dir(a))

T = (1,2,3)
print(dir(T))

List1 = [1,2,3]
# List1 is not an Iterator.
print(dir(iter(L)))


# Understanding how for loop works. 
print("Understanding how for loop works")
num = [1,2,3]
for i in num:
    print(i, end=' ')
# It fetch the iterator.
iter_num = iter(num)
# step2 --> next
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))



# my own for loop. 
def my_own_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

aList = [1,2,3,4,5,6,7]
my_own_for_loop(aList)

# A confusion point. 
num = [1,2,3]
iter_obj = iter(num)

print(id(iter_obj),'Address of iterator 1')
iter_obj2 = iter(iter_obj)
print(id(iter_obj2),'Address of iterator 2')

# Let's create our own range() function. 

class mero_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return mero_range_iterator(self)

class mero_range_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start+=1
        return current

a = mero_range(1,11)
print(type(a))


print("\n************************************")
