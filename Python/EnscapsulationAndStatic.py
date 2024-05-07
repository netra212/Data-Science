"""
Write an OOPS classes to handle the following scenarios:
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
        # self contains x1, y1. 
        # other contains x2, y2
        return ((self.x_coordinate - other.x_coordinate)**2+(self.y_coordinate - other.y_coordinate)**2) **0.5
    
    def distance_origin(self):
        # return self.euclidean_distance(Point(0,0))
        return (self.x_coordinate**2 + self.y_coordinate**2)**0.5
    
point1 = Point(4,3)
point2 = Point(5,2)

print(point1.euclidean_distance(point2))

# creating a line class. 
class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B 
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)


line1 = Line(3,4,5)
print(line1)