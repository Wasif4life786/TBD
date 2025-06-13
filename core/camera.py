<<<<<<< HEAD
import math
from core.matrix import Mat4
from core.vector import Vec3


class Camera:
    def __init__(self):
        self.position = Vec3(0, 0, 5)
        self.target = Vec3(0, 0, 0)
        self.world_up = Vec3(0, 1, 0)
        
        self.projection_type = "perspective"
        self.fov = 45.0  # degrees
        self.aspect_ratio = 16.0 / 9.0
        self.near = 0.1
        self.far = 1000.0
        self.ortho_size = 10.0

    def get_view_matrix(self):
        return Mat4.look_at(self.position, self.target, self.world_up)

    def get_projection_matrix(self):
        if self.projection_type == "perspective":
            return Mat4.perspective(
                math.radians(self.fov),
                self.aspect_ratio,
                self.near,
                self.far
        )
        elif self.projection_type == "orthographic":
            half_width = self.ortho_size / 2.0
            half_height = half_width / self.aspect_ratio
        
            return Mat4.orthographic(
            -half_width,    # left
            half_width,     # right
            -half_height,   # bottom
            half_height,    # top
            self.near,
            self.far
            )
        else:
            raise ValueError(f"Unknown projection type: {self.projection_type}")
=======
class Camera:
    def get_view_matrix():

    def get_projection_matrix():

    def get_mvp_matrix(model_matrix):
>>>>>>> 152e3e806b22f551fd638a8a5e2024634e9c6d9a
