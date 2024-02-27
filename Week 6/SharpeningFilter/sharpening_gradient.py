import numpy as np
import cv2
import math
image = cv2.imread('house.png', cv2.IMREAD_GRAYSCALE)
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

# Create an empty matrix for the sharpened image
sharpened_image = image.copy()

# Iterate over each pixel in the image
for i in range(1, dx - 1):
    for j in range(1, dy - 1):
        # Apply the sharpening filter
        sharpened_image[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * sharpening_filter)
        sharpened_image[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * sharpening_filter2)

# Clip the values to the range [0, 255]
sharpened_image = np.clip(sharpened_image, 0, 255)

# Convert the data type to uint8
sharpened_image = sharpened_image.astype(np.uint8)



# Show the sharpened image
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)