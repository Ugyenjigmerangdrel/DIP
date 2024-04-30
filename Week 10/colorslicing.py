import cv2
import numpy as np


img = cv2.imread("strawberry.png")


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


lower_red = np.array([150, 0, 0], dtype=np.uint8)
upper_red = np.array([255, 100, 100], dtype=np.uint8)


red_mask = cv2.inRange(img_rgb, lower_red, upper_red)


red_result = cv2.bitwise_and(img_rgb, img_rgb, mask=red_mask)


cv2.imshow("Original Image", img_rgb)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Red Result", red_result)

cv2.waitKey(0)
cv2.destroyAllWindows()
