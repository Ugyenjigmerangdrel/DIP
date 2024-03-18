import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('LaplacianImage.png', cv2.IMREAD_GRAYSCALE)
dx, dy = image.shape

frequency = {}
for i in range(dx):
    for j in range(dy):
        if image[i, j] in frequency.keys():
            frequency[image[i, j]] += 1
        else:
            frequency[image[i, j]] = 1

plt.bar(frequency.keys(), frequency.values())
            
plt.show()


cv2.imshow('Image', image)
cv2.waitKey(0)