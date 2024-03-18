import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

image = cv2.imread('moon.png', cv2.IMREAD_GRAYSCALE)
dx, dy = image.shape
# Create a sharpening filter
laplacian_operator = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
])

image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT)

alpha_matrix = np.zeros_like(image, dtype=np.float32)
sharpened_image = np.zeros_like(image, dtype=np.float32)
# result_image = np.zeros_like(image, dtype=np.float32)

c = -1
# for i in range(1, dx ):
#     for j in range(1, dy):
#         gxy = np.sum(image[i-1:i+2, j-1:j+2]*(laplacian_operator))
#         sharpened_image[i, j] = gxy

sharpened_image = cv2.filter2D(image, -1, laplacian_operator)

result_image = image + c*sharpened_image

result_image = np.clip(result_image, 0, 255)
min_value = np.min(result_image)
fm = result_image - min_value


K = 255  # Scaling factor, you can adjust this value as needed
fs = np.uint8(K * (fm / np.max(fm)))

scaled_up_image = np.uint8(fm)




# Show the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Manual', sharpened_image)
cv2.imshow('Scaled Up Image', result_image)
cv2.imshow('Filtered Image', fs)
cv2.waitKey(0)

