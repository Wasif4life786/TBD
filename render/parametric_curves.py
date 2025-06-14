from core.utility import linspace
from core.vector import Vec3

class ParametricCurve:
    def __init__(self, x_func, y_func, z_func):
        self.x_func = x_func
        self.y_func = y_func
        self.z_func = z_func
        self.points = []

    def generate_points(self, t_min, t_max, resolution=100):
        self.points = []
        t_values = linspace(t_min, t_max, resolution)
        for t in t_values:
            x = self.x_func(t)
            y = self.y_func(t)
            z = self.z_func(t)
            self.points.append(Vec3(x, y, z))
        return self.points

    def get_line_segments(self):
        segments = []
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                segments.append((self.points[i], self.points[i+1]))
        return segments