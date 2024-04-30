import cv2


img = cv2.imread("lena.jpg")


img_without_red = img.copy()
img_without_red[:, :, 2] = 0
cv2.imshow("Image without red", img_without_red)


img_without_green = img.copy()
img_without_green[:, :, 1] = 0
cv2.imshow("Image without green", img_without_green)


img_without_blue = img.copy()
img_without_blue[:, :, 0] = 0
cv2.imshow("Image without blue", img_without_blue)

cv2.waitKey(0)

cv2.destroyAllWindows()
