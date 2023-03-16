
import typing
import math
import numpy as np


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

# class Face:
    
#     def __init__(self, lines, opaque):
#         self.lines = lines
#         self.points = self.get_points()
#         self.opaque = opaque

        
#     def get_points(self):
#         points = []
#         for line in self.lines:
#             for point in line.points:
#                 plist = [point.x, point.y]
#                 if plist not in points:
#                     points.append(plist)
#         return points



#     def point_in_polygon(self, point):
#         """
#         Check if a 2D point is within a 2D polygon.
#         point: (x, y) tuple or list representing the coordinates of the point
#         polygon: list of (x, y) tuples or lists representing the vertices of the polygon
#         Returns: True if the point is inside the polygon, False otherwise
#         """
#         polygon = self.points
#         x, y = point
#         n = len(polygon)
#         inside = False

#         # Check if point is on the boundary of the polygon
#         for i in range(n):
#             x1, y1 = polygon[i]
#             x2, y2 = polygon[(i+1) % n]
#             if ((y1 <= y < y2 or y2 <= y < y1) and x > (x2 - x1) * (y - y1) / (y2 - y1) + x1):
#                 inside = not inside

#         # Cast a ray from the point and count the number of edge intersections
#         count = 0
#         for i in range(n):
#             x1, y1 = polygon[i]
#             x2, y2 = polygon[(i+1) % n]
#             if (y1 < y <= y2 or y2 < y <= y1) and x > (y - y1) * (x2 - x1) / (y2 - y1) + x1:
#                 count += 1

#         return count % 2 == 1 if inside else False
