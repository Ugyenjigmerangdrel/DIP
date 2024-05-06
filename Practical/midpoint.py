import numpy as np
import cv2

image = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)

dx, dy = image.shape

blurred_image = cv2.GaussianBlur(image, (11, 11), 0)
padding = 1
padded_image = np.pad(blurred_image, ((padding, padding), (padding, padding)), mode='constant', constant_values=0)

def midpointfilter(image, blurred_image):
    midpoint_image = np.zeros(image.shape)
    for i in range(padding, dx):
        for j in range(padding, dy):
            local_window = blurred_image[i-padding:i+padding+1, j-padding:j+padding+1].astype(np.uint32)
            # print(local_window)
            midpoint_image[i-padding, j-padding] =  int((np.max(local_window) + np.min(local_window))/2)

    return midpoint_image

midpoint_image = midpointfilter(image, padded_image)
midpoint_image = midpoint_image.astype(np.uint8)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Midpoint Image", midpoint_image)
cv2.waitKey(0)
