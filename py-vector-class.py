import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, x: float, y: float):
        return Vector(self.x + x, self.y + y)

    def __sub__(self, x: float, y: float):
        return Vector(self.x - x, self.y - y)

    def __mul__(self, x: float, y: float):
        if isinstance(x, (int, float)) and y is None:
            return Vector(self.x * x, self.y * x)
        elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
            return round(self.x * x + self.y * y, 4)
        else:
            raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, start_x: float, start_y: float, end_x: float, end_y: float):
        x = end_x - start_x
        y = end_y - start_y
        return cls(x, y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, x: float, y: float):
        dot_prod = self.x * x + self.y * y
        len_self = self.get_length()
        len_other = (x ** 2 + y ** 2) ** 0.5
        cos_theta = dot_prod / (len_self * len_other)

        cos_theta = max(min(cos_theta, 1), -1)
        angle_rad = math.acos(cos_theta)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self):
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = round(math.degrees(angle_rad))
        angle_from_y = angle_deg % 360
        return round(angle_from_y)

    def rotate(self, degrees: float):
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)


vector = Vector(-2.343, 8.008)
print(vector.x)  # -2.34
print(vector.y)  # 8.01

vector1 = Vector(2, 4)
vector3 = vector1.__add__(-1, 3)
print(vector3.x)  # 1
print(vector3.y)  # 7

vector1 = Vector(2, 4)
vector3 = vector1.__sub__(-1, 3)
print(vector3.x)  # 3
print(vector3.y)  # 1

vector1 = Vector(2, 4)
vector2 = vector1.__mul__(3.743, None)
print(vector2.x)  # 7.49
print(vector2.y)  # 14.97

# Dot product of vectors
vector1 = Vector(2.11, 4.55)
dot_product = vector1.__mul__(-3.51, 10.33)
print(dot_product)  # 39.5954

# Creating a vector from two points
vector = Vector.create_vector_by_two_points(5.2, 2.6, 10.7, 6)
print(vector.x)  # 5.5
print(vector.y)  # 3.4

# Vector length
vector = Vector(2, 4)
print(vector.get_length())  # 4.47213595499958

# Vector normalization
vector1 = Vector(13, -4)
vector2 = vector1.get_normalized()
print(vector2.x)  # 0.96
print(vector2.y)  # -0.29
print(vector2.get_length())  # 1.0

# Angle between vectors
vector1 = Vector(13, -4)
angle = vector1.angle_between(-6, -11)
print(angle)  # 102

# The angle between a vector and the positive Y axis
vector = Vector(33, 8)
print(vector.get_angle())  # 76

# Rotate vector
vector = Vector(33, 8)
vector2 = vector.rotate(45)
print(vector2.x)  # 17.68
print(vector2.y)  # 28.99
