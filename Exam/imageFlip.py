import numpy as np
import cv2

inputImage = cv2.imread('bone.png', 0)
dx, dy = np.shape(inputImage)
outputImage = np.zeros_like(inputImage)

for i in range(dx):
    for j in range(dy):
        outputImage[i][j] = inputImage[dx-1-i][dx-1-j]

cv2.imshow('input', inputImage)
cv2.imshow('output', outputImage)
cv2.waitKey(0)