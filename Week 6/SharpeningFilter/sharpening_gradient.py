import numpy as np
import cv2
import math
image = cv2.imread('noisy_img.jpg', cv2.IMREAD_GRAYSCALE)
dx, dy = image.shape
# Create a sharpening filter
sharpening_filter = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

sharpening_filter2 = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Create an copy of image matrix for the sharpened image
sharpened_image = np.zeros_like(image, dtype=np.float32)

# Apply padding
image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT)

alpha_matrix = np.zeros_like(image, dtype=np.float32)
# Iterate over each pixel in the image
for i in range(1, dx ):
    for j in range(1, dy):
        gx = np.sum(image[i-1:i+2, j-1:j+2] * sharpening_filter)
        gy = np.sum(image[i-1:i+2, j-1:j+2] * sharpening_filter2)
        sharpened_image[i-1, j-1] = abs(gx) + abs(gy)
        alpha_matrix[i-1, j-1] = math.atan2(gy, gx)

# Convert the data type to uint8
sharpened_image = sharpened_image.astype(np.uint8)
sharpened_image_2 = image.copy()
gX = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

combined = cv2.addWeighted(gX, 0.3, gY, 0.3, 127)

# Show the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Manual', sharpened_image)
cv2.imshow('CV2 Sobel', combined)
cv2.imshow('Alpha', alpha_matrix)
cv2.waitKey(0)