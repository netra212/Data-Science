
"""
#. Write an OOPS classes to handle the following scenarios:
1. A user can create and view 2D coordinates. 
2. A user can find out the distance between 2 coordinates. 
3. A user can find the distances of a coordinates from origin. 
4. A user can check if a point lies on a given line. 
5. A user can find the distance between a given 2D point and a given line. 
"""

class Point:

    def __init__(self,x,y):
        self.x_coordinate = x
        self.y_coordinate = y

    def __str__(self):
        return '<{},{}>'.format(self.x_coordinate, self.y_coordinate)

    def euclidean_distance(self,other):
        # self(first point) contains x1, y1. 
        # other(other point) contains x2, y2
        return ((self.x_coordinate - other.x_coordinate)**2+(self.y_coordinate - other.y_coordinate)**2) **0.5
    
    # A user can find the distance from the origin.
    def distance_origin(self):
        # return self.euclidean_distance(Point(0,0))
        return (self.x_coordinate**2 + self.y_coordinate**2)**0.5
    
point1 = Point(0,0)
point2 = Point(1,1)

# <x,y>
print(point1.euclidean_distance(point2))

# A user can check if a point given point lies on the line or not.
# creating a line class. 
# since the equation of the line is Ax + By + C.
# so, we need to pass the A,B, and C as paramter to the constructor. 
class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B 
        self.C = C

    # Displaying how our line object can be seen.
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    def point_on_line(line, point):
        if line.A * point.x_coordinate + line.B*point.y_coordinate + line.C == 0:
            return "Point lies on the line."
        else:
            return "Does not lie on the line."
    
    def shortest_distance(line,point):
        return abs(line.A*point.x_coordinate+line.B*point.y_coordinate+line.C)/(line.A**2+line.B**2) 
    
Line1 = Line(3,4,5)
p1 = Point(1,4)
print(Line1)
print(p1)

print(Line1.point_on_line(p1))
Line1.shortest_distance(p1)




