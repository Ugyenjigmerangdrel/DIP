import numpy as np

a = np.matrix('1 2 3; 4 5 6; 7 8 9')
b = np.matrix('4 3 2; 4 8 9; 7 6 9')
c = np.add(a, b)
mul = np.matmul(a, b)
sub = np.subtract(b, a)
smul = np.multiply(a, 2)
sdiv = np.divide(b, 2)
sadd = np.add(a, 1)
ssub = np.subtract(a, 1)
print("Input Matrix A: \n",a)
print("Input Matrix B: \n",b)
print("Addition: \n",c)
print("Multiplication: \n",mul)
print("Subtraction: \n",sub)
print("Scalar Multiplication: \n",smul)
print("Scalar Div: \n",sdiv)
print("Scalar Additions: \n",sadd)
print("Scalar Subtraction: \n",ssub)

#scalar matrix operation using for loop
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
dim = np.shape(a)
for i in range(0, dim[0]):
    for j in range(0, dim[1]):
        m[i][j] = 1 + m[i][j]
print(m)

#transpose of matrix
mat =  np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
tr = mat.transpose()

det = np.linalg.det(mat)

inv = np.linalg.inv(mat)
print(a)
print(b)
print(c)
print(tr)
print(inv)
print(det)
