import numpy as np
import os

class Matrix:
    def __init__(self, array):
        self.array = array

    def __add__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Matrices must be of the same dimensions to add")
        return Matrix(self.array + other.array)
    
    def __mul__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Matrices must be of the same dimensions for element-wise multiplication")
        return Matrix(self.array * other.array)
    
    def __matmul__(self, other):
        if self.array.shape[1] != other.array.shape[0]:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for matrix multiplication")
        return Matrix(self.array @ other.array)

    def __str__(self):
        return str(self.array)


def save_to_file(file_path, file_name, result):
    os.makedirs(file_path, exist_ok=True)
    file_path = os.path.join(file_path, file_name)
    with open(file_path, "w") as f:
        f.write(str(result))

np.random.seed(0)
matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

add_result = matrix1 + matrix2
mul_result = matrix1 * matrix2
matmul_result = matrix1 @ matrix2

save_to_file("artifacts/3.1", "matrix+.txt", add_result)
save_to_file("artifacts/3.1", "matrix*.txt", mul_result)
save_to_file("artifacts/3.1", "matrix@.txt", matmul_result)

