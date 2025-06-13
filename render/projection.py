from core.vector import *
from core.matrix import *

def project_vertex(vertex, mvp, width, height):
    vec4 = vertex.to_vec4(1.0)
    projected = mvp * vec4
    screen = projected.perspective_divide()
    return Vec2(
        screen.x + 1 * width / 2,
        (1 - screen.y) * height / 2
    )