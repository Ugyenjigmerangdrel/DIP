import numpy as np
import cv2

# Define input image
input_image = cv2.imread('beans.png', 0)

max_p = np.max(input_image)
min_p = np.min(input_image)

# Apply thresholding
threshold = 120
output_image = np.zeros(input_image.shape, dtype=np.uint8)
output_image[input_image > threshold] = 255

# Display the input and output images
cv2.imshow('input', input_image)
cv2.imshow('thresholded', output_image)

key = cv2.waitKey(0)
