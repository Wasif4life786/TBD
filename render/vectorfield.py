from core.vector import Vec3
from core.utility import linspace

class VectorField:
    def __init__(self, vector_function, bounds, resolution):
        self.vector_func = vector_function
        self.bounds = bounds
        self.resolution = resolution
        self.lines = []
        self.generate_lines()

    def generate_lines(self):
        self.lines = []
        min_x, max_x, min_y, max_y, min_z, max_z = self.bounds
        x_points = linspace(min_x, max_x, self.resolution)
        y_points = linspace(min_y, max_y, self.resolution)
        z_points = linspace(min_z, max_z, self.resolution)
        for x in x_points:
            for y in y_points:
                for z in z_points:
                    start_point = Vec3(x, y, z)
                    vector = self.vector_func(start_point)
                    end_point = start_point + vector
                    self.lines.append((start_point, end_point))

    def swirl_vector_field(p: Vec3):
        scale = 0.2
        return Vec3(-p.y * scale, p.x * scale, 0)