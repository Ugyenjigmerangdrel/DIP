import cv2
import numpy as np

def bit_slice(image, bit):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract the bit plane using bitwise shift right operator
    bit_plane = (gray_image >> bit) & 1
    
    
    # Create a binary image from the bit plane
    binary_image = np.uint8(bit_plane * 255)
    
    return binary_image

# Load the image
image = cv2.imread('bone.png')

# Perform bit-level slicing for bit 7
bit_7_image = bit_slice(image, 1)

# Display the result
cv2.imshow('Bit 7 Image', bit_7_image)
cv2.waitKey(0)
cv2.destroyAllWindows()