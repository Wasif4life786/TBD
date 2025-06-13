from core.vector import Vec3

def create_cube(size=1.0):
    s = size / 2
    vertices = [
        Vec3(-s, -s, -s), Vec3(s, -s, -s), Vec3(s, s, -s), Vec3(-s, s, -s),
        Vec3(-s, -s, s), Vec3(s, -s, s), Vec3(s, s, s), Vec3(-s, s, s),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 5, 6, 7),        
        (0, 1, 5, 4),
        (2, 3, 7, 6),
        (1, 2, 6, 5),
        (0, 3, 7, 4),
    ]
    return vertices, faces