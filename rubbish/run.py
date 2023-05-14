"""test script"""
import tkinter as tk

from etch_hologram import Draw, Shape, Point
import shapes

# Create a Tkinter window
print("Create a Tkinter window")
root = tk.Tk()
root.title("Point")
# Create a slider widget
print("Create a slider widget")
# slider = tk.Scale(root, from_=-2, to=-1, showvalue=True,resolution=0.1, orient="horizontal")
# slider.pack()
canvas = tk.Canvas(root, width=1000, height=1000)

# draw = Draw(canvas)
# shape = Shape()
# shape.add_line(Point(100,100,0),Point(300,300,0), 10)
print("Create a point")
# point = Point(100,100,100)
#shape.create_shape_from_line_choords(shapes.test_cube, shapes.DENSITY)

# Define a function to update the label text when the slider value changes
# def update_and_draw_points(value):
#     print("func_enter: update_and_draw_points")
#     # canvas.delete("all")
#     # draw.update_motion(value).draw_point(point)
#     print("func_exit: update_and_draw_points")

# Bind the update_label function to the slider widget
# slider.config(command=update_and_draw_points)
canvas.pack()

# Start the Tkinter event loop
print("Start the Tkinter event loop")
root.mainloop()
