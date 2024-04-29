import numpy as np
import cv2

#define image

iimage = cv2.imread('bone.png', 0)

dx, dy = np.shape(iimage)

output_image = np.zeros_like(iimage)
def bit_level_slicing(image, bit):
    # Apply bit-level slicing
    for i in range(dx):
        for j in range(dy):
            #print(np.binary_repr(iimage[i][j], width=8))
            binary_rep = np.binary_repr(iimage[i][j], width=8)
            reverse_br = binary_rep[::-1]
            output_image[i][j] = int(reverse_br[bit]) * 255
            

bit_level_slicing(iimage, 7)

cv2.imshow('input', iimage)
cv2.imshow('output', output_image)

cv2.waitKey(0)