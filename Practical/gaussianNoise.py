import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

# Generate random Gaussian noise
mean = 0
stddev = 10
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
# Add noise to image
noisy_img = cv2.add(img, noise)
cv2.imshow('original', img)
cv2.imshow('noisy_img', noisy_img)
cv2.imwrite('gnoise.png', noisy_img)
cv2.waitKey(0)
