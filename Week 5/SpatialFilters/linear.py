import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
image = cv2.imread('gaussian_Noise_Image.png', cv2.IMREAD_GRAYSCALE)
smoothed_image = np.zeros_like(image)

# Get the dimensions of the image
height, width = image.shape

# Define the 3x3 mean filter window
filter1 = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
], dtype=int) / 25

filter2 = np.array([
    [1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1],
    [1, 2, 4, 2, 1],
    [1, 2, 2, 2, 1],
    [1, 1, 1, 1, 1]], dtype=int) / 36  # Sum of filter elements = 16


padding_size = 2  # Adjust the padding size as needed
padded_image = cv2.copyMakeBorder(image, padding_size, padding_size, padding_size, padding_size, cv2.BORDER_CONSTANT)

# Create an empty output image of the same size
output_image_filter1 = np.zeros((height, width), dtype=np.uint8)
output_image_filter2 = np.zeros((height, width), dtype=np.uint8)

cv2.blur(image, (5, 5), smoothed_image)


for y in range(padding_size, height + padding_size):
    for x in range(padding_size, width + padding_size):
        
        output_image_filter1[y - padding_size, x - padding_size] = int(np.sum(
            padded_image[y - padding_size:y + padding_size + 1, x - padding_size:x + padding_size + 1] * filter1
        ))

for y in range(padding_size, height + padding_size):
    for x in range(padding_size, width + padding_size):
        output_image_filter2[y - padding_size, x - padding_size] = int(np.sum(
            padded_image[y - padding_size:y + padding_size + 1, x - padding_size:x + padding_size + 1] * filter2
        ))


cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Smoothed Grayscale Image 1', output_image_filter1)
cv2.imshow('Smoothed Grayscale Image 2', output_image_filter2)
cv2.imshow('Smoothed Grayscale Image cv', smoothed_image)

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.hist(image.ravel(), bins=256, range=(0, 256), color='b', alpha=0.6)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

plt.hist(output_image_filter1.ravel(), bins=256, range=(0, 256), color='r', alpha=0.6)
plt.title('Histogram of Smoothed Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

plt.hist(output_image_filter2.ravel(), bins=256, range=(0, 256), color='r', alpha=0.6)
plt.title('Histogram of Smoothed Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
