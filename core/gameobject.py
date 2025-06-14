from core.vector import Vec3
from core.matrix import Mat4

class GameObject:
    def __init__(self, vertices, triangles):
        self.vertices = vertices
        self.triangles = triangles
        self.position = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)
        self.scale = Vec3(1, 1, 1)

    def get_model_matrix(self) -> Mat4:
        trans_matrix = Mat4.translation(self.position.x, self.position.y, self.position.z)
        rot_x_matrix = Mat4.rotation_x(self.rotation.x)
        rot_y_matrix = Mat4.rotation_y(self.rotation.y)
        rot_z_matrix = Mat4.rotation_z(self.rotation.z)
        rot_matrix = rot_z_matrix * rot_x_matrix * rot_y_matrix
        scale_matrix = Mat4.scale(self.scale.x, self.scale.y, self.scale.z)
        model_matrix = trans_matrix * rot_matrix * scale_matrix
        return model_matrix