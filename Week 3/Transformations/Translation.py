#Ask the user from X, Y
#Display the transformed coordinates
#tx = 2, ty = 3

import numpy as np
def translation(mat, x, y, tx, ty):
    tmatrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    imatrix = np.array([[x],[y],[1]])
    transformed_mat =np.matmul(tmatrix, imatrix)
    xi = transformed_mat[0][0]
    yi = transformed_mat[1][0]
    #print(transformed_mat)
    return xi, yi

zmat = np.zeros((10, 10))
dim = np.shape(zmat)

cr = dim[0]//2
cc = dim[1]//2
for i in range((cr-3), (cr+3)):
    for j in range((cr-3), (cc+3)):
        zmat[i][j] = 1

print(zmat)
zmat = np.zeros((10, 10))
tx = int(input("TX="))
ty = int(input("TY="))

for i in range((cr-3), (cr+3)):
    for j in range((cr-3), (cc+3)):
        xi, yi = translation(zmat, i, j, tx, ty)
        if xi >= 0 and xi < 10 and yi >= 0 and yi < 10:
            zmat[xi, yi] = 1
print(zmat)
