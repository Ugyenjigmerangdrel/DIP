import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

image = cv2.imread('moon.png', cv2.IMREAD_GRAYSCALE)
dx, dy = image.shape
# Create a sharpening filter
laplacian_operator = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
])

image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT)

alpha_matrix = np.zeros_like(image, dtype=np.float32)
sharpened_image = np.zeros_like(image, dtype=np.float32)
result_image = np.zeros_like(image, dtype=np.float32)

c = -1
for i in range(1, dx ):
    for j in range(1, dy):
        gxy = np.sum(image[i-1:i+2, j-1:j+2]*(laplacian_operator))
        sharpened_image[i, j] = gxy


result_image = image + (c * sharpened_image)
min_value = np.min(result_image)
fm = result_image - min_value


K = 255  # Scaling factor, you can adjust this value as needed
fs = np.uint8(K * (fm / np.max(fm)))

scaled_up_image = np.uint8(fm)


# # Convert the data type to uint8
sharpened_image = sharpened_image.astype(np.uint8)

cv2_laplacian = cv2.Laplacian(image, cv2.CV_32F, ksize=3)

cv2_result = image + (c * cv2_laplacian)
min_value = np.min(cv2_result)
cv_fm = cv2_result - min_value


K = 255  # Scaling factor, you can adjust this value as needed
cv_fs = np.uint8(K * (fm / np.max(fm)))

scaled_up_image = np.uint8(fm)


# # Show the sharpened image
# cv2.imshow('Original Image', image)
# cv2.imshow('Manual', sharpened_image)
# cv2.imshow('Scaled Up Image', result_image)
# cv2.imshow('Filtered Image', fs)
# cv2.imshow('CV Filtered Image', cv_fs)
# cv2.imshow('CV2 Laplacian', cv2_laplacian)
# cv2.waitKey(0)


plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Laplacian Filter')

plt.subplot(2, 3, 3)
plt.imshow(fm, cmap='gray')
plt.title('Scaled Image')

plt.subplot(2, 3, 4)
plt.imshow(fs, cmap='gray')
plt.title('Filtered Image')

plt.tight_layout
plt.show()