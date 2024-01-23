import numpy as np
#10X10 matrix

zmat = np.zeros((10, 10))
dim = np.shape(zmat)

cr = dim[0]//2
cc = dim[1]//2

for i in range(cr-1, cr+2):
    for j in range(cc-1, cc+2):
        zmat[i][j] = 1

print(zmat)

