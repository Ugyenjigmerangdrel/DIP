import numpy as np

def scalingTrans(x, y, cx, cy):
    tmatrix = np.array([[cx, 0, 0], [0, cy, 0], [0, 0, 1]])
    imatrix = np.array([[x],[y],[1]])
    transformed_mat = np.matmul(tmatrix, imatrix)
    xi, yi = transformed_mat[0][0], transformed_mat[1][0]
    return xi, yi

zmat = np.zeros((10, 10))
dim = np.shape(zmat)

cr = dim[0] // 2
cc = dim[1] // 2

for i in range(cr - 2, cr + 2):
    for j in range(cr - 2, cc + 2):
        zmat[i][j] = 1

outputmatrix = np.zeros((10, 10))
cx = int(input("CX="))
cy = int(input("CY="))

while cx <= 0 or cy <= 0:
    print("Choose greater than 0: ")
    cx = int(input("CX="))
    cy = int(input("CY="))

all_xi = []
all_yi = []

for i in range(cr - 2, cr + 2):
    for j in range(cr - 2, cc + 2):
        xi, yi = scalingTrans(i, j, cx, cy)
        if 0 <= xi < 10 and 0 <= yi < 10:
            outputmatrix[int(xi), int(yi)] = 1
            all_xi.append(xi)
            all_yi.append(yi)

print("Input Matrix: \n",zmat)
outputmatrix[min(all_xi):(max(all_yi) + 2), min(all_xi):(max(all_yi) + 2)] = 1
print(outputmatrix)
