import numpy as np
import cv2
import matplotlib.pyplot as plt

def filter2D(image, kernal):
    dx, dy = image.shape
    padded_image = np.pad(image, 1, 'constant')
    result_image = np.zeros_like(image, dtype=np.float32)
    for i in range(dx):
        for j in range(dy):
            result_image[i, j] = np.sum(padded_image[i:i+3, j:j+3]*kernal)
    result_image = np.clip(result_image, 0, 255)
    result_image = result_image.astype(image.dtype)
    return result_image

image = cv2.imread('SmoothedImage.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])

# Apply the filter Output laplacian filter
filtered_image = filter2D(image, kernel)

filtered_image2 = cv2.filter2D(image, -1, kernel)



c = -1
g = image + c*filtered_image



fm = g - (np.min(g))

gClip = np.uint8(255*(fm/np.max(fm)))



plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(2, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Laplacian')

plt.subplot(2, 2, 3)
plt.imshow(g, cmap='gray')
plt.title('Filtered Image')

plt.subplot(2, 2, 4)
plt.imshow(gClip, cmap='gray')
plt.title('Scaled Laplacian')

plt.savefig('LaplacianImage.png')
plt.show()