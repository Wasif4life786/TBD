from core.vector import Vec3
from core.utility import linspace

class SurfacePlot:
    def __init__(self, surface_function, x_bounds, y_bounds, resolution):
        self.func = surface_function
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds
        self.resolution = resolution
        self.vertices = []
        self.triangles = []
        self.generate_mesh()

    def generate_mesh(self):
        x_values = linspace(self.x_bounds[0], self.x_bounds[1], self.resolution)
        y_values = linspace(self.y_bounds[0], self.y_bounds[1], self.resolution)
        for y in y_values:
            for x in x_values:
                self.vertices.append(Vec3(x, 0, y))
        for i in range(self.resolution - 1):
            for j in range(self.resolution - 1):
                p1 = i * self.resolution + j
                p2 = p1 + 1
                p3 = (i + 1) * self.resolution + j
                p4 = p3 + 1
                self.triangles.append((p1, p3, p4))
                self.triangles.append((p1, p4, p2))

    def update(self, time):
        for vertex in self.vertices:
            new_y = self.func(vertex.x, vertex.z, time)
            vertex.y = new_y