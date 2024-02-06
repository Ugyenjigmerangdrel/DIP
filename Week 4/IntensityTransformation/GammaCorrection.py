import numpy as np
import cv2

# Define input image
input_image = cv2.imread('map.png', 0)

#determine the maximum pixel value
max_pixel = np.max(input_image)
gamma = 3

# Apply gamma correction
output_image = np.array(1*(np.power(input_image/max_pixel, gamma)))

# Display the input and output images
cv2.imshow('input', input_image)
cv2.imshow('gamma corrected', output_image)

key = cv2.waitKey(0)



print(max_pixel)
