import cv2
import numpy as np

image = cv2.imread("imageofconcern2.jpeg", cv2.IMREAD_GRAYSCALE)

dx, dy = image.shape

threshold = np.max(image)/2

for i in range(dx):
    for j in range(dy):
        if image[i, j] >= threshold:
            image[i, j] = 255
        elif image[i, j] <= threshold:
            image[i, j] = 0

cv2.imshow("KAYTEE", image)
cv2.imwrite("binaryimage.jpg", image)
cv2.waitKey(0)

