import math

from core.vector import Vec2, Vec3
def DegToRad(deg):
    return float(deg * math.pi/180)
def RadToDeg(rad):
    return float(rad * 180/math.pi)

def clamp(x,MIN,MAX):
    if x < MIN:
        return MIN
    elif x > MAX:
        return MAX
    return x

def get_forward_vector(self):
    return (self.target - self.position).normalize()

def get_right_vector(self):
    forward = self.get_forward_vector()
    return forward.cross(self.world_up).normalize()

def get_up_vector(self):
    forward = self.get_forward_vector()
    right = self.get_right_vector()
    return right.cross(forward).normalize()

def world_to_screen(self, world_pos, viewport_width, viewport_height):
    view_matrix = self.get_view_matrix()
    proj_matrix = self.get_projection_matrix()
    clip_pos = proj_matrix * view_matrix * world_pos
    if clip_pos.w != 0:
        ndc_x = clip_pos.x / clip_pos.w
        ndc_y = clip_pos.y / clip_pos.w
    else:
        ndc_x = clip_pos.x
        ndc_y = clip_pos.y
    screen_x = (ndc_x + 1.0) * 0.5 * viewport_width
    screen_y = (1.0 - ndc_y) * 0.5 * viewport_height 
    return Vec2(screen_x, screen_y) 

def move_to(self, position):
    self.position = position

def look_at(self, target):
    self.target = target

def orbit_around(self, center, radius, theta, phi):
    x = center.x + radius * math.sin(phi) * math.cos(theta)
    y = center.y + radius * math.cos(phi)
    z = center.z + radius * math.sin(phi) * math.sin(theta)
    self.position = Vec3(x, y, z)
    self.target = center

def zoom(self, factor):
    direction = self.get_forward_vector()
    self.position += direction * factor

def set_frame_center(self, center):
    offset = self.position - self.target
    self.target = center
    self.position = center + offset

def linspace(start, stop, num=50):
    if num <= 0:
        return []
    if num == 1:
        return [float(start)]
    step = (float(stop) - float(start)) / (num - 1)
    return [start + i * step for i in range(num)]
