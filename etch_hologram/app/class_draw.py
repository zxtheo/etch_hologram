import math, datetime
from class_point import Point
from class_line import Line
from class_shape import Shape
import test_shapes

import drawsvg as dw
class Draw:
    def __init__(self, canvas):
        self.canvas = canvas
        self.test_shape = test_shapes.cube4
        self.shape = Shape()
        self.shape.coords_to_lines(self.test_shape)
        
        
        self.density = 2 
        self.x_adjust = 0 
        self.y_adjust = 0
        self.rotation = 0
        self.depth = 1
    
    def update_depth(self, depth):
        self.depth = depth # update the depth
        self.shape.coords_to_lines(self.test_shape) # update the shape
        for line in self.shape.lines:
            line.depth = depth # update the depth of each line
            line.create_points_along_line() # update the points of each line
        self.shape.set_points() # update the points of the shape
        self.draw() # draw the shape

    def update_density(self, density):
        self.density = density # update the density
        for line in self.shape.lines:
            line.density = density # update the density of each line
            line.create_points_along_line() # update the points of each line
        self.shape.set_points() # update the points of the shape
        self.draw() # draw the shape

    def draw(self):
        self.canvas.delete("all") # Clear the canvas
        for point in self.shape.points:
            self.draw_point(point)

    def draw_line(self, line):
        for point in line.points:
            self.draw_point(point)
          
  
    
    def draw_point(self, point):
        radius = 2 
        
        #adjust point on view curve
        curr_x = point.x + point.z * math.cos(self.rotation) 
        curr_y = point.y + point.z * math.sin(self.rotation)

        # print("func: Draw.draw_point : curr_x = " + str(curr_x))
        # print("func: Draw.draw_point : curr_y = " + str(curr_y))
        # print("func: Draw.draw_point : rotation = " + str(math.cos(self.rotation)))

        self.canvas.create_oval(
            curr_x - radius + self.x_adjust,
            curr_y - radius + self.y_adjust,
            curr_x + radius + self.x_adjust,
            curr_y + radius + self.y_adjust,
            fill="black",
            outline=""
        )

    def save_svg(self):
        now = datetime.datetime.now()
        now = now.strftime("%y-%m-%d__%H-%M-%S")
        filename = f"etch#{now}.svg"
         # Create a new SVG drawing
        dwg = dw.Drawing(500, 500)

        # Add shapes or elements to the drawing
        for point in self.shape.points:
            

            # Define the center coordinates
            center_x = point.x + self.x_adjust # adjust the x coordinate
            center_y = point.y +self.y_adjust # adjust the y coordinate
            a = -math.pi # start angle
            b = 0 # end angle
            r = point.z # radius

            # Create the arc path
            arc_path = dw.Path(stroke='black', fill='none') # stroke is the color of the line, fill is the color of the shape
            arc_path.M(center_x + r * math.cos(a), center_y + r * math.sin(a)) # M is the starting point of the path
            arc_path.A(r, r, 0, 0, 1, center_x + r * math.cos(b), center_y + r * math.sin(b)) # A is the arc path

            # Add the arc path to the drawing
            dwg.append(arc_path)


        print("func: Draw.save_svg : saving svg...")

        # Save the SVG file
        dwg.save_svg(filename)
        print("func: Draw.save_svg : svg saved at " + filename + ".")

        pass