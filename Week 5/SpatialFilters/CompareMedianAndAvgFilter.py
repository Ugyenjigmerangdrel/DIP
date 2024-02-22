import numpy as np
import cv2


image = cv2.imread('sandpnoisy.png', cv2.IMREAD_GRAYSCALE)


filter_gaussian = np.array([
    [1,1,1,1,1],
    [1,2,2,2,1],
    [1,2,4,2,1],
    [1,2,2,2,1],
    [1,1,1,1,1]], dtype=int)


factor = 1/36

padding_factor = 2

#function definition
def smoothImage(input_image, padding_factor, filter, factor):
    padded_image = cv2.copyMakeBorder(input_image, padding_factor, padding_factor, padding_factor, padding_factor, cv2.BORDER_CONSTANT)
    output_image = np.zeros_like(input_image, dtype=np.uint8)

    for i in range(padding_factor, input_image.shape[0] + padding_factor):
        for j in range(padding_factor, input_image.shape[1] + padding_factor):
                output_image[i-padding_factor, j-padding_factor] = int(np.sum(padded_image[i-padding_factor:i+padding_factor + 1, j-padding_factor:j+padding_factor+1] * filter) * factor)
    return output_image, padded_image

output_image, padded_image = smoothImage(image, padding_factor, filter_gaussian, factor)


#median filter

cv2_output_img = np.zeros_like(image)

# Get the dimensions of the image
height, width = image.shape

# Define the size of the median filter window (3x3)
window_size = 4

# Create an empty output image
output_image_median = np.zeros((height, width), dtype=np.uint8)

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
        output_image_median[y, x] = median_value

cv2.medianBlur(image, 5, cv2_output_img)


cv2.imshow('Original', image)
cv2.imshow('5by5 Average Filter', output_image)
cv2.imshow('median filter', output_image_median)


cv2.waitKey(0)
cv2.destroyAllWindows()
