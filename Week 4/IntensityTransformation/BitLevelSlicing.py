import numpy as np
import cv2

# Define input image
input_image = cv2.imread('bone.png', 0)

dx, dy = np.shape(input_image)

output_image = np.zeros((dx, dy), dtype=np.uint8)

for i in range(dx):
    for j in range(dy):
        binary_rep = np.binary_repr(input_image[i][j], width=8)
        bits = [binary_rep[i:i+1] for i in range(0, len(binary_rep), 1)]
        #print(bits)
        bits[1] = '1'
        bits[2:8] = '0'
        bits = "".join(bits)
        #print(bits)
        bits = int(bits, 2)
        output_image[i][j] = bits

cv2.imshow('input', input_image)    
cv2.imshow('bit_sliced', output_image)
key = cv2.waitKey(0)

test = '10001001'
bits = [test[i:i+1] for i in range(0, len(test), 1)]
print(bits)
        

        

