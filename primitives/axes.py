from core.vector import Vec3

def create_axes(length):
    vertices = [
        Vec3(0,0,0),
        Vec3(length, 0, 0),
        Vec3(0, length, 0),
        Vec3(0, 0, length)
    ]

    lines = [
        (0, 1),
        (0, 2),
        (0, 3),
    ]

    colours = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255)
    ]
    return vertices, lines, colours