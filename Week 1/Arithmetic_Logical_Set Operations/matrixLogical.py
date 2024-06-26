import numpy as np

#logical operations
print("Logical Operations")
a = np.matrix('0 1 0; 1 1 0; 0 0 0')
b = np.matrix('1 1 0; 1 1 0; 0 0 0')
print("Input Matrix A: \n",a)
print("Input Matrix B: \n",b)
print("Logical And: \n",np.logical_and(a,b))
print("Logical Or: \n",np.logical_or(a,b))
print("Logical XOR: \n",np.logical_xor(a,b))
print("Logical NOT: \n",np.logical_not(a))
print("Logical NOR: \n",np.logical_not(np.logical_or(a, b)))
print("Logical NAND: \n", np.logical_not(np.logical_and(a , b)))