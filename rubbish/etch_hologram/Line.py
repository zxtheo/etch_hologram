
"""container for all points in a defined line"""

import math
import typing
import numpy as np
from etch_hologram.Point import Point


class Line:
    """container for all points in a defined line
    """    
    def __init__(self, start: Point, end: Point, density: int):
        """
         init function of Line class. Initializes the line and its points. This function is called by the constructor
         
         @param start - start point of the line
         @param end - end point of the line e. g.
         @param the distance between points on a line
        """
        self.start = start
        self.end = end
        self.density = density
        self.points = []
        self.create_line()

    def create_line(self):
        """function that populates the line container with the points across the line
        """
        #define the direction of the vector
        direction = Point.sub(Point(0,0,0),self.end,self.start)

        # Define the desired length of the vector
        length = self.density

        # Normalize the direction vector
        normalized_direction = Point.divide(Point(0,0,0), direction, np.linalg.norm([direction.x, direction.y, direction.z]))

        # Create the new vector with the specified length
        line_vector = Point.times(Point(0,0,0),normalized_direction,length)
        
        self.points.append(self.start) ##add start point
        
        #cycle line postions accordging to the line_vector
        curr_point = self.start

        while (self._within_range(curr_point)):
            curr_point = Point.add(Point(0,0,0),line_vector, curr_point) #move point along line
            self.points.append(curr_point) #add point to list
            
        self.points.append(self.end) #add end point
    def _within_range(self, current_point: Point) -> bool:
        """
         Checks if the current point is not further than the end point of the line and if it is within the range
         
         @param current_point - point to test if it is within the range
         
         @return True if currnt point within line range
        """    
        dx = current_point.x - self.end.x
        dy = current_point.y - self.end.y
        dz = current_point.z - self.end.z

        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        
        if distance >= self.density:
            return True
        else:
            return False

    def __str__(self):
        return f"Line from {self.start} to {self.end} with {len(self.points)} points"