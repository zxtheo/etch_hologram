"""class that takes controls the rendering of the shapes on the canvas"""

import typing

from etch_hologram.Point import Point
from etch_hologram.Line import Line
from etch_hologram.Shape import Shape

class Draw:
    """class that takes controls the rendering of the shapes on the canvas
    """
    def __init__(self, canvas):
        """init function of Draw class

        Args:
            canvas (tk.canvas): the canvas to be used for drawing
        """        
        self.canvas = canvas
        self.motion: typing.Union[int, float]
        self.y_adjustment: typing.Union[int, float]
        self.x_adjustment: typing.Union[int, float]

    def draw_point (self, point: Point):
        """calls point.update to position the point in reation to the observers angle using self.motion, and draws that point taking into account altered self.x_pos and self.y_pos
        
        Args:
            point (Point): Point object to draw

        Returns:
            Draw: self
        """        
        point.update(self.motion)
        
        radius = 2
        x = point.curr_x + self.x_adjustment
        y = point.curr_y + self.y_adjustment
        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            fill="black",
            outline=""
        )
        return self
    
    def draw_line(self, line: Line):
        """draws each point in Line 
        Args:
            line (Line): Line to draw
        """        
        for point in line.points:
            self.draw_point(point)

    def draw_shape(self, shape: Shape):
        """draws each Line in a Shape
        Args:
            shape (Shape): Shape to draw
        """        
        for line in shape.lines:
            self.draw_line(line)

    def update_motion(self, value: typing.Union[int,float]):
        """update self.motion
        Args:
            value (int, float): _description_

        Returns:
            self
        """        
        self.motion = float(value)
        return self
    
    def update_y_pos(self, value: typing.Union[int, float]):
        """update self.y_pos

        Args:
            value (int, float): y pos value to add to object to move them around the draw screen

        Returns:
            self
        """        
        self.y_adjustment = int(value)
        return self