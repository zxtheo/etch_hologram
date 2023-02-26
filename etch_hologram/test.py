
import tkinter as tk
import numpy as np
Motion = 0
class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.startx = self.x-1
        self.endx = self.x + 1
        self.currx= None
        self.curry = None

        self.update(0)
        
    
    def update(self, motion):
        self.currx = self.x + motion
        self.curry = (0.001*(self.z/100) * (self.currx-self.x)**2) + self.y
        


    def draw(self, canvas):
        r = 3

        fill='#{:02x}{:02x}{:02x}'.format(*(int(self.z), int(self.z), int(self.z)))
        canvas.create_oval(
            self.currx - r,
            self.curry - r,
            self.currx + r,
            self.curry + r,
            fill=fill
        )
        #print([self.currx, self.curry, self.z])

class Line:
    def __init__(self, pointa, pointb, densty):
        self.pointa = np.array([pointa.x, pointa.y, pointa.z])
        self.pointb = np.array([pointb.x, pointb.y, pointb.z])
        self.density = densty
        self.points = []
        self.create_line()

    def create_line(self):
        temp = None
        direction = self.pointb - self.pointa
                
        # Define the desired length of the vector
        length = self.density

        # Normalize the direction vector
        normalized_direction = direction / np.linalg.norm(direction)

        # Create the new vector with the specified length
        line_vector = normalized_direction * length

        curr_point = self.pointa.astype('float64')
        self.points.append(Point(self.pointa[0], self.pointa[1], self.pointa[2]))
        while(not self._within_range(curr_point, self.pointb, self.density)):
            curr_point += line_vector
            self.points.append(Point(curr_point[0], curr_point[1], curr_point[2]))
            curr_point += line_vector
        self.points.append(Point(self.pointb[0], self.pointb[1], self.pointb[2]))

        print(self.points)
    
    def _within_range(self, pointa, pointb, density):
        x = pointa[0] - pointb[0] > - density and pointa[0] - pointb[0] < density
        y = pointa[1] - pointb[1] > - density and pointa[1] - pointb[1] < density
        z = pointa[2] - pointb[2] > - density and pointa[2] - pointb[2] < density
        if x and y and z:
            return True
        else:
            return False
        
    def draw(self, canvas, value):
        for point in self.points:
            point.update(int(value))
            point.draw(canvas)

class face:
    def __init__(self):
        pass


density = 10
cube = [Line(Point(100, 100, 1),Point(300, 100, 1),density),
         Line(Point(100, 100, 1),Point(100, 300, 1),density),
         Line(Point(100, 300, 1),Point(300, 300, 1),density),
         Line(Point(300, 100, 1),Point(300, 300, 1),density),
         Line(Point(50, 50, 100),Point(250, 50, 100),density),
         Line(Point(50, 50, 100),Point(50, 250, 100),density),
         Line(Point(50, 250, 100),Point(250, 250, 100),density),
         Line(Point(250, 50, 100),Point(250, 250, 100),density),
         Line(Point(100, 100, 1),Point(50, 50, 100),density),
         Line(Point(300, 300, 1),Point(250, 250, 100),density),
         Line(Point(100, 300, 1),Point(50, 250, 100),density),
         Line(Point(300, 100, 1),Point(250, 50, 100),density)]





# Create a Tkinter window
root = tk.Tk()
root.title("Point")
# Create a slider widget
slider = tk.Scale(root, from_=-100, to=100, orient="horizontal")
slider.pack()


# Define a function to update the label text when the slider value changes
def update_and_draw_points(value):
    canvas.delete("all")
    for line in cube:
        line.draw(canvas, value)
    


# Bind the update_label function to the slider widget
slider.config(command=update_and_draw_points)


# Create a canvas widget
canvas = tk.Canvas(root, width=1000, height=1000)

canvas.pack()




# Start the Tkinter event loop
root.mainloop()