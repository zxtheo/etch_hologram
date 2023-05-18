from class_line import Line
from class_point import Point

DENSITY = 2

square = [  
    Line(Point(100, 100, 100), Point(200, 100, 100), 10),
    Line(Point(200, 100, 100), Point(200, 200, 100), 10),
    Line(Point(200, 200, 100), Point(100, 200, 100), 10),
    Line(Point(100, 200, 100), Point(100, 100, 100), 10)
]

cube = [Line(Point(100, 100, 100), Point(300, 100, 100), DENSITY),
        Line(Point(100, 100, 100), Point(100, 300, 100), DENSITY),
        Line(Point(100, 300, 100), Point(300, 300, 100), DENSITY),
        Line(Point(300, 100, 100), Point(300, 300, 100), DENSITY),
        Line(Point(50, 50, 200), Point(250, 50, 200), DENSITY),
        Line(Point(50, 50, 200), Point(50, 250, 200), DENSITY),
        Line(Point(50, 250, 200), Point(250, 250, 200), DENSITY),
        Line(Point(250, 50, 200), Point(250, 250, 200), DENSITY),
        Line(Point(100, 100, 100), Point(50, 50, 200), DENSITY),
        Line(Point(300, 300, 100), Point(250, 250, 200), DENSITY),
        Line(Point(100, 300, 100), Point(50, 250, 200), DENSITY),
        Line(Point(300, 100, 100), Point(250, 50, 200), DENSITY)]

cube2 = [
    Line(Point(100, 100,    100),     Point(300,  100,    100), DENSITY),
    Line(Point(100, 100,    100),     Point(100,  300,    100), DENSITY),
    Line(Point(100, 300,    100),     Point(300,  300,    100), DENSITY),
    Line(Point(300, 100,    100),     Point(300,  300,    100), DENSITY),

    Line(Point(100, 100,  200),     Point(300,  100,  200), DENSITY),
    Line(Point(100, 100,  200),     Point(100,  300,  200), DENSITY),
    Line(Point(100, 300,  200),     Point(300,  300,  200), DENSITY),
    Line(Point(300, 100,  200),     Point(300,  300,  200), DENSITY),

    Line(Point(100, 100,    100),Point(100, 100,    200), DENSITY),
    Line(Point(100, 300,    100),Point(100, 300,    200), DENSITY),
    Line(Point(300, 300,    100),Point(300, 300,    200), DENSITY),
    Line(Point(300, 100,    100),Point(300, 100,    200), DENSITY)]

cube3 = [
    Line(Point(-0.707, 0.354, 0.354), Point(0,-0.146, 0.854), DENSITY),
    Line(Point(0,-0.146, 0.854), Point(0.707, 0.354, 0.354), DENSITY),
    Line(Point(0.707, 0.354, 0.354), Point(0.707, -0.354, -0.354), DENSITY),
    Line(Point(0.707, -0.354, -0.354), Point(0,0.146, -0.854), DENSITY),
    Line(Point(0,0.146, -0.854), Point(-0.707, -0.354, -0.354), DENSITY),
    Line(Point(-0.707, -0.354, -0.354), Point(-0.707, 0.354, 0.354), DENSITY),
    Line(Point(0,-0.146, 0.854), Point(0,-0.854,0.146), DENSITY),
    Line(Point(0,-0.854,0.146), Point(0.707, -0.354, -0.354), DENSITY),
    Line(Point(0,-0.854,0.146), Point(-0.707, -0.354, -0.354), DENSITY)
]

triangle = [  
    Line(Point(0, 0, 100    ), Point(200, 0, 100   ), DENSITY),
    Line(Point(200, 0, 100  ), Point(100, 200, 100  ), DENSITY),
    Line(Point(100, 200, 100), Point(0, 0, 100      ), DENSITY),
    Line(Point(0, 0, 100    ), Point(100, 100, 0   ), DENSITY),
    Line(Point(200, 0, 100  ), Point(100, 100, 0  ), DENSITY),
    Line(Point(100, 200, 100), Point(100, 100, 0   ), DENSITY)
]

cube4 = [
  [[50, 50, 50], [150, 50, 50]],
  [[150, 50, 50], [150, 150, 50]],
  [[150, 150, 50], [50, 150, 50]],
  [[50, 150, 50], [50, 50, 50]],
  [[50, 50, 150], [150, 50, 150]],
  [[150, 50, 150], [150, 150, 150]],
  [[150, 150, 150], [50, 150, 150]],
  [[50, 150, 150], [50, 50, 150]],
  [[50, 50, 50], [50, 50, 150]],
  [[150, 50, 50], [150, 50, 150]],
  [[150, 150, 50], [150, 150, 150]],
  [[50, 150, 50], [50, 150, 150]]
]