import cv2

path = "image.png"

img = cv2.imread(path)

# # Original Image
cv2.imshow('image', img)

#Converted To Grayscale
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)

print(grayscale)

#Converted To Binary
(thresh, binaryimage) = cv2.threshold(grayscale, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', binaryimage)

cv2.waitKey()

