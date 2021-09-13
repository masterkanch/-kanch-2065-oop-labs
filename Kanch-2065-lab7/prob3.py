"""
Kanch Ruansiripiyakul 633040206-5
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.radius, 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    radius = float(input('Enter a radius:'))
    circle = Circle(radius)
    print(
        f"The circle with radius {radius} has the area as {round(circle.calculate_area(),2)} and the perimeter as {round(circle.calculate_perimeter(),2)}")
