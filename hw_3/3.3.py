import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
    
    def __eq__(self, other):
        return np.array_equal(self.matrix, other.matrix)
    
    def __hash__(self):
        return hash((np.sum(self.matrix), np.prod(self.matrix.shape)))
    
    def __matmul__(self, other):
        return Matrix(self.matrix @ other.matrix)
    
    def __str__(self):
        return np.array_str(self.matrix)


# Функция для поиска коллизий
def find_collision():
    np.random.seed(0)
    hashes = {}
    for _ in range(10000):
        matrix = Matrix(np.random.randint(0, 10, (2, 2)))
        h = hash(matrix)
        if h in hashes and not np.array_equal(matrix.matrix, hashes[h].matrix):
            return matrix, hashes[h]
        else:
            hashes[h] = matrix
    return None, None


A, C = find_collision()
if A and C:
    B = Matrix(np.random.randint(0, 10, (2, 2)))
    D = B

    AB = A @ B
    CD = C @ D

    # Сохранение результатов
    matrices = [('A', A), ('B', B), ('C', C), ('D', D), ('AB', AB), ('CD', CD)]
    for name, matrix in matrices:
        with open(f'artifacts/3.3/{name}.txt', "w") as f:
            f.write(str(matrix))
    
    with open(f'artifacts/3.3/hash.txt', "w") as f:
        f.write(f"Hash(AB): {hash(AB)}\nHash(CD): {hash(CD)}")

    output_files = [f'artifacts/3.3/{name}.txt' for name, _ in matrices] + ['artifacts/3.3/hash.txt']
    output_files
else:
    "No collision found."



