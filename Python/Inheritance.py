# Inheritance and Polymorphism.

# Aggregation: has a relationships. 
# one class owns the other class. 
# If the one class owns the other class, then this type of relationships is called aggregation. 

class Customer:

    def __init__(self,name, gender, address):
        self.name = name 
        self.gender = gender
        self.address = address 

    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name 
        self.address.edit_address(new_city, new_pin, new_state)

class Address:

    def __init__(self, city, pin, state):
        self.__city = city # we cannot access the private variable when we are performing the aggregation. so, in order to print the city, we have to use the getter. 
        self.pin = pin 
        self.state = state 

    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin 
        self.state = new_state

address = Address("Digiya", 44600, "Banke")
customer = Customer("Netra", "Male", address)
# since in the above customer object, we are passing the object of the Address class which shows the Aggregation relationships.
print(customer.print_address())
print(customer.edit_profile("Netra123", "London", 1111,"Greenwich"))


"""
#. Inheritance: code reusability
#1. What is Inheritance ?
#2. Example ?
#3. What gets inherited ?
"""

class User:

    def __init__(self, username):
        self.name = username

    def login():
        pass

    def register():
        pass 

# child class.
class Instructor(User):

    def __init__(self):
        pass

    # create course
    # reply

# child class. 
class Students(User):

    def __init__(self, rollno):
        self.rollno = rollno

    def enroll():
        pass
    # enroll
    # reviews.

"""
#. What can be Inherited ?
1. Constructor. 
2. Non Private Attributes. 
3. Non Private Methods. 
"""

# Constructor Example:
# If the child class does not have their own constructor then parent constructor will be call. 
# child object cannot access the private member of the class. 

class Phone:

    def __init__(self,price, brand, camera):
        print("Inside phone constructor")
        self.__price = price  # object of the child class cannot access the private member of the class. 
        self.brand = brand 
        self.camera = camera 

    def buy(self):
        print("Buying a phone")

    # But using the getter, we can access the private member of the parent class. 
    def show(self):
        print(self.__price)

class SmartPhone(Phone):
    
    def __init__(self, os, ram):
        self.os = os 
        self.ram = ram 
        print("Inside SmartPhone constructor.")

s = SmartPhone("Android", 2)
print(s)


# child object cannot access the private member of the class. 
# But using the getter, we can access the private member of the parent class.
class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def show(self):
        print("This is in child class")
        
son=Child(100)
print(son.get_num())
son.show()


# 
class Parent:

    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):

    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val
        
son=Child(100,10)
print("Parent: Num:",son.get_num())
print("Child: Val:",son.get_val())


# 
class A:
    def __init__(self):
        self.var1=100

    def display1(self,var1):
        print("class A :", self.var1)
class B(A):
  
    def display2(self,var1):
        print("class B :", self.var1)

obj=B()
obj.display1(200)


# 
# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)

s.buy()

# super keyword. : always used inside the child class. 
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy() # calling parent buy() method.

s=SmartPhone(20000, "Apple", 13)

s.buy()

# using super outside the class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent ka buy method
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()

# can super access parent ka data?
# using super outside the class
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print ("Buying a smartphone")
        # syntax to call parent ka buy method
        print(super().brand)

s=SmartPhone(20000, "Apple", 13)

s.buy()

# super cannot access the variable. 
# super is only used to access the method of the class. 
# super -> constuctor
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print('Inside smartphone constructor')
        super().__init__(price, brand, camera) # calling the parent class constructor. 
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)

print(s.os)
print(s.brand)


"""
Inheritance in summary
- A class can inherit from another class.
- Inheritance improves code reuse.
- Constructor, attributes, methods get inherited to the child class.
- The parent has no access to the child class.
- Private properties of parent are not accessible directly in child class.
- Child class can override the attributes or methods. This is called method overriding.
- super() is an inbuilt function which is used to invoke the parent class methods and constructor.
"""

class Parent:

    def __init__(self,num):
      self.__num=num

    def get_num(self):
      return self.__num

class Child(Parent):
  
    def __init__(self,num,val):
      super().__init__(num)
      self.__val=val

    def get_val(self):
      return self.__val
      
son=Child(100,200)
print(son.get_num())
print(son.get_val())


# 
class Parent:
    def __init__(self):
        self.num=100

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.var=200
        
    def show(self): # self is a son
        print(self.num)
        print(self.var)

son=Child()
son.show()


# 
class Parent:
    def __init__(self):
        self.__num=100

    def show(self):
        print("Parent:",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print("Child:",self.__var)

obj=Child()
obj.show()

# 
class Parent:
    def __init__(self):
        self.__num=100

    def show(self):
        print("Parent:",self.__num)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print("Child:",self.__var)

obj=Child()
obj.show()

"""
# Types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Multiple Inheritance(Diamond Problem)
# Hybrid Inheritance
"""

# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()

# multilevel
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()


# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()

# Multiple
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()

# 
# the diamond problem
# https://stackoverflow.com/questions/56361048/what-is-the-diamond-problem-in-python-and-why-its-not-appear-in-python2
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class Product:
    def buy(self):
        print ("Product buy method")

# Method resolution order
class SmartPhone(Phone,Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()

# 
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
  
    def m2(self):
        return 20
obj1=A()
obj2=B()
obj3=C()
print(obj1.m1() + obj3.m1()+ obj3.m2())


# 
class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val=super().m1()+30
        return val

class C(B):
  
    def m1(self):
        val=self.m1()+20
        return val
obj=C()
print(obj.m1())

# 
"""
Polymorphism
Method Overriding
Method Overloading
Operator Overloading
"""
class Shape:

  def area(self,a,b=0):
    if b == 0:
      return 3.14*a*a
    else:
      return a*b

s = Shape()

print(s.area(2))
print(s.area(3,4))

"""
Abstraction:
"""
from abc import ABC,abstractmethod
class BankApp(ABC):

  def database(self):
    print('connected to database')

  @abstractmethod
  def security(self):
    pass

  @abstractmethod
  def display(self):
    pass

# 
class MobileApp(BankApp):

  def mobile_login(self):
    print('login into mobile')

  def security(self):
    print('mobile security')

  def display(self):
    print('display')

mob = MobileApp()
mob.security()
obj = BankApp()