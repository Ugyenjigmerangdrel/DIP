import numpy as np
import cv2


image = cv2.imread('letter.png', cv2.IMREAD_GRAYSCALE)
binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]

dx, dy = binary_image.shape

struc_element = np.ones((11, 11), np.uint8)

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


eroded_image = dilation(binary_image, struc_element)
cv2output = cv2.dilate(binary_image, struc_element, iterations=1)
cv2.imshow('Original', binary_image)
cv2.imshow('Dilated', eroded_image)
cv2.imshow('Cv2Generated', cv2output)
cv2.waitKey(0)

