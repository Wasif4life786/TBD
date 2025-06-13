class Matrix:
    def __init__(self,data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same num of cols")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])
    def add(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Addition unsuccessful: Matrices have different Lengths")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def sub(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Subtraction unsuccessful: Matrices have different Lengths")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)
    def multiply(self,other):
        if self.rows != other.cols:
            raise ValueError("Incompatible Matrix dimensions")
        result = [[sum(self.data[i][k] * other[k][j])] for k in range(self.cols) for j in range(other.cols) for i in range(other.rows)]
        return Matrix(result)
    def transpose(self):
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)
    def minor(self, i, j):
        return Matrix([[self.data[row][col] for col in range(self.cols) if col != j] for row in range(self.rows) if row != i])
    def determinant(self):
        if self.rows != self.cols:
            raise ValueError("Determinant is only defined for square matrices.")
        if self.rows == 1:
            return self.data[0][0]
        if self.rows == 2:
            return self.data[0][0]*self.data[1][1] - self.data[0][1]*self.data[1][0]
        det = 0
        for col in range(self.cols):
            sign = (-1) ** col
            minor_det = self.minor(0, col).determinant()
            det += sign * self.data[0][col] * minor_det
        return det
    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        if self.rows == 1:
            return Matrix([[1 / self.data[0][0]]])
        cofactors = []
        for i in range(self.rows):
            cofactor_row = []
            for j in range(self.cols):
                minor = self.minor(i, j)
                sign = (-1) ** (i + j)
                cofactor = sign * minor.determinant()
                cofactor_row.append(cofactor)
            cofactors.append(cofactor_row)
        cof_matrix = Matrix(cofactors)
        adjugate = cof_matrix.transpose()
        inverse_data = [[adjugate.data[i][j] / det for j in range(adjugate.cols)] for i in range(adjugate.rows)]
        return Matrix(inverse_data)