import numpy as np
import cv2

image_path = "map.png"

# Read the saved image using OpenCV
loaded_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
dx, dy = loaded_image.shape
log_transform = np.zeros((dx, dy), dtype=np.uint8)

normalized_image = loaded_image / 255.0
# negative_image = np.zeros()


for x in range(len(loaded_image)):
    for y in range(len(loaded_image[x])):
        log_transform[x, y] = np.array(25 * np.exp(normalized_image[x, y])).astype(dtype=np.uint8)

print(loaded_image)
print('=' *80)
print(log_transform)

cv2.imshow("Original Image", loaded_image)
cv2.imshow("Log Transform Image", log_transform)
cv2.waitKey(0)
cv2.destroyAllWindows()
