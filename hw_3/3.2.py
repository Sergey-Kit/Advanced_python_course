import numpy as np
import os


# Примесь для красивого отображения в консоли
class StrMixin:
    def __str__(self):
        return np.array_str(self.array)


# Примесь для записи объекта в файл
class FileMixin:
    def save_to_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(str(self))


# Примесь для геттеров и сеттеров
class AccessorsMixin:
    @property
    def array(self):
        return self._array
    
    @array.setter
    def array(self, value):
        if isinstance(value, np.ndarray):
            self._array = value
        else:
            raise ValueError("Value must be a numpy array")


# Основной класс для арифметических операций, использующий примеси
class NumpyArrayOperations(StrMixin, FileMixin, AccessorsMixin):
    def __init__(self, array):
        self.array = array  # Использует сеттер из AccessorsMixin

    def __add__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Matrices must be of the same dimensions to add")
        return NumpyArrayOperations(self.array + other.array)

    def __sub__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Matrices must be of the same dimensions to sub")
        return NumpyArrayOperations(self.array - other.array)

    def __mul__(self, other):
        if self.array.shape != other.array.shape:
            raise ValueError("Matrices must be of the same dimensions for element-wise multiplication")
        return NumpyArrayOperations(self.array * other.array)

    def __matmul__(self, other):
        if self.array.shape[1] != other.array.shape[0]:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix for matrix multiplication")
        return NumpyArrayOperations(self.array @ other.array)

    def __truediv__(self, other):
        if (self.array.shape != other.array.shape) or (other.array.shape == 0):
            raise ValueError("Matrices must be of the same dimensions for element-wise truediv and not zero div")
        return NumpyArrayOperations(self.array / other.array)


np.random.seed(0)
array1 = NumpyArrayOperations(np.random.randint(0, 10, (10, 10)))
array2 = NumpyArrayOperations(np.random.randint(0, 10, (10, 10)))

add_result = array1 + array2
mul_result = array1 * array2
matmul_result = array1 @ array2

add_result.save_to_file("artifacts/3.2/matrix+.txt")
mul_result.save_to_file("artifacts/3.2/matrix*.txt")
matmul_result.save_to_file("artifacts/3.2/matrix@.txt")
