import typing
from etch_hologram.Line import Line
from etch_hologram.Point import Point


class Shape:
    """container for all points contained in a shape
    """
    def __init__(self):
        """init function for Shape
        """
        self.points: typing.List[Point]
        self.lines: typing.List[Line]
        #self.faces = []

    def create_shape_from_line_choords(self,
                                       lines: typing.List[typing.List[typing.List[int]]], 
                                       density: int):
        """populates shape object using a series of start and end points of lines, creates lines of points using the desity 
        
        Args:
            lines (List[List[List[int]]]): [[start of line point[x,y,z] ,end of line point[x,y,z]], ...]
            density (int): space between points on a line
        """
        self.points = []
        self.lines = []
        #self.faces = []
        for line in lines:
            #get start and end point of line
            start_point = Point(line[0][0], line[0][1], line[0][2])
            end_point = Point(line[1][0], line[1][1], line[1][2])

            #generate line
            generated_line = Line(start_point, end_point, density)
            
            #append line to self.lines
            self.lines.append(generated_line)

            #append each point in line to self.points
            for point in generated_line.points:
                self.points.append(point)