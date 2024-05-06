import cv2
import numpy as np

input_image = cv2.imread('compre.jpg', cv2.IMREAD_GRAYSCALE)

blurred_image = cv2.blur(input_image, (3, 3))

inp = int(input("Enter 1 for highboost filtering and 2 for unsharp masking: "))
gmask = np.zeros(input_image.shape, dtype=np.uint8)
highboost_image = np.zeros(input_image.shape, dtype=np.uint8)
name = ""

if inp == 1:
    k = 2
    gmask = input_image - blurred_image
    highboost_image = np.uint8(input_image + (k * gmask))
    name = "High-boost Image"
elif inp == 2:
    k = 1
    gmask = input_image - blurred_image
    highboost_image = np.uint8(input_image + (k * gmask))
    name = "Unsharp Masking Image"



cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('g_mask Image', gmask)
cv2.imshow(name, highboost_image)
cv2.waitKey(0)
cv2.destroyAllWindows()