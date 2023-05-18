from class_line import Line
from class_point import Point

class Shape:
    def __init__(self):
        self.lines = []
        self.points = []
        self.set_points()

    def set_points(self):
        """
        Sets the points of the shape.
        """
        self.points = [] # clear the points list
        for line in self.lines: # for each line in the shape
            for point in line.points: # for each point in the line
                self.points.append(point) # add the point to the list of points
       
        self.points = list(set(self.points)) # remove duplicates from the list of points

    def coords_to_lines(self, coordinates):
        """
        Converts a list of coordinates to a list of lines.
        """
        self.lines= []
        for coord in coordinates: # for each coordinate in the list of coordinates
            generated_line = Line(Point(coord[0][0], coord[0][1], coord[0][2]),
                                   Point(coord[1][0], coord[1][1], coord[1][2]), 2) # create a line from the coordinate
            self.lines.append(generated_line) # add the line to the list of lines
        
        self.set_points() # set the points of the shape
        

        

        
            
    

    
