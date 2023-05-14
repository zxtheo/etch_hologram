"""class that controls the rendering of the shapes on the canvas"""

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
        print("func_enter: Draw.__init__")
        self.canvas = canvas
        self.motion: typing.Union[int, float]
        self.y_adjustment: typing.Union[int, float]
        self.x_adjustment: typing.Union[int, float]
        print("func_exit: Draw.__init__")

    def draw_point (self, point: Point):
        """calls point.update to position the point in reation to the observers angle using self.motion, and draws that point taking into account altered self.x_pos and self.y_pos
        
        Args:
            point (Point): Point object to draw

        Returns:
            Draw: self
        """        
        print("func_enter: Draw.draw_point")
        self.y_adjustment = 0
        self.x_adjustment = 0
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
        print("func_exit: Draw.draw_point")
        return self
    
    def draw_line(self, line: Line):
        """draws each point in Line 
        Args:
            line (Line): Line to draw
        """        
        print("func_enter: Draw.draw_line")
        for point in line.points:
            self.draw_point(point)
        print("func_exit: Draw.draw_line")

    def draw_shape(self, shape: Shape):
        """draws each Line in a Shape
        Args:
            shape (Shape): Shape to draw
        """        
        print("func_enter: Draw.draw_shape")
        for line in shape.lines:
            self.draw_line(line)
        print("func_exit: Draw.draw_shape")

    def update_motion(self, value: typing.Union[int,float]):
        """update self.motion
        Args:
            value (int, float): _description_

        Returns:
            self
        """        
        print("func_enter: Draw.update_motion")
        print("func: Draw.update_motion : value: ", value)
        self.motion = float(value)
        print("func_exit: Draw.update_motion")
        return self
    
    def update_y_adjustment(self, value: typing.Union[int, float]):
        """update self.y_adjustment

        Args:
            value (int, float): y adjustmnet value to add to object to move them around the draw screen

        Returns:
            self
        """        
        print("func_enter: Draw.update_y_adjustment")
        self.y_adjustment = int(value)
        print("func_exit: Draw.update_y_adjustment")
        return self

    def update_x_adjustment(self, value: typing.Union[int, float]):
        """update self.x_adjustment

        Args:
            value (int, float): x adjustment value to add to object to move them around the draw screen

        Returns:
            self
        """       
        print("func_enter: Draw.update_x_adjustment") 
        self.x_adjustment = int(value)
        print("func_exit: Draw.update_x_adjustment")
        return self