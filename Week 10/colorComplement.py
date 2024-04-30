import cv2

img = cv2.imread("strawberry.png")


img_hsi = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


h, s, i = cv2.split(img_hsi)


complement_i = 255 - i

complement_s = 255 - s


complement_hsi = cv2.merge([h, complement_s, complement_i])


complement_rgb = cv2.cvtColor(complement_hsi, cv2.COLOR_HSV2RGB)


cv2.imshow("Original Image", img)
cv2.imshow("Color Complemented Image", complement_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
