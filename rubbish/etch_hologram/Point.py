
"""contaner of all information and methods regarding an individual Point"""

import math
import typing


class Point:
    """Container of all information and methods regarding an individual Point"""
    
    def __init__(self, x: typing.Union[int, float], y: typing.Union[int, float], z: typing.Union[int, float]):

        """
        Initializes a Point object with the given x, y, and z coordinates.
        
        @param x - x coordinate of the point in world coordinates.
        @param y - y coordinate of the point in world coordinates.
        @param z - z coordinate of the point in world coordinates.
        """
        self.x = x
        self.y = y 
        self.z = z
        try:
            self.start_x = self.x-1
            self.end_x = self.x + 1
        except ZeroDivisionError:
            # handle division by zero error here
            pass
        self.curr_x: typing.Union[int, float]
        self.curr_y: typing.Union[int, float]
        self.visible = True

        self.update(0)


    def update(self, viewing_angle: typing.Union[float, int]) -> 'Point':
        
        """
        Updates the current position of the point using the viewers angle to create illusion of depth.
        
        @param viewing_angle - the angle of the viwer tied to the slider in view mode
        
        @return self The instance of the class for method chaining.
        """
        print("func_enter: Point.update()")
        print("func: Point.update : viewing_angle = " + str(viewing_angle))
        x = self.x
        y = self.y 
        radius = self.z 
        self.curr_x  = x + radius * math.cos(viewing_angle)
        self.curr_y = y + radius * math.sin(viewing_angle) + radius

        return self
    
    
    def sub(self, pointa, pointb):

        x = pointa.x - pointb.x
        y = pointa.y - pointb.y
        z = pointa.z - pointb.z

        return Point(x,y,z)
    
    def add(self, pointa, pointb):

        x = pointa.x + pointb.x
        y = pointa.y + pointb.y
        z = pointa.z + pointb.z

        return Point(x,y,z)
    
    def divide(self, pointa, divisible):

        x = pointa.x / divisible
        y = pointa.y / divisible
        z = pointa.z / divisible

        return Point(x,y,z)
    
    def times(self, pointa, product):

        x = pointa.x * product
        y = pointa.y * product
        z = pointa.z * product

        return Point(x,y,z)


    
