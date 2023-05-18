

class Point:
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Creates a point.
        
        @param x: The x coordinate of the point.
        @param y: The y coordinate of the point.
        @param z: The z coordinate of the point.
        """
        self.x = x
        self.y = y
        self.z = z
    

    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y}, {self.z})"
    
    def distance(self, other: 'Point') -> float:#
        """
        Returns the distance between this point and another point.
        
        @param other: The other point.

        @return: The distance between this point and the other point.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)**0.5

    def direction(self, other: 'Point') -> 'Point':
        """
        Returns the direction from this point to another point.

        @param other: The other point.

        @return: The direction from this point to the other point.
        """
        return Point(other.x - self.x, other.y - self.y, other.z - self.z)
    
    def divide(self, scalar: float) -> 'Point':
        """
        Returns the result of dividing this point by a scalar.

        @param scalar: The scalar to divide by.

        @return: The result of dividing this point by a scalar.
        """
        return Point(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def times(self, scalar: float) -> 'Point':
        """
        Returns the result of multiplying this point by a scalar.

        @param scalar: The scalar to multiply by.

        @return: The result of multiplying this point by a scalar.
        """
        return Point(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def add(self, other: 'Point') -> 'Point':
        """
        Returns the result of adding this point to another point.

        @param other: The other point.

        @return: The result of adding this point to another point.
        """
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


    