import pygame as pg
import math
from core.camera import Camera
from core.vector import Vec3
from render.projection import Renderer
from engine.scenes import setup_spinning_shapes_scene, setup_vector_field_scene, setup_parametric_curve_scene

# Change this variable to "shapes", "vector_field", or "parametric_curve"
ACTIVE_SCENE_NAME = "vector_field"

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
        pg.display.set_caption("WANIM - Spinning Shapes")
    elif ACTIVE_SCENE_NAME == "vector_field":
        scene_data = setup_vector_field_scene()
        pg.display.set_caption("WANIM - Vector Field")
    elif ACTIVE_SCENE_NAME == "parametric_curve":
        scene_data = setup_parametric_curve_scene()
        pg.display.set_caption("WANIM - Parametric Curve")
    mouse_down = False
    last_mouse_pos = None
    rotation_speed = 0.005
    zoom_speed = 0.1
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
        if scene_data.get("update"):
            scene_data["update"]()
        screen.fill((20, 20, 30))
        if scene_data["type"] == "meshes":
            renderer.render(scene_data["objects"], scene_data["light"])
        elif scene_data["type"] == "lines":
            mvp = camera.get_projection_matrix() * camera.get_view_matrix()
            renderer.render_lines(scene_data["lines"], scene_data["color"], mvp)
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main()
