import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena_gray.png')

# Generate random Gaussian noise
mean = 0
stddev = 180
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
# Add noise to image
noisy_img = cv2.add(img, noise)
# Save noisy image
cv2.cvtColor(noisy_img, cv2.COLOR_BGR2GRAY)
cv2.imshow('noisy_img', noisy_img)
cv2.waitKey(0)
