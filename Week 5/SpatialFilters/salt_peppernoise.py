import cv2
import numpy as np
import math

image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

salt_prob = 0.02
pepper_prob = 0.02

noisy_img = image.copy()

num_salt = math.ceil(salt_prob*image.size)
num_pepper = math.ceil(salt_prob*image.size)
coordinates = []

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        coordinates.append((i,j))
random_coordinates_salt = np.random.randint(0, len(coordinates), num_salt)
random_coordinates_pepper= np.random.randint(0, len(coordinates), num_pepper)

for i in random_coordinates_salt:
    x, y = coordinates[i]
    noisy_img[x][y] = 255

for i in random_coordinates_pepper:
    x, y = coordinates[i]
    noisy_img[x][y] = 0

cv2.imshow('Noisy', noisy_img)
cv2.imwrite('sandpnoisy.png', noisy_img)
cv2.waitKey(0)
