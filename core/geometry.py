import math
from core.vector import Vec3

def create_cube(size=1.0):
    s = size / 2
    vertices = [
        Vec3(-s, -s, -s), Vec3(s, -s, -s), Vec3(s, s, -s), Vec3(-s, s, -s),
        Vec3(-s, -s, s), Vec3(s, -s, s), Vec3(s, s, s), Vec3(-s, s, s),
    ]
    triangles = [
        (3, 2, 1), (3, 1, 0),
        (4, 5, 6), (4, 6, 7),
        (0, 1, 5), (0, 5, 4),
        (3, 7, 6), (3, 6, 2),
        (1, 2, 6), (1, 6, 5),
        (0, 4, 7), (0, 7, 3)
    ]
    
    return vertices, triangles

def create_sphere(radius=1.0, rings=16, sectors=32):
    vertices = []
    triangles = []
    for i in range(rings + 1):
        phi = math.pi * i / rings
        for j in range(sectors + 1):
            theta = 2 * math.pi * j / sectors
            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.cos(phi)
            z = radius * math.sin(phi) * math.sin(theta)
            vertices.append(Vec3(x, y, z))
    for i in range(rings):
        for j in range(sectors):
            first = (i * (sectors + 1)) + j
            second = first + sectors + 1
            triangles.append((first, second, first + 1))
            triangles.append((second, second + 1, first + 1))
    return vertices, triangles