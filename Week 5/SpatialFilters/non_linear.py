import cv2
import numpy as np

# Load the grayscale image
image = cv2.imread('gaussian_Noise_Image.png', cv2.IMREAD_GRAYSCALE)
cv2_output_img = np.zeros_like(image)

# Get the dimensions of the image
height, width = image.shape

# Define the size of the median filter window (3x3)
window_size = 3

# Create an empty output image
output_image = np.zeros((height, width), dtype=np.uint8)

# Iterate over the image pixels
for y in range(height):
    for x in range(width):
        # Extract the pixel neighborhood
        neighborhood = []
        for j in range(max(0, y - 1), min(height, y + 2)):
            for i in range(max(0, x - 1), min(width, x + 2)):
                neighborhood.append(image[j, i])

        # Apply the median filter by sorting and taking the middle value
        median_value = np.median(neighborhood)
        output_image[y, x] = median_value

cv2.medianBlur(image, 3, cv2_output_img)

# Display the original and median filtered grayscale images
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Median Filtered Grayscale Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
