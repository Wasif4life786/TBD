from math import *
from vector import Vec3, Vec4
class Mat3:
    def __init__(self, data=None):
        if data is None:
            self.data = [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]
            ]
        elif isinstance(data, list) and len(data) == 9:
            self.data = [
                [float(data[0]), float(data[1]), float(data[2])],
                [float(data[3]), float(data[4]), float(data[5])],
                [float(data[6]), float(data[7]), float(data[8])]
            ]
        elif isinstance(data, list) and len(data) == 3:
            self.data = [[float(data[i][j]) for j in range(3)] for i in range(3)]
        else:
            raise ValueError("Invalid data for Mat3 initialization")
        
    def __add__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Mat3(result)
    
    def __sub__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Mat3(result)   
    
    def __mul__(self, other):
        if isinstance(other, Mat3):
            result = [[0.0 for _ in range(3)] for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Mat3(result)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            x = self.data[0][0] * other.x + self.data[0][1] * other.y + self.data[0][2] * other.z
            y = self.data[1][0] * other.x + self.data[1][1] * other.y + self.data[1][2] * other.z
            z = self.data[2][0] * other.x + self.data[2][1] * other.y + self.data[2][2] * other.z
            return Vec3(x, y, z)
        else:
            result = []
            for i in range(3):
                row = []
                for j in range(3):
                    row.append(self.data[i][j] * other)
                result.append(row)
            return Mat3(result)   
        
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def transpose(self):
        result = [[0.0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[j][i] = self.data[i][j]
        return Mat3(result)
    
    def determinant(self):
        return (self.data[0][0] * (self.data[1][1] * self.data[2][2] - self.data[1][2] * self.data[2][1]) -
                self.data[0][1] * (self.data[1][0] * self.data[2][2] - self.data[1][2] * self.data[2][0]) +
                self.data[0][2] * (self.data[1][0] * self.data[2][1] - self.data[1][1] * self.data[2][0]))
    
    def inverse(self):
        det = self.determinant()
        if abs(det) < 1e-9:
            raise ValueError("Matrix is not invertible (determinant is zero)")
        inv_det = 1.0 / det
        result = [[0.0 for _ in range(3)] for _ in range(3)]       
        result[0][0] = (self.data[1][1] * self.data[2][2] - self.data[1][2] * self.data[2][1]) * inv_det
        result[0][1] = (self.data[0][2] * self.data[2][1] - self.data[0][1] * self.data[2][2]) * inv_det
        result[0][2] = (self.data[0][1] * self.data[1][2] - self.data[0][2] * self.data[1][1]) * inv_det
        result[1][0] = (self.data[1][2] * self.data[2][0] - self.data[1][0] * self.data[2][2]) * inv_det
        result[1][1] = (self.data[0][0] * self.data[2][2] - self.data[0][2] * self.data[2][0]) * inv_det
        result[1][2] = (self.data[0][2] * self.data[1][0] - self.data[0][0] * self.data[1][2]) * inv_det
        result[2][0] = (self.data[1][0] * self.data[2][1] - self.data[1][1] * self.data[2][0]) * inv_det
        result[2][1] = (self.data[0][1] * self.data[2][0] - self.data[0][0] * self.data[2][1]) * inv_det
        result[2][2] = (self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]) * inv_det     
        return Mat3(result)
    
    @staticmethod
    def rotation_x(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat3([
            1, 0, 0,
            0, cos_a, -sin_a,
            0, sin_a, cos_a
        ])   
    
    @staticmethod
    def rotation_y(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat3([
            cos_a, 0, sin_a,
            0, 1, 0,
            -sin_a, 0, cos_a
        ])   
    
    @staticmethod
    def rotation_z(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat3([
            cos_a, -sin_a, 0,
            sin_a, cos_a, 0,
            0, 0, 1
        ])
    
    @staticmethod
    def scale(sx, sy, sz):
        return Mat3([
            sx, 0, 0,
            0, sy, 0,
            0, 0, sz
        ])
    
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.data[row][col]
        else:
            return self.data[index]
        
    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            self.data[row][col] = float(value)
        else:
            if isinstance(value, list) and len(value) == 3:
                self.data[index] = [float(v) for v in value]
            else:
                raise ValueError("Row must be a list of 3 elements")   
            
    def __eq__(self, other):
        for i in range(3):
            for j in range(3):
                if abs(self.data[i][j] - other.data[i][j]) >= 1e-9:
                    return False
        return True
    
class Mat4:
    def __init__(self, data=None):
        if data is None:
            self.data = [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        elif isinstance(data, list) and len(data) == 16:
            self.data = [
                [float(data[0]), float(data[1]), float(data[2]), float(data[3])],
                [float(data[4]), float(data[5]), float(data[6]), float(data[7])],
                [float(data[8]), float(data[9]), float(data[10]), float(data[11])],
                [float(data[12]), float(data[13]), float(data[14]), float(data[15])]
            ]
        elif isinstance(data, list) and len(data) == 4:
            self.data = [[float(data[i][j]) for j in range(4)] for i in range(4)]
        else:
            raise ValueError("Invalid data for Mat4 initialization")   
        
    def __add__(self, other):
        result = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Mat4(result) 
    
    def __sub__(self, other):
        result = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.data[i][j] - other.data[i][j])
            result.append(row)
        return Mat4(result)
    
    def __mul__(self, other):
        if isinstance(other, Mat4):
            result = [[0.0 for _ in range(4)] for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            return Mat4(result)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z') and hasattr(other, 'w'):
            x = self.data[0][0] * other.x + self.data[0][1] * other.y + self.data[0][2] * other.z + self.data[0][3] * other.w
            y = self.data[1][0] * other.x + self.data[1][1] * other.y + self.data[1][2] * other.z + self.data[1][3] * other.w
            z = self.data[2][0] * other.x + self.data[2][1] * other.y + self.data[2][2] * other.z + self.data[2][3] * other.w
            w = self.data[3][0] * other.x + self.data[3][1] * other.y + self.data[3][2] * other.z + self.data[3][3] * other.w
            return Vec4(x, y, z, w)
        elif hasattr(other, 'x') and hasattr(other, 'y') and hasattr(other, 'z'):
            vec4 = Vec4(other.x, other.y, other.z, 1.0)
            result = self * vec4
            return result.to_vec3()
        else:
            result = []
            for i in range(4):
                row = []
                for j in range(4):
                    row.append(self.data[i][j] * other)
                result.append(row)
            return Mat4(result)
        
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    def transpose(self):
        result = [[0.0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                result[j][i] = self.data[i][j]
        return Mat4(result)
    
    def determinant(self):
        det = 0
        for j in range(4):
            submatrix = []
            for i in range(1, 4):
                row = []
                for k in range(4):
                    if k != j:
                        row.append(self.data[i][k])
                submatrix.append(row)
            sub_det = (submatrix[0][0] * (submatrix[1][1] * submatrix[2][2] - submatrix[1][2] * submatrix[2][1]) -
                      submatrix[0][1] * (submatrix[1][0] * submatrix[2][2] - submatrix[1][2] * submatrix[2][0]) +
                      submatrix[0][2] * (submatrix[1][0] * submatrix[2][1] - submatrix[1][1] * submatrix[2][0]))  
            det += ((-1) ** j) * self.data[0][j] * sub_det
        return det
    
    @staticmethod
    def translation(x, y, z):
        return Mat4([
            1, 0, 0, x,
            0, 1, 0, y,
            0, 0, 1, z,
            0, 0, 0, 1
        ])
    
    @staticmethod
    def rotation_x(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat4([
            1, 0, 0, 0,
            0, cos_a, -sin_a, 0,
            0, sin_a, cos_a, 0,
            0, 0, 0, 1
        ])
    
    @staticmethod
    def rotation_y(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat4([
            cos_a, 0, sin_a, 0,
            0, 1, 0, 0,
            -sin_a, 0, cos_a, 0,
            0, 0, 0, 1
        ])
    
    @staticmethod
    def rotation_z(angle):
        cos_a = cos(angle)
        sin_a = sin(angle)
        return Mat4([
            cos_a, -sin_a, 0, 0,
            sin_a, cos_a, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        ])
    
    @staticmethod
    def scale(sx, sy, sz):
        return Mat4([
            sx, 0, 0, 0,
            0, sy, 0, 0,
            0, 0, sz, 0,
            0, 0, 0, 1
        ])
    
    @staticmethod
    def perspective(fov, aspect, near, far):
        f = 1.0 / tan(fov / 2.0)
        return Mat4([
            f / aspect, 0, 0, 0,
            0, f, 0, 0,
            0, 0, (far + near) / (near - far), (2 * far * near) / (near - far),
            0, 0, -1, 0
        ])
    
    @staticmethod
    def orthographic(left, right, bottom, top, near, far):
        return Mat4([
            2 / (right - left), 0, 0, -(right + left) / (right - left),
            0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom),
            0, 0, -2 / (far - near), -(far + near) / (far - near),
            0, 0, 0, 1
        ])
    
    @staticmethod
    def look_at(eye, target, up):
        forward = (target - eye).normalize()
        right = forward.cross(up).normalize()
        up_corrected = right.cross(forward)
        return Mat4([
            right.x, right.y, right.z, -right.dot(eye),
            up_corrected.x, up_corrected.y, up_corrected.z, -up_corrected.dot(eye),
            -forward.x, -forward.y, -forward.z, forward.dot(eye),
            0, 0, 0, 1
        ])
    
    def to_mat3(self):
        return Mat3([
            [self.data[0][0], self.data[0][1], self.data[0][2]],
            [self.data[1][0], self.data[1][1], self.data[1][2]],
            [self.data[2][0], self.data[2][1], self.data[2][2]]
        ])
    
    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            return self.data[row][col]
        else:
            return self.data[index]
        
    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            self.data[row][col] = float(value)
        else:
            if isinstance(value, list) and len(value) == 4:
                self.data[index] = [float(v) for v in value]
            else:
                raise ValueError("Row must be a list of 4 elements")
            
    def __eq__(self, other):
        for i in range(4):
            for j in range(4):
                if abs(self.data[i][j] - other.data[i][j]) >= 1e-9:
                    return False
        return True