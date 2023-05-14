
import typing
from etch_hologram.Line import Line
from etch_hologram.Point import Point

class Shape:
    def __init__(self):
        self.points: typing.List[Point] = []
        self.lines: typing.List[Line] = []

    def create_shape_from_line_choords(self,
                                       lines: typing.List[typing.List[typing.List[int]]], 
                                       density: int) -> None:
        self.points = []
        self.lines = []

        for line in lines:
            start_point = Point(line[0][0], line[0][1], line[0][2])
            end_point = Point(line[1][0], line[1][1], line[1][2])

            generated_line = Line(start_point, end_point, density)
            
            self.lines.append(generated_line)

            for point in generated_line.points:
                self.points.append(point)

    def __str__(self) -> str:
        return f"Shape with {len(self.points)} points and {len(self.lines)} lines"

    def update_points(self, viewing_angle: typing.Union[float, int]) -> None:
        for point in self.points:
            point.update(viewing_angle)

    def add_line(self, start: Point, end: Point, density: int) -> None:
        generated_line = Line(start, end, density)
        self.lines.append(generated_line)
        for point in generated_line.points:
            self.points.append(point)