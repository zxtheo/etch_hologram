from class_point import Point
class Line:
    def __init__(self, start: Point, end: Point, density: int):
        self.start = start
        self.end = end
        self.density = density
        self.points = []
        self.create_points_along_line()

    def create_points_along_line(self):
        self.points = [] # clear the points list
        direction = self.start.direction(self.end) # direction of the line
        magnitude = self.start.distance(self.end)  # magnitude of the line
        normalised = direction.divide(magnitude) # normalised direction of the line
        line_vector = normalised.times(self.density) # vector of the line

        self.points.append(self.start) # add the start point
        curr_point = self.start # set the current point to the start point
        for i in range(1, int(magnitude/self.density)): # for each point along the line
            curr_point = curr_point.add(line_vector) # move the current point along the line
            self.points.append(curr_point) # add the current point to the list of points
        self.points.append(self.end) # add the end point

    def __str__(self):
        return "Line: start = " + str(self.start) + ",\n end = " + str(self.end) + ",\n density = " + str(self.density) + ",\n points = " + str(self.points)