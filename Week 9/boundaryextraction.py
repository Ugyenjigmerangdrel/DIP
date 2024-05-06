import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('forb.png', cv2.IMREAD_GRAYSCALE)
image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]

struc_element = np.ones((45, 45), np.uint8)

def erosion(image, kernel):
    rows, cols = image.shape
    
    kRows, kCols = kernel.shape
    kCenterX = kCols // 2
    kCenterY = kRows // 2
    
    result = np.zeros_like(image)
    
    for y in range(rows):
        for x in range(cols):
            if (x - kCenterX >= 0 and x + kCenterX < cols and
                y - kCenterY >= 0 and y + kCenterY < rows):
                if np.all(image[y - kCenterY:y + kCenterY + 1, x - kCenterX:x + kCenterX + 1] * kernel):
                    result[y, x] = 255
    
    return result

eroded_image = erosion(image, struc_element)

final_image = image - eroded_image

# Display the original and matched histograms
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Eroded Image')

plt.subplot(2, 3, 3)
plt.imshow(final_image, cmap='gray')
plt.title('Boundary Image')

plt.tight_layout
plt.show()


