import pygame as pg
import math
from core.camera import Camera
from core.geometry import create_cube, create_sphere
from primitives.axes import create_axes
from core.utility import project_vertex
from core.vector import Vec3, Vec4 

def main():
    pg.init()
    screen_width = 1024
    screen_height = 768
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("WANIM")
    clock = pg.time.Clock()
    camera = Camera()
    camera.aspect_ratio = screen_width / screen_height

    vertices, triangles = create_sphere()
    axes_vertices, axes_lines, axes_colours = create_axes(2.0)

    mouse_down = False
    last_mouse_pos = None
    rotation_speed = 0.005
    zoom_speed = 0.1

    light_direction_world = Vec3(1, 1, 1).normalize()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    last_mouse_pos = event.pos
                elif event.button == 4:
                    camera.radius -= zoom_speed * 10
                    camera.radius = max(1.0, camera.radius)
                    camera._update_position_from_angles()
                elif event.button == 5:
                    camera.radius += zoom_speed * 10
                    camera._update_position_from_angles()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            elif event.type == pg.MOUSEMOTION:
                if mouse_down:
                    current_mouse_pos = event.pos
                    dx = current_mouse_pos[0] - last_mouse_pos[0]
                    dy = current_mouse_pos[1] - last_mouse_pos[1]
                    camera.yaw += dx * rotation_speed
                    camera.pitch += dy * rotation_speed
                    camera.pitch = max(-math.pi / 2 + 0.01, min(math.pi / 2 - 0.01, camera.pitch))
                    camera._update_position_from_angles()
                    last_mouse_pos = current_mouse_pos
        
        screen.fill((0, 0, 0))

        mvp = camera.get_mvp_matrix()
        view_matrix = camera.get_view_matrix()

        light_dir_view_vec4 = view_matrix * Vec4(light_direction_world.x, light_direction_world.y, light_direction_world.z, 0.0)
        light_direction_view = Vec3(light_dir_view_vec4.x, light_dir_view_vec4.y, light_dir_view_vec4.z).normalize()

        triangles_to_render = []
        for tri_indices in triangles:
            v0, v1, v2 = vertices[tri_indices[0]], vertices[tri_indices[1]], vertices[tri_indices[2]]
            
            v0_view = view_matrix * v0
            v1_view = view_matrix * v1
            v2_view = view_matrix * v2
            
            normal = (v1_view - v0_view).cross(v2_view - v0_view).normalize()
            
            if normal.z < 0:
                continue

            intensity = max(0.1, min(1, normal.dot(light_direction_view)))
            face_color = (int(255 * intensity), int(192 * intensity), int(203 * intensity))
            
            p0_screen = project_vertex(v0, mvp, screen_width, screen_height)
            p1_screen = project_vertex(v1, mvp, screen_width, screen_height)
            p2_screen = project_vertex(v2, mvp, screen_width, screen_height)

            depth = (v0_view.z + v1_view.z + v2_view.z) / 3.0
            triangles_to_render.append((depth, [p0_screen, p1_screen, p2_screen], face_color))

        triangles_to_render.sort(key=lambda x: x[0], reverse=True)
        
        for _, points, color in triangles_to_render:
            pg.draw.polygon(screen, color, points)
            pg.draw.polygon(screen, (50, 50, 50), points, 1)

        projected_axes = [project_vertex(v, mvp, screen_width, screen_height) for v in axes_vertices]
        for i, line_indices in enumerate(axes_lines):
            p1_idx, p2_idx = line_indices
            p1_screen = projected_axes[p1_idx]
            p2_screen = projected_axes[p2_idx]
            pg.draw.line(screen, axes_colours[i], p1_screen, p2_screen, 2)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()