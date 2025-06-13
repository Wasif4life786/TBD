import math
def clamp(x,MIN,MAX):
    if x < MIN:
        return MIN
    elif x > MAX:
        return MAX
    return x
def project_vertex(vertex, mvp_matrix, screen_width, screen_height):
    projected = mvp_matrix * vertex.to_vec4(1.0)
    screen = projected.perspective_divide()
    return (
        int((screen.x + 1) * screen_width / 2),
        int((1 - screen.y) *screen_height / 2)
    )

