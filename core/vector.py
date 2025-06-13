from math import *
class Vec2:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    
    def add(self, w):
        return Vec2(self.x + w.x, self.y + w.y)
    
    def sub(self, w):
        return Vec2(self.x - w.x, self.y - w.y)
    
    def mul(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)
    
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

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def add(self, w):
        return Vec3(self.x + w.x, self.y + w.y, self.z + w.z)
    
    def sub(self, w):
        return Vec3(self.x - w.x, self.y - w.y, self.z - w.z)
    
    def mul(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
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
    
class Vec4:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

    def add(self, w):
        return Vec4(self.x + w.x, self.y + w.y, self.z + w.z, self.w + w.w)
    
    def sub(self, w):
        return Vec4(self.x - w.x, self.y - w.y, self.z - w.z, self.w - w.w)
    
    def mul(self, scalar):
        return Vec4(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
    
    def dot(self, w):
        return self.x * w.x + self.y * w.y + self.z * w.z + self.w * w.w
    
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2)
    
    def perspective_div(self):
        if self.w == 0:
            raise ZeroDivisionError("w component is zero.")
        return Vec3(self.x / self.w, self.y / self.w, self.z / self.w)
    