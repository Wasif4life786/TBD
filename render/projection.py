import pygame as pg
from core.vector import Vec2, Vec3, Vec4
from core.matrix import Mat4
from core.gameobject import GameObject
from typing import List
def project_vertex(vertex: Vec3, mvp: Mat4, w: int, h: int) -> Vec2:
    p_clip = mvp * vertex
    if p_clip.w == 0: return Vec2(-1, -1)
    p_ndc = Vec3(p_clip.x / p_clip.w, p_clip.y / p_clip.w, p_clip.z / p_clip.w)
    screen_x = (p_ndc.x + 1) * 0.5 * w
    screen_y = (1 - p_ndc.y) * 0.5 * h
    return Vec2(screen_x, screen_y)

class Renderer:
    def __init__(self, screen, camera):
        self.screen = screen
        self.camera = camera
        self.screen_width, self.screen_height = screen.get_size()

    def render(self, scene: List[GameObject], light_direction_world: Vec3):
        view_matrix = self.camera.get_view_matrix()
        proj_matrix = self.camera.get_projection_matrix()
        all_triangles_to_render = []
        for obj in scene:
            model_matrix = obj.get_model_matrix()
            for tri_indices in obj.triangles:
                v0, v1, v2 = obj.vertices[tri_indices[0]], obj.vertices[tri_indices[1]], obj.vertices[tri_indices[2]]
                v0_world = model_matrix * v0
                v1_world = model_matrix * v1
                v2_world = model_matrix * v2
                normal_world = (v1_world.to_vec3() - v0_world.to_vec3()).cross(v2_world.to_vec3() - v0_world.to_vec3()).normalize()
                intensity = max(0.1, min(1, normal_world.dot(light_direction_world)))
                face_color = (int(200 * intensity), int(200 * intensity), int(255 * intensity))
                v0_view = view_matrix * v0_world
                v1_view = view_matrix * v1_world
                v2_view = view_matrix * v2_world
                view_space_normal_z = (v1_view.to_vec3() - v0_view.to_vec3()).cross(v2_view.to_vec3() - v0_view.to_vec3()).normalize().z
                if view_space_normal_z < 0: continue
                depth = (v0_view.z + v1_view.z + v2_view.z) / 3.0
                mvp = proj_matrix * view_matrix * model_matrix
                p0_screen = project_vertex(v0, mvp, self.screen_width, self.screen_height)
                p1_screen = project_vertex(v1, mvp, self.screen_width, self.screen_height)
                p2_screen = project_vertex(v2, mvp, self.screen_width, self.screen_height)
                all_triangles_to_render.append((depth, [p0_screen, p1_screen, p2_screen], face_color))
        all_triangles_to_render.sort(key=lambda x: x[0])
        for _, points, color in all_triangles_to_render:
            pygame_points = [(p.x, p.y) for p in points]
            pg.draw.polygon(self.screen, color, pygame_points)
            pg.draw.polygon(self.screen, (50, 50, 50), pygame_points, 1)

    def render_lines(self, lines: List, color: tuple, mvp: Mat4):
        for line_start, line_end in lines:
            p0_screen = project_vertex(line_start, mvp, self.screen_width, self.screen_height)
            p1_screen = project_vertex(line_end, mvp, self.screen_width, self.screen_height)
            pygame_p0 = (p0_screen.x, p0_screen.y)
            pygame_p1 = (p1_screen.x, p1_screen.y)
            pg.draw.line(self.screen, color, pygame_p0, pygame_p1, 1)