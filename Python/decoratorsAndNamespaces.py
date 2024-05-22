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
