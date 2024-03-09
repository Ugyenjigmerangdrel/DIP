import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

image = cv2.imread('./lens.png', cv2.IMREAD_GRAYSCALE)

dx, dy = image.shape

sobely = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobelx = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])



gradient = np.zeros((dx, dy))
output_image = np.zeros((dx, dy))
padded_image = np.pad(image, ((1, 1), (1, 1)), 'constant')


test = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(sobelx * test[0:3, 0:3])
# print(np.sum(sobelx * test[0:3, 0:3]))
alpha_matrix = np.zeros((dx, dy))
gx = np.zeros((dx, dy))
gy = np.zeros((dx, dy))
for i in range(1, dx):
    for j in range(1, dy):
        gx[i-1, j-1] = np.sum(sobely * padded_image[i-1:i+2, j-1:j+2])
        gy[i-1, j-1] = np.sum(sobelx * padded_image[i-1:i+2, j-1:j+2])
        gradient[i-1, j-1] = math.sqrt(gx[i-1, j-1]**2 + gy[i-1, j-1]**2)
        alpha_matrix[i-1, j-1] = math.atan2(gy[i-1, j-1], gx[i-1, j-1])


gx = gx/gx.max() * 255
gy = gy/gy.max() * 255
output_image = (gradient / gradient.max()) * 255

final = image + output_image
# Show the before and after pictures
plt.subplot(2, 3, 1), plt.imshow(image, cmap='gray')
plt.title('Before'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5), plt.imshow(final, cmap='gray')
plt.title('Before'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 2), plt.imshow(output_image, cmap='gray')
plt.title('After'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 3), plt.imshow(gx, cmap='gray')
plt.title('Gx'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 4), plt.imshow(gy, cmap='gray')
plt.title('Gy'), plt.xticks([]), plt.yticks([])

plt.show()