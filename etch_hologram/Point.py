"""contaner of all information and methods regarding an individual Point"""

import math
import typing


class Point:
    """contaner of all information and methods regarding an individual Point
    """
    def __init__(self, x: typing.Union[int, float], y: typing.Union[int, float], z: typing.Union[int, float]):
        """init function of Point

        Args:
            x (int, float): x position (0,0 top left)
            y (int, float): y position (0,0 top left)
            z (int, float): z poisiton (larger = further away)
        """
        self.x = x
        self.y = y 
        self.z = z
        self.start_x = self.x-1 #hopefully prevents div by zero
        self.end_x = self.x + 1 #hopefully prevents div by zero
        self.curr_x: typing.Union[int, float]
        self.curr_y: typing.Union[int, float]
        self.visible = True

        self.update(0)

    def update(self, viewing_angle: typing.Union[float, int]):
        """update current position of point using the viewers angle

        Args:
            viewing_angle (int, float): the angle of the viwer, tied to the slider in view mode

        Returns:
            self (Point)
        """
        #follows the curve of a circle, 
        #using the z pos as the radius size to create the illusion of depth
        x = self.x
        y = self.y 
        radius = self.z 
        self.curr_x  = x + radius * math.cos(viewing_angle)
        self.curr_y = y + radius * math.sin(viewing_angle) + radius
        return self