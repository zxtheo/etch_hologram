"""container for all points in a defined line"""

import typing
import numpy as np
from etch_hologram.Point import Point


class Line:
    """container for all points in a defined line
    """    
    def __init__(self, start: Point, end: Point, densty: int):
        """init function of Line

        Args:
            pointa (Point): start point of line
            pointb (Point): end point of line
            densty (int): the distance between points on a line
        """
        self.start = np.array([start.x, start.y, start.z])
        self.end = np.array([end.x, end.y, end.z])
        self.density = densty
        self.points: typing.List[Point]
        self.create_line()

    def create_line(self):
        """function that populates the line container with the points across the line
        """
        #define the direction of the vector
        direction = self.end - self.start

        # Define the desired length of the vector
        length = self.density

        # Normalize the direction vector
        normalized_direction = direction / np.linalg.norm(direction)

        # Create the new vector with the specified length
        line_vector = normalized_direction * length
        
        self.points.append(Point(self.start[0], 
                                 self.start[1], 
                                 self.start[2])) ##add start point
        
        #cycle line postions accordging to the line_vector
        curr_point = self.start.astype('float64')
        while (self._within_range(curr_point)):
            curr_point += line_vector #move point along line
            self.points.append(Point(curr_point[0], 
                                     curr_point[1], 
                                     curr_point[2])) #add point to list
            
        self.points.append(Point(self.end[0], 
                                 self.end[1], 
                                 self.end[2])) #add end point

    def _within_range(self, current_point: Point) -> bool:
        """checks if point is not further than the end point of the line

        Args:
            current_point (Point): Point to test

        Returns:
            bool: if currnt point within line range
        """        
        x = current_point[0] - self.end[0] > - \
            self.density and current_point[0] - self.end[0] < self.density
        y = current_point[1] - self.end[1] > - \
            self.density and current_point[1] - self.end[1] < self.density
        z = current_point[2] - self.end[2] > - \
            self.density and current_point[2] - self.end[2] < self.density
        if x and y and z:
            return False
        else:
            return True