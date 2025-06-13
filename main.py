import pygame as pg
import math
from core.vector import Vec3
from core.camera import Camera
from core.geometry import create_cube
from primitives.axes import create_axes
from core.utility import project_vertex
def main():
    pg.init()
    screen_width = 1024
    screen_height = 768
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("WANIM")
    clock = pg.time.Clock()
    camera = Camera()
    camera.aspect_ratio = screen_width / screen_width
    
    vertices, faces = create_cube()
    axes_vertices, axes_lines, axes_colours = create_axes(2.0)

    mouse_down = False
    last_mouse_pos = None
    rotation_speed = 0.005
    zoom_speed = 0.1


    running = True
    while running:
        screen.fill((10, 10, 10))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_down = True
                    last_mouse_pos = event.pos
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
            elif event.type == pg.MOUSEMOTION:
                if mouse_down:
                    current_mouse_pos = event.pos
                    dx = last_mouse_pos[0] - current_mouse_pos[0]
                    dy = last_mouse_pos[1] - current_mouse_pos[1]

                    camera.yaw += dx * rotation_speed
                    camera.pitch -= dy * rotation_speed

                    camera.pitch = max(-math.pi / 2 + 0.01, min(math.pi / 2 - 0.01, camera.pitch))

                    camera._update_position_from_angles() 
                    last_mouse_pos = current_mouse_pos
                elif event.type == pg.MOUSEWHEEL:
                    camera.radius -= event.y * zoom_speed
                    camera.radius = max(1.0, camera.radius)
                    camera._update_position_from_angles()

                

        mvp = camera.get_mvp_matrix()
        projected = [project_vertex(v, mvp, 1024, 768) for v in vertices]

        for face in faces:
            for i in range(len(face)):
                p1 = projected[face[i]]
                p2 = projected[face[(i + 1) % len(face)]]
                pg.draw.line(screen, (255, 255, 255), p1, p2, 1)
        
        projected_axes = [project_vertex(v, mvp, screen_width, screen_height) for v in axes_vertices]
        for i, line_indices in enumerate(axes_lines):
            p1_idx, p2_idx = line_indices
            p1_screen = projected_axes[p1_idx]
            p2_screen = projected_axes[p2_idx]
            if p1_screen and p2_screen:
                pg.draw.line(screen, axes_colours[i], p1_screen, p2_screen, 2) 

        pg.display.flip()
        clock.tick(60)
        
    pg.quit()




if __name__ == "__main__":
    main()