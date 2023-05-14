import tkinter as tk

from etch_hologram import Point, Draw, Line
point = Point(100, 100, 0)
def update_and_draw_points(value):
    print("func_enter: update_and_draw_points")
    print(value)
    canvas.delete("all")
    draw.update_motion(value).draw_point(point)
    print("func_exit: update_and_draw_points")





root = tk.Tk()
root.title("etch_hologram")
root.geometry("1000x1000")
root.resizable(False, False)
print("Create a slider widget")


print("Create a point")

#point = Line(Point(100, 100, 0), Point(200, 200, 0), 10)



slider = tk.Scale(root, from_=-2, to=-1, showvalue=True,resolution=0.1, orient="horizontal")
slider.config(command=update_and_draw_points)
slider.pack()

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()
draw = Draw(canvas)


root.mainloop()

