import cv2

img = cv2.imread("lena.jpg")


b, g, r = cv2.split(img)


cv2.imshow("Original Image", img)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
