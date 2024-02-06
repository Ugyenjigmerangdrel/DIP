import numpy as np
import cv2

def contrast_stretching(image):
    # Calculate the minimum and maximum pixel values
    min_val = np.min(image)
    max_val = np.max(image)

    # Apply contrast stretching
    stretched_image = (image - min_val) * (255 / (max_val - min_val))

    # Convert the image to uint8 data type
    stretched_image = stretched_image.astype(np.uint8)

    return stretched_image

# Load the image
image = cv2.imread("beans.png", 0)

# Apply contrast stretching
stretched_image = contrast_stretching(image)

# Display the original and stretched images
cv2.imshow("Original Image", image)
cv2.imshow("Stretched Image", stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
