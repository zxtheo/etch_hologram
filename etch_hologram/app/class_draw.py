import math
from class_point import Point
from class_line import Line
class Draw:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shape = Line(Point(100, 100, 10), Point(200, 200, 10),10)
        self.density = 2
        self.x_adjust = 0
        self.y_adjust = 0
        self.rotation = 0
    
    def update_density(self, density):
        self.density = density
        self.shape.density = density
        self.shape.create_points_along_line()
        self.draw()

    def draw(self):
        self.canvas.delete("all") # Clear the canvas
        self.draw_line(self.shape)

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