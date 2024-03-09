import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('supernoisy.png', cv2.IMREAD_GRAYSCALE)
pepper = cv2.imread('pepper.png', cv2.IMREAD_GRAYSCALE)
salt = cv2.imread('salt.png', cv2.IMREAD_GRAYSCALE)
#median filter

height, width = image.shape

output_image_mid = np.zeros((height, width), dtype=np.uint8)


for y in range(height):
    for x in range(width):
        # Extract the pixel neighborhood
        neighborhood = [] 
       
        for j in range(max(0, y - 1), min(height, y + 2)):
            for i in range(max(0, x - 1), min(width, x + 2)):
                neighborhood.append(image[j, i])
        # print(neighborhood)   
        output_image_mid[y, x] = (np.max(neighborhood) + np.min(neighborhood))*0.5


cv2.imshow('original', image)
cv2.imshow('Mid point', output_image_mid)
cv2.waitKey(0)