import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('fingerprint.png', cv2.IMREAD_GRAYSCALE)
binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]

dx, dy = binary_image.shape

struc_element = np.ones((5, 5), np.uint8)

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

eroded_image = erosion(binary_image, struc_element)
opened_image = dilation(eroded_image, struc_element)

dilated_open = dilation(opened_image, struc_element)

closed_image = erosion(dilated_open, struc_element)


cv2output = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, struc_element)
cv2output1 = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, struc_element)


# Display the original and matched histograms
plt.subplot(2, 3, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Eroded Image')

plt.subplot(2, 3, 3)
plt.imshow(opened_image, cmap='gray')
plt.title('Opened Image')

plt.subplot(2, 3, 4)
plt.imshow(dilated_open, cmap='gray')
plt.title('Dilation on Opened Image')

plt.subplot(2, 3, 5)
plt.imshow(closed_image, cmap='gray')
plt.title('Closed Image')


plt.tight_layout
plt.show()


cv2.waitKey(0)
print(image)
