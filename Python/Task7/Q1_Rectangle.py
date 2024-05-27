"""
1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

2. Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.

3. Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
"""
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breath = breadth

    def perimeter(self):
        perimeter_rectangle = 2 * (self.length + self.breath)
        return perimeter_rectangle

    def area(self):
        area_rectangle = self.length * self.length
        return area_rectangle

    def display(self):
        print("Length of the rectangle is : ", self.length)
        print("Breadth of the rectangle is : ", self.breath)
        print("The perimeter of the rectangle is : ", self.perimeter())
        print("The area of rectangle is :", self.area())

my_rectangle = Rectangle(3,4)
my_rectangle.display()


