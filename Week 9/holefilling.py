import numpy as np
import cv2

import matplotlib.pyplot as plt

# image = cv2.imread('hole.png', cv2.IMREAD_GRAYSCALE)
# image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
# image_complement = cv2.bitwise_not(image)

image=np.array([[0,0,0,0,0,0,0],
                [0,0,1,1,0,0,0],
                [0,1,0,0,1,0,0],
                [0,1,0,0,1,0,0],
                [0,0,1,0,1,0,0],
                [0,0,1,0,1,0,0],
                [0,1,0,0,0,1,0],
                [0,1,0,0,0,1,0],
                [0,1,1,1,1,0,0],
                [0,0,0,0,0,0,0]])

image_complement = cv2.bitwise_not(image)


def dilation(image, kernel):
    rows, cols = image.shape
    
    kRows, kCols = kernel.shape
    kCenterX = kCols // 2
    kCenterY = kRows // 2
    
    result = np.zeros_like(image)
    
    for y in range(rows):
        for x in range(cols):
            if (x - kCenterX >= 0 and x + kCenterX < cols and
                y - kCenterY >= 0 and y + kCenterY < rows):
                # checks if any of the pixels in the neighborhood is white
                if np.any(image[y - kCenterY:y + kCenterY + 1, x - kCenterX:x + kCenterX + 1] * kernel):
                    result[y, x] = 255
    return result

def hole_filling(image):
    kernel=np.array([[0,1,0],
                 [1,1,1,],
                 [0,1,0]])
    
    filled_image = image.copy()
    
    while True:
        dilated_image = dilation(filled_image, kernel)
        intersection = cv2.bitwise_and(dilated_image, image_complement)
        filled_image = cv2.bitwise_or(filled_image, intersection)
        
        if np.array_equal(filled_image, dilated_image):
            break
    
    return filled_image, intersection

filled_image, intersection = hole_filling(image)


# Display the original and matched histograms
plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(filled_image, cmap='gray')
plt.title('Hole Filled Image')

plt.subplot(2, 3, 3)
plt.imshow(intersection, cmap='gray')
plt.title('Intersection Image')

plt.tight_layout
plt.show()
