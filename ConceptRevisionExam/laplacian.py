import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

image = cv2.imread('./moon.png', cv2.IMREAD_GRAYSCALE)

dx, dy = image.shape

laplacianf = np.array([[1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]])




laplacian = np.zeros((dx, dy))
output_image = np.zeros((dx, dy))
padded_image = np.pad(image, ((1, 1), (1, 1)), 'constant')


test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# print(sobelx * test[0:3, 0:3])
# print(np.sum(sobelx * test[0:3, 0:3]))

for i in range(1, dx):
    for j in range(1, dy):
        d2fxy = np.sum(padded_image[i-1:i+2, j-1:j+2] * laplacianf) 
        laplacian[i-1, j-1] = d2fxy
     

fm = laplacian - np.min(laplacian)

fs = np.uint8(255 * (fm / np.max(fm)))

output_image = image * laplacian





cv2.imshow('image', image)
cv2.imshow('sd', laplacian.astype(np.uint8))
cv2.imshow('sd2', fs)
cv2.imshow('final', output_image)
cv2.waitKey(0)




plt.show()