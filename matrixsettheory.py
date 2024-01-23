import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

# Union of matrices
union = np.union1d(matrix1, matrix2)
print("Union:")
print(union)

# Intersection of matrices
intersection = np.intersect1d(matrix1, matrix2)
print("Intersection:")
print(intersection)

# Difference of matrices
difference = np.setdiff1d(matrix1, matrix2)
print("Difference:")
print(difference)
