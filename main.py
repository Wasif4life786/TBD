import pygame as pg
import math
from core.vector import Vec3
from engine.scenes import setup_spinning_shapes_scene, setup_vector_field_scene, setup_parametric_curve_scene, setup_surface_plot_scene
from core.camera import Camera
from render.projection import Renderer

# Change this variable to "shapes", "vector_field", "parametric_curve", or "surface_plot"
ACTIVE_SCENE_NAME = "surface_plot"
def main():
    pg.init()
    screen_width, screen_height = 1024, 768
    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption("WANIM Engine")
    clock = pg.time.Clock()
    camera = Camera()
    camera.position = Vec3(0, 0, 10)
    camera.aspect_ratio = screen_width / screen_height
    renderer = Renderer(screen, camera)
    scene_data = {}
    if ACTIVE_SCENE_NAME == "shapes":
        scene_data = setup_spinning_shapes_scene()
    elif ACTIVE_SCENE_NAME == "vector_field":
        scene_data = setup_vector_field_scene()
    elif ACTIVE_SCENE_NAME == "parametric_curve":
        scene_data = setup_parametric_curve_scene()
    elif ACTIVE_SCENE_NAME == "surface_plot":
        scene_data = setup_surface_plot_scene()
    mouse_down = False
    last_mouse_pos = None
    rotation_speed = 0.005
    zoom_speed = 0.1
    time = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: mouse_down = True; last_mouse_pos = event.pos
                elif event.button == 4: camera.radius = max(1.0, camera.radius - zoom_speed * 10); camera._update_position_from_angles()
                elif event.button == 5: camera.radius += zoom_speed * 10; camera._update_position_from_angles()
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1: mouse_down = False
            elif event.type == pg.MOUSEMOTION and mouse_down:
                dx, dy = event.pos[0] - last_mouse_pos[0], event.pos[1] - last_mouse_pos[1]
                camera.yaw += dx * rotation_speed
                camera.pitch = max(-math.pi/2 + 0.01, min(math.pi/2 - 0.01, camera.pitch + dy * rotation_speed))
                camera._update_position_from_angles()
                last_mouse_pos = event.pos
        time += 0.05  
        update_func = scene_data.get("update")
        if update_func:
            update_func(time)
        screen.fill((20, 20, 30))
        if scene_data["type"] == "meshes":
            renderer.render(scene_data["objects"], scene_data["light"])
        elif scene_data["type"] == "lines":
            mvp = camera.get_projection_matrix() * camera.get_view_matrix()
            renderer.render_lines(scene_data["lines"], scene_data["colour"], mvp)
        pg.display.flip()
        clock.tick(60)
    pg.quit()
if __name__ == "__main__":
    main()