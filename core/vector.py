from math import *
class Vec2:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    
    def __add__(self, w):
        return Vec2(self.x + w.x, self.y + w.y)
    
    def __sub__(self, w):
        return Vec2(self.x - w.x, self.y - w.y)
    
    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def dot(self, w):
        return self.x * w.x + self.y * w.y
    
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vec2(0,0)
        return Vec2(self.x / magnitude, self.y / magnitude)
    
    def cross(self, w):
        return self.x * w.y - self.y * w.x
    
    def distance_to(self, w):
        return (self - w).magnitude()
    
    def lerp(self, w, t):
        return self + (w - self) * t
    
    def rotate(self, angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Vec2(
            self.x * cos_a - self.y * sin_a, 
            self.x * sin_a + self.y * cos_a
        )

    def angle(self):
        return atan2(self.y, self.x)

    def __eq__(self, w):
        return abs(self.x - w.x) < 1e-9 and abs(self.y - w.y) < 1e-9
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vec2 index out of range")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Vec2 index out of range")

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, w):
        return Vec3(self.x + w.x, self.y + w.y, self.z + w.z)
    
    def __sub__(self, w):
        return Vec3(self.x - w.x, self.y - w.y, self.z - w.z)
    
    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def dot(self, w):
        return self.x * w.x + self.y * w.y + self.z * w.z
    
    def cross(self, w):
        return Vec3(
            self.y * w.z - self.z * w.y,
            self.z * w.x - self.x * w.z,
            self.x * w.y - self.y * w.x
        )
    
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vec3(0,0,0)
        return Vec3(self.x / magnitude, self.y / magnitude, self.z / magnitude)
    
    def distance_to(self, w):
        return (self - w).magnitude()
    
    def lerp(self, w, t):
        return self + (w - self) * t
    
    def reflect(self, normal):
        return self - 2 * self.dot(normal) * normal
    
    def rotate_x(self, angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Vec3(
            self.x,
            self.y * cos_a - self.z * sin_a,
            self.y * sin_a + self.z * cos_a
        )
    
    def rotate_y(self, angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Vec3(
            self.x * cos_a + self.z * sin_a,
            self.y, 
            -self.x * sin_a + self.z * cos_a
        )

    def rotate_z(self, angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Vec3(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a,
            self.z
        )
    
    def to_vec2(self):
        return Vec2(self.x, self.y)

    def to_vec4(self, w):
        return Vec4(self.x, self.y, self.z, w)
    
    def __eq__(self, w):
        return abs(self.x - w.x) < 1e-9 and abs(self.y - w.y) < 1e-9 and abs(self.z - w.z) < 1e-9
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vec3 index out of range")
    
    def __setitem__(self, index, value):
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        elif index == 2:
            self.z = float(value)
        else:
            raise IndexError("Vec3 index out of range")
    


class Vec4:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def __add__(self, w):
        return Vec4(self.x + w.x, self.y + w.y, self.z + w.z, self.w + w.w)
    
    def __sub__(self, w):
        return Vec4(self.x - w.x, self.y - w.y, self.z - w.z, self.w - w.w)
    
    def __mul__(self, scalar):
        return Vec4(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def dot(self, w):
        return self.x * w.x + self.y * w.y + self.z * w.z + self.w * w.w
    
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)
    
    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vec4(0, 0, 0, 0)
        return Vec4(self.x / magnitude, self.y / magnitude, self.z / magnitude, self.w / magnitude)
    
    def lerp(self, w, t):
        return self + (w - self) * t

    def perspective_divide(self):
        if self.w == 0:
            raise ZeroDivisionError("w component is zero.")
        return Vec3(self.x / self.w, self.y / self.w, self.z / self.w)
    
    def to_vec3(self):
        return Vec3(self.x, self.y, self.z)
    
    def to_vec2(self):
        return Vec2(self.x, self.y)
    
    def __eq__(self, w):
        return abs(self.x - w.x) < 1e-9 and abs(self.y - w.y) < 1e-9 and abs(self.z - w.z) < 1e-9 and abs(self.w - w.w) < 1e-9
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        elif index == 3:
            return self.w
        else:
            raise IndexError("Vec4 index out of range")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        elif index == 2:
            self.z = float(value)
        elif index == 3:
            self.w = float(value)
        else:
            raise IndexError("Vec4 index out of range")