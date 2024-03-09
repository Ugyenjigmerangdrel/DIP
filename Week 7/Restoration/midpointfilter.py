import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('sandpnoisy.png', cv2.IMREAD_GRAYSCALE)
pepper = cv2.imread('pepper.png', cv2.IMREAD_GRAYSCALE)
salt = cv2.imread('salt.png', cv2.IMREAD_GRAYSCALE)
#median filter

height, width = image.shape

window_size = 4

output_image_median = np.zeros((height, width), dtype=np.uint8)
output_image_min = np.zeros((height, width), dtype=np.uint8)
output_image_max = np.zeros((height, width), dtype=np.uint8)
output_image_mid = np.zeros((height, width), dtype=np.uint8)
# for y in range(height):
#     for x in range(width):
#         # Extract the pixel neighborhood
#         neighborhood = []
#         for j in range(max(0, y - 1), min(height, y + 2)):
#             for i in range(max(0, x - 1), min(width, x + 2)):
#                 neighborhood.append(image[j, i])

#         # Apply the median filter by sorting and taking the middle value
#         median_value = np.median(neighborhood)
#         output_image_median[y, x] = median_value

for y in range(height):
    for x in range(width):
        # Extract the pixel neighborhood
        neighborhood = [] 
        neighborhood2 = [] 
        neighborhood3 = []
        for j in range(max(0, y - 1), min(height, y + 2)):
            for i in range(max(0, x - 1), min(width, x + 2)):
                neighborhood.append(image[j, i])
                neighborhood2.append(pepper[j, i])
                neighborhood3.append(salt[j, i])

        # Apply the median filter by sorting and taking the middle value
        output_image_median[y, x] = np.median(neighborhood)
        output_image_min[y, x] = np.min(neighborhood3)
        output_image_max[y, x] = np.max(neighborhood2)



plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(salt, cmap='gray')
plt.title('Salt Image')

plt.subplot(2, 3, 3)
plt.imshow(output_image_max, cmap='gray')
plt.title('Min Filter Image')

plt.subplot(2, 3, 4)
plt.imshow(pepper, cmap='gray')
plt.title('Pepper Image')

plt.subplot(2, 3, 5)
plt.imshow(output_image_min, cmap='gray')
plt.title('Max Filter Image')



plt.subplot(2, 3, 6)
plt.imshow(output_image_median, cmap='gray')
plt.title('Median Filter Image')

plt.tight_layout
plt.show()