import numpy as np
import math
import numpy as np

def rotate_transformations(inputmatrix, a):
    def rotateTransform(x, y, a):
        tmatrix = np.array([[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0, 0, 1]])
        imatrix = np.array([[x],[y],[1]])
        transformed_mat = np.dot(tmatrix, imatrix)
        xi, yi = transformed_mat[0][0], transformed_mat[1][0]
        return xi, yi
    dx, dy = np.shape(inputmatrix)
    cx = dx//2
    cy = dy//2

    outputmatrix = np.zeros((10, 10))

    for i in range(cx - 5, cx - 3):
        for j in range(cy - 5, cy - 1):
            xi, yi = rotateTransform(i, j, np.pi/2)
            print(math.ceil(xi), math.ceil(yi))
            if 0 <= math.ceil(xi) < 10 and 0 <= math.ceil(yi) < 10:
                outputmatrix[math.ceil(xi), math.ceil(yi)] = 1
    return outputmatrix


def scaling_transformation(input_matrix, cx, cy):
    def scaling_trans(x, y, cx, cy):
        tmatrix = np.array([[cx, 0, 0], [0, cy, 0], [0, 0, 1]])
        imatrix = np.array([[x],[y],[1]])
        transformed_mat = np.matmul(tmatrix, imatrix)
        xi, yi = transformed_mat[0][0], transformed_mat[1][0]
        return xi, yi

    output_matrix = np.zeros_like(input_matrix)
    cr, cc = input_matrix.shape[0] // 2, input_matrix.shape[1] // 2
    all_xi, all_yi = [], []

    for i in range(cr - 2, cr + 2):
        for j in range(cr - 2, cc + 2):
            xi, yi = scaling_trans(i, j, cx, cy)
            print(xi, yi)
            if 0 <= xi < input_matrix.shape[0] and 0 <= yi < input_matrix.shape[1]:
                output_matrix[int(xi), int(yi)] = 1
                all_xi.append(xi)
                all_yi.append(yi)

    output_matrix[min(all_xi):(max(all_yi) + 2), min(all_xi):(max(all_yi) + 2)] = 1

    return output_matrix

# Example usage:
input_matrix = np.zeros((10, 10))
cx = int(input("CX="))
cy = int(input("CY="))

while cx <= 0 or cy <= 0:
    print("Choose greater than 0: ")
    cx = int(input("CX="))
    cy = int(input("CY="))

scaling_transformation(input_matrix, cx, cy)



inputmatrix = np.zeros((10, 10))
dx, dy = np.shape(inputmatrix)
cx = dx//2
cy = dy//2
inputmatrix[((cx)-5):((cx)-3), ((cy)-5):((cy)-1)] = 1



rotate_transformations(inputmatrix, np.pi/2)