import numpy as np
import math

def rotateTransform(x, y, a):
    tmatrix = np.array([[np.cos(a), np.sin(a), 0], [-np.sin(a), np.cos(a), 0], [0, 0, 1]])
    imatrix = np.array([[x],[y],[1]])
    transformed_mat = np.dot(tmatrix, imatrix)
    xi, yi = transformed_mat[0][0], transformed_mat[1][0]
    return xi, yi

inputmatrix = np.zeros((10, 10))
dx, dy = np.shape(inputmatrix)

cx = dx//2
cy = dy//2

inputmatrix[((cx)-5):((cx)-3), ((cy)-5):((cy)-1)] = 1

outputmatrix = np.zeros((10, 10))

for i in range(cx - 5, cx - 3):
    for j in range(cy - 5, cy - 1):
        xi, yi = rotateTransform(i, j, 2*np.pi)
        print(math.ceil(xi), math.ceil(yi))
        if 0 <= math.ceil(xi) < 10 and 0 <= math.ceil(yi) < 10:
            outputmatrix[math.ceil(xi), math.ceil(yi)] = 1
print("Input Matrix\n",inputmatrix)
print("Output Matrix\n",outputmatrix)

#xi = x cos b + y sin b
#yi = y cos b - x sin b