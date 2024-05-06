import cv2
import numpy as np

image_path = "beans.png"
test_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define the piecewise function for contrast stretching
def contrast_stretching(r):
    if r < 19:
        s = int(r * 0.533)
    elif 20 <= r <= 220:
        s = int(1.75 * r - 62.5)
    else:
        s = int(0.519 * r + 122.631)
    return s

# Apply the contrast stretching function to the test image
stretched_image = np.zeros_like(test_image)
for i in range(test_image.shape[0]):
    for j in range(test_image.shape[1]):
        stretched_image[i, j] = contrast_stretching(test_image[i, j])

# Display the original and stretched images
cv2.imshow("Original Test Image", test_image)
cv2.imshow("Stretched Test Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
